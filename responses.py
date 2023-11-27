import random
import discord


def bot_response(message):
    p_message = message.lower()

    if p_message == "hello":
        return 'Hey There'
    
    if p_message == "roll":
        return str(random.randInt(1,6))
    
    if p_message == "help":
        return "`this is a help message that you can modify.`"
    
    if p_message == "createhero":
        return """Please select a class"""