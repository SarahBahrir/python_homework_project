import sys
from PIL import Image

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} image-filename")
        exit(-1)
    image_path = sys.argv[1]

    img = Image.open(image_path)
    r, g, b = img.split()



    red_img = Image.merge("RGB", (r, Image.new("L", r.size), Image.new("L", r.size)))
    green_img = Image.merge("RGB", (Image.new("L", g.size), g, Image.new("L", g.size)))
    blue_img = Image.merge("RGB", (Image.new("L", b.size), Image.new("L", b.size), b))


    red_img.show()
    green_img.show()
    blue_img.show()







if __name__ == "__main__":
    main()
