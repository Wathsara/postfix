# postfix
Accepts a postfix single letter operands and operators +,-,* and / and which print sequence of instructions to evaluate the expression and leave the result in the register.

LD A which places the operand A into the register
ST A which places the content of the register in to the variable A
AD A which adds the content of the variable A to the register
SB A which substracts the content of the variable A to the register
ML A which multiplies the content of the variable A to the register
DV A which divides the content of the variable A to the register

Use TEMPn as temporary veriable

Ex 
input ABC*+DE-/
output
LD B
ML C
ST Temp1
LD A
AD TEMP1
ST TEMP
LD D
SB E
ST TEMP3
LD TEMP2
DV TEMP3
ST TEMP4
