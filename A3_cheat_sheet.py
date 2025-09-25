# print("Welcome to the temp app!")

# Temp = int(input("What is the temperature of CPU? "))

# if(Temp > 80):
#     print("Warning, temperature too high!")
# else:
#     print("All cool, keep on going!")


# num = int(input("Insert number: "))
# Answer = num % 2
# if Answer == 0:
#     print(f"Parillinen: {Answer}")
# else:
#     print(f"Pariton: {Answer}")



# if(Temp > 80):
#     if(Temp > 90):
#         print("You are toast")
#     else:
#         print("Warning")
# else:
#     print("You are ok")

# PAREMPI TAPA

# if(Temp > 90):
#     print("You are toast")
# elif(Temp > 80):
#     print("Warning")
# else:
#     print("You are ok")



# name1=input("Anna nimi 1: ")
# name2=input("Anna nimi 2: ")
# if(len(name1)>len(name2)):
#     print("nimi1 on pidempi kuin nimi2")
# elif(len(name1)<len(name2)):
#     print("nimi2 on pidempi kuin nimi1")
# else:
#     print("nimet ovat yhtä pitkät")



# print("Hello, tell me the address you are now ")

# Street = input("Street: ")
# Building = int(input("Building number: "))
# Town = input("Town: ")

# if((Town == "Lahti" or "Lahtis") and Street == "Mukkulankatu" and Building == 19):
#     print("Congratulations, you are at LAB!")

# #1 ehto: True, ja 2. ehto False (jompi kumpi näistä tai molemmat?)
# elif(Town == "Lahti" or "Lahtis" and (Street != "Mukkulankatu" or Building != 19)):
#     print("You are in the correct town, but check the street address again")
# elif not(Town == "Lahti" or "Lahtis" and Street == "Mukkulankatu" and Building == 19):
#     print("You are lost...")



import random

# print (random.random())
#print (random.randint(1, 3))



pelaaja=int(input("Pelataan Kivi-Sakset-Paperi -peliä\nAnna valintasi:\n1 - Kivi\n2 - Sakset\n3 - Paperi\n"))
vastustaja=random.randint(1,3)
print(f"Pelasit {pelaaja}, tietokone pelasi {vastustaja}")
if pelaaja == vastustaja:
    print("Tasapeli!")
elif (pelaaja==1 and vastustaja==2) or (pelaaja==2 and vastustaja==3) or (pelaaja==3 and vastustaja==3):
    print("Sinä voitit!")
else:
    print("Tietokone voitti")