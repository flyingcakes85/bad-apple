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

    for i in range(1, 6573):
        
        path = "../frames/frame-" + f"{i:04d}" + ".jpg"
        try:
            image = PIL.Image.open(path)
        except:
            print(path, "Unable to find image ")
        # resize image
        image = resize(image)

        greyscale_image = to_greyscale(image)
        ascii_str = pixel_to_ascii(greyscale_image)
        
        frameFile = open("./ascii_frames/" + f"{i:04d}" + ".txt", "w")
        frameFile.write(ascii_str[:-1])
        frameFile.close()

main()
