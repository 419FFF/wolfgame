import initalize
debug_state = False
while True:
    console = input("> ")
    if console == "quit":
        print("Exiting...")
        break
    
  
    if console == "dm" and debug_state == False:
        console = ""  
        debug_state = True
        print("debug mode on")
    if console == "dm" and debug_state:
        console == ""  
        debug_state = False
        print("debug mode off")
    if console == "pack list full" and debug_state:
        print("Wolf NPCs:")
        print(initalize.packlist1)
        print(initalize.packlist2)
        print(initalize.packlist3)
        print(initalize.packlist4)
    if console == "pack list" and debug_state:
        print("Wolf Packs:")
        print("Pack 1:")
        print(initalize.packlist1["members"])
        print("Pack 2:")
        print(initalize.packlist2["members"])
        print("Pack 3:")
        print(initalize.packlist3["members"])
        print("Dispersals:")
        print(initalize.packlist4["members"])
  
    if console == "npc list full" and debug_state:
        print("Wolf NPCs:")
        print(initalize.npclist)
        print("Hare NPCs:")
        print(initalize.harelist)
    if console == "npc list" and debug_state:
        print("Wolf NPCs:")
        for i in initalize.npclist:
          print(i["id"])
        print("Hare NPCs:")
        for i in initalize.harelist:
          print(i["id"])
    if console == "npc" and debug_state:
      print("Expected argument(s). Use the \"help npc\" command to display a list of arguments.")
    if console == "help" and debug_state == False:
        console == ""
        print("Debug Mode is not enabled.")
    if console == "help" and debug_state:
        console == ""
        print("Commands:")
        print("help - Displays this list of commands, use \"help command\" or \"help command argument\" to get help with a specific command if more information is available.")
        print("npc - Controls and visualizes NPCs.")
    if console == "help npc" and debug_state:
      print("List of \"npc\" arguments:")
      print("npc delete - Deletes an NPC.")
      print("npc edit - Edits an NPC.")
    if console == "help npc edit" and debug_state:
      print("List of keys:")  
      print(initalize.npclist[0].keys())
      print("Editing ID and Position is not supported.")
    if console == "help npc list" and debug_state:
        print("npclist full - Displays all NPCs along with all attributes.")
    
    if console == "npc edit" and debug_state:
        try:
          changenpc = str("npc" + input("Which ID to change? > "))
        except ValueError:
          print("Was expecting an integer, got another type instead.")
          continue
        while True:
            changeat = input('What Attribute to change? > ')
            if changeat not in initalize.npclist[0].keys():
              print("Invalid Attribute")
              continue
            elif changeat == "id":
              print("Changing NPC ID is not supported.")
              continue
            elif changeat == "pos":
              print("Changing NPC Position is not supported.")
              continue
            else:
              break  
        while True:
          if changeat == "hp" or changeat == "age" or changeat == "pack" or changeat == "gender":
            try:
              changevalue = int(input("What value to set? > "))
              if changeat == "hp" and changevalue > 100:
                changevalue == 100
              if changeat == "hp" and changevalue < 0:
                changevalue == 0
              if changeat == "age" and changevalue < 0:
                age == 0
              if changeat == "pack" and changevalue <= 0 or changeat == "pack" and changevalue > 3:
                print("invalid pack, must be integer from 1-3")
                continue
              if changeat == "gender" and changevalue < 1 or changeat == "gender" and changevalue > 2:
                print("easier to implement with 2 values, must be integer from 1-2")
                continue
              else:
                break
            except ValueError:
              print("Was expecting an integer, got another type instead.")
              continue
          if changeat == "alive": 
              changevalue = input("What value to set? > ")
              if changevalue == "True" or changevalue == "true":
                changevalue = True
                break
              elif changevalue == "False" or changevalue == "false":
                changevalue = False
                break
              else:
                print("Was expecting a boolean, got another type instead.")
                continue

        try:
          print(f"{changenpc}, {changeat}, {changevalue}")
          initalize.edit(changenpc, changeat, changevalue)
        except IndexError:
          print("NPC ID out of range.")
          continue
    if console == "npc delete" and debug_state:
      try:
          delnpc = str("npc" + input("Which ID to change? > "))
          initalize.delete(delnpc)
      except IndexError:
        print("NPC ID out of range.")





  
