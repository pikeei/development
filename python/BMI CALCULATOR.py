

80
weight = float(input("enter a weight"))
height = float(input("enter a height"))

bmi = round(weight/height**2)
print(bmi)


if bmi<=18.5:
    print(f"your bmi is {bmi} underweight")
elif bmi<25:
    print(f"your bmi is {bmi} normal weight")
elif bmi<30:
    print(f"your bmi is {bmi} overweight")
elif bmi<35:
    print(f"your bmi is {bmi} obese")
else:
    print(f"your bmi is {bmi} clinically obese")


    

    


