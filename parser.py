# parser.py
from utils import eval_condition, parseValue, eval_skip
from commands import get_command_map


def tokenize(line):
    return line.strip().split()

def parseLine(program, tokens):        
    # Empty line
    if not tokens:
        return
    
    # Line skip
    if eval_skip(program, tokens):
        #print("!--- Salto de linea")
        return
    
    command = tokens[0]
    
    # Basic Commands
    if command in program.commands:
        program.commands[command](program, tokens)
        return
    
    # Math
    if command in program.memo:
        command = tokens[1]
        program.commands[command](program, tokens)
        return
    

    # Complex Commands
    # If
    if command == "Apoco_si":
        var, op, val = tokens[1], tokens[2], tokens[3]
        result = eval_condition(program, var, str(op), val)
        
        program.execution_stack.append("if:True" if result else "if:False")
        
        return
        """ program.jump = False if result else True
        
        program.execution_stack.append("else:False" if result else "else:True")
        return """

    # Else
    if command == "Ahora_que_si_no":
        last_if = program.execution_stack.pop()
        
        program.execution_stack.append("else:False" if last_if == "if:True" else "else:True")
    
        return


