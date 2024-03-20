def love_calculator():
    print("Welcome to the Love Calculator!")
    print("This program will calculate your compatibility based on age.")
    print("Please enter your ages to begin.")

    age1 = int(input("Enter the age of the first person: "))
    age2 = int(input("Enter the age of the second person: "))

    total_age = age1 + age2

    if total_age <= 100:
        compatibility = total_age * 2
    else:
        compatibility = 100

    print("\nCompatibility Score: {}%".format(compatibility))

    if compatibility >= 80:
        print("Wow! You are a perfect match!")
    elif compatibility >= 60:
        print("You two have a good chance!")
    elif compatibility >= 40:
        print("There's potential, but it might take some work.")
    else:
        print("Hmm... It might be better to just be friends.")

love_calculator()
