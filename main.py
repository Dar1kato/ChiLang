from dic import DIC
import sys

class Program:
    def __init__(self):
        self.current_task = [] # Stack
        self.memo = {}
        self.example = "Mi_carnal pulpo dice_que 5"
        
    def tokenize(self, line):
        tokenized_line = line.strip().split(" ")
        
        #print(f'Tokens de la linea "{line}": {tokenized_line}')
        return tokenized_line
    
    def getMemo(self):
        #print(f'Memoria actual: {self.memo}')
        return
    
    
    def parseValue(self, value):
        if value.isdigit():
            return int(value)
        if value == "Simón":
            return True
        if value == "Nel":
            return False
        return value  # Asume string si no es ninguno de los anteriores

    
    
    def parseLine(self, tokens):
        # Program Starts
        if tokens[0] == "Que_tranza":
            self.current_task.append("Start")
            return
        
        if tokens[0] == "Camara":
            self.current_task.pop()
            return
            
        # Programa Corriendo
        if self.current_task and self.current_task[-1] == "Start":
            
            # Declaración de variables
            if tokens[0] == "Mi_carnal" and tokens[2] == "dice_que":
                self.memo[tokens[1]] = self.parseValue(tokens[3])
                return
            
            # Operaciones aritmeticas a variables
            if tokens[0] in self.memo:
                
                # Suma
                if tokens[1] == "y_echale":
                    val = self.memo[tokens[2]] if tokens[2] in self.memo else self.parseValue(tokens[2])
                    self.memo[tokens[0]] = int(self.memo[tokens[0]]) + int(val)
                    return

                # Resta
                if tokens[1] == "y_quitale":
                    val = self.memo[tokens[2]] if tokens[2] in self.memo else self.parseValue(tokens[2])
                    self.memo[tokens[0]] = int(self.memo[tokens[0]]) - int(val)
                    return

                # div
                if tokens[1] == "y_partelo_en":
                    val = self.memo[tokens[2]] if tokens[2] in self.memo else self.parseValue(tokens[2])
                    self.memo[tokens[0]] = int(self.memo[tokens[0]]) / int(val)
                    return
                
            
            # Condicional 
            if tokens[0] == "Apoco_si":
                self.current_task.append("Cond")
                
                if tokens[1] == "no_le_llega_a":
                    if (tokens[1] < tokens[-1]):
                        pass
                        
            if tokens[0] == "Ahora_que_si_no" and not self.current_task[-1] == "Cond":
                pass
                        
                
            
        # Print
        if tokens[0] == "Llamale_a":
            item = self.memo[tokens[-1]]
            print(f'¡{item}, señitooo!')
            return
        
    def run(self, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                if line.strip():  # Ignora líneas vacías
                    tokenized_line = self.tokenize(line)
                    self.parseLine(tokenized_line)
                    
                    #print(f'Memoria actual: {self.memo}')
                    #print(f"Acción actual: {self.current_task}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 lenguaje.py archivo.txt")
        sys.exit(1)

    archivo = sys.argv[1]
    program = Program()
    program.run(archivo)

