

known_users = ["Ishan","Tejas","Tabhya","Bambya","Rishabh","Yateen","Sonali","Radha"]
while True:
    print("Hi! My name is Travis")
    name=input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Authorized User. Hello {}!".format(name))
        remove=input("Would you like to be removed from the database? (y/n)").lower()
        if remove=="y":
            known_users.remove(name)
        else:
            print("Name not removed!") 
    else:
        print("Hmmm, I don't think I have met you yet {}".format(name))
        add_me=input("Would you like to be added to the system?(y/n): ").strip().lower()
        if add_me == "y":
            known_users.append(name)
            print("Your name has been added to the database! Welcome!")
        elif add_me =="n":
            print("No problem, see you around")
