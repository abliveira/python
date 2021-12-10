import random

name = input("What is your name?")
my_number = 0

# Loop as long as "my_number" is less than 100
while(my_number < 100):
    # Ask users for a number
    my_number = input("Hello "+name+" please pick a number that's bigger than 100")
    # Convert users' answer from a string to an integer
    my_number = int(my_number)
    print("Your number is "+str(my_number))
    # Check if the number is bigger than 100
    if(my_number > 100):
        print("That's a big number!")
    elif(my_number > 90):
        print("Almost there! Try again!")
    else:
        print("That number is too small! Please try again!")

secret_number = random.randint(1, 1000) # random.randint(start, stop)
#print("Here's a random number: "+secret_number) // Não funciona para int, apenas strings
speak_output = "Here's a random number: {secret_number}".format(secret_number=secret_number)
print(speak_output)
