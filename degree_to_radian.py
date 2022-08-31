from math import pi

# to achieve radian of a degree we should multiply degree to PI/180
# to achieve degree of a radian we should multiply radian to 180/PI

def ConvertToRadianDegree(choice):

    if choice == "d":
        degree_to_radian = float(input("Enter a degree: "))
        radian = degree_to_radian * (pi / 180)
        return f"{degree_to_radian} Deg is {round(radian, 6)} Rad"
    elif choice == "r":
        radian_to_degree = float(input("Enter a radian: "))
        degree = radian_to_degree * (180 / pi)
        return f"{radian_to_degree} Rad is {round(degree, 4)} Deg"
    else:
        return "Wrong choice!!!"

userChoice = input("Press 'd' to convert degrees to radians, and 'r' to convert radians to degrees : ").lower()

result = ConvertToRadianDegree(userChoice)
print(result)




