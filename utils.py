def parseValue(value):
    if value.isdigit():
        return int(value)
    if value == "Simón":
        return True
    if value == "Nel":
        return False
    return value

def eval_condition(program, left, op, right):
    left_val = program.memo[left] if left in program.memo else parseValue(left)
    right_val = program.memo[right] if right in program.memo else parseValue(right)

    if op == "==": return left_val == right_val
    if op == "!=": return left_val != right_val
    if op == ">": return left_val > right_val
    if op == "<": return left_val < right_val
    if op == ">=": return left_val >= right_val
    if op == "<=": return left_val <= right_val
    
    return False

def eval_skip(program, tokens):
    if tokens[0] == "Camara":
        return False
    
    for state in program.execution_stack:
        if state.endswith(":False") and tokens[0] != "Ahora_que_si_no":
            return True
    return False
    
    