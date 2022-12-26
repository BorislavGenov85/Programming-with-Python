number = input()
sum_prime = 0
non_prime = 0

while number != "stop":
    current_num = int(number)

    if current_num < 0:
        print("Number is negative.")
        number = input()
        continue

    counter = 0
    for i in range(1, current_num + 1):
        if current_num % i == 0:
            counter += 1

    if counter == 2:
        sum_prime += current_num
    else:
        non_prime += current_num

    number = input()
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {non_prime}")
