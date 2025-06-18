from dic import DIC
import sys

class Program:
    def __init__(self):
        self.current_task = [] # Stack
        self.memo = {}
        self.example = "Mi_carnal pulpo dice_que 5"
        
    def tokenize(self, line):
        tokenized_line = line.strip().split(" ")
        
        print(f'Tokens de la linea "{line}": {tokenized_line}')
        return tokenized_line
    
    def getMemo(self):
        print(f'Memoria actual: {self.memo}')
        return
    
    
    def parseLine(self, tokens):
        # Program Starts
        if tokens[0] == "Que_tranza":
            self.current_task.append("Start")
            return
        
        if tokens[0] == "Camara":
            self.current_task.pop()
            return
            
        if self.current_task and self.current_task[-1] == "Start":
            if tokens[0] == "Mi_carnal" and tokens[2] == "dice_que":
                self.memo[tokens[1]] = tokens[3]
                return
            
            if tokens[0] in self.memo:
                if tokens[1] == "y_echale":
                    new_val = int(self.memo[tokens[0]]) + int(tokens[2])
                    self.memo[tokens[0]] = new_val
                    return
                
                if tokens[1] == "y_quitale":
                    new_val = int(self.memo[tokens[0]]) - int(tokens[2])
                    self.memo[tokens[0]] = new_val
                    return
            
        if tokens[0] == "Gritale":
            item = self.memo[tokens[-1]]
            print(item)
            return
        
    def run(self, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                if line.strip():  # Ignora líneas vacías
                    tokenized_line = self.tokenize(line)
                    self.parseLine(tokenized_line)
                    
                    print(f'Memoria actual: {self.memo}')
                    print(f"Acción actual: {self.current_task}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 lenguaje.py archivo.txt")
        sys.exit(1)

    archivo = sys.argv[1]
    program = Program()
    program.run(archivo)



# program.tokenize("Mi_carnal pulpo dice_que 5")
# program.getMemo()
# program.parseLine(program.tokenize("Mi_carnal pulpo dice_que 5"))
# program.getMemo()
# program.parseLine(program.tokenize("pulpo y_echale 10"))
# program.getMemo()
# program.parseLine(program.tokenize("Gritale pulpo"))
