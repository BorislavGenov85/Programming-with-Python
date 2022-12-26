cpu_price_usd = float(input())
video_card_usd = float(input())
ram_price_usd = float(input())
ram_count = int(input())
percent_discount = float(input())

cpu_price_lv = cpu_price_usd * 1.57
video_card_price_lv = video_card_usd * 1.57
ram_price_lv = ram_price_usd * 1.57
total_ram_price = ram_price_lv * ram_count
total_cpu_price = cpu_price_lv - (cpu_price_lv * percent_discount)
total_video_card_price_lv = video_card_price_lv - (video_card_price_lv * percent_discount)

total_price_for_parts = total_cpu_price + total_ram_price + total_video_card_price_lv

print(f"Money needed - {total_price_for_parts:.2f} leva.")

