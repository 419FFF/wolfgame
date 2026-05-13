print("Please enlarge the console, as this is meant to be used in full screen! (also i dont want to have to figure out how to abide by resolution)")
import math
import initalize
initalize.map()
console = ""
wolvestoinitalize = 30 # max 30 or computer explodes
try: 
  initalize.initialize(wolvestoinitalize)
  initalize.hareinitialize(10)
  initalize.packinitialize()
except MemoryError:
  print("Out Of Memory. Lower the amount of NPCs!")
while True:
  if (len(initalize.packlist1["members"]) > round(wolvestoinitalize / 2.25) or len(initalize.packlist2["members"]) > round(wolvestoinitalize / 2.25) or len(initalize.packlist3["members"]) > round(wolvestoinitalize / 2.25) or len(initalize.packlist1["members"]) < 2 or len(initalize.packlist2["members"]) < 2 or len(initalize.packlist3["members"]) < 2 or len(initalize.packlist3["members"]) == 0 or len(initalize.packlist2["members"]) == 0 or len(initalize.packlist1["members"]) == 0):
    initalize.clear()
    initalize.initialize(wolvestoinitalize)
    initalize.packinitialize()
    continue
  else:
    break

debug_state = False
import console
