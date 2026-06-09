# CLAUDE.md — Memória do Projeto BSTEN (ler sempre no início)

> Este arquivo é a memória persistente. NÃO perder nada daqui. Atualizar quando algo mudar.

## ⛔ LIMITES DO BOTCLICK (crítico — já foi esquecido uma vez)
- Campo **PROMPT** (01_GERAL): máximo **10.000 caracteres**.
- Cada **DOC**: máximo **2.000 caracteres**.
- Por isso o COMERCIAL foi dividido em 3 (02a/02b/02c) e os VÍDEOS em 2 (08a/08b).
- SEMPRE medir com `wc -m` antes de entregar. Nenhum doc pode passar de 2.000; prompt não passa de 10.000.

## 📁 Estrutura dos docs do bot (pasta botclick/)
PROMPT (só este): `01_GERAL_PROMPT.md`
DOCS: `02a_COMERCIAL_FLUXO` · `02b_COMERCIAL_PERGUNTAS` · `02c_COMERCIAL_GATILHOS` · `03_SUPORTE` · `04_FINANCEIRO` · `05_ATIVACAO` · `06_COMPORTAMENTO` · `07_EMPRESA` · `08a_VIDEOS_VENDA` · `08b_VIDEOS_SUPORTE_LINKS` · `produto_BSTEN_PRO_BLINDADO`
`LEIA-ME.md` = guia interno, NÃO sobe no bot. Plataforma: Botclick (WhatsApp + IA por prompt). CLI não acessa o painel — entrego os arquivos prontos e o usuário cola.

## 🏢 Empresa
- Bsten LTDA · CNPJ 17.867.757/0001-80 (ativa) · desde 2013 · sede Sumaré-SP (Rua José Vedovatto, 1903, Sala 9, Jardim Bom Retiro/Nova Veneza, CEP 13181-680)
- Atende todo o Brasil, frete grátis. Sem loja física. Canal: só WhatsApp 5519971478541.
- E-mail oficial (ÚNICO): gpsbspaga@gmail.com · Instagram @bsten_ofc
- Usuário/dono: Francisco Santos (adm.bsten@gmail.com)

## 📦 Produto — BSTEN PRO BLINDADO (nome comercial ÚNICO)
- Sistema de proteção e controle (não "rastreador comum"). 4G+2G, oculto, chip multioperadora, módulo de bloqueio remoto incluso, bateria lítio backup, Anatel (04695-25-16219), 8–90V (carro/moto/caminhão).
- Chega PRONTO: testado + app configurado (usuário e senha do cliente).
- App BSTEN PRO: tempo real, bloqueio, função âncora, histórico, alertas, Street View.
- Preços: equipamento *R$ 139,97* (única, frete grátis) + plataforma *R$ 35,97/mês* (sem fidelidade). 15 dias sem cobrança. Âncora: ~R$ 1,20/dia.
- Pagamento: ANTECIPADO, só Pix ou boleto. NÃO tem cartão, NÃO tem pagamento na entrega.
- NUNCA citar: BSTEN Solo/Smart/Start/Plus, 11 cidades, DDD 19.

## 💰 CHIP E RECORRÊNCIA (crítico — onde está o faturamento)
- Maior faturamento = RECORRÊNCIA mensal (chip + plataforma da BSTEN). Chip multioperadora INCLUSO (2G+3G+4G), sempre o NOSSO.
- NUNCA o bot pode dizer "compre o chip por fora / use chip próprio / troque só o chip" — isso mata a recorrência. Não abrir brecha.
- NÃO existe "chip 4G/5G" nem "trocar chip 2G por 4G": 2G/4G é o APARELHO, não o chip. IA não inventa — não sabe, transfere.
- Cliente com rastreador 2G = NEUROVENDA: oferecer UPGRADE do APARELHO 4G (última geração, multioperadora), condição especial por ser cliente, sem aumentar mensalidade → encaminhar à equipe (equipe define o preço; bot não inventa valor). Doc: 02d_COMERCIAL_CHIP_UPGRADE.

## 🔗 Links oficiais (nunca inventar outro)
- Vídeos: https://adsbs.com.br/assets/v-*.mp4 (lista em 08a) + imagens img-*.png
- Busca de instaladores em todo o Brasil: https://bstentec.com.br/busca (enviar em qualquer dúvida sobre instalador)
- Landing: adsbs.com.br · Painel: painel.adsbs.com.br

## 🤖 Persona e regras-chave do bot
- Nome do atendente: **Francisco Santos** (nunca "Bia"). Apresenta-se 1x.
- CONECTAR ANTES DE AGIR: situação incerta → 1 pergunta. Só "bom dia" sem pergunta → saudar + "como ajudar?", NUNCA despejar preço/specs.
- CPF por último: qualifica (veículo/cidade) → reserva com nome+WhatsApp → CPF/e-mail só no fim (nota).
- NUNCA inventar telefone/e-mail/forma de pagamento/link/garantia/nº de clientes.
- Formato WhatsApp: fracionar 2-3 msgs, *negrito*/_itálico_ nativos; PROIBIDO **negrito duplo**, ###, listas, bullets. Nunca escrever "BSTEN:" nem duplicar msg. Máx 1 emoji.
- Suporte ≠ roubo: "carro não liga" = suporte (perguntar do bloqueio), não emergência. Crítica = só roubo/furto.
- Cliente existente / "já tenho rastreador" → não vende, conecta e direciona.
- Assistente NÃO manda áudio → manda vídeo (link). "Alto reverso": vídeo abre dando play + botão "Voltar pro WhatsApp".
- Gatilhos éticos: âncora R$1,20/dia, risco zero (15 dias+sem fidelidade), posse futura, poder na mão, fechamento assumido. PROIBIDO escassez falsa/desconto/depoimento inventado.
- Confiança ("não confio"): CNPJ verificável + Instagram + Pix em nome da BSTEN LTDA + risco zero + vídeo.
- NÃO SABE / NÃO TEM ACESSO (status de chip, ICCID, "está ativo/4G?"): nunca inventa, NUNCA manda procurar a operadora/terceiro → encaminha pra EQUIPE BSTEN (do assunto; se não souber o setor, transfere mesmo assim).
- CADA CONTATO É NOVO: não retomar conversas antigas por conta própria. "oi" = recomeça do zero. (Botclick puxa histórico longo — se persistir, reduzir a janela de memória nas config do bot.)

## 📣 Meta Ads (conta bsten, id 2042341952909252, BRL)
- Campanha 1: BSTEN_LANDING_BR_CONVERSAO_v1 (LINK_CLICKS, otimiza visita à página — "cega" p/ venda, falta evento Contact no Pixel). Pixel 1889198695087796.
- Campanha 2: BSTEN_WHATSAPP_BR_CONVERSAS_v1 (Conversas) — a que converte. Custo/conversa ~R$ 3,47. Orçamento aumentado p/ **R$ 40/dia** em 07/06 (Meta pausa ao editar budget → reativar sempre).
- Ambas vinham sub-entregando (~R$3/dia de R$25). Gargalo real = pós-clique (bot + follow-up).
- Posso editar campanhas via MCP (ads_update_entity / ads_activate_entity).

## 🔧 Infra
- VPS Hetzner root@178.156.182.239 (acesso por chave SSH bsten_vps no PC do usuário; CLI não acessa). Script backup-github.sh faz commit+push dos 3 repos.
- Repos: bsten-app (este), bsten-admin, bsten-landing, rastreapro, adsbs (funil, fora do escopo desta sessão), controlebs, bstecnico, bsten-ads-dashboard.
- PDFs gerados via reportlab (gen_pdf.py, gen_pdf_master.py). LibreOffice e fpdf2 estão quebrados no ambiente.

## 🌿 Git
- Branch de trabalho: **claude/oi-ZYvfp**. PR #2 (draft) com deploy preview Netlify (eventos do Netlify = ruído, sem ação).
- Fluxo: edita docs → mede chars → regenera zip (`zip -j ../botclick_bsten_pro_blindado.zip *.md`) → commit → push → envia arquivos ao usuário.

## ✅ Pendências
1. Usuário subir o pacote no Botclick (trocar tudo) e testar.
2. Vídeo "Preciso depender de central" (falta URL). Tutoriais de suporte (senha, boleto, âncora, app, alertas, histórico) — URLs a preencher quando criados.
3. Confirmar prazo de garantia (vira âncora na objeção de risco).
4. Funil de follow-up (lead que deu nome+WhatsApp e sumiu antes do CPF).
5. Evento Contact no Pixel da landing (destrava a campanha de Landing).
6. Mapa dos vídeos na landing (8 seções).
7. Confirmar Pix cadastrado em nome da BSTEN LTDA (confiança no pagamento).
8. Botões de entrada (ice breakers) do WhatsApp: "Quero contratar / Preço / Como funciona / Ser instalador".
9. Segurança/LGPD: rotacionar chaves, trocar senha do painel (bsten2026), consentimento PII.
