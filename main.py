# main.py
import sys
from context import Program
from parser import parser
from commands import get_command_map
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

            
def run(file_name):
    program = Program()
    
    with open(file_name, 'r') as file:
        tokens = lexer(file)
        #print(f"{tokens}\n")
        ast = parser(program, tokens)
        #print("\n")
        #debug_tree(ast)
        evaluator(ast, program)

           
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 main.py archivo.chilang")
        sys.exit(1)

    run(sys.argv[1])



