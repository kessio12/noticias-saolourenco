with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's inspect where cards-quatro-mares ends in the tide section
idx_sec = html.find('<!-- SEÇÃO: TÁBUA DE MARÉS DO POVOADO -->')
idx_cards_end = html.find('id="cards-quatro-mares"></div>\n          </div>\n        </div>', idx_sec)
print("Found cards end:", idx_cards_end != -1)
if idx_cards_end != -1:
    print(html[idx_cards_end-50:idx_cards_end+150])