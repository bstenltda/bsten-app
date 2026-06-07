# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, ListFlowable, ListItem, HRFlowable, PageBreak)

GREEN = colors.HexColor("#00aa55"); DGREEN = colors.HexColor("#008844")
BLUE = colors.HexColor("#0066aa"); LIGHT = colors.HexColor("#eef7f0")
GREY = colors.HexColor("#777777"); REDBG = colors.HexColor("#fff0f0")
RED = colors.HexColor("#cc3322"); AMBER = colors.HexColor("#e6a700")
AMBBG = colors.HexColor("#fff7e6")

styles = getSampleStyleSheet()
def S(name, **kw):
    base = kw.pop("parent", styles["Normal"]); return ParagraphStyle(name, parent=base, **kw)
body = S("body", fontSize=10, leading=14, spaceAfter=5)
h1 = S("h1", fontSize=21, leading=24, textColor=GREEN, spaceAfter=2, fontName="Helvetica-Bold")
suby = S("sub", fontSize=9.5, leading=12, textColor=GREY, spaceAfter=10)
h2 = S("h2", fontSize=14, leading=17, textColor=DGREEN, spaceBefore=16, spaceAfter=4, fontName="Helvetica-Bold")
h3 = S("h3", fontSize=11.5, leading=14, textColor=BLUE, spaceBefore=8, spaceAfter=2, fontName="Helvetica-Bold")
boxst = S("box", fontSize=10, leading=14, backColor=LIGHT, leftIndent=8, rightIndent=8,
          spaceBefore=6, spaceAfter=8, borderPadding=(7,7,7,7))
redbox = S("redbox", fontSize=10, leading=14, backColor=REDBG, textColor=colors.HexColor("#882222"),
           leftIndent=8, rightIndent=8, spaceBefore=6, spaceAfter=8, borderPadding=(7,7,7,7))
ambbox = S("ambbox", fontSize=10, leading=14, backColor=AMBBG, leftIndent=8, rightIndent=8,
           spaceBefore=6, spaceAfter=8, borderPadding=(7,7,7,7))
quote = S("quote", fontSize=10, leading=14, textColor=colors.HexColor("#333333"),
          leftIndent=14, spaceAfter=2, fontName="Helvetica-Oblique")
muted = S("muted", fontSize=9, leading=12, textColor=GREY, spaceAfter=6)

story = []
def P(t, s=body): story.append(Paragraph(t, s))
def SP(h=6): story.append(Spacer(1, h))
def Q(t): story.append(Paragraph("“"+t+"”", quote))
def bullets(items, s=body):
    its=[ListItem(Paragraph(x, s), leftIndent=12) for x in items]
    story.append(ListFlowable(its, bulletType="bullet", start="•", bulletColor=GREEN, leftIndent=14, spaceAfter=6))
def numbered(items, s=body):
    its=[ListItem(Paragraph(x, s)) for x in items]
    story.append(ListFlowable(its, bulletType="1", leftIndent=16, spaceAfter=6))
cs = S("cell", fontSize=9, leading=12)
cb = S("cellb", fontSize=9, leading=12, fontName="Helvetica-Bold", textColor=DGREEN)
def cell(t, s=None): return Paragraph(t, s or cs)
def table(rows, col_widths, header=True):
    t=Table(rows, colWidths=col_widths, repeatRows=1 if header else 0)
    cmds=[("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#bbbbbb")),("VALIGN",(0,0),(-1,-1),"TOP"),
          ("FONTSIZE",(0,0),(-1,-1),9),("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),
          ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4)]
    if header: cmds+=[("BACKGROUND",(0,0),(-1,0),LIGHT),("TEXTCOLOR",(0,0),(-1,0),DGREEN),("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")]
    t.setStyle(TableStyle(cmds)); story.append(t); SP(8)
def hr(): story.append(HRFlowable(width="100%", color=colors.HexColor("#dddddd"), spaceBefore=10, spaceAfter=10))

# ===== CAPA / TÍTULO =====
P("BSTEN PRO BLINDADO — Documento Mestre (Memória)", h1)
P("Tudo o que vale hoje na BSTEN: produto, preços, estratégia, regras do bot e fluxo de vendas · Atualizado em 07/06/2026", suby)
P("<b>O que é este documento:</b> a fotografia consolidada de todas as decisões tomadas até hoje — produto, "
  "posicionamento, regras de atendimento do bot (formatação, coleta de dados, objeções) e fluxo comercial. "
  "Serve como memória única e como briefing para qualquer pessoa ou IA que for trabalhar a marca.", boxst)

# ===== 1. EMPRESA =====
P("1. A empresa", h2)
table([
 [cell("Razão social", cb), cell("Bsten LTDA (fantasia: Bsten)")],
 [cell("CNPJ", cb), cell("17.867.757/0001-80 — Ativa")],
 [cell("Desde", cb), cell("2013 (mais de 10 anos)")],
 [cell("Sede", cb), cell("Sumaré – SP (Rua José Vedovatto, 1903, Sala 9 — Jardim Bom Retiro / Nova Veneza — CEP 13181-680)")],
 [cell("Envio", cb), cell("Todo o Brasil, frete grátis")],
 [cell("Venda/atendimento", cb), cell("100% WhatsApp (5519971478541) — sem loja física. Seg–sex 9h–17h; app 24h")],
 [cell("Instagram", cb), cell("@bsten_ofc")],
], [3.3*cm, 12.7*cm], header=False)

# ===== 2. PRODUTO =====
P("2. Produto — BSTEN PRO BLINDADO", h2)
P("Não é \"rastreador comum\": é um <b>sistema de proteção e controle veicular</b>. O cliente acompanha e "
  "<b>bloqueia</b> o veículo pelo celular, com autonomia total (sem central humana).")
P("Equipamento", h3)
bullets([
 "Oculto no veículo · tecnologia <b>4G + 2G</b> · <b>chip multioperadora</b>",
 "<b>Módulo de bloqueio remoto incluso</b> (nunca \"relé grátis\"/brinde)",
 "<b>Bateria de lítio interna de backup</b> (funciona mesmo se cortarem a energia)",
 "Compatível com <b>carro, moto e caminhão</b> (8–90V) · homologado <b>Anatel</b> (04695-25-16219)",
])
P("Diferencial \"chega pronto pra usar\"", h3)
P("O aparelho sai da base <b>testado</b> e com o <b>app já configurado</b> (usuário e senha no nome do cliente). "
  "Na instalação, a equipe BSTEN <b>orienta e dá suporte ao profissional</b>.")
P("App BSTEN PRO (24h)", h3)
bullets([
 "Localização em tempo real · bloqueio remoto pelo app",
 "Função Âncora (área virtual + alerta de movimentação)",
 "Histórico de rotas · alertas inteligentes · Street View",
])

# ===== 3. KIT + PREÇOS =====
P("3. Kit e condições comerciais", h2)
bullets([
 "Rastreador 4G+2G blindado · módulo de bloqueio incluso · chip multioperadora · app BSTEN PRO",
 "Frete grátis · sem fidelidade · 15 dias de uso da plataforma sem cobrança",
])
table([
 [cell("Item", cb), cell("Valor", cb), cell("Observação", cb)],
 [cell("Equipamento"), cell("<b>R$ 139,97</b>"), cell("Compra única · frete grátis")],
 [cell("Plataforma/app"), cell("<b>R$ 35,97/mês</b>"), cell("Sem fidelidade · cobra só após 15 dias")],
 [cell("Teste sem risco"), cell("<b>15 dias grátis</b>"), cell("Instala, usa e conhece antes da 1ª cobrança")],
], [5.5*cm, 3.5*cm, 7*cm])

# ===== 4. POSICIONAMENTO =====
P("4. Posicionamento e neurovendas", h2)
bullets([
 "<b>Vender consequências, não componentes:</b> localização em tempo real, controle pelo celular, bloqueio na hora, autonomia, proteção.",
 "<b>Valor antes do preço:</b> construir desejo (demonstração + app + 15 dias) antes do número.",
 "<b>Headline principal:</b> \"Mais do que rastrear. Tenha controle.\"",
 "Nome comercial único: <b>BSTEN PRO BLINDADO</b> (nunca citar nomes internos de plano).",
])

story.append(PageBreak())

# ===== 5. REGRAS DO BOT (MEMÓRIA DAS DECISÕES) =====
P("5. Regras do bot — decisões consolidadas", h2)
P("Estas são as correções acumuladas das auditorias de conversas reais. Valem para o prompt do bot e para a equipe humana.", muted)

P("5.1 Formatação das mensagens (WhatsApp)", h3)
bullets([
 "<b>Fracionar</b> em 2-4 mensagens curtas (máx ~2 linhas), uma ideia por mensagem.",
 "<b>*negrito*</b> (asterisco simples) só em palavras-chave: produto, valor, benefício, garantia.",
 "<b>_itálico_</b> para ênfase leve (ex.: _sem fidelidade_, _testado_).",
 "Máx 1 emoji por mensagem. Sempre terminar com <b>uma pergunta</b> que conduz o próximo passo.",
 "PROIBIDO: <b>negrito duplo</b>, ###, listas numeradas (1. 2. 3.), bullets.",
])
P("5.2 Erros que NÃO podem mais acontecer", h3)
P("Nunca escrever o próprio rótulo no texto (ex.: começar com \"BSTEN:\"). Nunca repetir a saudação "
  "(saúda uma vez só). Nunca enviar duas mensagens que se contradizem. Nunca dizer \"tive um problema técnico\".", redbox)

P("5.3 Coleta de dados — CPF por último (evita rejeição)", h3)
P("CPF <b>nunca a frio</b>. Mesmo no \"quero contratar\", qualificar primeiro e reservar só com nome + WhatsApp. "
  "CPF + e-mail só no passo final, pra emitir a nota — já transferindo pra equipe.", ambbox)
numbered([
 "Qualificar: veículo (carro/moto/caminhão) + cidade de envio.",
 "Reservar: <b>nome completo</b> + <b>melhor WhatsApp com DDD</b>.",
 "Finalizar (último passo): <b>e-mail</b> + <b>CPF</b> — \"pra emitir sua nota\".",
])

P("5.4 Autonomia e situações", h3)
bullets([
 "Sem central humana: o cliente bloqueia pelo app. Nunca \"nossa central monitora/recupera\".",
 "Roubo/furto: remove emoji, não vende, não pede CPF/placa, registra e (no horário) oferece transferir.",
 "Cliente existente: para de vender, reconhece e transfere.",
 "Ativação (IMEI) só quando o cliente JÁ tem o aparelho (\"comprei/recebi/chegou\"). \"Quero contratar\" = comercial, nunca IMEI.",
])

# ===== 6. FLUXO COMERCIAL =====
P("6. Fluxo comercial (valor → preço → reserva → CPF no fim)", h2)
P("E1 — Acolher + veículo", h3)
Q("Olá! Que bom que você veio 😊"); Q("O *BSTEN PRO BLINDADO* deixa você acompanhar e *bloquear* o veículo pelo celular."); Q("É pra carro, moto ou caminhão?")
P("E2 — Cidade (envio) · E3 — Objetivo (segurança / localização / os dois)", h3)
P("E4 — Demonstração (espelha o objetivo) + E5 — Teste sem risco (15 dias)", h3)
P("E6 — Preço (fracionado, só após 1 qualificação)", h3)
Q("O equipamento é *R$ 139,97* 😊 compra única, com frete grátis."); Q("A plataforma fica *R$ 35,97/mês*, sem fidelidade — e os _primeiros 15 dias são sem cobrança_."); Q("Quer que eu já reserve o seu?")
P("E7 — Reserva e fechamento", h3)
Q("Pra já reservar, me passa seu *nome completo* e o melhor *WhatsApp com DDD* 😊")
Q("(no fim, emitir nota) Por último, pra emitir sua nota: seu *e-mail* e *CPF* 😊")

# ===== 7. OBJEÇÕES =====
P("7. Objeções — respostas-modelo", h2)
P("\"Quem instala? / e pra pôr na moto?\"", h3)
Q("Fica tranquilo 😊"); Q("O aparelho já sai da base *pronto e testado*, com o app configurado e seu usuário e senha."); Q("A instalação é simples: dá pra fazer numa auto elétrica de confiança, e a _nossa equipe orienta o profissional_.")
P("(Não afirmar que a BSTEN instala em todo o Brasil; não prometer instalador por região.)", muted)
P("\"E se não funcionar?\"", h3)
Q("Pode ficar tranquilo 😊"); Q("O aparelho sai daqui *testado* e já configurado — então chega funcionando."); Q("E se aparecer qualquer coisa na instalação, a _nossa equipe dá o suporte_ e orienta o profissional na hora. Você não fica na mão.")
P("(Sem inventar prazo de garantia — pendente confirmar o prazo oficial.)", muted)
P("\"Tá caro\" / \"Vou pensar\"", h3)
bullets([
 "\"Tá caro\" → reforça 15 dias sem cobrança + sem fidelidade (nunca dar desconto).",
 "\"Vou pensar\" → \"Claro 😊 Qualquer dúvida estou por aqui.\" (não pressiona)",
])

story.append(PageBreak())

# ===== 8. VÍDEOS =====
P("8. Os 15 vídeos (apoio à venda)", h2)
vr=[[cell("#",cb),cell("Tema",cb),cell("Mensagem central",cb)]]
for n,t,m in [("1","Como funciona o bloqueio","Autonomia — bloqueia pelo app, na hora"),
 ("2","Rastreamento","Tempo real, histórico, alertas"),("3","E se roubarem?","Decisão rápida com info na hora"),
 ("4","Quem instala","Profissional + suporte da equipe"),("5","O que vem no kit","Bloqueio incluso, chip, app, frete grátis"),
 ("6","Carro/moto/caminhão","Compatibilidade 8–90V"),("7","Se desligarem a bateria","Bateria interna de reserva"),
 ("8","Chip multioperadora","Mais conexão, sempre conectado"),("9","Tem fidelidade?","Não — liberdade e transparência"),
 ("10","Quanto custa","R$ 139,97 + R$ 35,97/mês + 15 dias grátis"),("11","Função âncora","Área virtual + alerta"),
 ("12","Quem é a Bsten","Especializada, autonomia, Brasil todo"),("13","Por que PRO BLINDADO","Segurança operacional"),
 ("14","Depender de central?","Não — autonomia pelo app"),("15","Por que escolher","Tech + autonomia + sem fidelidade")]:
    vr.append([cell(n),cell(t),cell(m)])
table(vr, [1*cm,5.5*cm,9.5*cm])

# ===== 9. LANDING =====
P("9. Landing page (estrutura, 8 seções)", h2)
numbered([
 "Headline + botão \"Quero proteger meu veículo\"","Vídeo do produto","Benefício: \"Localize e bloqueie pelo celular\"",
 "BSTEN PRO BLINDADO (herói)","App BSTEN PRO (tempo real, âncora, histórico, alertas)",
 "Teste sem risco — 15 dias (\"Compre sem pressão\")","Condições: R$ 139,97 · R$ 35,97/mês · frete grátis · sem fidelidade","WhatsApp (CTA final)",
])

# ===== 10. MÍDIA =====
P("10. Mídia / campanhas", h2)
bullets([
 "Meta Ads: Landing (Brasil) + Click-to-WhatsApp Conversas (Brasil). Lead Form a corrigir p/ Brasil.",
 "Meta Pixel 1889198695087796 · Página 1101848589687022 · IG @bsten_ofc",
 "Maiores ralos: leads fora do horário (anúncio 24/7 x atendimento 9–17h) e tempo de resposta.",
])

# ===== 11. PENDÊNCIAS =====
P("11. Pendências (por impacto)", h2)
numbered([
 "<b>Subir docs v8 no Botclick</b> (01_GERAL na aba Prompt + 02_COMERCIAL/produto nos DOCS) — bug \"BSTEN:\" ainda aparece porque não foi atualizado.",
 "<b>Confirmar prazo de garantia</b> do equipamento → vira âncora na objeção \"e se não funcionar?\".",
 "<b>Follow-up</b> de lead que deu nome+WhatsApp e sumiu antes do CPF (maior recuperador de venda).",
 "<b>24/7</b>: cobrir leads fora do horário (bot reserva + equipe confirma no dia útil).",
 "<b>Painel/infra</b>: monitor + auto-restart + backup (já criado backup-github.sh).",
 "<b>Landing</b>: reescrever com headline de dor + encaixar os 15 vídeos.",
 "<b>Segurança/LGPD</b>: rotacionar chaves, trocar senha do painel, consentimento/retenção de PII.",
])

hr()
P("Bsten LTDA · CNPJ 17.867.757/0001-80 · adsbs.com.br · WhatsApp 5519971478541 · "
  "Documento sem dados sigilosos (senhas/chaves ficam fora). Atualizado em 07/06/2026.", muted)

doc=SimpleDocTemplate("/home/user/bsten-app/BSTEN_DOC_MESTRE.pdf", pagesize=A4,
     topMargin=1.7*cm, bottomMargin=1.5*cm, leftMargin=1.8*cm, rightMargin=1.8*cm,
     title="BSTEN PRO BLINDADO - Documento Mestre", author="Bsten LTDA")
doc.build(story)
print("PDF mestre gerado")
