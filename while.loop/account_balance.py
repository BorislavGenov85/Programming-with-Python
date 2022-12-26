balance = 0

while True:
    deposit_sum = input()
    if deposit_sum == "NoMoreMoney":
        break

    deposit_sum = float(deposit_sum)

    if deposit_sum >= 0:
        balance += deposit_sum
        print(f"Increase: {deposit_sum:.2f}")

    else:
        print("Invalid operation!")
        break
print(f"Total: {balance:.2f}")
