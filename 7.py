class PercentageError(Exception):
    pass

class InvalidPercentageError(PercentageError):
    pass

class LessPercentageError(PercentageError):
    pass


class Student:
    def __init__(self, name, percentage):
        self.name = name
        self.percentage = percentage

    def check_eligibility(self, cutoff, maximum):
        try:
            if self.percentage < 0:
                raise InvalidPercentageError(
                    "Invalid Percentage! Must be between 0 and 100"
                )

            if self.percentage > maximum:
                raise InvalidPercentageError(
                    "Percentage exceeds maximum allowed score"
                )

            if self.percentage < cutoff:
                raise LessPercentageError(
                    "Percentage is less than cutoff"
                )

            print(self.name, "is eligible for enrollment")

        except PercentageError as e:
            print(self.name, "->", e)


cutoff = 50
maximum = 100

name = input("Enter student name: ")
percentage = float(input("Enter student percentage: "))

student = Student(name, percentage)
student.check_eligibility(cutoff, maximum)