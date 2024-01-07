films = {
"Finding Dory": [3,5],
"Andhadhund": [18,10],
"Tarzan": [16,20],
"Ghostbusters": [16,15]
}
while True:
    choice = input("What film do you want to watch?: ").strip().title()
    if choice in films:
        age=int(input("How old are you?: ").strip())
        if age>=films[choice][0]:
            if films[choice][1]>0:
                print("Enjoy the film!")
                films[choice][1]=films[choice][1]-1
            else:
                print("Sorry! No more seats left!")

        else:
            print("You are too young to see the film.")   
    else:
        print("We don't have that film...")


