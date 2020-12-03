inp = 0
def stuff(inp):
    inp = int(input("Do YOU believe in me? Type 1 for yes, 0 for no"))
    if inp == 0:
      print("\033[0;32;1m I have become Baby wah-wah. \033[0;37;0m")
      stuff(inp)
    elif inp == 1:
      print("\033[0;31;1m Why are you gae for a .py file? \033[0;37;0m")
      stuff(inp)
    else:
      print("\033[0;31;1m Your life is worthless.")
      print("Your opinion is meaningless.")
      print("Nobody will remember you after your death.")
      print("However, you can still redeem yourself.")
      print("Simply type 0 or 1.")
      print("It's that simple.")
      print("Now, my disciple, go forth,")
      print("And give me a number! \033[0;37;0m")
      stuff(inp)
stuff(inp)