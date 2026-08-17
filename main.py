from services.image_service import ImageService


def main():

    print("=" * 40)
    print(" Lavanda Upload Assistant")
    print("=" * 40)

    service = ImageService()

    service.scan_images()

    print("\nFim.")


if __name__ == "__main__":
    main()