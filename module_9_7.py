
def is_prime(fanc):
    def wrapper(*args, **kwargs):
        result = fanc(*args, **kwargs)
        summa = sum(args)
        counter = 0
        for i in range(1, summa % 2 + 1):
            if summa % i == 0:
                counter += 1
        if counter > 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    total = sum(args)
    return total

result = sum_three(2, 3, 6)
print(result)