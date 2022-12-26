num1 = int(input())
num2 = int(input())

num1_first = int(num1 / 1000)
num1_second = int((num1 / 100) % 10)
num1_third = int((num1 / 10) % 10)
num1_fourth = int(num1 % 10)

num2_first = int(num2 / 1000)
num2_second = int((num2 / 100) % 10)
num2_third = int((num2 / 10) % 10)
num2_fourth = int(num2 % 10)

for i in range(num1_first, num2_first + 1):
    for j in range(num1_second, num2_second + 1):
        for k in range(num1_third, num2_third + 1):
            for l in range(num1_fourth, num2_fourth + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    print(f'{i}{j}{k}{l}', end=" ")
