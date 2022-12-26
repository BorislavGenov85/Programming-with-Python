rent = int(input())

statuettes = rent * 0.70
kettering = statuettes * 0.85
noise = kettering / 2

total_price = rent + statuettes + kettering + noise
print(f"{total_price:.2f}")
