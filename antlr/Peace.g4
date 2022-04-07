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
basetype: ( Int | Bool | Void | String | Identifier ); 
funcpointertype: LParen basetype Multiply RParen Arrow basetype; 
atype: basetype | funcpointertype;

expression: Digits |
            Identifier |
            expression (Add | Subtract | Multiply | Divide | Modulo ) expression |
            expression (LessThan | GreaterThan | LessThanOrEq | GreaterThanOrEq ) expression |
            expression LParen expression* RParen |
            Amp Identifier
            ;
vardec: Let Identifier Colon atype Assign expression;
statement:  vardec Semicolon |
            While LParen expression RParen LBracket statement* RBracket Semicolon |
            If LParen expression RParen LBracket statement* RBracket (Else LBracket statement* RBracket)? Semicolon |
            Match expression LBracket case* RBracket Semicolon |
            return expression Semicolon | 
            return Semicolon | 
            func LParen expression* RParen Semicolon |
            expression LParen expression* RParen Semicolon |
            print LParen expression RParen Semicolon
            ;

case: pattern MatchArrow expression ;
pattern: Identifier | Any | Identifier LParen pattern RParen;
parameter: Identifier Colon atype;
func: atype Identifier LParen parameter* RParen LBracket statement* RBracket;
enumdef: ;
cdef: Identifier LParen atype RParen;
program: func;
