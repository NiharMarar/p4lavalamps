class Math:

    def __init__(self ,a ,b, word):
        self._product = (a*b)
        self._sum = (a+b)
        self._characterlist = [char for char in word]

    @property
    def product(self):
        return self._product
    @property
    def sum(self):
        return self._sum
    @property
    def words(self):
        return self._characterlist

a = input("What is the first number?")
b = input("What is the second number?")
a = int(a)
b = int(b)
word = input("What is a word you would like to split?")
math = Math(a,b, word)
print(f"The sum of the two provided numbers are {math.sum} ")
print(f"The product of the two provided numbers are {math.product} ")
print(f"The word you gave me splitted comes out to, ")
for x in math.words:
    print(x)



