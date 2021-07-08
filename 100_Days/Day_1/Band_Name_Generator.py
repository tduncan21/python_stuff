#1. Create a greeting for your program.
def greeting():
    greeting = """Hello! Welcome to the Band Name Generator!
    Follow the prompts and you will get a cool band name!"""
    print(greeting)
    get_user_input()
    return

def get_user_input():
    #2. Ask the user for the city that they grew up in.
    user_city = input("Please enter the city you grew up in:\n")

    #3. Ask the user for the name of a pet.
    user_pet_name = input("Please enter the name of a pet:\n")

    generate_band_name(user_city, user_pet_name)
    return

#4. Combine the name of their city and pet and show them their band name.
def generate_band_name(user_city, user_pet_name):
    #5. Make sure the input cursor shows on a new line, see the example at:
    gen_band_name = user_city + " " + user_pet_name
    print("Your new band name is called {}!".format(gen_band_name))
    pass

greeting()


#   https://band-name-generator-end.appbrewery.repl.run/