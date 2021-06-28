class cal:
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

        if self.operator == "+":
            print(f"The sum of {self.num1} and {self.num2} is {self.num1 + self.num2}")
        elif self.operator == "-":
            print(f"The difference between {self.num1} and {self.num2} is {self.num1 - self.num2}")
        elif self.operator == "*":
            print(f"The product of {self.num1} and {self.num2} is {self.num1 * self.num2}")
        elif self.operator == "**":
            print(f"The result when the power of {self.num1} is {self.num2} is {self.num1 ** self.num2}")
        elif self.operator == "/":
            print(f"The quotient when {self.num1} is divided by {self.num2} is {self.num1 / self.num2}")
        elif self.operator == "//":
            print(f"The nearest number which can divide {self.num1} with {self.num2} is {self.num1 // self.num2}")
        elif self.operator == "%":
            print(f"The remainder when {self.num1} is divided by {self.num2} is {self.num1 % self.num2}")
        else:
            print("Please select one from these given operators: +, -, *, **, /, //, % \n")

op = input("Enter a operator here to choose what you want to do, the options are: +, -, *, **, /, //, % \n")
a = int(input("Enter a number here\n"))
b = int(input("Enter another number here\n"))
e = cal(a, b, op)