# Predictive Parsing
Converts infix notation single-digit operations to postfix notation using predictive parsing. <br>
- Example of valid expression: 1+3/4%3+(2-1)<br>
- Example of invalid expression: 1+<b>23</b>/3

College project for Programming Languages Class

### Reference:
* What is Predictive Parsing? -> http://www.personal.kent.edu/~rmuhamma/Compilers/MyCompiler/predictiveParse.htm

### Grammar used:
* expr → operation rest
* rest → + operation {print (‘+’)}  rest | - operation {print (‘-’)}  rest | ε
* operation → operand rest2
* rest2 → * operand {print (‘*’)}  rest2 | / operand {print (‘/’)}  rest2 | ε
* operand → factor rest3
* rest3 → % factor {print (‘*’)} | ε
* factor → digit | ( expr )
* digit → 0 {print(‘0’)} (where 0 can be any digit from 0 to 9)
