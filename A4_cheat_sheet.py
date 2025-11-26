# Dogs = 4
# Hometown = "Ylöjärvi"

# # Lista
# TownsInFinland = ["Lahti", "Helsinki", "Lappeenranta", "Tampere", "Oulu"]

# RandomInformation = ["Elisa", 32, False, Dogs, Hometown]

# print(TownsInFinland[0])
# TownsInFinland.append("Rovaniemi")

# NumOfTowns = len(TownsInFinland) #vast: 6
# print(TownsInFinland[NumOfTowns-1])

# Municipality = ["Heinola", "Asikkala", "Hollola", "Karvia", "Kempele"]
# Towns = ["Lahti", "Helsinki", "Lappeenranta", "Tampere", "Oulu"]
# Places = [Municipality, Towns]

# print(Places[1][-2]) #otetaan listoista 0 tai 1, eli nyt 1, ja siitä -2 eli toisiksi viimeinen

# Towns.sort() #aakkosjärjestys
# print(Towns)


# #Dictionarys

# Teacher = {
#     'name': 'Juha',
#     'age': 45,
#     'city': 'Lahti'
# }

# print(Teacher["name"])

# Teacher['email'] = 'juha.hyytainen@lab.fi'

# print(Teacher)

# for key in Teacher:
#     print(key, end=' ')
#     print(Teacher[key])

# Student = [
#     {'name': 'Mikko', 'age': 30, 'city': 'Tampere'},
#     {'name': 'Elisa', 'age': 32, 'city': 'Sastamala'},
#     {'name': 'Ville', 'age': 27, 'city': 'Helsinki'}
# ]

# print(Student[0])

# Cities = {
#     'Finland' :['Tampere', 'Espoo', 'Helsinki'],
#     'Sweden' :['Stockholm', 'Malmö']
# }

# print(Cities['Finland'][0]) #suomen listasta ensimmäinen eli nro 0



# for town in Towns:
#     print(f"The town of {town}")
# print(f"All of the towns: {Towns}")



# #mitähäntässävälissäoli????

# print("")
# Total = 0
# for i in range(1,101):
#     Total +=i
#     print(Total)

# print(Total)

# for i in range(9):
#     if (i == 3):
#         continue
#     print(i)


#opiskele loopit for ja while, sekä niihin liittyvät komennot continue ja break!
#for oli just se mikä meni vähän ohi....


# while 1 < 10:
#     print("Do not try me at home xD")

i = 0
while i < 10:
    print(f"Iteration number: {i}")
    i += 1 #i = i + 1

#loop

continueLoop = True
while continueLoop == True:
    if input("Do you want to continue? ") != "yes":
        continueLoop = False
#break

while True:
    if input("Do you want to continue? ") != "yes":
        break
    else:
        continue


