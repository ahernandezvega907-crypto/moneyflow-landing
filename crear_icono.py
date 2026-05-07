from PIL import Image, ImageDraw, ImageFont

# Dimensiones: 600x600 (mínimo requerido por Gumroad)
size = 600
img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fondo circular verde menta (#00BFA6)
circle_color = (0, 191, 166, 255)
draw.ellipse((50, 50, size - 50, size - 50), fill=circle_color)

# Símbolo "$" en blanco
try:
    # Intentar con una fuente grande del sistema
    font = ImageFont.truetype("arial.ttf", 320)
except:
    # Si no encuentra Arial, usar la fuente por defecto (más pequeña)
    font = ImageFont.load_default()

# Dibujar "$" centrado
draw.text((size // 2, size // 2), "$", fill=(255, 255, 255), anchor="mm", font=font)

# Guardar el PNG
img.save("moneyflow_icon.png")
print("✅ Icono guardado como moneyflow_icon.png")