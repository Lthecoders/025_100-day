import random

print(
    "\033[35m",
    "-------------------> ⚔️  Character Stats Generator ⚔️ <-----------------------",
    "\033[0m")
print("\033[34m",
      "      -----------------------------------------------------------",
      "\033[0m")


def crazzy_dise_2():

  side1 = random.randint(1, 6)
  side2 = random.randint(1, 8)
  return side1 * side2


def crazzy_dise():
  # side = random.randint(1, 50)
  # return side
  name_user = input("\n\nwhat is your Warrior name ? ---> ")
  while not name_user.isalpha():
    print(
        "\nYou can only put character names in alphabets and not in numbers.")
    name_user = input("\nPlease enter your Warrior name again: ")

  show_dise_2 = crazzy_dise_2()
  # print(type(show_dise_2))
  # print(show_dise_2)

  if show_dise_2 < 20:
    print("\033[31m", "\n", name_user, "'s health is:", show_dise_2,
          "hp that is very low. 😕 you must have food\n", "\033[0m")
  elif show_dise_2 >= 20 and show_dise_2 <= 35:
    print("\033[34m", "\n", name_user, "'s health is:", show_dise_2,
          "hp that is medium. 👍 you can have food later on\n", "\033[0m")
  elif show_dise_2 > 35 and show_dise_2 <= 48:
    print("\033[32m", "\n", name_user, "'s health is:", show_dise_2,
          "hp that is high. 😮👍you can have fight All the BEST\n", "\033[0m")
  else:
    print("error😕")


# print(crazzy_dise.__doc__)
show_dise_1 = crazzy_dise()
# print(show_dise_2)

while True:
  decide = input(
      "\n\n\ndo you want to see the helth of another warrior? (yes or no) ---> "
  )
  if decide == "yes":
    crazzy_dise()
  elif decide == "no":
    print("\033[35m", "\n-----------> by my buddy 🥲 <-------------", "\033[0m")
    break
  else:
    print("\033[31m", "\nyou can only enter yes or no (lowercase)", "\033[0m")
    continue
