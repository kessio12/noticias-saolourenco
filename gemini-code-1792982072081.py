import os

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

print("Current length of index.html:", len(html))
print("Files present:", os.listdir("."))