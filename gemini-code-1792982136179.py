idx_d = html.find('const dadosMaresSemana =')
idx_d_end = html.find('];', idx_d)
print(html[idx_d:idx_d_end+2])