from PIL import Image, ImageDraw, ImageFont
import zipfile

def criar_icone(tamanho, nome_arquivo):
    img = Image.new('RGBA', (tamanho, tamanho), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([(8, 8), (tamanho - 8, tamanho - 8)], fill=(12, 74, 110, 255), outline=(245, 158, 11, 255), width=max(4, tamanho // 35))
    cor_onda = (2, 132, 199, 200)
    draw.chord([(tamanho * 0.15, tamanho * 0.45), (tamanho * 0.85, tamanho * 0.85)], start=0, end=180, fill=cor_onda)
    draw.ellipse([(tamanho * 0.38, tamanho * 0.22), (tamanho * 0.62, tamanho * 0.46)], fill=(251, 191, 36, 255))
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(tamanho * 0.32))
        draw.text((tamanho * 0.5, tamanho * 0.65), "SL", fill=(255, 255, 255, 255), font=font, anchor="mm")
    except Exception:
        draw.rectangle([(tamanho*0.35, tamanho*0.55), (tamanho*0.65, tamanho*0.75)], fill=(255, 255, 255, 255))
    img.save(nome_arquivo, "PNG")

criar_icone(192, "icon-192.png")
criar_icone(512, "icon-512.png")

with zipfile.ZipFile("portal-pwa.zip", "w") as z:
    z.write("index.html")
    z.write("manifest.json")
    z.write("sw.js")
    z.write("icon-192.png")
    z.write("icon-512.png")
    z.write("igreja.jpg")

print("portal-pwa.zip criado com sucesso com todos os 6 ficheiros!")