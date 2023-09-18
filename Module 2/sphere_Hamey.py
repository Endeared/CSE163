# Ross Hamey
# CSE163 - P2.4
# 9/17/2023
# https://github.com/Endeared

import math

radius = float(input("Enter a radius: "))
diameter = 2 * radius
circumference = 2 * radius * math.pi
surface_area = 4 * (radius ** 2) * math.pi
volume = (4 / 3) * (radius ** 3) * math.pi

print(f'Radius = {radius}')
print(f'Diameter     : {diameter}')
print(f'Circumference: {circumference}')
print(f'Surface area : {surface_area}')
print(f'Volume       : {volume}')
