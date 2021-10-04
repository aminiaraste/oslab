weight = int(input(" please enter your weight : "))
hight = float (input(" please enter your hight :"))
BMI =  (weight /(hight * hight))
if BMI < 18.5 :
    print("you are UNDERWEIGHT ! eat more food ")
elif 18.5< BMI < 24.9 :
    print(" you look soo good :)")
elif 25< BMI < 29.9 :
    print (" be careful")
elif 30 < BMI < 34.9 :
    print(" you are ABESE !! do more workout")
else :
    print(" you are EXTERMLY OBESE shame on you :/")
