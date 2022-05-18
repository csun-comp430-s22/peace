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
Line_Comment: '//' .*? '\r'? '\n' -> skip;
Comment: '/*' .*? '*/' -> skip;

//Match C-style rules about identifiers (can not start with a digit, allow underscores)
//TOOD: Possibly allow any non-digit Unicode?
fragment IdentifierChar: [a-zA-Z_];
fragment NonZeroDigit: [1-9];
fragment Digit: [0-9];
Identifier: IdentifierChar (IdentifierChar | Digit)*;
Digits: Digit+;
FloatConst: Digits '.' Digits;
StringLiteral: '"' .*? '"' ;


//Rules
basetype: ( Int | Bool | Void | String | Identifier ); 
funcpointertype: LParen basetype (Comma basetype)*  RParen Arrow basetype;
atype: basetype | funcpointertype;
op: (Add | Subtract | Multiply | Divide | Modulo );

expression: Digits #DigitExpr
            | FloatConst #FloatExpr
            | Identifier #IdentExpr
            | StringLiteral #StringLiteralExpr
            | (BoolTrue | BoolFalse) #BoolExpr
            | expression op expression #ArithmeticExpr
            | expression (LessThan | GreaterThan | LessThanOrEq | GreaterThanOrEq ) expression #CompExpr
            | expression LParen expression* RParen #FuncCallOrEnumExpr
            | expression Assign expression  #AssignExpr
            | Amp Identifier  #FuncPointCreateExpr
            ;
vardec: Let Identifier Colon atype Assign expression;
statement:  expression Semicolon    #ExprStmt
            | vardec Semicolon      #VarDecStmt
            | While LParen expression RParen block (Semicolon)?  #WhileStmt
            | If LParen expression RParen block (Else block)? (Semicolon)?    #IfStmt
            | Match expression LBracket case_ (Comma case_)* RBracket (Semicolon)?  #MatchStmt 
            | Return expression Semicolon   #ReturnExprStmt 
            | Return Semicolon  #ReturnStmt 
            | Print LParen expression RParen Semicolon  #PrintStmt 
            ;
block: LBracket statement* RBracket;    

case_: pattern MatchArrow block;
pattern: Digits | Identifier | Any | Identifier LParen (Identifier)* RParen;
parameter: Identifier Colon atype;
func_stmt: atype Identifier LParen (parameter (Comma parameter)*)* RParen block (Semicolon)?;
cdef: Identifier Colon atype (Comma atype)* Semicolon;
enumdef: Enum Identifier LBracket cdef+ RBracket (Semicolon)?;
program: enumdef* func_stmt+;