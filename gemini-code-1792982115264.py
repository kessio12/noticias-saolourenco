idx_grid_start = html.find('id="grid-dados-mare"')
idx_div_end = html.find('</div>\n\n        <div class="bg-mar-900/50 rounded-2xl p-4 border border-mar-700', idx_grid_start)
if idx_div_end == -1:
    idx_div_end = html.find('</div>', html.find('id="cards-quatro-mares"', idx_grid_start))
    idx_div_end = html.find('</div>', idx_div_end + 5)
print("Position:", idx_div_end)
print(html[idx_div_end-100:idx_div_end+250])