class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.stack = [0]
        self.stack_pos = 0

    def __append_stack(self, value: int):
        if len(self.stack) <= self.stack_pos + 1:
            self.stack.append(value)
        else:
            self.stack[self.stack_pos + 1] = value

    def __increment_pos(self):
        new_pos = self.stack_pos + 1
        if new_pos > len(self.stack) - 1:
            return
        self.stack_pos = new_pos
        self.value = self.value + self.stack[self.stack_pos]

    def __decrement_pos(self):
        new_pos = self.stack_pos - 1
        if new_pos < 0:
            return
        self.value = self.value - self.stack[self.stack_pos]
        self.stack_pos = new_pos
        

    def add(self, num: int):
        self.__append_stack(num)
        self.__increment_pos()

    def subtract(self, num: int):
        self.__append_stack(-1 * num)
        self.__increment_pos()

    def undo(self):
        self.__decrement_pos()

    def redo(self):
        self.__increment_pos()

    def bulk_undo(self, steps: int):
        while steps != 0:
            self.undo()
            steps -= 1

    def bulk_redo(self, steps: int):
        while steps != 0:
            self.redo()
            steps -= 1