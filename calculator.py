
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    def multiply(self):
        return self.num1 * self.num2
    def substract(self):
        return self.num1 - self.num2
    def divide(self):
        return self.num1 / self.num2
    def raisetopower(self):
        return self.num1 ** self.num2
    
def main():
    numbers = Calculator(int(input("First Number: ")), int(input("Secon Number: ")))
    calculation = input("What do you want to do: ")
    result = getattr(numbers,calculation, "Non-existend")
    print(result())
    if input("do you wish to continue? yes/no \n") == "yes":
        main()
    
        



if __name__ == '__main__':
    main()