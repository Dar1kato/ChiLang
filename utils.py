from tokens import Token
from nodes import Node


def findValueType(value):
    if value.isdigit():
        return Token(type="INT", value= int(value))
    
    if value == "Simón":
        return Token(type="BOOL", value= True)
    
    if value == "Nel":
        return Token(type="BOOL", value= False)
    
    if value in ["==", "!=", ">", "<", ">=", "<=", "Y", "O", "No_es"]:
        return Token(type="OPERATOR", value= value)
    
    if value in ["+", "-", "*", "/"]:
        return Token(type="OPERATOR", value= value)
    
    if value in ["(", ")"]:
        return Token(type="ENCLOSURE", value= value)
    
    return Token(type="IDENTIFIER", value= value)



def link_nodes(nodes):
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0] if nodes else None


def eval_condition(program, left, op, right):
    left_val = program.memo[left] if left in program.memo else findValueType(left)
    right_val = program.memo[right] if right in program.memo else findValueType(right)

    if op == "==": return left_val == right_val
    if op == "!=": return left_val != right_val
    if op == ">": return left_val > right_val
    if op == "<": return left_val < right_val
    if op == ">=": return left_val >= right_val
    if op == "<=": return left_val <= right_val
    if op == "Y": return left_val and right_val
    if op == "O": return left_val or right_val
    if op == "No_es": return left_val != right_val
    
    return False



def eval_skip(program, tokens) -> bool:
    # Siempre permitir 'Camara' para cerrar bloques
    if tokens[0] == "Camara":
        return False

    if tokens[0] == "Ahora_que_si_no":
        return False
    
    # Si cualquier bloque activo en el stack tiene condición False, saltar
    for block in reversed(program.execution_stack):
        if block["closed"] == False:
            if block["cond"] == False:
                print("!--- Skip line")
                return True
            if block["cond"] == True:
                return False
            
            
def evaluator(head: Node, program):
    current = head

    while current is not None:
        #print(f"Ejecutando nodo: {current.__class__.__name__}")
        #print(f"Nodo: {current}, siguiente: {current.next}")
        current.call()
        current = current.next



    