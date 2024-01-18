amount_purchase=int(input("enter amount purchase of meal"))
tip=(amount_purchase*15)/100
sale_tax=(amount_purchase*7)/100
total_tax=tip+sale_tax
total=amount_purchase+total_tax
print(amount_purchase)
print(tip)
print(sale_tax)
print(total_tax)
print(total)
