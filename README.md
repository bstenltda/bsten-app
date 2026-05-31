# BSTEN — Termo de Responsabilidade Digital

App web (React + Vite) com formulário de assinatura digital em etapas para
clientes do rastreamento veicular BSTEN: CPF/CNPJ, nome, WhatsApp, data de
nascimento, placa do veículo e assinatura na tela. Os dados são enviados para
uma planilha via Google Apps Script.

## Rodando localmente

```bash
npm install
npm run dev
```

Abra o endereço exibido no terminal (por padrão `http://localhost:5173`).

## Build de produção

```bash
npm run build
npm run preview
```

## Configuração

Antes de usar em produção, edite `src/App.jsx`:

- `WA_PHONE` — número de WhatsApp para o botão "Chamar no WhatsApp".
- `GOOGLE_SHEET_URL` — URL do seu Google Apps Script que recebe os dados do
  formulário (`POST` com JSON).
