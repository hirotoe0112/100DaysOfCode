height = float(input())
weight = int(input())

bmi = weight / height**2
bmi_result = f"Your BMI is {bmi}"

if bmi < 18.5:
    print(f"{bmi_result}, you are underweight.")
elif bmi < 25:
    print(f"{bmi_result}, you have a normal weight.")
elif bmi < 30:
    print(f"{bmi_result}, you are slightly overweight.")
elif bmi < 35:
    print(f"{bmi_result}, you are obese.")
else:
    print(f"{bmi_result}, you are clinically obese.")
