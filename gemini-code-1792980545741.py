with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update popup modal image
old_popup_img = '<img src="https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1000&q=80" \n             alt="São Lourenço Goiana" class="w-full h-full object-cover opacity-35">'
new_popup_img = '<img src="igreja.jpg" \n             alt="Igreja Matriz de São Lourenço" class="w-full h-full object-cover opacity-50">'

if old_popup_img in html:
    html = html.replace(old_popup_img, new_popup_img)
    print("Popup image replaced successfully!")
else:
    # Try flexible replacement
    html = re.sub(r'<img src="https://images\.unsplash\.com/photo-1518709268805-4e9042af9f23[^>]+São Lourenço Goiana[^>]+>',
                  '<img src="igreja.jpg" alt="Igreja Matriz de São Lourenço" class="w-full h-full object-cover opacity-50">',
                  html)
    print("Popup image replaced via regex!")

# 2. Update news card for satelite/heritage to feature the Church
old_news = """      {
        id: "noticia-satelite-mapeamento",
        categoria: "Satélite & Mapa",
        titulo: "Mapeamento via satélite destaca preservação das áreas de mangue e patrimônio de 1555",
        autor: "Geografia Comunitária",
        data: "Destaque",
        imagem: "https://images.unsplash.com/photo-1548625361-16ef7ef7fe0f?auto=format&fit=crop&w=800&q=80",
        resumo: "Imagens orbitais mostram a exuberância dos esteiros do Rio Goiana e a localização estratégica do território.",
        corpo: `<p>A visão de satélite revela a riqueza territorial de São Lourenço, onde as águas do estuário abraçam a comunidade e sustentam gerações de famílias quilombolas através da pesca artesanal e da carcinicultura consciente.</p>`
      }"""

new_news = """      {
        id: "noticia-igreja-matriz-1555",
        categoria: "História & Fé",
        titulo: "Igreja Matriz de São Lourenço (~1555): Cinco séculos de fé, devoção e patrimônio às margens do Rio Goiana",
        autor: "Memória Quilombola & Povoação",
        data: "Patrimônio Secular",
        imagem: "igreja.jpg",
        resumo: "Com frontaria colonial preservada e cruzeiro secular, a histórica Igreja Matriz é o coração de fé e símbolo maior da comunidade.",
        corpo: `<p>A histórica <strong>Igreja Matriz de São Lourenço</strong>, erguida por volta de 1555 nas proximidades do estuário do Rio Goiana, permanece como o símbolo maior da identidade, fé e resistência da comunidade quilombola.</p><p>Com a sua imponente fachada colonial caiada de branco, portas e janelas no tom azul tradicional, cruzeiro no frontão e torre sineira lateral, o templo secular é o ponto de encontro de gerações de pescadores, marisqueiras e famílias que mantêm vivas as celebrações religiosas e tradições ancestrais da povoação.</p>`
      }"""

if old_news in html:
    html = html.replace(old_news, new_news)
    print("News item replaced with Church article!")
else:
    print("old_news not found verbatim, checking...")

# 3. Add category button for "História & Igreja" if helpful, or keep current filters
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

# 4. Update sw.js to cache 'igreja.jpg' and bump version to v7
with open("sw.js", "r", encoding="utf-8") as f:
    sw_code = f.read()

sw_code = sw_code.replace("sao-lourenco-v6", "sao-lourenco-v7").replace("sao-lourenco-v5", "sao-lourenco-v7")
if "'./igreja.jpg'" not in sw_code:
    sw_code = sw_code.replace("'./icon-512.png'", "'./icon-512.png',\n  './igreja.jpg'")

with open("sw.js", "w", encoding="utf-8") as f:
    f.write(sw_code)

print("sw.js updated with igreja.jpg and v7!")