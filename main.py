# main.py
import sys
from context import Program
from parser import tokenize, parseLine
from commands import get_command_map
from lexer import lexer

def run(file_name):
    program = Program()
    program.commands = get_command_map()

    with open(file_name, 'r') as file:
        num = 0
        for line in file:
            num += 1
            tokens = tokenize(line)
            parseLine(program, tokens)
            
            """ print(f"LINE {num}")
            print(f"Tokens: {tokens}")
            print(f"Stack: {program.getExecutionStack()}")
            print(f"Memo: {program.getMemo()}")
            print("\n") """
            if not program.execution_stack:
                return
            
def debug_run(file_name):
    program = Program()
    
    with open(file_name, 'r') as file:
        tokens = lexer(file)
        print(tokens)
           
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 main.py archivo.chilang")
        sys.exit(1)

    debug_run(sys.argv[1])


