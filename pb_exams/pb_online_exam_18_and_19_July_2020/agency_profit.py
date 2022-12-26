company_name = input()
adult_tickets = int(input())
children_tickets = int(input())
adult_tickets_price = float(input())
service_price = float(input())

children_tickets_price = adult_tickets_price * 0.30
adult_plus_service = adult_tickets_price + service_price
children_plus_service = children_tickets_price + service_price
total_price = (children_tickets * children_plus_service) + (adult_tickets * adult_plus_service)
profit = total_price * 0.20
print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")
