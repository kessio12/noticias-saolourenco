# Check where main starts and where the top bar is
print("--- Topbar search ---")
idx_tema = html.find('id="btn-tema"')
print(html[idx_tema-200:idx_tema+150])

print("--- Main search ---")
idx_main = html.find('<main')
print(html[idx_main:idx_main+200])

print("--- Tide section search ---")
idx_tide_sec = html.find('<!-- SEÇÃO: TÁBUA DE MARÉS DO POVOADO -->')
print(html[idx_tide_sec:idx_tide_sec+400])