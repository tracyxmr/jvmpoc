# jvmpoc
A simple JVM like virtual machine to understand how Java bytecode works.

# Example
The Java source code:
```java
int first = 42;
int second = 78;
int result = first + second;
```
Equals to:
```python
bipush(42)
istore(1)
bipush(78)
istore(2)
iload(1)
iload(2)
iadd()
istore(3)
```
Output:
```
Bytecode: [16, 42, 54, 1, 16, 78, 54, 2, 21, 1, 21, 2, 96, 54, 3]
Stack Frame Operand Stack: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Stack Frame Local Variables: [0, 42, 78, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

- `bipush` - byte push, operand being an immediate
- `istore` - store the top operand value to a local variable
- `iload` - load a variables value into the operand stack
- `iadd` - pop the two operand stack values and add them

The `i` prefixs in these function names refer to `int`