import peoplelist

list = peoplelist.getuserdata()

print(list)

print(peoplelist.getuserdata())
print(peoplelist.findbyfirstname("Rishikesh"))
print(peoplelist.findbyfirstname(""))
newuser=["Miid","Aychit","une",5020893341]
peoplelist.addnewuser(newuser)

print(peoplelist.masterlist)

user5=["Atharv","Ayachit","Pune",8766516783]
peoplelist.updateuserinfo(user5)
#print(findbyfirstname("Rishikesh"))
#print(findbylastname("Kumashi"))
print("----------------")
print(peoplelist.masterlist)
print("----------------")

print(peoplelist.findallbylastname("Ayachit"))


print(peoplelist.findallbycity("une"))