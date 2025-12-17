name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

height_m = height / 100
bmi = weight / (height_m ** 2)

print(f"{name}, your BMI is {bmi:.1f}")