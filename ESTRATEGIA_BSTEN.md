# 📌 Estratégia BSTEN — versão atual (atualizado em 04/06/2026)

> Documento vivo de estratégia. **Sem segredos** (senhas/keys ficam no `.env` do servidor / cofre).
> Sempre que a estratégia mudar, atualizar aqui.

---

## 🔄 MUDANÇA-CHAVE (jun/2026): produto ÚNICO e nacional

A BSTEN **simplificou o portfólio** para um só produto, vendido no **Brasil inteiro**:

- **Produto:** **BSTEN Solo** (rastreador 4G, homologado Anatel)
- **Aparelho:** **R$ 139,97** — compra única, é do cliente · frete grátis (PAC), de Sumaré-SP · prazo 5–15 dias úteis
- **Mensalidade:** **R$ 35,97/mês**
- **Fidelidade:** nenhuma (cancela quando quiser)
- **Abrangência:** **nacional** — qualquer cidade do Brasil
- **Instalação:** por conta do cliente (lista de instaladores)
- **Preço transparente desde o início** (não esconde mais o valor)

### ❌ O que saiu (não usar mais)
- Planos **Start** e **Plus** (não existem mais)
- Roteamento por cidade / **DDD 19** / **"11 cidades"** (Campinas) — só permanecem como *regra de proibição* pro bot NÃO citar
- Taxa de R$ 200 / permanência de 12 meses

---

## 🎯 Funil de venda

```
Anúncio (Meta) ──> Landing (adsbs.com.br)  ──┐
                                             ├─> WhatsApp (bot) ─> Atendente humano
Anúncio (Click-to-WhatsApp) ─────────────────┘
```

- **Landing:** https://adsbs.com.br/  (vídeo + CTA WhatsApp)
- **WhatsApp de atendimento (bot):** `5519971478541` (número verificado "Atendimento Bsten Rastreamento")
- **Bot:** acolhe, apresenta o Solo com preço transparente, qualifica e encaminha pro humano (seg–sex 9h–17h)
- **Painel comercial:** https://painel.adsbs.com.br (app `bsten-admin` no VPS)

---

## 📣 Estratégia de anúncios (Meta) — conta `bsten` (2042341952909252, BRL)

**Princípio:** como o produto é nacional, **todas as campanhas miram o Brasil inteiro**. Otimizar para a ação que indica comprador (visita à página / conversa no WhatsApp), não para clique barato.

| Campanha | Objetivo / otimização | Público | Status |
|---|---|---|---|
| **BSTEN_LANDING_BR_CONVERSAO_v1** | Tráfego → Visualização de Página | Brasil | 🟢 Ativa (R$ 25/dia) |
| **BSTEN_WHATSAPP_BR_CONVERSAS_v1** | Engajamento → Conversas (Click-to-WhatsApp) | Brasil | 🟡 Pausada |
| **BSTEN_LEADS_…_CADASTRO_v1** | Cadastros (Lead Form) | ⚠️ era Campinas → **deve ser Brasil** | 🟡 Pausada |

### Copy padrão (preço transparente, sem citar cidade)
> "Rastreador 4G com app: rastreie e bloqueie pelo celular. **R$ 139,97** o aparelho + **R$ 35,97/mês**, sem fidelidade, frete grátis pra todo o Brasil. Chame no WhatsApp."

---

## ✅ Pendências / próximos passos

1. **Lead Form:** trocar segmentação de *Campinas 45 km* → **Brasil** (Start/Plus não existem mais). Renomear p/ `BR_Nacional_LeadForm`.
2. **WhatsApp Conversas:** apontar destino para `5519971478541` (estava no nº errado 99887-5860/Vendas) → depois **ativar**.
3. **Pixel/landing:** instalar rastreamento de **play do vídeo** (`VideoPlay`) e **clique no WhatsApp** (`Contact`) — o `Contact` permite otimizar a campanha por conversão real.
4. **Painel `bsten-admin`:** manter no ar (`pm2 restart bsten-admin --update-env` quando cair) — senão o painel zera e o webhook de leads para.

---

## 🔧 Ativos técnicos (referência — não-secretos)

- **Meta Pixel ID:** `1889198695087796`
- **Página Facebook:** Bsten (`1101848589687022`) · **Instagram:** `bsten_ofc`
- **WhatsApp atendimento:** `5519971478541`
- **Domínios:** `adsbs.com.br` (landing) · `painel.adsbs.com.br` (painel)
- **Servidor:** VPS Hetzner (Ubuntu) — app em `/opt/bsten-admin` (PM2)

> 🔐 Credenciais e segredos: ver `BSTEN — Mapa de Acessos` + `.env` no servidor / cofre. **Nunca** commitar segredos aqui.

---

## 💡 Aprendizados de mídia (jun/2026)

- Otimizar por **"cliques"** trazia tráfego curioso (CTR alto, CPC baixíssimo, mas ~74% sumiam entre clique e landing) → mudamos para **Visualização de Página / Conversas**.
- O **Click-to-WhatsApp** é o formato mais aderente: leva direto pro bot que já vende, sem o vazamento da landing.
- Medir **play do vídeo** e **clique no WhatsApp** na landing dá sinal de intenção e alimenta a otimização (via Pixel `1889198695087796`).
