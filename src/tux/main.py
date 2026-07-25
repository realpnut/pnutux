import json
import os
import time
import random
from datetime import date, datetime

HOME = os.path.expanduser("~")
SAVE_FILE = os.path.join(HOME, ".tux_pet_save.json")

default_data = {
    "coins": 0,
    "level": 1,
    "name": "",
    "happiness": 50,
    "uses": 0,
    "last_daily": "",
    "last_seen": ""
}

def load():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return default_data.copy()
    return default_data.copy()

def save(data):
    data["last_seen"] = datetime.now().isoformat()
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def apply_time_decay(data):
    if not data.get("last_seen"):
        return
    try:
        last_seen = datetime.fromisoformat(data["last_seen"])
        hours_passed = int((datetime.now() - last_seen).total_seconds() / 3600)
        if hours_passed > 0:
            decay = hours_passed * 2
            data["happiness"] = max(0, data["happiness"] - decay)
            print(f"\nyou were away for {hours_passed} hours. {data['name']} missed you! (-{decay} happiness)")
            time.sleep(3)
    except ValueError:
        pass



def play_fishing_game(data):
    os.system("cls" if os.name == "nt" else "clear")
    print("=== FISHING HOLE ===")
    print("wait for the fish...")
    time.sleep(random.uniform(1.5, 4.0))
    
    print("\n!!! PULL NOW !!! (press Enter instantly)")
    start_time = time.time()
    input()
    reaction_time = time.time() - start_time
    
    if reaction_time < 0.1:
        print("Too fast! You scared the fish away.")
    elif reaction_time < 0.45:
        reward = random.randint(15, 30)
        data["coins"] += reward
        print(f"Perfect catch! Reaction time: {reaction_time:.2f}s. You got a big fish and sold it for {reward} coins!")
    elif reaction_time < 0.8:
        reward = random.randint(5, 12)
        data["coins"] += reward
        print(f"Caught it! Reaction time: {reaction_time:.2f}s. Small fish sold for {reward} coins.")
    else:
        print(f"Too slow! ({reaction_time:.2f}s) The fish ate the bait and swam away.")
    time.sleep(3)

def run_game():
    data = load()
    apply_time_decay(data)

    event = random.randint(1,1000)
    if event == 420:
        print("A mysterious penguin gave you 200 coins!")
        data["coins"] += 200

    if data["uses"] == 0:
        print("yo this is ur first time opening the game")
        name = input("what do u wanna name ur penguin? ")
        if name.strip() == "":
            name = "penguin"
        data["name"] = name
    data["uses"] += 1
    os.system("cls" if os.name == "nt" else "clear")

    today = str(date.today())
    if data["last_daily"] != today:
        data["coins"] += 10
        data["last_daily"] = today
        print("daily reward claimed! (+10 coins)")

    print(f"welcome back, mr {data['name']}")
    while True:
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        if data["happiness"] <= 20:
            print("   _   ")
            print(" (╥_╥) ")
            print("//-=-\\\\")
            print("(\\_=_/)")
            print(" ^^ ^^ ")
        elif 21 <= data["happiness"] <= 79:
            print("   _   ")
            print(" (´-´) ")
            print("//-=-\\\\")
            print("(\\_=_/)")
            print(" ^^ ^^ ")
        else:
            print("   _   ")
            print(" (^v^) ")
            print("//-=-\\\\")
            print("(\\_=_/)")
            print(" ^^ ^^ ")

        print("\n=== TUX PET ===")
        print("your pet:", data["name"])
        print("coins:", data["coins"])
        print("happiness:", data["happiness"])
        print("times opened:", data["uses"])
        print("level:", data["level"])

        print("\nwhat do u wanna do?")
        print("1. show status")
        print("2. change name (cost 50 coins)")
        print("3. add happiness (cost 10 coins)")
        print("4. open a case (cost 25 coins)")
        print("5. go fishing (earn coins)")
        print("6. talk to the penguin")
        print("7. shop")
        print("8. exit")

        choice = input("> ")

        if choice == "1":
            print("\n=== STATUS ===")
            print(data)
            time.sleep(2)
        elif choice == "2":
            if data["coins"] >= 50:
                name = input("new name: ")
                if name.strip() != "":
                    data["name"] = name
                    data["coins"] -= 50
                    print("name changed!")
            else:
                print("not enough coins :(")
                time.sleep(1)
        elif choice == "3":
            if data["coins"] >= 10:
                data["happiness"] = min(100, data["happiness"] + 10)
                data["coins"] -= 10
                print("your penguin is happier!")
            else:
                print("not enough coins")
                time.sleep(1)
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
                time.sleep(2)
            else:
                print("not enough coins")
                time.sleep(1)
        elif choice == "5":
            play_fishing_game(data)
        elif choice == "6":
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
                print("   _   ")
                print(" (·u·) ")
                print("//-=-\\\\")
                print("(\\_=_/)")
                print(" ^^ ^^ ")
                data["happiness"] = min(100, data["happiness"] + 5)
            elif choi == "2":
                print("You tell penguin he is too heavy to fly...\n")
                time.sleep(2)
                print("Why are you so mean to him?")
                print("   _   ")
                print(" (╥_╥) ")
                print("//-=-\\\\")
                print("(\\_=_/)")
                print(" ^^ ^^ ")
                data["happiness"] = max(0, data["happiness"] - 15)
            elif choi == "3":
                print("You flirt with penguin...\n")
                time.sleep(1)
                print("You dont know the result...")
                print("   _   ")
                print(" (~v~) ")
                print("//-=-\\\\")
                print("(\\_=_/)")
                print(" ^^ ^^ ")
                flr = random.randint(0, 1)
                if flr == 0:
                    print("Penguin liked it!")
                    data["happiness"] = min(100, data["happiness"] + 20)
                else:
                    print("Penguin got uncomfortable...")
                    data["happiness"] = max(0, data["happiness"] - 10)
            elif choi == "4":
                print("You tell penguin a joke...\n")
                time.sleep(2)
                joke = random.randint(0, 10)
                if joke <= 9:
                    print("The joke was good and penguin laughed!")
                    print("   _   ")
                    print(".·°՞(˃ᗜ˂)՞°·.")
                    print("//-=-\\\\")
                    print("(\\_=_/)")
                    print(" ^^ ^^ ")
                    data["happiness"] = min(100, data["happiness"] + 10)
                    time.sleep(0.2)
                else:
                    print("Couldn't you think of a better joke..?")
                    print("   _   ")
                    print(" (´-´) ")
                    print("//-=-\\\\")
                    print("(\\_=_/)")
                    print(" ^^ ^^ ")
                    data["happiness"] = max(0, data["happiness"] - 5)
                    time.sleep(0.4)
            elif choi == "5":
                print("You stared at penguin...\n")
                time.sleep(3)
                print("The penguin stared back!")
                print("   _   ")
                print(" (⏺_⏺) ")
                print("//-=-\\\\")
                print("(\\_=_/)")
                print(" ^^ ^^ ")
            else:
                print("Wrong answer!")
            time.sleep(2)
        elif choice == "7":
            print("You enter the shop...")
            time.sleep(1)
            print("What would you like to buy?")
            print("1. Fish (10 coins)")
            print("2. Ice Cream (5 coins)")
            print("3. Toy (15 coins)")
            print("4. Level Up (100 coins)")
            print("5. Exit Shop")
            shop = input("Enter your choice: ")
            if shop == "1":
                if data["coins"] >= 10:
                    print("You bought some fish!")
                    data["coins"] -= 10
                    data["happiness"] = min(100, data["happiness"] + 5)
                else:
                    print("Not enough coins!")
            elif shop == "2":
                if data["coins"] >= 5:
                    print("You bought some ice cream!")
                    data["coins"] -= 5
                    data["happiness"] = min(100, data["happiness"] + 2)
                else:
                    print("Not enough coins!")
            elif shop == "3":
                if data["coins"] >= 15:
                    print("You bought a toy!")
                    data["coins"] -= 15
                    data["happiness"] = min(100, data["happiness"] + 10)
                else:
                    print("Not enough coins!")
            elif shop == "4":
                if data["coins"] >= 100:
                    print("You leveled up!")
                    data["coins"] -= 100
                    data["level"] += 1
                else:
                    print("Not enough coins to level up!")
            elif shop == "5":
                print("Exiting shop...")
            else:
                print("Invalid option!")
            time.sleep(2)
        elif choice == "8" or choice.lower() == "exit" or choice == "0":
            save(data)
            print("bye")
            break
        else:
            print("invalid option")
            time.sleep(1)

        data["happiness"] = max(0, min(100, data["happiness"]))
        save(data)

if __name__ == "__main__":
    run_game()
