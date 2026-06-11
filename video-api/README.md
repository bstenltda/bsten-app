# API de Busca de Vídeos/Tutoriais — BSTEN

Endpoint que recebe a dúvida do cliente e devolve o link certo do catálogo.
O bot (Botclik, ferramenta HTTP Request) chama isso durante a conversa: se achar, manda o link; se não, não manda (responde em texto). Você NUNCA mais mexe nos documentos do bot — só no `videos.json`.

## ✏️ Como adicionar/remover vídeo (a única coisa que você faz)
Edite SÓ o `videos.json`. Cada item:
```json
{
  "tema": "boleto",
  "titulo": "Como emitir 2ª via do boleto",
  "tipo": "tutorial",
  "url": "https://adsbs.com.br/assets/v-boleto.mp4",
  "keywords": ["boleto", "segunda via", "ver boleto", "fatura"]
}
```
- Para ativar um tutorial: troque `"url": null` pela URL real.
- Para desativar: volte para `"url": null` (o bot deixa de enviar).
- `keywords` = as palavras que o cliente costuma usar. Quanto mais, melhor o acerto.

## 🚀 Deploy — escolha 1 das opções

### Opção A — Netlify Functions (se adsbs.com.br está na Netlify)
1. Crie a pasta `netlify/functions/` e coloque lá `buscar-video.js` + `videos.json`.
2. No `netlify.toml` adicione um atalho de URL:
   ```toml
   [[redirects]]
     from = "/api/buscar-video"
     to = "/.netlify/functions/buscar-video"
     status = 200
   ```
3. Deploy. Endpoint final: `https://adsbs.com.br/api/buscar-video?q=...`

### Opção B — Servidor PHP (VPS/cPanel — mais universal)
1. Suba `buscar-video.php` + `videos.json` para uma pasta pública, ex.: `/api/`.
2. Endpoint final: `https://adsbs.com.br/api/buscar-video.php?q=...`

### Opção C — VPS com Node
`buscar-video.js` já exporta `handler`. Pode rodar atrás de um Express/serverless. (Posso montar o server.js se precisar.)

## ✅ Testar (curl)
```
curl "https://adsbs.com.br/api/buscar-video?q=como%20funciona%20o%20bloqueio"
# => {"found":true,"title":"Como funciona o bloqueio","url":"...","theme":"bloqueio","type":"video"}

curl "https://adsbs.com.br/api/buscar-video?q=ver%20boleto"
# => {"found":false}   (enquanto o tutorial de boleto não tiver URL)
```

## 🤖 Configuração no Botclik (ferramenta HTTP Request)
- **Nome interno:** Buscar vídeo/tutorial
- **Método:** GET
- **URL:** `https://adsbs.com.br/api/buscar-video`
- **Parâmetro (query):** `q` = a dúvida resumida do cliente
- **Autenticação:** Sem autenticação (ou API Key, se quiser proteger)
- **Timeout:** 8s

**Instruções para a IA (cole no campo de instruções da ferramenta):**
```
Use esta ferramenta quando o cliente pedir vídeo, tutorial, demonstração, "me mostra",
"como funciona", ou ajuda passo a passo (senha, boleto, âncora, app, alertas, histórico).
Envie a dúvida resumida em q (ex.: q="como ver o boleto").
Se a resposta vier found=true, mande UMA frase curta + o url (ex.: "Olha esse rapidinho 😊" + url)
e depois retome com uma pergunta.
Se found=false, NÃO invente link: responda em texto e, se for suporte, encaminhe para a equipe.
```

## Como funciona por dentro
`videos.json` (catálogo) → `buscar-video` (normaliza a dúvida, pontua por keywords, escolhe o melhor) → retorna `{found,url,...}`. Itens com `url:null` retornam `found:false` (não enviam).
