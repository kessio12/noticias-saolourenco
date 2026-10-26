function alternarModoLeve() {
  const painel = document.getElementById('painel-sinal-fraco');
  const mapa = document.querySelector('iframe');
  const btn = document.getElementById('btn-modo-leve');
  const ativo = document.body.classList.toggle('modo-sinal-fraco');

  if (ativo) {
    if (painel) painel.classList.remove('hidden');
    if (mapa) mapa.style.display = 'none'; // Desativa carregamento de mapa pesado
    if (btn) btn.classList.replace('bg-emerald-700', 'bg-amber-600');
    localStorage.setItem('sl_modo_leve', 'sim');
  } else {
    if (painel) painel.classList.add('hidden');
    if (mapa) mapa.style.display = 'block';
    if (btn) btn.classList.replace('bg-amber-600', 'bg-emerald-700');
    localStorage.setItem('sl_modo_leve', 'nao');
  }
}

// Inicia com a preferência gravada
if (localStorage.getItem('sl_modo_leve') === 'sim') {
  alternarModoLeve();
}