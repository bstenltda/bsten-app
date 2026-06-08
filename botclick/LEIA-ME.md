# 📦 BSTEN PRO BLINDADO — Arquivos do Bot (Botclick) — v2 (correções de atendimento)

Correções aplicadas: localização/abrangência nacional, nunca CPF p/ pergunta simples, lead ≠ ativação (IMEI), instalação padronizada, vídeo, alarme, "perguntas rápidas" (responde antes de vender), remoção total de BSTEN Solo/Smart/Start/Plus.

## Onde colocar
| Arquivo | Aba |
|---|---|
| 01_GERAL_PROMPT.md | **PROMPT** (deixe só este na aba Prompt) |
| produto_BSTEN_PRO_BLINDADO.md | DOCS |
| 02_COMERCIAL.md | DOCS |
| 03_SUPORTE.md | DOCS |
| 04_FINANCEIRO.md | DOCS |
| 05_ATIVACAO.md | DOCS |
| 06_COMPORTAMENTO.md | DOCS |
| 07_EMPRESA.md | DOCS |
| 08_VIDEOS.md | DOCS |

## Passo a passo
1. PROMPT: apague o conteúdo atual e cole o 01_GERAL_PROMPT.md.
2. DOCS: substitua os docs pelos desta pasta e aguarde "Sincronizado".
3. Apague qualquer doc antigo que cite Solo/Smart/Start/Plus/11 cidades.

> Novidade nesta v5: bloco institucional (07_EMPRESA.md — sede Sumaré-SP, CNPJ, desde 2013) p/ objeção de confiança, e atualização do 01_GERAL (localização/sede). Suba 01_GERAL e 07_EMPRESA.

> Novidade v6 (formatação de mensagens): 01_GERAL §15 reescrita — fracionar em 2-3 mensagens curtas, usar *negrito* (asterisco simples) e _itálico_ nativos do WhatsApp pra dar vida, proibido **negrito duplo**/listas. 02_COMERCIAL: instalação numa resposta só (sem agendar, sem contradição) + preço/fechamento fracionados. Suba 01_GERAL e 02_COMERCIAL.

> Novidade v7 (2ª auditoria): corrige bug do prefixo "BSTEN:" no texto e saudação duplicada (01_GERAL §15). Instalação reescrita: lidera com "aparelho chega PRONTO e testado, app configurado, equipe orienta o profissional" — sem afirmar que a BSTEN instala em todo o Brasil (01_GERAL §4, 02_COMERCIAL, produto). Nova objeção "e se não funcionar?" (resposta firme, sem soar frágil, sem inventar garantia). Preço com 1 pergunta de qualificação antes. Suba 01_GERAL, 02_COMERCIAL e produto_BSTEN_PRO_BLINDADO.

> Novidade v8 (coleta de dados): CPF NUNCA a frio — gera rejeição. Mesmo no "quero contratar", qualifica primeiro (veículo + cidade), reserva só com *nome + WhatsApp*, e pede *e-mail + CPF* só no passo final (emitir nota), já transferindo pra equipe. 01_GERAL §7/§12/§14 e 02_COMERCIAL ETAPA 7. Suba 01_GERAL e 02_COMERCIAL.

> Novidade v12 (vídeos): novo doc 08_VIDEOS com os links REAIS dos vídeos (adsbs.com.br/assets) mapeados por pergunta — o bot envia o vídeo certo (bloqueio, rastreamento, "serve pra moto", quanto custa, etc.), 1 por vez, e retoma com pergunta. Regra: nunca inventar URL, usar só as do doc. 01_GERAL §16 e 02_COMERCIAL (Vídeo) referenciam. Suba 01_GERAL, 02_COMERCIAL e o novo 08_VIDEOS.

> Novidade v11 (confiança/contato): contato oficial gravado — e-mail gpsbspaga@gmail.com (único válido; bot nunca inventa outro), Instagram @bsten_ofc. Nova "pilha de confiança" pra objeção "não acho confiável" (07_EMPRESA): além do CNPJ, usar Pix em nome da BSTEN LTDA, CNPJ verificável na Receita, Instagram, 15 dias risco zero, vídeos. 01_GERAL §3/§4d e 02_COMERCIAL (parceiro) referenciam o e-mail oficial. Suba 01_GERAL, 02_COMERCIAL e 07_EMPRESA.

> Novidade v10 (gatilhos de venda): seção GATILHOS DE VENDA no 02_COMERCIAL (âncora por dia R$ 1,20, risco zero, posse futura, poder na mão, facilidade, autoridade real, fechamento assumido, dois sims). Etapas 4/5/6/7 turbinadas e objeções "tá caro"/"vou pensar"/"não confio" com gatilho. Tudo ético — proibido escassez falsa, desconto e depoimento/nº de clientes inventado. 01_GERAL §6 referencia os gatilhos. Suba 01_GERAL e 02_COMERCIAL.

> Novidade v9 (auditoria 07/06): assistente passa a se chamar *Francisco Santos* (nunca "Bia") — 01_GERAL §1. Anti-alucinação de contato: NUNCA inventar telefone/e-mail/forma de pagamento (§3). Pagamento: só *Pix* ou *boleto* antecipado, sem cartão, sem pagamento na entrega (§4c, COMERCIAL). Fluxo de PARCEIRO/INSTALADOR credenciado: registra nome+cidade+WhatsApp e passa pra equipe, sem inventar contato (§4d, COMERCIAL). Responder info que está nos docs (ex.: mensalidade) — não empurrar pra "equipe define". ATENÇÃO: a maioria desses bugs (CPF a frio, markdown, ativação pra lead) só some quando o 01_GERAL for subido na aba PROMPT — apague também qualquer doc antigo que cite "BSTEN Solo". Suba 01_GERAL e 02_COMERCIAL.
