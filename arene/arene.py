from PIL import Image, ImageDraw
import random

W, H = 1280, 720

img = Image.new("RGB", (W, H))
draw = ImageDraw.Draw(img)

# 1. Draw the Gradient Sky
for y in range(H):
    t = y / H
    r = int(230 - 40 * t)
    g = int(200 - 50 * t)
    b = int(140 - 30 * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# 2. Draw the Dunes
for _ in range(8):
    x = random.randint(-200, W)
    y = random.randint(H//2, H)
    w = random.randint(400, 900)
    h = random.randint(80, 160)

    # Fixed: consistency in variable naming
    dune_color = (
        random.randint(210, 225),
        random.randint(185, 200),
        random.randint(130, 145)
    )

    draw.ellipse(
        [x, y, x + w, y + h],
        fill=dune_color
    )

# 3. Draw Sand Texture (Grain)
# Fixed: added the missing loop variable 'i'
for i in range(12000):
    x = random.randint(0, W)
    # Hint: Change 0 to H//2 if you want grain ONLY on the desert floor
    y = random.randint(H//2, H) 
    draw.point(
        (x, y),
        fill=(
            random.randint(210, 235),
            random.randint(190, 210),
            random.randint(140, 160)
        )
    )

# 4. Draw Rocks/Debris
for _ in range(25):
    x = random.randint(0, W)
    y = random.randint(H//2, H)
    r = random.randint(6, 14)
    draw.ellipse(
        [x, y, x + r, y + r],
        fill=(160, 140, 100)
    )

img.save("fond_de_map_desert.png")
print("Fond désert créé : fond_de_map_desert.png")
img.show()