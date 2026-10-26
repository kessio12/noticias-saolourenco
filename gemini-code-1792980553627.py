import zipfile

with zipfile.ZipFile("portal-pwa.zip", "w") as z:
    z.write("index.html")
    z.write("manifest.json")
    z.write("sw.js")
    z.write("icon-192.png")
    z.write("icon-512.png")
    z.write("igreja.jpg")

print("portal-pwa.zip gerado com todos os ficheiros, incluindo igreja.jpg!")