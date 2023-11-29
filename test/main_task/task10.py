# Write a program that calculates the total stock in a company from the array/list below
#  if we know that the stock is the last digit in every array/list.

# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]



prods = [['omo','30kshs','300'], ['milk','50kshs','200'],['bread','45kshs','359'], ['coffee','5kshs','79']]

total_stock =0

for products in prods:
    stock = int(products[-1])   #get the last element of an integer
    total_stock+= stock

print("Total stock:", total_stock)