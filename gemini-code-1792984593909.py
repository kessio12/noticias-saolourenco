# Let's inspect dadosMaresSemana in index.html
idx_d = html.find('const dadosMaresSemana = [')
idx_d_end = html.find('];', idx_d)
print(html[idx_d:idx_d+400])

idx_render = html.find('function renderizarMare(diaIndex) {')
idx_render_end = html.find('function selecionarDiaMare', idx_render)
print("--- renderizarMare ---")
print(html[idx_render:idx_render+400])