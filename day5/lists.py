
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

#exercise 6
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
#7
print(it_companies)
#8
print(len(it_companies))
#9
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

#10
it_companies[3] = 'Samsung'
print(it_companies)

#11
it_companies.append("ROGSTRX")
print(it_companies)

#13
it_companies[1] = it_companies[1].upper()
print(it_companies)

#14
new_company = '# '.join(it_companies)
print(new_company)

#15
print(it_companies.index('Oracle'))

#16
it_companies.sort()
print(it_companies)

#17
it_companies.reverse()
print(it_companies)

#18-20
#print("Exercise 18-20")
print(it_companies[3:])
print(it_companies[:5])
no_middle = it_companies[:3] + it_companies[5:]
print(no_middle)

#21-25
del it_companies[0]
print(it_companies)
del it_companies[6]
print(it_companies)
del it_companies[2:4]
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
#print(it_companies)

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()
print(full_stack)
full_stack.insert(5,'Python')
print(full_stack)
full_stack.insert(6,'SQL')
print(full_stack)

#Exercise Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.insert(1, 19)
print(ages)
ages.insert(11, 26)
print(ages)
median = (ages[5]+ages[6]) / 2
print(median)
sum =0
for i in ages:
    sum += i
average = sum / len(ages)
print(average)
age_range = ages[11] - ages[0]
print(age_range)
value1 = abs(19-average)
value2 = abs(26-average)
print(value1 > value2)