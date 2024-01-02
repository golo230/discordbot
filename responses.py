import random

answer_dict={1:"It is certain.",
            2:"It is decidedly so.",
            3: "Without a doubt.",
            4:"Yes definitely.",
            5:"You may rely on it.",
            6:"As I see it, yes.",
            7:"Most likely.",
            8:"Outlook good.",
            9:"Yes.",
            10:"Signs point to yes.",
            11:"Reply hazy, try again.",
            12:"Ask again later.",
            13:"Better not tell you now.",
            14:"Cannot predict now.",
            15:"Concentrate and ask again.",
            16:"Don't count on it.",
            17:"My reply is no.",
            18:"My sources say no.",
            19:"Outlook not so good.",
            20:"Very doubtful."}

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there! :wave:'
    
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
        return random.choice(['heads', 'tails'])
    
    if p_message == '8ball':
        return answer_dict[random.randint(1, 20)]

    return 'Unknown command'