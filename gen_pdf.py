# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, ListFlowable, ListItem, HRFlowable)
from reportlab.lib.enums import TA_LEFT

GREEN = colors.HexColor("#00aa55")
DGREEN = colors.HexColor("#008844")
BLUE = colors.HexColor("#0066aa")
LIGHT = colors.HexColor("#eef7f0")
GREY = colors.HexColor("#777777")

styles = getSampleStyleSheet()
def S(name, **kw):
    base = kw.pop("parent", styles["Normal"])
    return ParagraphStyle(name, parent=base, **kw)

body = S("body", fontSize=10, leading=14, spaceAfter=5)
h1 = S("h1", fontSize=21, leading=24, textColor=GREEN, spaceAfter=2, spaceBefore=0, fontName="Helvetica-Bold")
sub = S("sub", fontSize=9.5, leading=12, textColor=GREY, spaceAfter=10)
h2 = S("h2", fontSize=14, leading=17, textColor=DGREEN, spaceBefore=16, spaceAfter=4, fontName="Helvetica-Bold")
h3 = S("h3", fontSize=11.5, leading=14, textColor=BLUE, spaceBefore=8, spaceAfter=2, fontName="Helvetica-Bold")
boxst = S("box", fontSize=10, leading=14, backColor=LIGHT, borderColor=GREEN,
          borderWidth=0, leftIndent=8, rightIndent=8, spaceBefore=6, spaceAfter=8,
          borderPadding=(7,7,7,7))
ital = S("ital", parent=body, fontName="Helvetica-Oblique")
muted = S("muted", fontSize=9, leading=12, textColor=GREY, spaceAfter=6)

story = []
def P(t, s=body): story.append(Paragraph(t, s))
def SP(h=6): story.append(Spacer(1, h))
def bullets(items, s=body):
    its = [ListItem(Paragraph(x, s), leftIndent=12, value=None) for x in items]
    story.append(ListFlowable(its, bulletType="bullet", start="•",
                 bulletColor=GREEN, leftIndent=14, spaceAfter=6))
def numbered(items, s=body):
    its = [ListItem(Paragraph(x, s)) for x in items]
    story.append(ListFlowable(its, bulletType="1", leftIndent=16, spaceAfter=6))

def table(rows, col_widths, header=True):
    t = Table(rows, colWidths=col_widths, repeatRows=1 if header else 0)
    cmds = [
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#bbbbbb")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("FONTSIZE", (0,0), (-1,-1), 9),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]
    if header:
        cmds += [("BACKGROUND", (0,0), (-1,0), LIGHT),
                 ("TEXTCOLOR", (0,0), (-1,0), DGREEN),
                 ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold")]
    t.setStyle(TableStyle(cmds))
    story.append(t)
    SP(8)

def cell(t, s=None):
    return Paragraph(t, s or S("cell", fontSize=9, leading=12))
cb = S("cellb", fontSize=9, leading=12, fontName="Helvetica-Bold", textColor=DGREEN)

# ---------------- CONTENT ----------------
P("BSTEN PRO BLINDADO — Briefing Completo da Empresa", h1)
P("Documento de referência para criação de Landing Page · Tudo o que a empresa oferece hoje e como oferece · Atualizado em 05/06/2026", sub)

P("<b>Como usar este documento:</b> Este briefing reúne tudo o que a BSTEN oferece hoje — produto, "
  "preços, diferenciais, público, canais, vídeos e regras de comunicação. Use-o para pedir a outras "
  "IAs (Gemini, ChatGPT, etc.) propostas de landing page de alta conversão. No final há um roteiro "
  "pronto com o que pedir a cada IA.", boxst)

P("1. A empresa (institucional)", h2)
table([
    [cell("Razão social", cb), cell("Bsten LTDA (nome fantasia: Bsten)")],
    [cell("CNPJ", cb), cell("17.867.757/0001-80 — situação Ativa")],
    [cell("No mercado desde", cb), cell("2013 (mais de 10 anos)")],
    [cell("Sede (matriz)", cb), cell("Sumaré – SP (Rua José Vedovatto, 1903, Sala 9 — Jardim Bom Retiro / Nova Veneza — CEP 13181-680)")],
    [cell("Abrangência", cb), cell("Atende todo o Brasil — envio do equipamento por frete grátis")],
    [cell("Modelo de venda", cb), cell("100% digital, pelo WhatsApp (não há loja/atendimento presencial)")],
], [3.5*cm, 12.5*cm], header=False)
P("Esses dados são usados como prova de credibilidade quando o cliente hesita por segurança "
  "(\"vocês existem mesmo?\", \"qual o CNPJ?\").", muted)

P("2. O produto — BSTEN PRO BLINDADO", h2)
P("<b>Não é um \"rastreador comum\".</b> É um <b>sistema de proteção e controle veicular</b>: o cliente "
  "acompanha e <b>bloqueia</b> o próprio veículo pelo celular, com autonomia total (sem depender de central humana).")
P("Características do equipamento", h3)
bullets([
    "Rastreador desenvolvido para permanecer <b>oculto no veículo</b>",
    "Tecnologia <b>4G + 2G</b> (mais estabilidade de conexão)",
    "<b>Chip multioperadora</b> — conecta na operadora com melhor sinal na região, mantendo o veículo sempre conectado",
    "<b>Módulo de Bloqueio Remoto incluso</b> (parte essencial — nunca tratar como \"brinde\" ou \"relé grátis\")",
    "<b>Bateria interna de lítio de backup</b> — continua funcionando mesmo se desligarem a bateria do veículo",
    "Estrutura resistente à água",
    "Compatível com <b>carro, moto e caminhão</b> (alimentação 8–90V)",
    "Homologado <b>Anatel</b>",
])
P("Aplicativo BSTEN PRO (controle na palma da mão, 24h)", h3)
bullets([
    "Localização em <b>tempo real</b>",
    "<b>Bloqueio remoto</b> do veículo direto pelo app",
    "<b>Função âncora</b> — cria uma área virtual e alerta se o veículo se mover dela",
    "Histórico de rotas / trajetos",
    "Alertas inteligentes de movimentação",
    "Visualização de mapa (incl. Street View)",
])

P("3. O que vem no KIT (o que o cliente recebe)", h2)
bullets([
    "Rastreador 4G blindado (oculto)",
    "Módulo de Bloqueio Remoto <b>incluso</b>",
    "Chip multioperadora",
    "Aplicativo BSTEN PRO",
    "<b>Frete grátis</b> para todo o Brasil",
    "<b>Sem fidelidade</b>",
    "<b>15 dias de uso da plataforma sem cobrança</b>",
])

P("4. Preços e condições", h2)
table([
    [cell("Item", cb), cell("Valor", cb), cell("Observação", cb)],
    [cell("Equipamento (BSTEN PRO BLINDADO)"), cell("<b>R$ 139,97</b>"), cell("Compra única · frete grátis")],
    [cell("Plataforma / app"), cell("<b>R$ 35,97/mês</b>"), cell("Sem fidelidade · cobrança começa só após os 15 dias")],
    [cell("Teste sem risco"), cell("<b>15 dias grátis</b>"), cell("Instala, usa e conhece tudo antes da 1ª cobrança")],
], [6*cm, 3.5*cm, 6.5*cm])

P("5. Diferenciais (o que torna a oferta forte)", h2)
bullets([
    "<b>\"Compre sem pressão\" (maior diferencial):</b> instale, use e conheça todas as funções — a primeira cobrança da plataforma só acontece após os primeiros 15 dias. É um redutor de risco, não uma promoção.",
    "<b>Sem fidelidade / sem permanência:</b> liberdade total, transparência, sem multa de cancelamento.",
    "<b>Autonomia:</b> o próprio cliente bloqueia pelo app, na hora, sem depender de central.",
    "<b>Bloqueio remoto incluso:</b> não é item à parte — já vem no kit.",
    "<b>Cobertura nacional + frete grátis.</b>",
    "<b>Credibilidade:</b> empresa ativa desde 2013, CNPJ, homologação Anatel.",
])

P("6. Público-alvo e dores", h2)
bullets([
    "Donos de carro, moto e caminhão preocupados com <b>roubo/furto</b>.",
    "Quem quer <b>saber onde o veículo está</b> no dia a dia (uso pessoal, frota, familiar).",
    "Dor central: medo de perder o veículo e <b>não ter o poder de agir na hora</b>.",
    "Objeções comuns: \"é caro?\", \"tem fidelidade?\", \"vocês são confiáveis?\", \"serve pro meu veículo?\", \"quem instala?\".",
])

P("7. Posicionamento e neurovendas (tom da comunicação)", h2)
bullets([
    "<b>Vender consequências, não componentes:</b> em vez de \"rastreador/relé/chip\", falar \"localização em tempo real / controle pelo celular / bloqueio na hora / mais autonomia / mais proteção\".",
    "<b>Valor antes do preço:</b> construir desejo (demonstração + app + 15 dias) antes de mostrar o número.",
    "<b>Headline principal:</b> \"Mais do que rastrear. Tenha controle.\"",
    "<b>Alternativas A/B:</b> \"Localize. Monitore. Bloqueie. Tudo pelo seu celular.\" · \"Saiba onde seu veículo está e tenha o poder de agir imediatamente.\"",
    "Nome comercial único: <b>BSTEN PRO BLINDADO</b> (nunca citar nomes internos de plano).",
])

P("8. Canais de venda e atendimento", h2)
table([
    [cell("Canal", cb), cell("WhatsApp: 5519971478541 (atendimento e venda 100% por aqui)")],
    [cell("Horário humano", cb), cell("Seg–sex, 9h–17h (sem plantão). O app funciona 24h.")],
    [cell("Landing atual", cb), cell("adsbs.com.br")],
    [cell("Instagram", cb), cell("@bsten_ofc")],
    [cell("Instalação", cb), cell("Após a compra, o cliente recebe lista de instaladores parceiros em diversas regiões; pode também usar um profissional de confiança.")],
], [3.5*cm, 12.5*cm], header=False)

P("9. Os 15 vídeos disponíveis (para usar na landing e no atendimento)", h2)
P("Material já gravado, em fase de edição. Cada vídeo responde uma dúvida/objeção específica.", muted)
vrows = [[cell("#", cb), cell("Tema", cb), cell("Mensagem central", cb)]]
vids = [
 ("1","Como funciona o bloqueio","Autonomia — você bloqueia pelo app, na hora"),
 ("2","Como funciona o rastreamento","Tempo real, histórico de rotas, alertas"),
 ("3","E se roubarem?","Decisão rápida com acesso imediato à informação"),
 ("4","Quem faz a instalação","Rede de parceiros na sua região"),
 ("5","O que vem no kit","Rastreador + bloqueio incluso + chip + app + frete grátis"),
 ("6","Serve para carro/moto/caminhão","Compatibilidade 8–90V"),
 ("7","Se desligarem a bateria","Bateria interna de reserva mantém funcionando"),
 ("8","Chip multioperadora","Mais conexão — objetivo é manter o veículo conectado"),
 ("9","Tem fidelidade?","Não — liberdade e transparência"),
 ("10","Quanto custa","R$ 139,97 + R$ 35,97/mês + 15 dias grátis"),
 ("11","Função âncora","Área virtual + alerta de movimentação"),
 ("12","Quem é a Bsten","Empresa especializada, autonomia, Brasil todo"),
 ("13","Por que \"PRO BLINDADO\"","Segurança operacional, solução única"),
 ("14","Preciso depender de central?","Não — autonomia total pelo app"),
 ("15","Por que escolher a BSTEN","Tecnologia + praticidade + autonomia + sem fidelidade + Brasil"),
]
for n,t,m in vids:
    vrows.append([cell(n), cell(t), cell(m)])
table(vrows, [1*cm, 6*cm, 9*cm])

P("10. Estrutura atual da landing (8 seções)", h2)
numbered([
    "<b>Headline forte</b> + botão \"Quero proteger meu veículo\"",
    "<b>Vídeo do produto</b> (equipamento + app + bloqueio)",
    "<b>Benefício principal:</b> \"Localize e bloqueie pelo celular.\"",
    "<b>BSTEN PRO BLINDADO</b> (herói: oculto, 4G, multioperadora, resistente à água, bloqueio incluso)",
    "<b>Aplicativo BSTEN PRO</b> (tempo real, âncora, histórico, alertas, Street View)",
    "<b>Teste sem risco (15 dias)</b> — seção \"Compre sem pressão\"",
    "<b>Condições comerciais:</b> R$ 139,97 · R$ 35,97/mês · frete grátis · sem fidelidade",
    "<b>WhatsApp</b> (CTA final)",
])

P("11. Mídia / campanhas (contexto)", h2)
bullets([
    "Campanhas ativas no Meta Ads (Facebook/Instagram): tráfego para Landing (Brasil) e Click-to-WhatsApp Conversas (Brasil).",
    "Click-to-WhatsApp cai direto num bot de atendimento que qualifica o lead.",
    "Meta Pixel instalado na landing para rastrear conversões.",
    "Maiores ralos de conversão identificados: leads que chegam fora do horário (anúncio roda 24/7) e tempo de resposta.",
])

P("12. Perguntas frequentes (respostas oficiais)", h2)
frows = [[cell("Pergunta", cb), cell("Resposta", cb)]]
faq = [
 ("Atende minha cidade?","Sim — atende todo o Brasil, com frete grátis."),
 ("Tem fidelidade?","Não. Sem permanência e sem multa."),
 ("Serve pra moto/caminhão?","Sim — carro, moto e caminhão (8–90V)."),
 ("E se desligarem a bateria?","Tem bateria interna de backup."),
 ("Preciso de central de monitoramento?","Não — você controla tudo pelo app, com autonomia."),
 ("Quem instala?","Rede de instaladores parceiros (lista liberada após a compra) ou profissional de confiança."),
 ("Quanto custa?","R$ 139,97 o equipamento + R$ 35,97/mês, com 15 dias grátis."),
]
for q,a in faq:
    frows.append([cell(q), cell(a)])
table(frows, [5.5*cm, 10.5*cm])

story.append(HRFlowable(width="100%", color=colors.HexColor("#dddddd"), spaceBefore=10, spaceAfter=10))

P("13. O que pedir às IAs (roteiro pronto para colar)", h2)
P("<b>Prompt sugerido para Gemini / ChatGPT:</b>", body)
P("\"Você é um especialista em copywriting e CRO (otimização de conversão) para landing pages de "
  "produtos físicos vendidos por WhatsApp no Brasil. Abaixo está o briefing completo do meu produto "
  "(segue o documento). Quero que você crie uma proposta de landing page de altíssima conversão, "
  "incluindo: (1) 3 opções de headline + subheadline que batam na dor de roubo de veículo; "
  "(2) a ordem ideal das seções, aplicando 'valor antes do preço'; (3) o texto completo de cada seção; "
  "(4) onde encaixar cada um dos 15 vídeos; (5) o texto do CTA principal e em quais pontos repeti-lo; "
  "(6) elementos de prova social e quebra de objeção que faltam; (7) o que remover se estiver "
  "atrapalhando a conversão. Objetivo final: gerar conversas qualificadas no WhatsApp e vendas. "
  "Seja específico e me entregue pronto para implementar.\"", boxst)
P("Peça o mesmo para cada IA, compare as três respostas e escolha o que cada uma fez de melhor. "
  "Quando voltar com o material, eu ajudo a consolidar a melhor versão e a implementar no código da landing.")

story.append(HRFlowable(width="100%", color=colors.HexColor("#dddddd"), spaceBefore=10, spaceAfter=8))
P("BSTEN PRO BLINDADO · Bsten LTDA · CNPJ 17.867.757/0001-80 · adsbs.com.br · WhatsApp 5519971478541 · "
  "Documento sem dados sigilosos (senhas/chaves ficam fora deste material).", muted)

doc = SimpleDocTemplate("/home/user/bsten-app/BRIEFING_BSTEN.pdf", pagesize=A4,
                        topMargin=1.8*cm, bottomMargin=1.6*cm,
                        leftMargin=1.8*cm, rightMargin=1.8*cm,
                        title="BSTEN PRO BLINDADO - Briefing Completo",
                        author="Bsten LTDA")
doc.build(story)
print("PDF gerado com sucesso")
