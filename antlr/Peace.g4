grammar Peace;

//Types
Int: 'int';
Float: 'float';
Bool: 'bool';
Void: 'void';
String: 'string';

//Operations
Add: '+';
Subtract: '-';
Multiply: '*';
Divide: '/';
Modulo: '%';
LessThan: '<';
GreaterThan: '>';
LessThanOrEq: '<=';
GreaterThanOrEq: '>=';
Equal: '==';
NotEqual: '!=';

//Vars
Let: 'let';

//Function Pointers
Arrow: '->';

While: 'while';
If: 'if';
Else: 'else';
Return: 'return';
Function: 'func';
Print: 'print';

//PatternMatching
Match: 'match';
MatchArrow: '=>';
Any: '_';

Assign: '=';
Amp: '&';
Colon: ':';
Semicolon: ';';
LParen: '(';
RParen: ')';
LBracket: '{';
RBracket: '}';

WS : [ \t]+ -> skip;
Newline : ('\r' '\n'? | '\n') -> skip;

//Rules
statement: expression Semicolon | Identifier '=' expression Semicolon;
expression: expression (Add | Subtract | Multiply | Divide | Modulo ) expression
          | expression (LessThan | GreaterThan | LessThanOrEq | GreaterThanOrEq ) expression
          | Identifier;

Identifier: [a-zA-Z]+;
Digit: [0-9];
Digits: Digit+;