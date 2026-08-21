#Exercise 1
emptytpl = tuple()
brothers = ('Yuru','Dera')
print(brothers)
sisters = ('Asa','Gabby')
print(sisters)
siblings = brothers + sisters
print(siblings)
print(len(siblings))
#change tuple to list and modify
family_members = list(siblings)
family_members.append('Jin')
family_members.append('Hana')
#change list back to tuple
family_members = tuple(family_members)
print(family_members)


#Exercise 2
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('Wool','Milk','Egg','Feather')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
#print(len(food_stuff_tp))
print(food_stuff_tp)
middle = food_stuff_tp[6:7]
print(middle)
first3_and_last3 = food_stuff_lt[3:10]
print(first3_and_last3)
del food_stuff_tp

#checking if items exist
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)