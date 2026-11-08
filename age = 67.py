distance = 150.5
consumption = 8.5
price = 55.4
total_liters = (distance * consumption) / 100
total_cost = total_liters * price
distance_20 = distance * 1.2
liters_20 = (distance_20 * consumption) / 100
cost_20 = liters_20 * price
print("Base calculation:")
print(total_liters)
print(total_cost)
print("Plus 20% distance:")
print(liters_20)
print(cost_20)