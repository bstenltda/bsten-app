# BSTEN — Pacote do Bot (Botclick) — PROMPT ÚNICO

Desde que o Botclik liberou 50k no prompt, TUDO foi consolidado num só arquivo. Não há mais documentos separados.

## Onde colocar
| Arquivo | Aba |
|---|---|
| 01_GERAL_PROMPT.md | **PROMPT** (só este) |

(O LEIA-ME é só seu guia — não sobe. Os docs antigos estão em `_arquivo_consolidado/` apenas como histórico — NÃO subir.)

## Passos no Botclik
1. PROMPT: apaga tudo e cola o `01_GERAL_PROMPT.md`.
2. DOCS: **apaga TODOS os documentos** (já estão dentro do prompt).
3. Ferramenta: mantém a HTTP Request *Buscar vídeo/tutorial* (e, quando o TI fizer, a *Consultar porta*).
4. Aguarda "Sincronizado" e testa.

## Não esquecer (config do Botclik, não é o prompt)
- Tirar o prefixo **"BSTEN:"** (campo de nome do agente).
- Mapear a resposta da ferramenta (`url`, `found`) na variável que o bot escreve — senão o link vem vazio.

## Testes rápidos
- "bom dia" → só cumprimenta + "como posso ajudar?" (não despeja preço).
- "tem vídeo do valor?" → link cru, sozinho, sem [texto](url).
- "quero contratar" → qualifica (carro/moto?) e reserva com nome+WhatsApp; CPF só no fim.
- "tá caro" → âncora R$ 1,20/dia + 15 dias risco zero.
- "vocês têm a tag?" → fala da TAG (R$50 + R$10/mês), sem chamar de GPS.
- "roubaram minha moto" → remove emoji, não vende, oferece transferir.
