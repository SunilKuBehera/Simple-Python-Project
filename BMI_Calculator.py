name = input("Enter Your Name : ")
weight = int(input("Enter your weight in pound : "))
height = int(input("Enter your height in inches : "))
BMI = (weight * 703) / (height * height)
print("BMI is : ",BMI)

if(BMI<18.5):
    print("Under weight - Minimal")
elif(BMI >= 18.5) and (BMI < 24.9):
    print("Normal Weight - Minimal")
elif(BMI >= 25) and (BMI < 29.9):
    print("Over Weight! - Increased")
elif(BMI >= 30) and (BMI < 34.9):
    print("Obese - High")
elif(BMI >= 35) and (BMI < 39.9):
    print("Severely Obese - Very High")
elif(BMI > 40):
    print("Morbidly Obese - Extreamly High")
else:
    print("Invalid input!")