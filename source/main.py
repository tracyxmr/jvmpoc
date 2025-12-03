from builder import Builder
from vm import VM

b = Builder()

b.bipush(42)
b.istore(1)
b.bipush(78)
b.istore(2)
b.iload(1)
b.iload(2)
b.iadd()
b.istore(3)

vm = VM(b.bytecode)
vm.execute()