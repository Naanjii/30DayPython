#1 concatenate
string_one,string_two,string_three,string_four = 'Thirty','Days','Of','Python'
space = ' '
concat_string_one = string_one +space + string_two +space +string_three +space + string_four
print(concat_string_one)

#2 concatenate
string_five, string_six, string_seven = 'Coding', 'For', 'All'
concat_string_two = string_five + space + string_six + space + string_seven
print(concat_string_two)

#string methods exer 4-13, 15-17
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:])
print(company.find('Coding'))
print(company[10])

print(company.replace('Coding For All',"Python"))
print(company.split(' '))

#exer 14
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(', '))


#exercise 18-22
pfe = 'Python For Everyone'
cfa = 'Coding For All'
print(company.find('C'))
print(company.find('F'))
print(company.rfind('I'))

#exercise 23-27
sentence_one = 'You cannot end a sentence with because because because is a conjunction'
print(sentence_one.find('because'))
print(sentence_one.rfind('because'))
first_slice = sentence_one[0:31]
second_slice = sentence_one[55:]
new_sentece = first_slice + second_slice
print(new_sentece)


#exercise 28-31
print(cfa.startswith("Coding"))
print(cfa.startswith("coding"))

new_coding = '   Coding For All      '
print(new_coding.strip("   "))
#31
'''
    Which one of the following variables return True when we use the method isidentifier():
        30DaysOfPython
        thirty_days_of_python
    thirty_days_of_python, cannot start with a number.
'''
#32
this_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
next_list = '# '.join(this_list)
print(next_list)

#33
this_sentence = "I am enjoying this challenge.\nI just wonder what is next."
print(this_sentence)

#34
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

#35
radius = 10
area = 3.14 *radius ** 2
print('The area of a cirlce with radius {} is {} meters square'.format(str(radius), str(area)))

#36
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))