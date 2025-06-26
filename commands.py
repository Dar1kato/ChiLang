# commands.py
from utils import parseValue

def que_tranza(program, tokens):
    program.current_task.append("Start")

def camara(program, tokens):
    if program.current_task:
        program.current_task.pop()

def mi_carnal(program, tokens):
    program.memo[tokens[1]] = parseValue(tokens[3])

def gritale(program, tokens):
    print(f"¡{tokens[-1]}, señitooo!")

def llamale_a(program, tokens):
    print(f"¡{program.memo[tokens[-1]]}, señitooo!")

def get_command_map():
    return {
        "Que_tranza": que_tranza,
        "Camara": camara,
        "Mi_carnal": mi_carnal,
        "Gritale": gritale,
        "Llamale_a": llamale_a
    }
