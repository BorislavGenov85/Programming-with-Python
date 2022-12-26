cargo_count = int(input())
total_all_cargo = 0
total_van_count = 0
total_truck_count = 0
total_train_count = 0
for i in range(1, cargo_count + 1):
    cargo_t = int(input())
    all_cargo = 0
    van_count = 0
    truck_count = 0
    train_count = 0
    if cargo_t <= 3:
        all_cargo += cargo_t
        van_count += cargo_t

    elif cargo_t <= 11:
        all_cargo += cargo_t
        truck_count = cargo_t

    elif cargo_t > 11:
        all_cargo += cargo_t
        train_count = cargo_t
    total_all_cargo += all_cargo
    total_van_count += van_count
    total_truck_count += truck_count
    total_train_count += train_count
average_per_t = (total_van_count * 200 + total_truck_count * 175 + total_train_count * 120) / total_all_cargo
van_percent = (total_van_count / total_all_cargo) * 100
truck_percent = (total_truck_count / total_all_cargo) * 100
train_percent = (total_train_count / total_all_cargo) * 100
print(f"{average_per_t:.2f}")
print(f"{van_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")
