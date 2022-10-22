masterlist=[]


def getuserdata():

    user1=["Atharv","Ayachit","Pune",8766517383]
    masterlist.append(user1)
    user2=["Ishaan","Kumashi","mumbai",9960863165]
    masterlist.append(user2)
    user3=["Rishikesh","Kumashi","pune",9834216936]
    masterlist.append(user3)
    user4=["Milind","Ayachit","solapur",7020893341]
    masterlist.append(user4)

    return masterlist

def findbyfirstname(firstname):
    for x in masterlist:
        if x[0] == firstname:
            return x

    return None


def addnewuser(userinfo):
    masterlist.append(userinfo)
    print("user info added, - ", userinfo)

    return



def findbylastname(lastname):
    for y in masterlist:
        if y[1] == lastname:
            return y

    return None


def updateuserinfo(userinfo):
    for x in range (len(masterlist)):
        currentuserinfo=masterlist[x]
        if currentuserinfo[0]==userinfo[0] and currentuserinfo[1]==userinfo[1]:
            masterlist[x]=userinfo
            return
    return





def findallbylastname(lastname):
    searchlist=[]
    for y in masterlist:
        if y[1] == lastname:
            searchlist.append(y)
            #print(y)
    return searchlist



def findallbycity(city):
    citylist=[]
    for y in masterlist:
        if y[-2].lower() == city.lower():
            citylist.append(y)
    return citylist







