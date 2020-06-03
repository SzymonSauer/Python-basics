print("Enter your height: ")
height = float(input())
if height >=3.00:
    print("Wow! You are the world's highest man! ;)")
print("Enter your weight: ")
weight = float(input())

bmi = weight/(height**2)


print("BMI:"+str(bmi))
if bmi<18.5:
    print("You are too thin!")
elif bmi>=18.5 and bmi <25:
    print("Congratulatons! You have great BMI!")
elif bmi>=25:
    print("You are overweight!")