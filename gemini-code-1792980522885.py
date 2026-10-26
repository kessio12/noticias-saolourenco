with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
img_tags = re.findall(r'<img[^>]+>', html)
for it in img_tags:
    print(it)
print("-" * 50)
news_imgs = re.findall(r'imagem:\s*"[^"]+"', html)
for ni in news_imgs:
    print(ni)