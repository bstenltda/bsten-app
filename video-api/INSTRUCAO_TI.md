# Instrução de Deploy — Endpoint "Buscar Vídeo" (BSTEN)

**Objetivo:** subir um endpoint Node na VPS que recebe a dúvida do cliente e devolve o link do vídeo/tutorial correspondente. O bot (Botclik) consulta esse endpoint na conversa.

**Stack:** Node.js + PM2 + nginx (reverse proxy). Sem dependências externas (só Node puro).

**Arquivos (entregues nesta pasta):**
- `server.js` — o servidor HTTP
- `buscar-video.js` — lógica de busca
- `videos.json` — catálogo (FONTE ÚNICA; é o único arquivo que o cliente edita depois)

---

## 1. Colocar os arquivos na VPS
Criar uma pasta, ex.: `/opt/buscar-video/`, e copiar os 3 arquivos para lá.
```bash
mkdir -p /opt/buscar-video
# copiar server.js, buscar-video.js e videos.json para /opt/buscar-video/
cd /opt/buscar-video
node -v   # confirmar que o Node está instalado (v16+)
```

## 2. Subir com PM2
```bash
cd /opt/buscar-video
PORT=3001 pm2 start server.js --name buscar-video
pm2 save
```
Testar localmente:
```bash
curl "http://localhost:3001/api/buscar-video?q=como funciona o bloqueio"
# Esperado: {"found":true,"title":"...","url":"https://adsbs.com.br/assets/v-...mp4",...}
```

## 3. Expor via nginx (no server block do adsbs.com.br)
Adicionar este `location` dentro do `server { ... }` do `adsbs.com.br` (HTTPS):
```nginx
location /api/buscar-video {
    proxy_pass http://127.0.0.1:3001/api/buscar-video;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```
Recarregar:
```bash
nginx -t && systemctl reload nginx
```
Testar pela internet:
```bash
curl "https://adsbs.com.br/api/buscar-video?q=serve pra moto"
```

## 4. Atualizar o catálogo no futuro (sem reiniciar)
O `server.js` lê o `videos.json` a CADA requisição. Então, para adicionar/remover vídeo, basta **editar o `videos.json`** e salvar — não precisa reiniciar o PM2.
- Ativar um tutorial: trocar `"url": null` pela URL real.
- Desativar: voltar para `"url": null` (o bot deixa de enviar).

## 5. Configurar no Botclik (ferramenta HTTP Request)
- Método: **GET**
- URL: **https://adsbs.com.br/api/buscar-video**
- Parâmetro de query: **q** = dúvida resumida do cliente
- Autenticação: nenhuma (opcional: API Key)
- Timeout: 8s
- Instruções para a IA:
```
Use esta ferramenta quando o cliente pedir vídeo, tutorial, demonstração, "me mostra",
"como funciona", ou ajuda passo a passo (senha, boleto, âncora, app, alertas, histórico).
Envie a dúvida resumida em q.
Se found=true, mande uma frase curta + o url e retome com uma pergunta.
Se found=false, NÃO invente link: responda em texto e, se for suporte, encaminhe à equipe.
```

## Resposta do endpoint
```json
{ "found": true, "title": "Como funciona o bloqueio",
  "url": "https://adsbs.com.br/assets/v-como-funciona-o-bloqueio.mp4",
  "theme": "bloqueio", "type": "video" }
```
Sem correspondência (ou tutorial sem URL ainda):
```json
{ "found": false }
```

## Observações de segurança (opcional)
- Pode proteger o endpoint com API Key (header) e configurar a mesma key no Botclik.
- O endpoint só lê o catálogo; não grava nada.
