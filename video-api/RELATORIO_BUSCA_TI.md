# Relatório — ajustes na API de busca (buscar-video)

Baseado em teste real do bot. O endpoint está respondendo (ótimo!), mas precisa de 4 ajustes pra parar a "bagunça". Tudo aqui é do lado do **servidor/portal**, não do prompt do bot.

## 1. Matching frágil (acha por sorte, depende da palavra exata)
No teste: `q=como funciona o rastreador` → **found:false**; `q=como funciona o rastreamento` → **found:true** (mesma intenção!).
- Precisa de busca **fuzzy / por sinônimos / por palavra-chave**, não match exato.
- Ex.: "rastreador" ≈ "rastreamento" ≈ "gps" ≈ "localização"; "valor" ≈ "preço" ≈ "quanto custa"; "bloqueio" ≈ "desligar" ≈ "trava".
- Sugestão: normalizar (minúsculas, sem acento), quebrar em tokens e casar por tags/keywords de cada item do catálogo, com score. Retornar o de maior score; só `found:false` se nada passar de um limiar baixo.

## 2. Miniatura ≠ link (clica no link abre o vídeo certo; na miniatura abre o errado)
A prévia que o WhatsApp monta vem das **meta tags OG da página `/v/...`**. Hoje parece que todas as páginas compartilham a mesma OG (ou OG genérica), então a miniatura não bate com o vídeo.
- Cada página `/v/<slug>` precisa de OG **própria**: `og:title`, `og:description`, `og:image` (thumb daquele vídeo) e `og:video`.
- Sem isso, a miniatura sempre mostra "o vídeo errado".

## 3. Tipo de URL inconsistente
Às vezes a API devolve a **página** `/v/...` (com botão "Voltar pro WhatsApp" + rastreio — ✅ o ideal), às vezes o **.mp4 cru** (`/assets/v-...mp4` — sem botão, sem rastreio).
- Padronizar: **sempre** devolver a página `/v/<slug>` (nunca o .mp4 direto).

## 4. Dados técnicos (porta/APN por modelo) não estão na busca
No teste: `q=porta do coban` → **found:false**, mas o portal TEM a ferramenta "Qual a porta do seu rastreador?" (GT06, TK103, FMB920, Coban...).
- Decidir: **(a)** indexar essa tabela técnica no mesmo endpoint `buscar-video` (retornando type=texto/dado), ou **(b)** criar um 2º endpoint (ex.: `/api/porta?modelo=coban`) e o bot ganha uma 2ª ferramenta.
- Hoje o bot só tem a ferramenta de vídeo/tutorial — ele não alcança esse dado.

## 5. (Checar) prefixo "BSTEN:" nas respostas
Toda resposta do bot sai com "BSTEN:" na frente. O prompt proíbe isso — então provavelmente é um **campo de nome do agente** no Botclik sendo prefixado, OU algo no template da ferramenta. Verificar a config do agente/fluxo no Botclik.

---
Prioridade: **2 e 3** (miniatura/URL) resolvem a "bagunça" visual; **1** melhora a taxa de acerto; **4** é decisão de produto.
