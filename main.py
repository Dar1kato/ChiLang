# main.py
import sys
import time
from functools import wraps

from context import Program
from parser import parser
from lexer import lexer
from nodes import PrintNode, AssignNode, ConditionalNode
from utils import evaluator

def debug_tree(node, depth=0):
    indent = "    " * depth
    while node:
        print(f"{indent}{type(node).__name__}", end="")

        # Imprime información específica según el tipo
        if isinstance(node, PrintNode):
            print(f" (Print: {getattr(node.value, 'value', node.value)})")

        elif isinstance(node, AssignNode):
            var = getattr(node.var, 'value', node.var)
            val = getattr(node.val, 'value', node.val)
            print(f" (Assign: {var} = {val})")

        elif isinstance(node, ConditionalNode):
            print(f" (If {node.left} {node.cond} {node.right})")
            print(f"{indent}  True branch:")
            debug_tree(node.trueOp, depth + 1)
            print(f"{indent}  False branch:")
            debug_tree(node.falseOp, depth + 1)

        else:
            print()

        node = node.next
        
def debug_mode(func):
    """
    Decorador que añade funcionalidad de debug a la función run()
    """
    @wraps(func)
    def wrapper(file_name, debug=False):
        program = Program()
        
        with open(file_name, 'r') as file:
            if debug:
                print("Starting program...\n")
                time.sleep(1)
            
            tokens = lexer(file)
            
            if debug:
                print("Getting tokens...\n")
                time.sleep(1)
                
                for token in tokens:
                    print(f"{token}\n")
                    time.sleep(0.1)
                
                time.sleep(1)
                print("Building AST...")
            
            ast = parser(program, tokens)
            
            if debug:
                print("\n")
                debug_tree(ast)
    
    return wrapper

@debug_mode
def run(file_name, debug: bool):
    program = Program()
    
    with open(file_name, 'r') as file:
        tokens = lexer(file)
        ast = parser(program, tokens)
        
        if debug:
            print("\nExecuting program...\n")
            time.sleep(1)
            
        evaluator(ast, program)  # ¡Esto faltaba en el decorador!
           
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 main.py archivo.chilang")
        sys.exit(1)

    run(sys.argv[1], True)


