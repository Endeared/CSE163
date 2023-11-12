# Ross Hamey
# CSE163 - P9.1
# 11/12/2023
# https://github.com/Endeared

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    
    def __eq__(self, other):
        return self.name == other.name and self.scores == other.scores
    
    def __lt__(self, other):
        return self.name < other.name
    
    def __ge__(self, other):
        return self.name >= other.name
        
    # Write method definitions here

def main():
    """A simple test."""
    student = Student("Ken", 5)
    student_two = Student("Ken", 5)

    print(f'{student.__eq__(student_two)}: {student.__eq__(student_two)}')
    print(f'{student.__lt__(student_two)}: {student.__lt__(student_two)}')
    print(f'{student.__ge__(student_two)}: {student.__ge__(student_two)}')

if __name__ == "__main__":
    main()
