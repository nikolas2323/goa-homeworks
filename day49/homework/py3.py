height = int(input("Enter you height(cm): "))

weight = int(input("Enter you weight(kg): "))

res = weight / height

if res < 18.5:
    print("Underweight")

elif res > 18.5 and res < 25:
    print("Normal")

elif res > 25 and res < 30:
    print("Overweight")

elif res > 30:
    print("Obese")