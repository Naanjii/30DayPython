import math

#1 declare age and height
age = 29
height = 5.10
complex_num = 5-5j

#2 script trianlge
base = float(input("Enter base: " ))
height = float(input("Enter height: " ))
area = 0.5 * base * height
print(f'The area of th triangle is {area}')

#3 script perimeter
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
print(f"The perimeter of the triangle is {side_a + side_b + side_c}")

#4 rectangle area
length = int(input("Enter length: "))
width = int(input("Enter width: "))
rect_area = length * width
rect_perimeter = 2 * (length +width)
print(f"The area is {rect_area} and the perimeter is {rect_perimeter}")

#5 circle
circ_radius = float(input("Enter a radius: "))
circ_area = 3.14 * (circ_radius **2)
circ_circum = 2 * 3.14 * circ_radius

#6 slopes
slope_1 = 2
slope_2 = math.sqrt(((2-6)**2) + ((2-10)**2))
print(slope_1 <= slope_2)

#7 length
drag_leng = len("dragon")
python_leng = len("python")
#falsy compare
print(python_leng != drag_leng)
#if on
print("on" in "dragon" and "on" in "python")

#jargon
print("jargon" in  "I hope this course is not full of jargon")

#not
print(not "on" in "dragon" and "python")

python_float = float(python_leng)
python_string = str(python_leng)

#floor and int
print(7//3 == int(2.7))

#check types
print (type('10') == type(10))

#check if equal
print(int(9.8) == -10)

#script hourly
hrs = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
print(f'Your weekly earning is {hrs * rate}')

#sec to live
years_lived = int(input('Enter the number of years you have lived: '))
years_to_sec = years_lived * 31536000
print(f'You have lived for {years_to_sec} seconds.')