# parser.py
from utils import eval_condition, parseValue
from commands import get_command_map

def tokenize(line):
    return line.strip().split()

def parseLine(program, tokens):
    if not tokens:
        return

    command = tokens[0]
    if command in program.commands:
        program.commands[command](program, tokens)
        return

    # Instrucciones especiales no incluidas en el mapa
    if command == "Apoco_si":
        var, op, val = tokens[1], tokens[2], tokens[3]
        result = eval_condition(program.memo, var, op, val)
        program.current_task.append("if:True" if result else "if:False")
        return

    if command == "Ahora_que_si_no":
        if program.current_task:
            program.current_task.pop()
        return

    if any(t.endswith(":False") for t in program.current_task):
        return
