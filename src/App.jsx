import React, { useState, useRef, useEffect } from "react";

// --- CONFIGURAÇÕES ---
const WA_PHONE = "5519971478541";
// SUBSTITUA PELA SUA URL DO GOOGLE APPS SCRIPT
const GOOGLE_SHEET_URL = "SUA_URL_DO_GOOGLE_SCRIPT_AQUI";

const STEPS = [
  { id: "doc", title: "CPF ou CNPJ", sub: "Informe o documento do titular" },
  { id: "nome", title: "Nome Completo", sub: "Como no documento" },
  { id: "wp", title: "WhatsApp", sub: "Número com DDD" },
  { id: "nasc", title: "Nascimento", sub: "Data de nascimento" },
  { id: "placa", title: "Placa", sub: "Placa do veículo rastreado" },
  { id: "sig", title: "Assinatura", sub: "Assine na tela abaixo" },
  { id: "review", title: "Revisão", sub: "Confirme os dados" },
];

export default function App() {
  const [mode, setMode] = useState("welcome");
  const [step, setStep] = useState(0);
  const [form, setForm] = useState({ doc: "", nome: "", wp: "+55 (", nasc: "", placa: "" });
  const [sigImg, setSigImg] = useState(null);
  const [loading, setLoading] = useState(false);
  const canvasRef = useRef(null);

  const maskDoc = (v) => {
    v = v.replace(/\D/g, "");
    if (v.length <= 11) return v.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4").slice(0, 14);
    return v.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, "$1.$2.$3/$4-$5").slice(0, 18);
  };

  const handleNext = async () => {
    if (step < STEPS.length - 1) return setStep(step + 1);
    setLoading(true);
    const finalData = { ...form, id: Date.now(), signedAt: new Date().toISOString(), sigImg };
    try {
      await fetch(GOOGLE_SHEET_URL, { method: "POST", mode: "no-cors", body: JSON.stringify(finalData) });
      setMode("success");
    } catch (e) {
      alert("Erro ao salvar. Verifique o link do Google Sheets.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (step === 5 && canvasRef.current) {
      const canvas = canvasRef.current;
      const ctx = canvas.getContext("2d");
      ctx.lineWidth = 2; ctx.strokeStyle = "#1a2e6e"; ctx.lineCap = "round";
      let drawing = false;
      const getPos = (e) => {
        const r = canvas.getBoundingClientRect();
        const t = e.touches ? e.touches[0] : e;
        return { x: t.clientX - r.left, y: t.clientY - r.top };
      };
      canvas.ontouchstart = canvas.onmousedown = (e) => { drawing = true; const p = getPos(e); ctx.beginPath(); ctx.moveTo(p.x, p.y); };
      canvas.ontouchmove = canvas.onmousemove = (e) => { if(!drawing) return; const p = getPos(e); ctx.lineTo(p.x, p.y); ctx.stroke(); };
      canvas.ontouchend = canvas.onmouseup = () => { drawing = false; setSigImg(canvas.toDataURL()); };
    }
  }, [step]);

  if (mode === "welcome") return (
    <div style={ui.fullPage}>
      <h1 style={{fontSize: 50, margin: 0}}>BSTEN</h1>
      <p style={{marginBottom: 40}}>Termo de Responsabilidade Digital</p>
      <button style={ui.btnPrimary} onClick={() => setMode("form")}>Iniciar Assinatura</button>
    </div>
  );

  if (mode === "success") return (
    <div style={ui.fullPageWhite}>
      <div style={{fontSize: 60, color: "#27ae60", marginBottom: 20}}>✓</div>
      <h2>Assinado com Sucesso!</h2>
      <p>O termo foi registrado na nossa central.</p>
      <button style={ui.btnPrimary} onClick={() => window.open(`https://wa.me/${WA_PHONE}`)}>Chamar no WhatsApp</button>
    </div>
  );

  const s = STEPS[step];
  return (
    <div style={ui.fullPageWhite}>
      <div style={ui.progress}><div style={{...ui.bar, width: `${(step/6)*100}%`}} /></div>
      <h2 style={{marginBottom: 5}}>{s.title}</h2>
      <p style={{fontSize: 14, color: "#666", marginBottom: 25}}>{s.sub}</p>

      <div style={{width: '100%', maxWidth: 300}}>
        {step === 0 && <input style={ui.input} value={form.doc} onChange={e => setForm({...form, doc: maskDoc(e.target.value)})} placeholder="CPF ou CNPJ" />}
        {step === 1 && <input style={ui.input} value={form.nome} onChange={e => setForm({...form, nome: e.target.value})} placeholder="Nome Completo" />}
        {step === 2 && <input style={ui.input} value={form.wp} onChange={e => setForm({...form, wp: e.target.value})} placeholder="(00) 00000-0000" />}
        {step === 3 && <input type="date" style={ui.input} value={form.nasc} onChange={e => setForm({...form, nasc: e.target.value})} />}
        {step === 4 && <input style={ui.input} value={form.placa} onChange={e => setForm({...form, placa: e.target.value.toUpperCase()})} placeholder="ABC1D23" />}
        {step === 5 && <canvas ref={canvasRef} width={300} height={150} style={ui.canvas} />}
        {step === 6 && (
          <div style={{background: "#fff", padding: 15, borderRadius: 10, border: "1px solid #eee"}}>
            <p><b>Nome:</b> {form.nome}</p>
            <p><b>Placa:</b> {form.placa}</p>
            <p style={{fontSize: 11, color: "#999"}}>Ao confirmar, você aceita o monitoramento BSTEN.</p>
          </div>
        )}
      </div>

      <div style={{display: "flex", gap: 10, width: "100%", maxWidth: 300, marginTop: 25}}>
        {step > 0 && <button style={ui.btnSec} onClick={() => setStep(step - 1)}>Voltar</button>}
        <button style={ui.btnPrimary} onClick={handleNext} disabled={loading}>
          {loading ? "Enviando..." : step === 6 ? "Aceitar e Enviar" : "Próximo"}
        </button>
      </div>
    </div>
  );
}

const ui = {
  fullPage: { height: "100vh", background: "#1a2e6e", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", color: "#fff", fontFamily: "sans-serif", textAlign: "center", padding: 20, boxSizing: "border-box" },
  fullPageWhite: { height: "100vh", background: "#f8f9fa", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", color: "#333", fontFamily: "sans-serif", padding: 20, boxSizing: "border-box" },
  btnPrimary: { background: "#1a2e6e", color: "#fff", border: "none", padding: "16px", borderRadius: 12, fontSize: 16, fontWeight: "bold", cursor: "pointer", width: "100%", maxWidth: 300 },
  btnSec: { background: "#ddd", color: "#333", border: "none", padding: "16px", borderRadius: 12, fontWeight: "bold", cursor: "pointer", flex: 1 },
  input: { width: "100%", padding: 14, fontSize: 16, borderRadius: 10, border: "1px solid #ccc", boxSizing: "border-box" },
  canvas: { background: "#fff", border: "2px dashed #1a2e6e", borderRadius: 10, width: "100%" },
  progress: { height: 6, background: "#eee", borderRadius: 3, width: "100%", maxWidth: 300, marginBottom: 30, overflow: "hidden" },
  bar: { height: "100%", background: "#1a2e6e", transition: "0.3s" }
};
