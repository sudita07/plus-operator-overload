# class bubble:
#     def __init__(self, volume):
#         self.volume = volume
#     def __str__(self):
#         return "volume is " + str(self.volume)
#     def __add__(self, other):
#         volume = self.volume + other.volume
#         return bubble(volume)
# b1=bubble(10)
# b2=bubble(5)
# b3=(b1+b2)
# print(b3)

class pool:
    def __init__(self, line, water):
        self.line=line
        self.water=water
    def __add__(self, other):
        x=self.line+other.line
        y=self.water+other.water
        z=x+y
        return z
h=pool(3,7)
b=pool(2,7)
q=(h+b)
print(q)