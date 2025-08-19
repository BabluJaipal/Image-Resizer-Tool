

import os
from PIL import Image

def resize_single_image(image_path, output_folder, width, height, output_format="JPEG"):
    """Resize a single image."""
    try:
        with Image.open(image_path) as img:
            resized_img = img.resize((width, height), Image.Resampling.LANCZOS)

            # Get image name
            base_name = os.path.splitext(os.path.basename(image_path))[0]
            output_file = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")

            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            resized_img.save(output_file, output_format)
            print(f"✔ Saved: {output_file}")

    except Exception as e:
        print(f"✘ Error resizing {image_path} (Error: {e})")

def resize_images(input_folder, output_folder, width, height, output_format="JPEG"):
    """Resize and convert all images in a folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)

        try:
            with Image.open(file_path) as img:
                resized_img = img.resize((width, height), Image.Resampling.LANCZOS)

                base_name, _ = os.path.splitext(file_name)
                output_file = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")

                resized_img.save(output_file, output_format)
                print(f"✔ Saved: {output_file}")

        except Exception as e:
            print(f"✘ Skipped {file_name} (Error: {e})")

if __name__ == "__main__":
    print("Choose Mode:")
    print("1. Resize all images in a folder")
    print("2. Resize a single image")
    choice = input("Enter choice (1/2): ")

    width = int(input("Enter desired width: "))
    height = int(input("Enter desired height: "))
    output_format = input("Enter output format (JPEG/PNG/WEBP): ").upper()

    if choice == "1":
        input_folder = "input_images"
        output_folder = "output_images"
        resize_images(input_folder, output_folder, width, height, output_format)

    elif choice == "2":
        image_path = input("Enter full path of the image: ")
        output_folder = "output_single"
        resize_single_image(image_path, output_folder, width, height, output_format)

    else:
        print("❌ Invalid choice. Please run again.")
