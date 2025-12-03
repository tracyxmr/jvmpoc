import opcodes
from typing import List

"""
Builder class.
Builds the bytecode
"""
class Builder:
    def __init__(self):
        self.bytecode = []

    def emit(self, _bytes: List[int]):
        for byte in _bytes:
            self.bytecode.append(byte)

    def bipush(self, imm: int):
        self.emit([ opcodes.BIPUSH, imm ])

    def istore(self, idx: int):
        self.emit([ opcodes.ISTORE, idx ])

    def iload(self, idx: int):
        self.emit([ opcodes.ILOAD, idx ])

    def iadd(self):
        self.emit([ opcodes.IADD ])