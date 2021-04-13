# ask age
# under 18 gotta leave
# 18-20 wristband
# 21+ drink, normal entry

age = input("Welcome to the salty spitoon... How old are ya?\n")

if age:
    age = int(age)
    if age >= 21:
        print("Howdy pardner! Come on in and drink!")
    elif age >= 18:
        print("Come on in, but you're wearing a wristband.")
    else:
        print("Go across the street to Weenie Hut Junior's! Get outta here!")
else:
    print("Please enter a proper age, pardner...")
