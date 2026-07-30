#Day 2: 30 Days of python programming

#Exercises: Level 1
firstName = 'This' 
lastName = 'Nanji'
fullName = firstName + ' ' + lastName
country = "States"
city = 'Worth'
age = 28
year = 26
is_married = False
is_true = True
is_light_on = True
music, artist, fan = "J-Pop" , "Ado" , True

#Exercise Level 2
#1.Data Types
print(type(firstName))
print(type(lastName))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(music))
print(type(artist))
print(type(fan))

#2 len()
print(len(firstName))
#3 compare length
print(len(lastName))

#4 num_one, num_two
num_one = 5
num_two = 4
#5 add total
total = num_one + num_two
print(total)
#6 subtract
diff = num_one - num_two
print(diff)
#7 multiply
product = num_two * num_one
print(product)
#8 divide
division = num_one / num_two
print(division)
#9 modulus
remainder = num_two % num_one
print(remainder)
#10 power
exp = num_one ** num_two
print(exp)
#11 floor 
floor_division = num_one // num_two
print(floor_division)


#12 circle
#i
radius = 30
pi = 3.14
area_of_circle = pi * (radius ** 2)
print(area_of_circle)
#ii
circum_of_circle = 2 * pi * radius
print(circum_of_circle)
#iii 
radius = float(input("Enter the radius: "))
area_of_circle = pi * (radius ** 2)
print(area_of_circle)

#13 inputs
fName = input("Give a first name: ")
lName = input("Give a last name: ")
Yourcountry = input("Give your country: ")
yourAge = input("What is your age ? ")
print("First Name: ", fName)
print("Last Name: ", lName)
print("Country : ", Yourcountry)
print("Age : ", yourAge)