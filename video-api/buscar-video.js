// Endpoint de busca de vídeos/tutoriais da BSTEN.
// Recebe a dúvida do cliente (q) e devolve o link certo do catálogo (videos.json).
// Funciona como Netlify Function E como módulo reutilizável.

const fs = require("fs");
const path = require("path");

// remove acentos, deixa minúsculo
function normalizar(s) {
  return (s || "")
    .toString()
    .toLowerCase()
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .replace(/[^a-z0-9\s]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function carregarCatalogo() {
  const raw = fs.readFileSync(path.join(__dirname, "videos.json"), "utf8");
  return JSON.parse(raw).itens || [];
}

// pontua cada item pela quantidade de palavras da dúvida que batem nas keywords
function buscar(q, itens) {
  const consulta = normalizar(q);
  if (!consulta) return { found: false };
  const tokens = consulta.split(" ").filter((t) => t.length >= 3);

  let melhor = null;
  let melhorScore = 0;

  for (const item of itens) {
    let score = 0;
    for (const kw of item.keywords || []) {
      const k = normalizar(kw);
      if (!k) continue;
      // frase-chave inteira aparece na dúvida = peso forte
      if (consulta.includes(k)) score += 3 + k.length / 10;
      // alguma palavra da dúvida bate com a keyword
      for (const t of tokens) {
        if (k === t) score += 2;
        else if (k.includes(t) || t.includes(k)) score += 1;
      }
    }
    if (score > melhorScore) {
      melhorScore = score;
      melhor = item;
    }
  }

  // achou tema, mas o vídeo/tutorial ainda não tem URL => não envia
  if (!melhor || melhorScore < 2) return { found: false };
  if (!melhor.url) return { found: false, tema: melhor.tema };

  return {
    found: true,
    title: melhor.titulo,
    url: melhor.url,
    theme: melhor.tema,
    type: melhor.tipo,
  };
}

// ---- Netlify Function handler ----
exports.handler = async (event) => {
  let q = "";
  try {
    if (event.queryStringParameters && event.queryStringParameters.q) {
      q = event.queryStringParameters.q;
    } else if (event.body) {
      const body = JSON.parse(event.body);
      q = body.q || (body.query && body.query.q) || "";
    }
  } catch (e) {
    q = "";
  }

  const resultado = buscar(q, carregarCatalogo());
  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json; charset=utf-8" },
    body: JSON.stringify(resultado),
  };
};

// exportado para teste/reuso
exports.buscar = buscar;
exports.carregarCatalogo = carregarCatalogo;
