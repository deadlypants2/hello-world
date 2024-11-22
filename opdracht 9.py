#het aanmaken van de list
list1=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(list1)

#een kort script voor het verwijderen van een lijst getallen binnen een list
to_remove = [29, 53, 67, 83]
for item in to_remove:
    if item in list1:
        list1.remove(item)
print(list1)

#Hierbij wordt een lijst getallen achter een list bijgeplakt.
to_add = [101, 103, 107, 109, 113, 127]
for item in to_add:
    if item not in list1:
        list1.append(item)
print(list1)

#de lijst van groot naar klein sorteren.
list1.sort(reverse=True)
print(list1)

#het aantal getallen binnen de list
print(len(list1))

#het gemiddelde en totaal van de lijst
print(sum(list1))
avg = sum(list1) / len(list1)
print(avg)