def main():
    print("Set the number of digits from which you want to calculate the arithmetic mean: ")
    numbers = float(input())

    sum = 0
    i = 1
    while i<=numbers:
        print("Enter a number: ")
        number = float(input())
        sum += number
        i+=1
    print("Arithmetic mean: " + str(sum/numbers))

if __name__ == "__main__":
    main()