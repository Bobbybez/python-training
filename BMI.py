w = float(input("Enter wight in kg:") )
h = float(input("Enter height in cm: ") )
hm = h/100

bmi = w /hm**2
bmi = round(bmi, 2)
print(f"BMI={bmi}")


if bmi<16.0:
 print("Underwight (Severe thinness)")

elif 16<=bmi<=16.9:
  print("Underweight (Moderate thinness")	

elif 17.0<=bmi<=18.4:
  print("Underweight (Mild thinness")


elif 18.5<=bmi<=24.9:
    print("Normal range")

elif 25.0<=bmi<=29.9:
    print("Overweight (Pre-obese")

        
elif 30.0<=bmi<=34.9:
    print("Obese (Class I)")

elif 35.0<=bmi<=39.9:
    print("Obese (Class II)")