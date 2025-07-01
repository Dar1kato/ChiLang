# main.py
import sys
from context import Program
from parser import parser
from commands import get_command_map
from lexer import lexer
            
def run(file_name):
    program = Program()
    
    with open(file_name, 'r') as file:
        tokens = lexer(file)
        print(f"{tokens}\n")
        parser(program, tokens)
           
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 main.py archivo.chilang")
        sys.exit(1)

    run(sys.argv[1])


