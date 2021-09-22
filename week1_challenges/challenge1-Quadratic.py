import math 

def quadratic_solver(values_list, access_answer):
    a = values_list[0]
    b = values_list[1]
    c = values_list[2]
    if access_answer == 1: 
        answer = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    else: 
        answer = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    return answer


values = []
print("Welcome to this bomb program that can solve a quadratic equation.")
print("Please enter the following values") 

for i in range(0,3):  
    if i == 0: 
        values.append(int(input("Please input a value for a: ")))
    elif i == 1: 
        values.append(int(input("Please input a value for b: ")))
    else:
        values.append(int(input("Please input a value for c: ")))

for i in range(1,3):
    print(f"This is the {i} root: {quadratic_solver(values,i)}")
