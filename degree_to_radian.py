from math import pi

# to achieve radian of a degree we should multiply degree to PI/180
# to achieve degree of a radian we should multiply radian to 180/PI
my_pi = pi

while True:
    choice = input("For degree to radian pres 'd',"
                   " for radian to degree press 'r': \n".lower())
    if choice == "d":
        degree_to_radian = int(input("Enter a degree: "))
        radian = degree_to_radian * my_pi / 180
        print(f"Radian of {degree_to_radian} degree is {radian}")
        break
    elif choice == "r":
        radian_to_degree = float(input("Enter a radian: "))
        degree = radian_to_degree * 180/my_pi
        print(f"Degree of {radian_to_degree} radian is {int(degree)}")
        break
    else:
        print("Wrong choice!!!")




