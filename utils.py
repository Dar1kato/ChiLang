def parseValue(value):
    if value.isdigit():
        return int(value)
    if value == "Simón":
        return True
    if value == "Nel":
        return False
    return value

def eval_condition(memo, left, op, right):
    left_val = memo.get(left, parseValue(left))
    right_val = memo.get(right, parseValue(right))

    if op == "==": return left_val == right_val
    if op == "!=": return left_val != right_val
    if op == ">": return left_val > right_val
    if op == "<": return left_val < right_val
    if op == ">=": return left_val >= right_val
    if op == "<=": return left_val <= right_val
    return False
