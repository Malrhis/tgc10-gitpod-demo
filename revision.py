print("Happy 2021!!!")

# variables
secret_of_life = 42
gst_percentage = 0.07

# BMI Calculator
weight = float(input("Please enter your weight in kg"))
height = float(input("Please enter your height in metres"))
bmi = weight / (height * height)

if bmi < 18.5:
    print("underweight")
# else if bmi < 