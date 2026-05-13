npclist = []
harelist = []
packlist1 = {
  "packnum": "1",
  "territory pos": [0,6],
  "members": []
}

packlist2 = {
  "packnum": "2",
  "territory pos": [6,6],
  "members": []
}

packlist3 = {
  "packnum": "3",
  "territory pos": [0,0],
  "members": []
}
#dispersal reserved pack
packlist4 = {
  "packnum": "4",
  "members": []
}
#player reserved pack
packlist5 = {
  "packnum": "5",
  "members": []
}
import random
#wolf NPC generation
def initialize(number):
    global npclist
    for i in range(number):
        npc = {
            "id": f"npc{i}",
            "hp": 100,
            "age": random.randint(0,8),
            "pack": random.randint(1,4),
            "gender": random.randint(1,2),
            "pos": [0, 0],
            "alive": True
        }
        npclist.append(npc)
#hare
def hareinitialize(number):
    global harelist
    for i in range(number):
        npc_hare = {
            "id": f"harenpc{i}",
            "pos": [0, 0],
            "alive": True
        }
        harelist.append(npc_hare)









#for commands and later automatic use, i dont plan on implementing hare editing bc thats kinda useless
def edit(value, insidevalue, changeto):
    for i in npclist:
      if i["id"] == value:
        i[insidevalue] = changeto
def delete(deleting):
    for i in npclist:
      if i["id"] == deleting:
        npclist.remove(i)
        print(f"Deleted {deleting}")

def packinitialize():
  global packlist1
  global packlist2
  global packlist3
  try:
      for i in npclist:
        if i["pack"] == 1:
            packlist1["members"].append(i["id"]) 
        elif i["pack"] == 2:
          packlist2["members"].append(i["id"])
        elif i["pack"] == 3:
          packlist3["members"].append(i["id"])
        elif i["pack"] == 4:
          packlist4["members"].append(i["id"])
  except UnboundLocalError:
    print("UnboundLocalError - something wasnt global or something")

  print(packlist1)
  print(packlist2)
  print(packlist3)
  print(packlist4)
  
def clear():
  print("Wolves cleared.")
  npclist.clear()
  packlist1["members"].clear()
  packlist2["members"].clear()
  packlist3["members"].clear()
  packlist4["members"].clear()






#text art 6x6 map, territory percentages will be in len() (length of 2 x%--, length of 3 would be xx%-, length 4 xxx% to keep spacing accurate)
def map():
  print(f"===========================================")
  print(f"|------|------|------|------|------|------|")
  print(f"|------|------|------|------|------|------|")
  print(f"|======|======|======|======|======|======|")
  print(f"|------|------|------|------|------|------|")
  print(f"|------|------|------|------|------|------|")
  print(f"|======|======|======|======|======|======|")
  print(f"|------|------|------|------|------|------|")
  print(f"|------|------|------|------|------|------|")
  print(f"|======|======|======|======|======|======|")
  print(f"|------|------|------|------|------|------|")
  print(f"|------|------|------|------|------|------|")
  print(f"|======|======|======|======|======|======|")
  print(f"|------|------|------|------|------|------|")
  print(f"|------|------|------|------|------|------|")
  print(f"|------|------|------|------|------|------|")
  print(f"===========================================")
