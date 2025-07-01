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
    }

def lexer(file) -> list:
    tokens = []
    
    for line in file:
        lex_tokens = evalLine(line)
        
        for item in lex_tokens:
            if item not in commands:
                token = findValueType(item)
                tokens.append(token)
                
            if item in commands:
                token = Token(type="KEYWORD", value= commands[item])
                tokens.append(token)
                
    return tokens
                
    