import json
import os
import random

SAVE_FILE = "save.json"

default_data = {
    "coins": 0,
    "level": 1,
    "name": "",
    "happiness": 50,
    "uses": 0
}


def load():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return default_data.copy()


def save(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)


data = load()

if data["uses"] == 0:
    print("yo this is ur first time opening the game")
    name = input("what do u wanna name ur penguin? ")

    if name.strip() == "":
        name = "penguin"

    data["name"] = name

data["uses"] += 1
data["coins"] += 10

print("\n=== TUX PET ===")
print("your pet:", data["name"])
print("coins:", data["coins"])
print("happiness:", data["happiness"])
print("times opened:", data["uses"])

print("\nwhat do u wanna do?")
print("1. show status")
print("2. change name (cost 50 coins)")
print("3. add happiness (cost 10 coins)")
print("4. open a case (cost 25 coins)")
print("5. exit")

choice = input("> ")

if choice == "1":
    print("\n=== STATUS ===")
    print(data)

elif choice == "2":
    if data["coins"] >= 50:
        name = input("new name: ")

        if name.strip() != "":
            data["name"] = name

        data["coins"] -= 50
        print("name changed!")
    else:
        print("not enough coins :(")

elif choice == "3":
    if data["coins"] >= 10:
        data["happiness"] += 10
        data["coins"] -= 10
        print("your penguin is happier!")
    else:
        print("not enough coins")

elif choice == "4":
    if data["coins"] >= 25:
        data["coins"] -= 25

        print("opening a case...")
        cas = random.randint(1, 100)

        if cas == 100:
            print("JACKPOT! You won 100 coins!")
            data["coins"] += 100

        elif cas >= 80:
            print("You won 50 coins!")
            data["coins"] += 50

        elif cas >= 30:
            print("You won 10 coins!")
            data["coins"] += 10

        else:
            print("You didnt win anything!")

    else:
        print("not enough coins")

elif choice == "5":
    print("bye")

else:
    print("invalid option")

save(data)
