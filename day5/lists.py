
#exercise1-4
nolist = []
items = ['controller','console','charger','disc','monitor']
print(items)
print(len(items))
first_item = items[0]
print(first_item)
middle_item = items[2]
print(middle_item)
last_item = items[4]
print(last_item)

#exercise 5
mixed_data = ['Nanji', 28, 68, 'Dating', 'Apartment']

#exercise 6-11
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])
it_companies[3] = 'Samsung'
print(it_companies)
it_companies.append("ROGSTRX")
print(it_companies)
it_companies[1] = it_companies[1].upper()
print(it_companies)
new_company = '# '.join(it_companies)
print(new_company)
print(it_companies.index('Oracle'))
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[3:])
print(it_companies[:-3])
