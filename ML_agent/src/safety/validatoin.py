# safety/validation.py

def validate_input(user_input):
    return len(user_input.strip()) > 3 and all(x.isprintable() for x in user_input)
