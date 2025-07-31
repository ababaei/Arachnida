import argparse
import os
import sys
from PIL import Image, ExifTags

IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')

def is_image_valid(path):
    return path.lower().endswith(IMAGE_EXTENSIONS)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+', help='images list to analyze')

    args = parser.parse_args()

    try:
        for file in args.files:
            print("Processing:", file)
            if not os.path.exists(file):
                print("File doesn't exist !")
                continue
            if is_image_valid(file):
                img = Image.open(file)
                img_exif = img.getexif()
                if img_exif is None or len(img_exif) == 0:
                    print("Image has no exif data.")
                else:
                    for key, val in img_exif.items():
                        if key in ExifTags.TAGS:
                            print(f"{ExifTags.TAGS[key]}:{val}")
                        else:
                            print(f"{key}:{val}")
                print("____________________________________")
    except Exception as e:
        print(f"error with file {file}: {e}")