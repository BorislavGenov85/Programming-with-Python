voucher_volume = int(input())
purchase = input()
movie_count = 0
something = 0
price = 0
while purchase != "End":

    if len(purchase) > 8:
        letter_one = purchase[0]
        letter_two = purchase[1]
        price += ord(letter_one) + ord(letter_two)
        if voucher_volume - price <= 0:
            print(f"{movie_count}")
            print(f"{something}")
            break
        movie_count += 1
    elif len(purchase) <= 8:
        letter_one = purchase[0]
        price += ord(letter_one)
        if voucher_volume - price <= 0:
            print(f"{movie_count}")
            print(f"{something}")
            break
        something += 1

    purchase = input()
else:
    print(f"{movie_count}")
    print(f"{something}")
