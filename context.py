class Program:
    def __init__(self):
        self.current_task = []
        self.memo = {}
        self.commands = {}  # Se llenará desde commands.py

    def getMemo(self):
        return self.memo
