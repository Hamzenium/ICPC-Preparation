
def average(salary) -> float:
    maximum = max(salary)
    minimum = min(salary)
    return (sum(salary)-(maximum+minimum))/(len(salary)-2)

array = [1000,2000,3000,2302,2323]
print(average(array))