class Time:

    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"

    def __add__(self, other):

        temp = Time()

        temp.h = self.h + other.h
        temp.m = self.m + other.m
        temp.s = self.s + other.s

        if temp.s > 59:
            temp.s = temp.s % 60
            temp.m = temp.m + 1

        if temp.m > 59:
            temp.m = temp.m % 60
            temp.h = temp.h + 1

        return temp


t1 = Time(2, 30, 45)
print(t1)

t2 = Time(3, 20, 30)
print(t2)

t3 = t1 + t2
print(t3)