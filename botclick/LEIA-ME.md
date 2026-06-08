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

## Passo a passo
1. PROMPT: apague o conteúdo atual e cole o 01_GERAL_PROMPT.md.
2. DOCS: substitua os docs pelos desta pasta e aguarde "Sincronizado".
3. Apague qualquer doc antigo que cite Solo/Smart/Start/Plus/11 cidades.

> Novidade nesta v5: bloco institucional (07_EMPRESA.md — sede Sumaré-SP, CNPJ, desde 2013) p/ objeção de confiança, e atualização do 01_GERAL (localização/sede). Suba 01_GERAL e 07_EMPRESA.

> Novidade v6 (formatação de mensagens): 01_GERAL §15 reescrita — fracionar em 2-3 mensagens curtas, usar *negrito* (asterisco simples) e _itálico_ nativos do WhatsApp pra dar vida, proibido **negrito duplo**/listas. 02_COMERCIAL: instalação numa resposta só (sem agendar, sem contradição) + preço/fechamento fracionados. Suba 01_GERAL e 02_COMERCIAL.

> Novidade v7 (2ª auditoria): corrige bug do prefixo "BSTEN:" no texto e saudação duplicada (01_GERAL §15). Instalação reescrita: lidera com "aparelho chega PRONTO e testado, app configurado, equipe orienta o profissional" — sem afirmar que a BSTEN instala em todo o Brasil (01_GERAL §4, 02_COMERCIAL, produto). Nova objeção "e se não funcionar?" (resposta firme, sem soar frágil, sem inventar garantia). Preço com 1 pergunta de qualificação antes. Suba 01_GERAL, 02_COMERCIAL e produto_BSTEN_PRO_BLINDADO.

> Novidade v8 (coleta de dados): CPF NUNCA a frio — gera rejeição. Mesmo no "quero contratar", qualifica primeiro (veículo + cidade), reserva só com *nome + WhatsApp*, e pede *e-mail + CPF* só no passo final (emitir nota), já transferindo pra equipe. 01_GERAL §7/§12/§14 e 02_COMERCIAL ETAPA 7. Suba 01_GERAL e 02_COMERCIAL.

> Novidade v9 (auditoria 07/06): assistente passa a se chamar *Francisco Santos* (nunca "Bia") — 01_GERAL §1. Anti-alucinação de contato: NUNCA inventar telefone/e-mail/forma de pagamento (§3). Pagamento: só *Pix* ou *boleto* antecipado, sem cartão, sem pagamento na entrega (§4c, COMERCIAL). Fluxo de PARCEIRO/INSTALADOR credenciado: registra nome+cidade+WhatsApp e passa pra equipe, sem inventar contato (§4d, COMERCIAL). Responder info que está nos docs (ex.: mensalidade) — não empurrar pra "equipe define". ATENÇÃO: a maioria desses bugs (CPF a frio, markdown, ativação pra lead) só some quando o 01_GERAL for subido na aba PROMPT — apague também qualquer doc antigo que cite "BSTEN Solo". Suba 01_GERAL e 02_COMERCIAL.
