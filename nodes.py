
class Node:
    def __init__(self, next):
        self.type = type
        self.next = next
        
    def call(self):
        self.next.call()
    

class BoolNode(Node):
    def __ini__(self, val: bool):
        self.val = val
        super().__init__
        
    def call(self) -> bool:
        return self.val
        

class TextNode(Node):
    def __init__(self, value: str):
        self.value = value
        
    def call(self) -> str:
        return self.value
    
    
class IntNode(Node):
    def __init__(self, value: int):
        self.value = value
        
    def call(self) -> int:
        return self.value
    
        
class MathNode(Node):
    def __init__(self, left: IntNode, right: IntNode, op):
        self.left = left
        self.right = right
        self.op = op
        
    def call(self):
        if not isinstance(self.left, IntNode) or not isinstance(self.right, IntNode):
            raise TypeError("MathNode requiere operandos tipo IntNode")

        match self.op:
            case "+":
                return self.left.call() + self.right.call()
            case "-":
                return self.left.call() - self.right.call()
            case "*":
                return self.left.call() * self.right.call()
            case "/":
                return self.left.call() / self.right.call()



class ConditionalNode(Node):
    def __init__(self, left, right, trueOp, falseOp, cond):
        self.left = left
        self.right = right
        self.trueOp = trueOp
        self.falseOp = falseOp
        self.cond = cond
        
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
            return
            
        else:
            self.falseOp.call()
            return 
        
            
class PrintNode(Node):
    def __init__(self, value):
        self.value = value
    
    def call(self):
        print(self.value.call() if hasattr(self.value, "call") else self.value)
        
        
class VariableNode(Node):
    def __init__(self, name: str, program):
        self.name = name
        self.program = program
        
    def call(self):
        return self.program.memo[self.name]
    
    
        
class AssignNode(Node):
    def __init__(self, var: str, val, program):
        self.var = var
        self.val = val
        self.program = program
        
    def call(self) -> None:
        var_name = self.var.call() if hasattr(self.var, "call") else self.var
        value = self.val.call() if hasattr(self.val, "call") else self.val
        self.program.memo[var_name] = value
        return

        
        
