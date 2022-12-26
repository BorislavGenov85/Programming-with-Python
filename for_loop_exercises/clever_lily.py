age = int(input())
washer_price = float(input())
toy_price = int(input())

toy_count = 0
money = 0
total_sum = 0
brother_count = 0
for i in range(1, age + 1):
    if i % 2 != 0:
        toy_count = toy_count + 1
    else:
        money = money + 10
        total_sum = total_sum + money
        brother_count = brother_count + 1
result = ((toy_count * toy_price) + total_sum) - brother_count
diff = abs(result - washer_price)
if result >= washer_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
