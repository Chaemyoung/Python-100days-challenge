# Simple Function
def greet():
    print("Hellow people")
    print("How do you do Jack Bauer?")
    print("Isn't the weather nice today?")

greet()

# Function that allows for input

def greet_with_name(name):
    print(f"Hellow{name}")
    print(f"How do you do {name}")

greet_with_name("idk")

def hellowpeople(greet):
    print("How are u doing?")

hellowpeople()

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hellow {name}")
    print(f"What is it like in {location}?")

greet_with(location = "london",  name = "Tad")
