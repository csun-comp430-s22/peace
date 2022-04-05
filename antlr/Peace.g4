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
statement: expression Semicolon | Identifier '=' expression Semicolon;
expression: expression (Add | Subtract | Multiply | Divide | Modulo ) expression
          | expression (LessThan | GreaterThan | LessThanOrEq | GreaterThanOrEq ) expression
          | Identifier;

type_: ( Int | Bool | Void | String | Identifier ) ;
case: pattern MatchArrow expression ;
pattern: Identifier | Any | Identifier LParen pattern RParen;
parameter: Identifier Colon type_;
func: type_ Identifier LParen parameter* RParen LBracket statement* RBracket;
enumdef: ;
cdef: Identifier LParen type_ RParen;
program: func;


