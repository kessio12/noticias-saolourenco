// ATUALIZAÇÃO DOS DADOS SEMANAIS COM AS JANELAS DE TRABALHO
const dadosMaresSemana = [
  {
    diaRotulo: "Hoje",
    lua: "Lua Cheia",
    tipo: "Maré de Sizígia (Maré Grande)",
    alturaAtual: "1.2m",
    statusTexto: "Vazando",
    dica: "A baixa-mar abre excelentes coroas nas margens de São Lourenço para cata de marisco e unhas-de-velho.",
    janelaMangueHorario: "07:00 às 11:30",
    janelaMangueDetalhe: "Vaza seca a lama a partir das 07h. <strong>Reponta da maré às 12h00</strong>: comece a recolher e saia do mangue fundo até 11h30 para não atolar.",
    janelaMangueTempo: "Tempo útil: ~4h30",
    janelaComportasHorario: "15:15 às 17:10",
    janelaComportasDetalhe: "Cota de água atinge nível de renovação <strong>100% por gravidade</strong> (Pico de 2.4m às 15:58). Economia de bombas.",
    janelaComportasTempo: "Janela: ~2h00 de cota cheia",
    eventos: [
      { hora: "03:22", tipo: "Preamar (Cheia)", altura: "2.3m", icone: "fa-arrow-up", cor: "text-sky-400" },
      { hora: "09:40", tipo: "Baixa-mar (Seca)", altura: "0.2m", icone: "fa-arrow-down", cor: "text-amber-400" },
      { hora: "15:58", tipo: "Preamar (Cheia)", altura: "2.4m", icone: "fa-arrow-up", cor: "text-sky-400" },
      { hora: "22:15", tipo: "Baixa-mar (Seca)", altura: "0.3m", icone: "fa-arrow-down", cor: "text-amber-400" }
    ]
  },
  {
    diaRotulo: "Amanhã",
    lua: "Lua Cheia",
    tipo: "Maré de Sizígia (Pico Forte)",
    alturaAtual: "1.6m",
    statusTexto: "Enchendo",
    dica: "Preamar baterá 2.5m à tarde: volume ideal para renovar as comportas dos tanques de camarão.",
    janelaMangueHorario: "07:45 às 12:15",
    janelaMangueDetalhe: "Seca extrema (0.1m às 10:22): vaza muito profunda e coroas abertas. Sair até 12h15 antes da reponta forte.",
    janelaMangueTempo: "Tempo útil: ~4h30",
    janelaComportasHorario: "15:55 às 17:50",
    janelaComportasDetalhe: "Pico máximo de 2.5m às 16:40. Volume volumoso para sangria e abastecimento geral dos tanques.",
    janelaComportasTempo: "Janela: ~2h00 de cota cheia",
    eventos: [
      { hora: "04:05", tipo: "Preamar (Cheia)", altura: "2.4m", icone: "fa-arrow-up", cor: "text-sky-400" },
      { hora: "10:22", tipo: "Baixa-mar (Seca)", altura: "0.1m", icone: "fa-arrow-down", cor: "text-amber-400" },
      { hora: "16:40", tipo: "Preamar (Cheia)", altura: "2.5m", icone: "fa-arrow-up", cor: "text-sky-400" },
      { hora: "22:58", tipo: "Baixa-mar (Seca)", altura: "0.2m", icone: "fa-arrow-down", cor: "text-amber-400" }
    ]
  },
  {
    diaRotulo: "+2 Dias",
    lua: "Lua Cheia",
    tipo: "Maré Grande",
    alturaAtual: "0.9m",
    statusTexto: "Baixa-mar",
    dica: "Seca funda pela manhã no estuário para mariscagem.",
    janelaMangueHorario: "08:30 às 13:00",
    janelaMangueDetalhe: "Excelente para cata de marisco branco e unhas-de-velho pela manhã. Sair até 13h00.",
    janelaMangueTempo: "Tempo útil: ~4h30",
    janelaComportasHorario: "16:40 às 18:30",
    janelaComportasDetalhe: "Renovação rápida aproveitando o pico de 2.4m no final da tarde.",
    janelaComportasTempo: "Janela: ~1h50 de cota cheia",
    eventos: [
      { hora: "04:48", tipo: "Preamar (Cheia)", altura: "2.3m", icone: "fa-arrow-up", cor: "text-sky-400" },
      { hora: "11:05", tipo: "Baixa-mar (Seca)", altura: "0.2m", icone: "fa-arrow-down", cor: "text-amber-400" },
      { hora: "17:25", tipo: "Preamar (Cheia)", altura: "2.4m", icone: "fa-arrow-up", cor: "text-sky-400" },
      { hora: "23:42", tipo: "Baixa-mar (Seca)", altura: "0.3m", icone: "fa-arrow-down", cor: "text-amber-400" }
    ]
  },
  {
    diaRotulo: "+3 Dias",
    lua: "Minguante Desse",
    tipo: "Início de Maré Quebrada",
    alturaAtual: "1.4m",
    statusTexto: "Águas Calmas",
    dica: "Correnteza mais branda no Rio Goiana, excelente para pesca de siri e tarrafa.",
    janelaMangueHorario: "09:15 às 13:45",
    janelaMangueDetalhe: "Maré quebrada com menor velocidade de correnteza. Janela favorável até 13h45.",
    janelaMangueTempo: "Tempo útil: ~4h30",
    janelaComportasHorario: "17:30 às 19:15",
    janelaComportasDetalhe: "Cota suficiente (2.2m) para reforço de oxigenação nas comportas principais.",
    janelaComportasTempo: "Janela: ~1h45 de cota cheia",
    eventos: [
      { hora: "05:32", tipo: "Preamar (Cheia)", altura: "2.1m", icone: "fa-arrow-up", cor: "text-sky-400" },
      { hora: "11:50", tipo: "Baixa-mar (Seca)", altura: "0.4m", icone: "fa-arrow-down", cor: "text-amber-400" },
      { hora: "18:12", tipo: "Preamar (Cheia)", altura: "2.2m", icone: "fa-arrow-up", cor: "text-sky-400" },
      { hora: "00:29", tipo: "Baixa-mar (Seca)", altura: "0.5m", icone: "fa-arrow-down", cor: "text-amber-400" }
    ]
  }
];

// ATUALIZAÇÃO DA FUNÇÃO RENDERIZAR MARÉ
function renderizarMare(diaIndex) {
  const d = dadosMaresSemana[diaIndex];
  document.getElementById('mare-status-texto').innerText = d.statusTexto;
  document.getElementById('mare-altura-atual').innerText = d.alturaAtual;
  document.getElementById('mare-lua-nome').innerHTML = `<i class="fas fa-circle text-amber-300 text-lg"></i> ${d.lua}`;
  document.getElementById('mare-tipo-nome').innerText = d.tipo;
  document.getElementById('dica-mare-dia').innerText = d.dica;
  document.getElementById('resumo-mare-topo').innerText = `${d.statusTexto} (${d.alturaAtual})`;

  // Atualizar Calculadora de Janelas
  const jmHorario = document.getElementById('janela-mangue-horario');
  if (jmHorario) jmHorario.innerText = d.janelaMangueHorario;
  const jmDetalhe = document.getElementById('janela-mangue-detalhe');
  if (jmDetalhe) jmDetalhe.innerHTML = d.janelaMangueDetalhe;
  const jmSeguro = document.getElementById('janela-mangue-seguro');
  if (jmSeguro) jmSeguro.innerText = d.janelaMangueTempo;

  const jcHorario = document.getElementById('janela-comportas-horario');
  if (jcHorario) jcHorario.innerText = d.janelaComportasHorario;
  const jcDetalhe = document.getElementById('janela-comportas-detalhe');
  if (jcDetalhe) jcDetalhe.innerHTML = d.janelaComportasDetalhe;
  const jcTempo = document.getElementById('janela-comportas-tempo');
  if (jcTempo) jcTempo.innerText = d.janelaComportasTempo;

  // Atualizar dados do modo sinal fraco
  const rapidoMare = document.getElementById('rapido-mare');
  if (rapidoMare) rapidoMare.innerText = `${d.alturaAtual} ${d.statusTexto}`;
  const rapidoSair = document.getElementById('rapido-sair');
  if (rapidoSair) rapidoSair.innerText = `Até ${d.janelaMangueHorario.split('às')[1].trim()}`;
  const rapidoComporta = document.getElementById('rapido-comporta');
  if (rapidoComporta) rapidoComporta.innerText = d.janelaComportasHorario;

  const container = document.getElementById('cards-quatro-mares');
  container.innerHTML = '';
  d.eventos.forEach(ev => {
    container.innerHTML += `
      <div class="bg-mar-900/80 p-2.5 rounded-xl border border-mar-800 flex flex-col justify-center">
        <span class="text-xs font-mono font-bold text-white flex items-center justify-center gap-1">
          <i class="fas ${ev.icone} ${ev.cor}"></i> ${ev.hora}
        </span>
        <span class="text-[11px] text-slate-300 font-semibold mt-1">${ev.tipo}</span>
        <span class="text-xs font-black ${ev.cor}">${ev.altura}</span>
      </div>
    `;
  });

  const btns = document.querySelectorAll('.btn-dia');
  btns.forEach((btn, idx) => {
    btn.className = (idx === diaIndex) 
      ? "btn-dia px-3 py-2 rounded-xl bg-sky-500 text-white font-bold transition" 
      : "btn-dia px-3 py-2 rounded-xl text-slate-300 hover:bg-mar-800 transition";
  });
}

// ALTERNAR MODO SINAL FRACO
function alternarModoLeve() {
  const painel = document.getElementById('painel-sinal-fraco');
  const mapa = document.querySelector('iframe');
  const btn = document.getElementById('btn-modo-leve');
  const ativo = document.body.classList.toggle('modo-sinal-fraco');

  if (ativo) {
    if (painel) painel.classList.remove('hidden');
    if (mapa) mapa.style.display = 'none';
    if (btn) btn.classList.replace('bg-emerald-700', 'bg-amber-600');
    localStorage.setItem('sl_modo_leve', 'sim');
  } else {
    if (painel) painel.classList.add('hidden');
    if (mapa) mapa.style.display = 'block';
    if (btn) btn.classList.replace('bg-amber-600', 'bg-emerald-700');
    localStorage.setItem('sl_modo_leve', 'nao');
  }
}

if (localStorage.getItem('sl_modo_leve') === 'sim') {
  alternarModoLeve();
}

// SALVAR TÁBUA DE MARÉS COMO IMAGEM OFFLINE
function salvarMareComoFoto() {
  const canvas = document.createElement('canvas');
  canvas.width = 1080;
  canvas.height = 1420;
  const ctx = canvas.getContext('2d');

  ctx.fillStyle = '#0c4a6e';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.strokeStyle = '#f59e0b';
  ctx.lineWidth = 14;
  ctx.strokeRect(20, 20, canvas.width - 40, canvas.height - 40);

  ctx.fillStyle = '#f59e0b';
  ctx.font = 'bold 44px sans-serif';
  ctx.textAlign = 'center';
  ctx.fillText('PORTAL SÃO LOURENÇO NOTÍCIAS', 540, 95);

  ctx.fillStyle = '#ffffff';
  ctx.font = 'bold 36px sans-serif';
  ctx.fillText('Tábua de Marés & Janelas de Trabalho da Semana', 540, 150);

  ctx.fillStyle = '#7dd3fc';
  ctx.font = '26px sans-serif';
  ctx.fillText('Goiana - PE • Estuário do Rio Goiana • Uso Offline', 540, 195);

  let yOffset = 240;
  dadosMaresSemana.forEach((d) => {
    ctx.fillStyle = '#082f49';
    ctx.fillRect(50, yOffset, 980, 260);
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 3;
    ctx.strokeRect(50, yOffset, 980, 260);

    ctx.textAlign = 'left';
    ctx.fillStyle = '#fbbf24';
    ctx.font = 'bold 32px sans-serif';
    ctx.fillText(`${d.diaRotulo.toUpperCase()} — ${d.lua} (${d.tipo})`, 75, yOffset + 48);

    ctx.font = '24px monospace';
    ctx.fillStyle = '#ffffff';
    let evTexto = d.eventos.map(e => `${e.hora} ${e.tipo.split(' ')[0]} (${e.altura})`).join('  |  ');
    ctx.fillText(evTexto, 75, yOffset + 105);

    ctx.font = 'bold 24px sans-serif';
    ctx.fillStyle = '#34d399';
    ctx.fillText(`🦀 Mangue no Seco: ${d.janelaMangueHorario} (Sair antes da cheia)`, 75, yOffset + 165);

    ctx.fillStyle = '#38bdf8';
    ctx.fillText(`🦐 Comportas Viveiro (≥ 2.2m): ${d.janelaComportasHorario}`, 75, yOffset + 215);

    yOffset += 285;
  });

  ctx.textAlign = 'center';
  ctx.fillStyle = '#94a3b8';
  ctx.font = '22px sans-serif';
  ctx.fillText('Consulte diariamente: kessio12.github.io/noticias-saolourenco', 540, 1380);

  const link = document.createElement('a');
  link.download = `tabua-mares-sao-lourenco.png`;
  link.href = canvas.toDataURL('image/png');
  link.click();
}