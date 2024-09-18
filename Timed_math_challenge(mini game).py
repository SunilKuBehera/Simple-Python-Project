import random
import time

operators = ["+","-","*"]
min_operand = int(input("Enter the minimum operand : "))
max_operand = int(input("Enter the maximum operand : "))
total_problems = int(input("Enter the number of problems you want to solve : "))

def generate_problem():
    left = random.randint(min_operand,max_operand)
    right = random.randint(min_operand,max_operand)
    operator = random.choice(operators)
    
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr,answer

wrong = 0 
input("Press Enter To Start !")
print("----------------------")

start_time = time.time()

for i in range(total_problems):
    expr,answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + " : " + expr + " = ")
        if guess == str(answer):
            break
        wrong == 1
        
end_time = time.time()
total_time = round(end_time - start_time,2)
        
print("-----------------------")
print("Nice work ! You finished in ",total_time,"seconds!")