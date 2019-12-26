from my_math import divisor_master

num_1 = 124

if divisor_master.is_simple_number(num_1):
    print("{} - это простое число".format(num_1))
else:
    print("{} - это не простое число".format(num_1))

print("\n--------- Делители числа {} -------".format(num_1))
print(divisor_master.all_divisors(num_1))

print("\n--------- Наибольший простой делитель числа {} -------".format(num_1))
print(divisor_master.get_biggest_simple_divisor(num_1))

print("\n--------- Наибольший делитель числа {} -------".format(num_1))
print(divisor_master.get_biggest_divisor(num_1))
