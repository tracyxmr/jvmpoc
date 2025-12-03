import opcodes
from typing import List

class StackFrame:
    def __init__(self):
        self.local_variables = [0] * 16
        self.operand_stack = [0] * 16

class VM:
    def __init__(self, bytecode: List[int]):
        self.bytecode = bytecode
        self.current_stack_frame = StackFrame()

    def execute(self):
        pc = 0

        while pc < len(self.bytecode):
            opcode = self.bytecode[pc]

            if opcode == opcodes.BIPUSH:
                imm = self.bytecode[pc + 1]
                (self.
                 current_stack_frame.
                 operand_stack.append(imm))
                pc += 2
            elif opcode == opcodes.ISTORE:
                idx = self.bytecode[pc + 1]
                value = self.current_stack_frame.operand_stack.pop()
                self.current_stack_frame.local_variables[idx] = value
                pc += 1
            elif opcode == opcodes.ILOAD:
                idx = self.bytecode[pc + 1]
                value = self.current_stack_frame.local_variables[idx]
                self.current_stack_frame.operand_stack.append(value)
                pc += 1
            elif opcode == opcodes.IADD:
                value1 = self.current_stack_frame.operand_stack.pop()
                value2 = self.current_stack_frame.operand_stack.pop()
                self.current_stack_frame.operand_stack.append(value1 + value2)
                pc += 1
            else:
                pc += 1

        print(f"Bytecode: {self.bytecode}")
        print(f"Stack Frame Operand Stack: {self.current_stack_frame.operand_stack}")
        print(f"Stack Frame Local Variables: {self.current_stack_frame.local_variables}")