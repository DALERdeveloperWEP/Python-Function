user_height = float(input("Bo'y: "))
user_weight = float(input("Og'irlik: "))

def calculate_bmi(weight: float, height: float):
    BMI = weight / (height ** 2)
    return BMI

def bmi_status(bmi: float):
    if bmi < 18.5:
        print(f"BMI = {round(bmi,2)}")
        print("Underweight (ozg‘in)")
    elif 18.5 <= bmi < 25:
        print(f"BMI = {round(bmi,2)}")
        print("Normal")
    elif 25 <= bmi < 30:
        print(f"BMI = {round(bmi,2)}")
        print("Overweight (semiz)")
    elif bmi >= 30:
        print(f"BMI = {round(bmi,2)}")
        print("Obesity (semirib ketgan)")

bmi_status(calculate_bmi(user_weight, user_height))