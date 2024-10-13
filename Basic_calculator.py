while True:
    operator = input("Please select an operator : (+ , - , / , *) \n")

    num1 = float(input("Please enter number one   :"))
    num2 = float (input("Please enter number two   :"))

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "*":
        print(num1 * num2)
    else:
        print("You have selected an invalid operator!")
