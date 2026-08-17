from pathlib import Path


class ImageService:

    def __init__(self):

        self.input_folder = Path("input")

        self.extensions = [".jpg", ".jpeg", ".png", ".webp"]


    def scan_images(self):

        if not self.input_folder.exists():

            print("❌ Pasta input não encontrada.")

            return

        print("📁 Pasta encontrada.\n")

        images: list[Path] = []

        for file in self.input_folder.iterdir():

            if file.suffix.lower() in self.extensions:

                images.append(file)

        print(f"🖼️ Encontradas {len(images)} imagens.")