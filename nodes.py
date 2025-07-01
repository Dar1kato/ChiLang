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
        
        
class EndNode(Node):
    def __init__(self):
        super().__init__()
        self.type = "End"
        
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
            
        # Next Node
        if self.next:
            self.next.call()

        return result


class ConditionalNode(Node):
    def __init__(self, left, right, cond, trueOp, falseOp):
        self.left = left
        self.right = right
        self.cond = cond
        self.trueOp = trueOp
        self.falseOp = falseOp
        super().__init__()
        
    def eval(self) -> bool:
        left_val = self.left.call() if hasattr(self.left, "call") else self.left
        right_val = self.right.call() if hasattr(self.right, "call") else self.right

        match self.cond:
            case "==":
                return left_val == right_val
            case "!=":
                return left_val != right_val
            case "<":
                return left_val < right_val
            case ">":
                return left_val > right_val
            
            # Y el resto
        
    def call(self) -> None:
        if self.eval():
            self.trueOp.call()
            
            # Next node
            if self.next:
                self.next.call()
            
        else:
            self.falseOp.call()
            
            # Next Node
            if self.next:
                self.next.call()
                
        if self.next:
            self.next.call()
            
            
class PrintNode(Node):
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    def call(self):
        print(self.value.call() if hasattr(self.value, "call") else self.value)
        
        # Next Node
        if self.next:
            self.next.call()
        
        
class VariableNode(Node):
    def __init__(self, name: str, program):
        self.name = name
        self.program = program
        super().__init__()
        
    def call(self):
        return self.program.memo[self.name]

        
class AssignNode(Node):
    def __init__(self, var: str, val, program):
        self.var = var
        self.val = val
        self.program = program
        super().__init__()
        
    def call(self) -> None:
        var_name = self.var.call() if hasattr(self.var, "call") else self.var
        value = self.val.call() if hasattr(self.val, "call") else self.val
        self.program.memo[var_name] = value
        
        if self.next:
            self.next.call()


        
        
