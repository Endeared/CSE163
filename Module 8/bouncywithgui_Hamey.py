# Ross Hamey
# CSE163 - P8.2
# 10/29/2023
# https://github.com/Endeared

"""
File: bouncywithgui.py
Project 8.2

Determines the distance traveled by a bouncing ball.

Inputs: Initial height, bounciness index, and number of bounces
"""

from breezypythongui import EasyFrame

def computeDistance(height, index, bounces):
    """Computes the total distance traveled by the ball,
    given an initial height, bounciness index, and
    number of bounces."""
    pass

class BouncyGUI(EasyFrame):

    def __init__(self):
        """Set up the window and widgets."""
        EasyFrame.__init__(self,  title = "Bouncy")
        """Define the following fields"""
        # self.heightField (number entry)
        self.addLabel(text = "Initial height", row = 0, column = 0)
        self.heightField = self.addFloatField(value = 0.0, row = 0, column = 1)

        # self.indexField (number entry)
        self.addLabel(text = "Bounciness index", row = 1, column = 0)
        self.indexField = self.addFloatField(value = 0.0, row = 1, column = 1)

        # self.bouncesField (number entry)
        self.addLabel(text = "Number of bounces", row = 2, column = 0)
        self.bouncesField = self.addIntegerField(value = 0, row = 2, column = 1)

        # self.computeButton (button)
        self.computeButton = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.computeDistance)

        # self.distanceField (result result)
        self.addLabel(text = "Total distance", row = 4, column = 0)
        self.distanceField = self.addFloatField(value = 0.0, row = 4, column = 1)


    def computeDistance(self):
        height = self.heightField.getNumber()
        bounciness = self.indexField.getNumber()
        bounces = self.bouncesField.getNumber()

        distance = 0
        for i in range(bounces):
            distance += height
            height *= bounciness
            distance += height
        
        self.distanceField.setNumber(distance)

def main():
    """Instantiate and pop up the window."""
    BouncyGUI().mainloop()

if __name__ == "__main__":
    main()

