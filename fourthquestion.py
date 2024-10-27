def is_perfect(num):
    if num < 2:
        return False
    divisors_sum = sum(i for i in range(1,num) if num % i ==0) 
    return divisors_sum == num
def find_perfect_numbers(limit):
    perfect_numbers = []
    for i in range(2, limit):
        if is_perfect(i):
            perfect_numbers.append(i)  
            return perfect_numbers


limit = 1000000
perfect_numbers =find_perfect_numbers(limit)
print(perfect_numbers)




