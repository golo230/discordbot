import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello world!'
    
    if p_message == 'ping':
        return 'pong!'
    
    if p_message == 'd4':
        return random.randint(1, 4)
    
    if p_message == 'd6':
        return random.randint(1, 6)
    
    if p_message == 'd8':
        return random.randint(1, 8)
    
    if p_message == 'd10':
        return random.randint(1, 10)
    
    if p_message == 'd12':
        return random.randint(1, 12)
    
    if p_message == 'd20':
        return random.randint(1, 20)
    
    if p_message == 'd100':
        return random.randint(1, 100)
    
    if p_message == 'rps':
        return random.randint(0, 2)
    
    if p_message == 'coin':
        x = random.randint(1, 2)
        if x == 1:
            return 'heads'
        else:
            return 'tails'