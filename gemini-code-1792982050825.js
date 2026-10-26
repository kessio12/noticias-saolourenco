function salvarMareComoFoto() {
  const canvas = document.createElement('canvas');
  canvas.width = 1080;
  canvas.height = 1420;
  const ctx = canvas.getContext('2d');

  // Fundo profissional
  ctx.fillStyle = '#0c4a6e';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Borda Dourada
  ctx.strokeStyle = '#f59e0b';
  ctx.lineWidth = 14;
  ctx.strokeRect(20, 20, canvas.width - 40, canvas.height - 40);

  // Cabeçalho
  ctx.fillStyle = '#f59e0b';
  ctx.font = 'bold 44px sans-serif';
  ctx.textAlign = 'center';
  ctx.fillText('PORTAL SÃO LOURENÇO NOTÍCIAS', 540, 95);

  ctx.fillStyle = '#ffffff';
  ctx.font = 'bold 36px sans-serif';
  ctx.fillText('Tábua de Marés & Janelas de Trabalho da Semana', 540, 150);

  ctx.fillStyle = '#7dd3fc';
  ctx.font = '26px sans-serif';
  ctx.fillText('Goiana - PE • Estuário do Rio Goiana • Salvo para uso Offline', 540, 195);

  // Desenhar os 4 dias
  let yOffset = 240;
  dadosMaresSemana.forEach((d, idx) => {
    ctx.fillStyle = '#082f49';
    ctx.roundRect ? ctx.roundRect(50, yOffset, 980, 260, 20) : ctx.fillRect(50, yOffset, 980, 260);
    ctx.fill();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 3;
    ctx.stroke();

    ctx.textAlign = 'left';
    ctx.fillStyle = '#fbbf24';
    ctx.font = 'bold 32px sans-serif';
    ctx.fillText(`${d.diaRotulo.toUpperCase()} — ${d.lua} (${d.tipo})`, 75, yOffset + 48);

    // Horários dos picos
    ctx.font = '26px monospace';
    ctx.fillStyle = '#ffffff';
    let evTexto = d.eventos.map(e => `${e.hora} ${e.tipo.split(' ')[0]} (${e.altura})`).join('  |  ');
    ctx.fillText(evTexto, 75, yOffset + 105);

    // Janela de Trabalho e Comportas
    ctx.font = 'bold 24px sans-serif';
    ctx.fillStyle = '#34d399';
    ctx.fillText(`🦀 Mangue no Seco: ${d.janelaMangueHorario || '07:00 às 11:30'} (Sair antes da cheia)`, 75, yOffset + 165);

    ctx.fillStyle = '#38bdf8';
    ctx.fillText(`🦐 Comportas Viveiro (≥ 2.2m): ${d.janelaComportasHorario || '15:15 às 17:10'}`, 75, yOffset + 215);

    yOffset += 285;
  });

  // Rodapé da imagem
  ctx.textAlign = 'center';
  ctx.fillStyle = '#94a3b8';
  ctx.font = '22px sans-serif';
  ctx.fillText('Consulte diariamente: kessio12.github.io/noticias-saolourenco', 540, 1380);

  // Disparar download da imagem
  const link = document.createElement('a');
  link.download = `tabua-mares-sao-lourenco.png`;
  link.href = canvas.toDataURL('image/png');
  link.click();
}