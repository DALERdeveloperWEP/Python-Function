user_money = float(input('oylik: '))

def calculate_tax(salary: float):
    if salary > 5_000_000:
        return salary * 0.20
    else:
        return salary * 0.13


def calculate_net_salary(salary: float):
    return user_money - calculate_tax(salary) 

print("Soliq:", calculate_tax(user_money))
print("Sof maosh:", calculate_net_salary(user_money))