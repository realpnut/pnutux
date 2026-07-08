import json
import os
import time
import random
from datetime import date

SAVE_FILE = "save.json"

default_data = {
    "coins": 0,
    "level": 1,
    "name": "",
    "happiness": 50,
    "uses": 0,
    "last_daily": ""
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

today = str(date.today())

if data["last_daily"] != today:
    data["coins"] += 10
    data["last_daily"] = today
    print("daily reward claimed! (+10 coins)")

while True:
    if data["happiness"] <= 20:
        print("       _")
        print("     (╥_╥)")
        print("    //-=-\\\\")
        print("    (\\_=_/)")
        print("     ^^ ^^")
    elif 21 <= data["happiness"] <= 79:
        print("       _")
        print("     (`-`)")
        print("    //-=-\\\\")
        print("    (\\_=_/)")
        print("     ^^ ^^")
    else:
        print("       _")
        print("     (`v`)")
        print("    //-=-\\\\")
        print("    (\\_=_/)")
        print("     ^^ ^^")

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
    print("5. talk to the penguin")
    print("6. exit")

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
            time.sleep(1)

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
        print("1. Compliment the penguin")
        print("2. Be mean")
        print("3. Flirt")
        print("4. Tell a joke")
        print("5. Stare at penguin")

        choi = input("Choose: ")

        if choi == "1":
            print("You tell penguin he is the best bird...\n")
            time.sleep(2)
            print("Penguin is happier now!")
            print("       _")
            print("     (·u·)")
            print("    //-=-\\\\")
            print("    (\\_=_/)")
            print("     ^^ ^^")
            data["happiness"] += 5

        elif choi == "2":
            print("You tell penguin he is too heavy to fly...\n")
            time.sleep(2)
            print("Why are you so mean to him?")
            print("       _")
            print("     (╥_╥)")
            print("    //-=-\\\\")
            print("    (\\_=_/)")
            print("     ^^ ^^")
            data["happiness"] -= 15

        elif choi == "3":
            print("You flirt with penguin...\n")
            time.sleep(1)
            print("You dont know the result...")
            print("       _")
            print("     (~v~)")
            print("    //-=-\\\\")
            print("    (\\_=_/)")
            print("     ^^ ^^")

            flr = random.randint(0, 1)

            if flr == 0:
                print("Penguin liked it!")
                data["happiness"] += 20
            else:
                print("Penguin got uncomfortable...")
                data["happiness"] -= 10

        elif choi == "4":
            print("You tell penguin a joke...\n")
            time.sleep(2)

            joke = random.randint(0, 10)

            if joke <= 9:
                print("The joke was good and penguin laughed!")
                print("       _")
                print(" .·°՞(˃ᗜ˂)՞°·.")
                print("    //-=-\\\\")
                print("    (\\_=_/)")
                print("     ^^ ^^")
                data["happiness"] += 10
                time.sleep(0.2)
            else:
                print("Couldn't you think of a better joke..?")
                print("       _")
                print("     (`-`)")
                print("    //-=-\\\\")
                print("    (\\_=_/)")
                print("     ^^ ^^")
                data["happiness"] -= 5
                time.sleep(0.4)

        elif choi == "5":
            print("You stared at penguin...\n")
            time.sleep(3)
            print("The penguin stared back!")
            print("       _")
            print("     (⏺_⏺)")
            print("    //-=-\\\\")
            print("    (\\_=_/)")
            print("     ^^ ^^")

        else:
            print("Wrong answer!")
            time.sleep(1)

    elif choice == "6":
        save(data)
        print("bye")
        break

    else:
        print("invalid option")

    data["happiness"] = max(0, min(100, data["happiness"]))

    save(data)
