from tokens import Token
from utils import findValueType

def evalLine(line) -> list:
    return line.strip().split()

commands =  {
        "Que_tranza": "Que_tranza",
        "Camara": "Camara",
        "Mi_carnal": "Mi_carnal",
        "Gritale": "Gritale",
        "Llamale_a": "Llamale_a", 
        "y_echale": "y_echale",
        "y_quitale": "y_quitale",
        "Apoco_si": "Apoco_si",
        "Ahora_que_si_no": "Ahora_que_si_no",
        "dice_que": "dice_que"
    }

def lexer(file) -> list:
    final_tokens = []
    
    for line in file:
        tokens = []
        lex_tokens = evalLine(line)
        
        for item in lex_tokens:
            if item not in commands:
                token = findValueType(item)
                tokens.append(token)
                
            if item in commands:
                token = Token(type="KEYWORD", value= commands[item])
                tokens.append(token)
        
        final_tokens.append(tokens) if tokens else None
                
    return final_tokens
                
    