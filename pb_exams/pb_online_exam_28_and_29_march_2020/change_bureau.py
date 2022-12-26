
bitcoin = int(input())
china_yuan = float(input())
comisionna = float(input())

total_bitcoin = bitcoin * 1168
dollars = china_yuan * 0.15
dollars_leva = dollars * 1.76
total = total_bitcoin + dollars_leva
evro = total / 1.95
comision = evro * comisionna / 100
total_money = evro - comision
print(f"{total_money:.2f}")
