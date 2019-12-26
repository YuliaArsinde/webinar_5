def is_simple_number(target_number):
    for num in range(2, target_number):
        if target_number % num == 0:
            return False
    return True


def all_divisors(target_number):
    divisors_list = []
    for divisor in range(1, target_number + 1):
        if target_number % divisor == 0:
            divisors_list.append(divisor)
    return divisors_list


def get_biggest_simple_divisor(target_number):
    if is_simple_number(target_number):
        return target_number
    else:
        divisors = all_divisors(target_number)
        for d in reversed(divisors):
            if is_simple_number(d):
                return d




def get_biggest_divisor(target_number):
    if is_simple_number(target_number):
        return target_number
    for divisor in range(2, target_number):
        if target_number % divisor == 0:
            return int(target_number / divisor)

