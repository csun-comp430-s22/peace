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
BoolTrue: 'true';
BoolFalse: 'false';

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
DoubleQuote: '"';

WS : [ \t]+ -> skip;
Newline : ('\r' '\n'? | '\n') -> skip;

//Match C-style rules about identifiers (can not start with a digit, allow underscores)
//TOOD: Possibly allow any non-digit Unicode?
fragment IdentifierChar: [a-zA-Z_];
fragment NonZeroDigit: [1-9];
fragment Digit: [0-9];
Identifier: IdentifierChar (IdentifierChar | Digit)*;
Digits: Digit+;
FloatConst: Digits '.' Digits;

//Rules
statement: expression Semicolon | Identifier '=' expression Semicolon |
           return expression Semicolon | 
           return Semicolon | 
           func LParen expression* RParen Semicolon |
           expression LParen expression* RParen Semicolon |
           print LParen expression RParen Semicolon
           ;

expression: expression (Add | Subtract | Multiply | Divide | Modulo ) expression
          | expression (LessThan | GreaterThan | LessThanOrEq | GreaterThanOrEq ) expression
          | Identifier;
