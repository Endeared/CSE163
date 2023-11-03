# Ross Hamey
# CSE163 - P7.6
# 10/29/2023
# https://github.com/Endeared

# import Image class from images.py
from images import Image

# source function - unchanged
def grayscale1(image):
    """Converts an image to grayscale using the
    psychologically accurate transformations."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))

def grayscale2(image):
    # iterate over every pixel
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            # grab rgb values of pixel, calculate average, then set
            # each rgb value of pixel to our average
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            image.setPixel(x, y, (average, average, average))

# main function - unchanged
def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    grayscale2(image)
    image.draw()

if __name__ == "__main__":
    main()
