# main.py
import sys
from context import Program
from parser import tokenize, parseLine
from commands import get_command_map

def run(file_name):
    program = Program()
    program.commands = get_command_map()

    with open(file_name, 'r') as file:
        for line in file:
            tokens = tokenize(line)
            #print(f"Tokens: {tokens}")
            parseLine(program, tokens)
            #print(f"Stack: {program.getExecutionStack()}")
            #print(f"Memo: {program.getMemo()}")
            #print("\n")
            if not program.execution_stack:
                return
            
           
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 main.py archivo.chilang")
        sys.exit(1)

    run(sys.argv[1])


