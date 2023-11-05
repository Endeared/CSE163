# Ross Hamey
# CSE163 - P8.3
# 11/5/2023
# https://github.com/Endeared


"""
File: temperatureconverter.py
Project 8.3
Temperature conversion between Fahrenheit and Celsius.
Illustrates the use of numeric data fields.
"""

from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    """A termperature conversion program."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Temperature Converter")

        # self.addLabel (Label for Celsius)
        self.addLabel(text = "Celsius", row = 0, column = 0)

        # self.celsiusField (Celsius field)
        self.celsiusField = self.addFloatField(value = 0.0, row = 1, column = 0)

        # self.addLabel (Label for Fahrenheit)
        self.addLabel(text = "Fahrenheit", row = 0, column = 1)

        # self.fahrField (Fahrenheit field)
        self.fahrField = self.addFloatField(value = 32.0, row = 1, column = 1)

        # self.addButton (Celsius button)
        self.celsBtn = self.addButton(text = ">>>>", row = 2, column = 0, command = self.computeCelsius)

        # self.addButton (Fahrenheit button)
        self.fahrBtn = self.addButton(text = "<<<<", row = 2, column = 1, command = self.computeFahr)

    # The controller methods
    def computeFahr(self):
        celsius = self.celsiusField.getNumber()
        fahr = (9 / 5) * celsius + 32
        round(fahr, 1)
        self.fahrField.setNumber(fahr)

    def computeCelsius(self):
        fahr = self.fahrField.getNumber()
        celsius = (fahr - 32) * (5 / 9)
        round(celsius, 1)
        self.celsiusField.setNumber(celsius)
        
def main():
    """Instantiate and pop up the window."""
    TemperatureConverter().mainloop()

if __name__ == "__main__":
    main()

