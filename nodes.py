import tokens

class Node:
    def __init__(self):
        self.type = None
        self.next = None
        
    def call(self):
        self.next.call()

class StarNode(Node):
    def __init__(self):
        super().__init__()
        self.type = "Start"
        
    def __repr__(self):
        print("Programa iniciando")
        
        
class EndNode(Node):
    def __init__(self):
        super().__init__()
        self.type = "End"
        
    def __repr__(self):
        print("Fin del programa")
        

class MathNode(Node):
    def __init__(self, left, right, op):
        super().__init__()
        self.left = left
        self.right = right
        self.op = op

    def call(self):
        left_val = self.left.call() if hasattr(self.left, "call") else self.left
        right_val = self.right.call() if hasattr(self.right, "call") else self.right

        match self.op:
            case "+":
                result = left_val + right_val
            case "-":
                result = left_val - right_val
            case "*":
                result = left_val * right_val
            case "/":
                result = left_val / right_val
            case _:
                raise ValueError(f"Operador no soportado: {self.op}")

        return result


class ConditionalNode(Node):
    def __init__(self, left, right, cond, trueOp, falseOp, program):
        super().__init__()
        self.left = left
        self.right = right
        self.cond = cond
        self.trueOp = trueOp
        self.falseOp = falseOp
        self.program = program

    def __repr__(self):
        return f"ConditionalNode({self.left} {self.cond} {self.right})"
    
    def eval(self):
        def resolve(value):
            if hasattr(value, 'name'):  
                var_name = value.name
                if var_name in self.program.memo:
                    resultado = self.program.memo[var_name]
                    return resultado
            elif isinstance(value, str) and value in self.program.memo:
                resultado = self.program.memo[value]
                return resultado
            elif hasattr(value, "value"):
                resultado = value.value
                return resultado
            else:
                print(f"Devolviendo valor original: {value}")
                return value

        left_val = resolve(self.left)
        right_val = resolve(self.right)

        match self.cond:
            case "==": return left_val == right_val
            case "!=": return left_val != right_val
            case "<": return left_val < right_val
            case ">": return left_val > right_val
            case "<=": return left_val <= right_val
            case ">=": return left_val >= right_val
            case _: raise ValueError(f"Operador condicional desconocido: {self.cond}")

    def call(self):
        # Elegir la rama (NO llamar aquí, solo redirigir el flujo)
        chosen_branch = self.trueOp if self.eval() else self.falseOp

        if chosen_branch:
            # Encuentra el último nodo de la rama y conéctalo con el siguiente del if
            last = chosen_branch
            while last.next:
                last = last.next
            last.next = self.next

            # Redirige el flujo: reemplaza `self.next` por la rama correcta
            self.next = chosen_branch
            
            
class PrintNode(Node):
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    def __repr__(self):
        return f"Imprimiendo el valor {self.value}"
    
    def call(self):
        print(self.value)

        
        
class VariableNode(Node):
    def __init__(self, name: str, program):
        self.name = name
        self.program = program
        super().__init__()
        
    def __repr__(self):
        return f"{self.name}"
    
    def call(self):
        return self.program.memo[self.name]

        
class AssignNode(Node):
    def __init__(self, var: str, val, program):
        self.var = var
        self.val = val
        self.program = program
        super().__init__()
        
    def __repr__(self):
        return f"Asignando variable {self.var} con valor {self.val}"
        
    def call(self):
        var_name = self.var.value
        value = self.val.value

        self.program.memo[var_name] = value

        
        
