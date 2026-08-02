#1 concatenate
string_one,string_two,string_three,string_four = 'Thirty','Days','Of','Python'
space = ' '
concat_string_one = string_one +space + string_two +space +string_three +space + string_four
print(concat_string_one)

#2 concatenate
string_five, string_six, string_seven = 'Coding', 'For', 'All'
concat_string_two = string_five + space + string_six + space + string_seven
print(concat_string_two)

#string methods 1
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


#exercise 18-22
pfe = 'Python For Everyone'
cfa = 'Coding For All'
print(company.find('C'))
print(company.find('F'))
print(company.rfind('I'))

#exercise 19-
sentence_one = 'You cannot end a sentence with because because because is a conjunction'
print(sentence_one.find('because'))
print(sentence_one.rfind('because'))
first_slice = sentence_one[0:31]
second_slice = sentence_one[53:]
new_sentece = first_slice + second_slice
print(new_sentece)
