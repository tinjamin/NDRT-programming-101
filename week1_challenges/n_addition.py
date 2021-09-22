answer = None 
n = int(input("Please input the number that you would like to find the total sum of every preceeding number, including the number: "))

for i in range(0, n+1):
    if i == 0:
        answer = i
    else: 
        answer = answer + i 

print(f"{answer}")
