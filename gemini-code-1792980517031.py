from PIL import Image
img = Image.open("input_file_1.png")
print("Image size:", img.size, img.format, img.mode)

# Save it as igreja.jpg
img_rgb = img.convert("RGB")
img_rgb.save("igreja.jpg", "JPEG", quality=90)
print("igreja.jpg salvo com sucesso!")