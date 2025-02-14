#De dictionary wordt aangemaakt.
fruit_dictionary = {
    "appel" : "apple",
    "peer" : "pear",
    "mandarijn" : "mandarin",
    "sinaasappel" : "orange",
    "druif" : "grape",
    "banaan" : "banana",
}

#De dictionary wordt eenmalig uitgeprint
print(fruit_dictionary)

#Twee specifieke items worden vanuit de dictionary geprint
print(
    fruit_dictionary["peer"],
    fruit_dictionary["sinaasappel"],
)

#Hierbij worden de keys, values en items apart van elkaar uitgeprint.
print(fruit_dictionary.keys())

print(fruit_dictionary.values())

print(fruit_dictionary.items())

#Door middel van een loop wordt de dictionary op een nette manier uitgeprint
for k,v in fruit_dictionary.items():
    print(k, "=", v)

#De value van watermeloen wordt toegevoegd en druif wordt verwijderd.
fruit_dictionary["watermeloen"] = "watermelon"

fruit_dictionary.pop("druif")

#hierbij word nogmaals de dictionary op een nette manier uitgeprint om de veranderingen van hiervoor te weergeven.
for k,v in fruit_dictionary.items():
    print(k, "=", v)
