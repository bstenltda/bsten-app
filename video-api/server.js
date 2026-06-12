// Servidor Node (sem dependências) para o endpoint de busca de vídeos.
// Roda na VPS com PM2, atrás do nginx. Lê o videos.json a cada requisição,
// então editar o catálogo NÃO exige reiniciar o servidor.
//
// Subir:  pm2 start server.js --name buscar-video
// Testar: curl "http://localhost:3001/api/buscar-video?q=como funciona o bloqueio"

const http = require("http");
const { URL } = require("url");
const { buscar, carregarCatalogo } = require("./buscar-video.js");

const PORT = process.env.PORT || 3001;

function responder(res, status, obj) {
  res.writeHead(status, {
    "Content-Type": "application/json; charset=utf-8",
    "Access-Control-Allow-Origin": "*",
  });
  res.end(JSON.stringify(obj));
}

const server = http.createServer((req, res) => {
  const u = new URL(req.url, `http://${req.headers.host}`);

  // health check
  if (u.pathname === "/" || u.pathname === "/health") {
    return responder(res, 200, { ok: true, servico: "buscar-video" });
  }

  if (u.pathname.endsWith("/buscar-video")) {
    // GET ?q=...
    if (req.method === "GET") {
      const q = u.searchParams.get("q") || "";
      return responder(res, 200, buscar(q, carregarCatalogo()));
    }
    // POST {"q":"..."} ou {"query":{"q":"..."}}
    if (req.method === "POST") {
      let body = "";
      req.on("data", (c) => (body += c));
      req.on("end", () => {
        let q = "";
        try {
          const j = JSON.parse(body || "{}");
          q = j.q || (j.query && j.query.q) || "";
        } catch (e) {}
        return responder(res, 200, buscar(q, carregarCatalogo()));
      });
      return;
    }
  }

  responder(res, 404, { found: false, erro: "rota nao encontrada" });
});

server.listen(PORT, () => {
  console.log(`buscar-video rodando na porta ${PORT}`);
});
