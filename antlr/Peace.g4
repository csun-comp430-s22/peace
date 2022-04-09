grammar Peace;

//Types
Int: 'int';
Float: 'float';
Bool: 'bool';
Void: 'void';
String: 'string';
Enum: 'enum';

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
Comma: ',';

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
            expression Assign expression |
            Amp Identifier |
            Enum
            ;
vardec: Let Identifier Colon atype Assign expression;
statement:  expression Semicolon |
            vardec Semicolon |
            While LParen expression RParen LBracket statement* RBracket (Semicolon)? |
            If LParen expression RParen LBracket statement* RBracket (Else LBracket statement* RBracket)? (Semicolon)? |
            Match expression LBracket case_ (Comma case_)* RBracket (Semicolon)? |
            Return expression Semicolon | 
            Return Semicolon | 
            expression LParen expression* RParen Semicolon |
            Print LParen expression RParen Semicolon | 
            func_call |
            func_stmt |
            enumdef;
            

func_call: expression LParen expression* RParen Semicolon;
case_: pattern MatchArrow expression;
pattern: Digits | Identifier | Any | Identifier LParen pattern RParen;
parameter: Identifier Colon atype;
func_stmt: atype Identifier LParen parameter* (Comma parameter)* RParen LBracket statement* RBracket (Semicolon)?;
cdef: Identifier Colon atype Semicolon;
enumdef: Enum expression Assign LBracket cdef+ RBracket (Semicolon)?;
program: enumdef* func_stmt+;
