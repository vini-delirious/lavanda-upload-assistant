from pathlib import Path

from PIL import Image


class ImageProcessor:

    OUTPUT_WIDTH = 1080
    OUTPUT_HEIGHT = 1350

    def resize_image(self, image_path: Path, output_folder: Path):

        with Image.open(image_path) as image:

            image.thumbnail(
                (self.OUTPUT_WIDTH, self.OUTPUT_HEIGHT),
                Image.Resampling.LANCZOS
            )

            canvas = Image.new(
                "RGB",
                (self.OUTPUT_WIDTH, self.OUTPUT_HEIGHT),
                "white"
            )

            x = (self.OUTPUT_WIDTH - image.width) // 2
            y = (self.OUTPUT_HEIGHT - image.height) // 2

            canvas.paste(image, (x, y))

            output_file = output_folder / image_path.name

            canvas.save(
                output_file,
                quality=95,
                optimize=True
            )