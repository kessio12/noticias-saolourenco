# Let's inspect where renderizarMare is and the surrounding code
idx_render = html.find('function renderizarMare(diaIndex)')
idx_render_end = html.find('function selecionarDiaMare', idx_render)
print(html[idx_render:idx_render_end])