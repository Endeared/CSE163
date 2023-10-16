# Ross Hamey
# CSE163 - P3.4
# 9/24/2023
# https://github.com/Endeared

# grabbing inputs from user, setting initial distance var
height = int(input("Enter the height from which the ball is dropped: "))
bounciness = float(input("Enter the bounciness index of the ball: "))
bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))
total_distance = 0

# iterating through bounces, adding distance from drop, then
# distance from bounce back up
for i in range(bounces):
    total_distance += height
    height *= bounciness
    total_distance += height

# print distance
print(f'The total distance traveled is {total_distance:.3f} units.')
