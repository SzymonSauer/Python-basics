def main():
    end = False
    while not end:
        print("Give me a number: ")
        number1 = float(input())
        print("Now select one of the options: +, -, *, /, %, ^")
        process = input()
        print("And now give me the second number: ")
        number2 = float(input())

        if process =='+':
            result = number1+number2
        elif process =='-':
            result = number1 - number2
        elif process =='*':
            result = number1 * number2
        elif process =='/':
            result = number1 / number2
        elif process =='%':
            result = number1 - number2
        elif process =='^':
            result = number1 ** number2
        else:
            print("You have selected a bad character, please try again: ")
            continue

        print("Result: "+str(result))
        print("Do you want to continue? Press: y or n")

        next_process = input()
        if next_process=='n':
            end = True
        elif next_process!='y':
            print("You have selected a bad character!")
            break


if __name__ == "__main__":
    main()
