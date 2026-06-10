from PIL import Image
import os

input_folder = "assets\\testwebp\\img"
output_folder = "assets\\testwebp\\webp"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.lower().endswith(".jpg"):
        img = Image.open(os.path.join(input_folder, file))
        name = os.path.splitext(file)[0]
        img.save(os.path.join(output_folder, name + ".webp"), "webp", quality=80)

print("done")