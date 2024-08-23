def is_prime(func):
    def wrapper (*args, **kwargs):
        original_result = func(*args, **kwargs)
        for i in range(2, (original_result // 2) + 1):
            if original_result % i == 0:
                return f'Составное\n{original_result}'
        return f'Простое\n{original_result}'
    return wrapper


@is_prime
def sum_three(*args):
    a = 0
    for i in args:
        a += i
    return a


result = sum_three(2, 3, 6)
print(result)