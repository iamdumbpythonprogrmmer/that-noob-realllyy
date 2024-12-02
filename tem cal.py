unit = input("the unit : ")
tempeture = float(input("the tempeture : "))
if unit == "f":
    answer = (tempeture - 32) * 5/9
    ("answer is : " + str(round(answer))+ "f")
else :
    answer = (tempeture * 9/5) + 32
print("answer is : " + str(round(answer))+ "c")

