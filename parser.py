# parser.py
from utils import link_nodes
from nodes import StarNode, EndNode, AssignNode, PrintNode, MathNode, ConditionalNode, VariableNode


def parser(program, tokens):
    head = None
    last = None
    i = 0

    while i < len(tokens):
        node, consumed = parseStatement(program, tokens, i)
        
        i += consumed

        if node:
            if head is None:
                head = node
                last = head
            else:
                last.next = node
                last = node

                while last.next:
                    last = last.next

    return head


def parseStatement(program, tokens, i):  
    
    # FUNCIONES  
    if tokens[i].type == "KEYWORD":
        match tokens[i].value:
            
            # ASIGNAR VALOR
            case "Mi_carnal":
                if tokens[i + 2].value == "dice_que":
                    var_name = tokens[i + 1] if tokens[i + 1].type == "IDENTIFIER" else None
                    
                    value = tokens[i + 3] if tokens[i + 3].type == "INT" or tokens[i + 3].type == "IDENTIFIER" else None
                    
                    return AssignNode(var= var_name, val= value, program= program), 4
                
                return None, 1
                
            # IMPRIMIR VALOR
            case "Gritale":
                to_print_token = tokens[i + 1]
                to_print = VariableNode(to_print_token.value, program) if to_print_token.type == "IDENTIFIER" else to_print_token.value
                
                return PrintNode(value=to_print), 2

            
            
            # CONDICIONAL
            case "Apoco_si":
                left = VariableNode(tokens[i + 1].value, program) if tokens[i + 1].type == "IDENTIFIER" else tokens[i + 1]
                op = tokens[i + 2].value
                right = VariableNode(tokens[i + 3].value, program) if tokens[i + 3].type == "IDENTIFIER" else tokens[i + 3]

                j = i + 4  
                true_nodes = []
                false_nodes = []
                current_branch = true_nodes

                while j < len(tokens):
                    if tokens[j].value == "Ahora_que_si_no":
                        current_branch = false_nodes
                        j += 1
                        continue
                    
                    if tokens[j].value == "Camara":
                        j += 1
                        break
                    
                    node, consumed = parseStatement(program, tokens, j)
                    if node:
                        current_branch.append(node)
                    j += consumed

                true_branch = link_nodes(true_nodes)
                false_branch = link_nodes(false_nodes)

                return ConditionalNode(left, right, op, true_branch, false_branch, program= program), j  
                
            
            case default:
                return None, 1
        
    # OPERADORES  MATEMATICOS   
    if tokens[i].type == "OPERATOR" and tokens[i].value in ["+", "-", "*", "/"]:

        if i > 0 and i + 1 < len(tokens):
            left_token = tokens[i - 1]
            right_token = tokens[i + 1]

            left = VariableNode(left_token.value, program) if left_token.type == "IDENTIFIER" else left_token.value
            right = VariableNode(right_token.value, program) if right_token.type == "IDENTIFIER" else right_token.value

            return MathNode(left=left, right=right, op=tokens[i].value), 3
        
        else:
            return None, 1

            

            
        
    

