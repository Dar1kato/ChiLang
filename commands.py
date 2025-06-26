# commands.py
from utils import parseValue

def que_tranza(program, tokens):
    program.execution_stack.append("Start")

def camara(program, tokens):
    if program.execution_stack:
        program.execution_stack.pop()

        return

def mi_carnal(program, tokens):
    program.memo[tokens[1]] = parseValue(tokens[3])

def gritale(program, tokens):
    print(f"¡{tokens[-1]}, señitooo!")

def llamale_a(program, tokens):
    print(f"¡{program.memo[tokens[-1]]}, señitooo!")
    
def y_echale(program, tokens):
    val = program.memo[tokens[2]] if tokens[2] in program.memo else parseValue(tokens[2])
    program.memo[tokens[0]] = int(program.memo[tokens[0]]) + int(val)
    return

def y_quitale(program, tokens):
    val = program.memo[tokens[2]] if tokens[2] in program.memo else parseValue(tokens[2])
    program.memo[tokens[0]] = int(program.memo[tokens[0]]) - int(val)
    return

def get_command_map():
    return {
        "Que_tranza": que_tranza,
        "Camara": camara,
        "Mi_carnal": mi_carnal,
        "Gritale": gritale,
        "Llamale_a": llamale_a, 
        "y_echale": y_echale,
        "y_quitale": y_quitale,
    }
