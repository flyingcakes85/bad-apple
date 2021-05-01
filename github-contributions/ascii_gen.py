import PIL.Image
import time

ASCII_CHARS = ["0", "4", "4"]


def to_greyscale(image):
    return image.convert("L")


def resize(image, new_width=50):
    width, height = image.size
    new_height = new_width * height / width
    return image.resize((int(new_width), int(new_height)))


def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//128]
        ascii_str += ","
    return ascii_str


def main():

    print ("var frames = [\n")

    # for i in range(1, 5):
    for i in range(1, 6573):
        print ( "[")
        path = "../frames/frame-" + f"{i:04d}" + ".jpg"
        try:
            image = PIL.Image.open(path)
        except:
            print(path, "Unable to find image ")
        # resize image
        image = resize(image)

        # convert image to greyscale image
        # convert greyscale image to ascii characters
        greyscale_image = to_greyscale(image)
        ascii_str = pixel_to_ascii(greyscale_image)
        img_width = greyscale_image.width
        ascii_str_len = len(ascii_str)
        ascii_img = ""

        # Split the string based on width  of the image
        for i in range(0, ascii_str_len, img_width*2):
            ascii_img += ascii_str[i:i+img_width*2] + \
                "\n"

        ascii_arr = ascii_img.replace(",\n", "],\n[")
        ascii_img = "[" + ascii_arr[:-1]
        ascii_arr = ascii_img[:-2]
        print(ascii_arr)
        print ( "],\n")

    print("]")

main()
