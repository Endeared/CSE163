# Ross Hamey
# CSE163 - P7.5
# 10/29/2023
# https://github.com/Endeared

# importing Image class from images.py
from images import Image

# posterize func, which takes in an image and tuple of colors (r, g, b)
def posterize(image, colors):
    # for each pixel in our image
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            # get the tuple r g b values of current pixel, calculate avg of values
            (r, g, b) = image.getPixel(x, y)
            average_current = (r + g + b) // 3

            # if our avg is less than 128, we set the pixel to our colors tuple
            if average_current < 128:
                image.setPixel(x, y, colors)
            else:
            # otherwise, we set the pixel to white
                image.setPixel(x, y, (255, 255, 255))

# source code - unchanged
def main():
    filename = input("Enter the image file name: ")
    red = int(input("Enter an integer [0..255] for red: "))
    green = int(input("Enter an integer [0..255] for green: "))
    blue = int(input("Enter an integer [0..255] for blue: "))                    
    image = Image(filename)
    posterize(image, (red, green, blue))
    image.draw()

if __name__ == "__main__":
   main()