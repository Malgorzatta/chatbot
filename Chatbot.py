name=input("Hello, what is your name?")
print("Welcome",name)
x1=(input("May I ask You some questions? Please answer Yes or No"))
if x1=="Yes":
    print("Thanks")
elif x1=="No":
    print("That's so sad. I'm not gonna take your time anymore. It was nice to meet you",name)
    print("Have a nice day, bye!")
    exit()
else:
    print("I'm confused. I'll ask you some questions. But if you want to end this conversation, please type 'quit'.")
x2=(input("What is your country?"))
if x2=="quit":
    exit()
if x2=="Scotland" or x2=="Italy" or x2=="United States":
    print("That's wonderful! Few years back I visited", x2)
    if x2=="United States":
        x3=(input("What state?"))
        if x3=="California" or x3=="Texas" or x3=="New York":
            print("I've been there.",x3,"is great place to live in.")
        elif x3!="California" or x3!="Texas" or x3!="New York":
            print("Didn't get there. I'm dreaming to see",x3, "one day.")
elif x2!="Scotland" or x2!="Italy" or x2!="United States":
    print("Do you like living there? I've never been in",x2)