from asyncio.windows_events import NULL
import copy
from gettext import gettext
from logging.config import IDENTIFIER
from peace.antlr.generated.PeaceParser import PeaceParser
from peace.antlr.generated.PeaceVisitor import PeaceVisitor
from peace.antlr.generated.PeaceListener import PeaceListener

class PeaceType():
    #Extra "Token" Types for the typechecker since they are not defined in the grammar
    FUNCTION = 999
    FUNCTION_POINTER = 998
    ENUM_CONSTRUCTOR = 997

    def __init__(self, token_type: int, token: str, param_types = [], ret_type = None):
        self.token_type = token_type
        self.token = token
        self.param_types = param_types
        self.ret_type = ret_type

    def __eq__(self, other) -> bool:
        return (self.token_type == other.token_type and self.token == other.token)

class PeaceTypecheckError(Exception):
    def __init__(self, message):
        self.message = message

class PeaceTypeNotFoundError(Exception):
    def __init__(self, message):
        self.message = message

class PeaceTypechecker(PeaceVisitor):
    def __init__(self) -> None:
        self.type_environments = []
        self.ret_type = PeaceType(PeaceParser.Void, 'void')
        super().__init__()

    #Helpers
    def lookup_type(self, name:str) -> PeaceType:
        if (self.type_environments and name in self.type_environments[-1]):
            return self.type_environments[-1][name]
        raise PeaceTypeNotFoundError("Type not found: " + name)

    def append_type_environment(self):
        new_type_environment = dict()
        if (self.type_environments):
            new_type_environment = copy.deepcopy(self.type_environments[-1])
        self.type_environments.append(new_type_environment)


    def generate_function_signature(self, param_types, ret_type) -> str:
        sig = '('
        for index, param_type in enumerate(param_types):
            sig += param_type.token
            if (index != len(param_types) - 1):
                sig += ', '
        sig += ') -> '
        sig += ret_type.token

    # Visit a parse tree produced by PeaceParser#basetype.
    def visitBasetype(self, ctx:PeaceParser.BasetypeContext):
        return PeaceType(ctx.start.type, ctx.getText())


    # Visit a parse tree produced by PeaceParser#funcpointertype.
    def visitFuncpointertype(self, ctx:PeaceParser.FuncpointertypeContext):
        return PeaceType(ctx.start.type, ctx.getText())


    # Visit a parse tree produced by PeaceParser#atype.
    def visitAtype(self, ctx:PeaceParser.AtypeContext):
        type = self.visit(ctx.getChild(0))
        # Catch invalid identifiers here
        if (type is None):
            raise PeaceTypecheckError("Invalid type: " + ctx.getText())
        return type;


    # Visit a parse tree produced by PeaceParser#op.
    def visitOp(self, ctx:PeaceParser.OpContext):   
        return self.visitChildren(ctx)
    

    # Visit a parse tree produced by PeaceParser#BoolExpr.
    def visitBoolExpr(self, ctx:PeaceParser.BoolExprContext):
        return PeaceType(PeaceParser.Bool, 'bool')


    # Visit a parse tree produced by PeaceParser#IdentExpr.
    def visitIdentExpr(self, ctx:PeaceParser.IdentExprContext):
        try:
            return self.lookup_type(ctx.Identifier().getText())
        except PeaceTypeNotFoundError:
            return PeaceType(PeaceParser.Identifier, ctx.Identifier().getText())


    # Visit a parse tree produced by PeaceParser#FloatExpr.
    def visitFloatExpr(self, ctx:PeaceParser.FloatExprContext):
        return PeaceType(PeaceParser.Float, 'float')
        

    # Visit a parse tree produced by PeaceParser#StringLiteralExpr.
    def visitStringLiteralExpr(self, ctx:PeaceParser.StringLiteralExprContext):
        return PeaceType(PeaceParser.String, 'string')


    # Visit a parse tree produced by PeaceParser#ArithmeticExpr.
    def visitArithmeticExpr(self, ctx:PeaceParser.ArithmeticExprContext):
        l_type = self.visit(ctx.expression(0))
        r_type = self.visit(ctx.expression(1))
        if (l_type.token_type != PeaceParser.Int and l_type.token_type != PeaceParser.Float):
            raise PeaceTypecheckError("Invalid type for arithmetic expression: " + l_type.token)
        if (r_type.token_type != PeaceParser.Int and r_type.token_type != PeaceParser.Float):
            raise PeaceTypecheckError("Invalid type for arithmetic expression: " + r_type.token)
        if (l_type.token_type == PeaceParser.Float):
            return l_type
        if (r_type.token_type == PeaceParser.Float):
            return r_type
        return l_type


    # Visit a parse tree produced by PeaceParser#DigitExpr.
    def visitDigitExpr(self, ctx:PeaceParser.DigitExprContext):
        return PeaceType(PeaceParser.Int, 'int')


    # Visit a parse tree produced by PeaceParser#CompExpr.
    def visitCompExpr(self, ctx:PeaceParser.CompExprContext):
        l_type = self.visit(ctx.expression(0))
        r_type = self.visit(ctx.expression(1))
        if (ctx.Equal() or ctx.NotEqual()):
            if (l_type.token_type != PeaceParser.Int 
                and l_type.token_type != PeaceParser.Float
                and l_type.token_type != PeaceParser.String):
                raise PeaceTypecheckError("Invalid types for comparison: " + l_type.token + ", " + r_type.token)
        else:
            if (l_type.token_type != PeaceParser.Int and l_type.token_type != PeaceParser.Float):
                raise PeaceTypecheckError("Invalid type for comparison: " + l_type.token)
            if (r_type.token_type != PeaceParser.Int and r_type.token_type != PeaceParser.Float):
                raise PeaceTypecheckError("Invalid type for comparison: " + r_type.token)
        return PeaceType(PeaceParser.Bool, 'bool')


    # Visit a parse tree produced by PeaceParser#FuncPointCreateExpr.
    def visitFuncPointCreateExpr(self, ctx:PeaceParser.FuncPointCreateExprContext):
        try:
            type = self.lookup_type(ctx.Identifier().getText())
            if (type.token_type != PeaceParser.Func):
                raise PeaceTypecheckError("Invalid type for function pointer creation: " + type.token)
            return PeaceType(PeaceParser.FUNCTION_POINTER, type.token)
        except PeaceTypeNotFoundError:
            raise PeaceTypecheckError("Invalid type for function pointer creation: " + ctx.Identifier().getText())


    # Visit a parse tree produced by PeaceParser#FuncCallOrEnumExpr.
    def visitFuncCallOrEnumExpr(self, ctx:PeaceParser.FuncCallOrEnumExprContext):
        expressions = ctx.expression()
        function_type = self.visit(expressions[0])
        if (function_type.token_type == PeaceType.FUNCTION or function_type.token_type == PeaceType.ENUM_CONSTRUCTOR):
            for index, exp in enumerate(expressions[1:]):
                type = self.visit(exp)
                if type.token_type != function_type.param_types[index].token_type:
                    raise PeaceTypecheckError("Invalid param " + index + " for function/constructor call: " + type.token)
            return function_type.ret_type

        raise PeaceTypecheckError("No matching function or enum constructor found: " + function_type.token)


    # Visit a parse tree produced by PeaceParser#AssignExpr.
    def visitAssignExpr(self, ctx:PeaceParser.AssignExprContext):
        l_type = self.visit(ctx.expression(0))
        r_type = self.visit(ctx.expression(1))
        if (l_type != r_type):
            raise PeaceTypecheckError("Assignment type mismatch: " + l_type.token + " and " + r_type.token)
        return l_type


    # Visit a parse tree produced by PeaceParser#vardec.
    def visitVardec(self, ctx:PeaceParser.VardecContext):
        r_type = self.visit(ctx.expression())
        l_type = PeaceType(ctx.atype().start.type, ctx.atype().getText())
        if (ctx.atype().start.type == PeaceParser.Identifier):
            try:
                l_type = self.lookup_type(ctx.atype().getText())
            except PeaceTypeNotFoundError:
                raise PeaceTypecheckError("Trying to declare invalid type: " + ctx.atype().getText())
        if (r_type != l_type):
            raise PeaceTypecheckError("Variable declaration type mismatch: " + l_type.token + " and " + r_type.token)
        self.type_environments[-1][ctx.Identifier().getText()] =  l_type


    # Visit a parse tree produced by PeaceParser#ExprStmt.
    def visitExprStmt(self, ctx:PeaceParser.ExprStmtContext):
        return self.visit(ctx.expression())


    # Visit a parse tree produced by PeaceParser#VarDecStmt.
    def visitVarDecStmt(self, ctx:PeaceParser.VarDecStmtContext):
        return self.visit(ctx.vardec())


    # Visit a parse tree produced by PeaceParser#WhileStmt.
    def visitWhileStmt(self, ctx:PeaceParser.WhileStmtContext):
        l_type = self.visit(ctx.expression())
        r_type = PeaceType(PeaceParser.Bool, 'bool')
        if (l_type != r_type):
            raise PeaceTypecheckError("Variable declaration type mismatch: " + l_type.token + " and " + r_type.token)
        return r_type
        


    # Visit a parse tree produced by PeaceParser#IfStmt.
    def visitIfStmt(self, ctx:PeaceParser.IfStmtContext):
        l_type = self.visit(ctx.expression())
        r_type = PeaceType(PeaceParser.Bool, 'bool')
        if (l_type != r_type):
            raise PeaceTypecheckError("Variable declaration type mismatch: " + l_type.token + " and " + r_type.token)
        return r_type


    # Visit a parse tree produced by PeaceParser#MatchStmt.
    def visitMatchStmt(self, ctx:PeaceParser.MatchStmtContext):
        # Don't need the types here, just need to visit the children
        # but the code generator might care about the types
        self.match_on_type = self.visit(ctx.expression())
        for case in ctx.case_():
            case_type = self.visit(case)

    # Visit a parse tree produced by PeaceParser#case_.
    def visitCase_(self, ctx:PeaceParser.Case_Context):
        #case: pattern => expression
        #x => y = 3
        # matchstmt
        #   -casestmt <- current context (think of pos)
        #       -pattern
        #       -matcharrow
        #       -block
        #           -any statement (type checked 'here' in block)
        # Each case can introduce temp variables so we need to add their
        # types so tha the child block can be type checked
        self.append_type_environment();
        ret_type = self.visit(ctx.pattern()) 
        self.visit(ctx.block())
        self.type_environments.pop()
        return ret_type


    # Visit a parse tree produced by PeaceParser#DigitPattern.
    def visitDigitPattern(self, ctx:PeaceParser.DigitPatternContext):
        return PeaceType(PeaceParser.Int, 'int')


    # Visit a parse tree produced by PeaceParser#FloatPattern.
    def visitFloatPattern(self, ctx:PeaceParser.FloatPatternContext):
        return PeaceType(PeaceParser.Float, 'float');


    # Visit a parse tree produced by PeaceParser#StringPattern.
    def visitStringPattern(self, ctx:PeaceParser.StringPatternContext):
        return PeaceType(PeaceParser.String, 'string');


    # Visit a parse tree produced by PeaceParser#IdentifierPattern.
    def visitIdentifierPattern(self, ctx:PeaceParser.IdentifierPatternContext):
        # This pattern is used to pass the value of the expression we're matching
        # to the block so it has the same type 
        self.type_environments[-1][ctx.Identifier().getText()] =  self.match_on_type
        return self.match_on_type


    # Visit a parse tree produced by PeaceParser#AnyPattern.
    def visitAnyPattern(self, ctx:PeaceParser.AnyPatternContext):
        # Special case so we'll just return void and let code gen handle it
        return PeaceType(PeaceParser.Void, 'void')


    # Visit a parse tree produced by PeaceParser#ConstructorPattern.
    def visitConstructorPattern(self, ctx:PeaceParser.ConstructorPatternContext):
        try:
            identifiers = list(map(lambda x: x.getText(), ctx.Identifier()))
            cons_type = self.lookup_type(identifiers[0])
            if len(identifiers) - 1 == len(cons_type.param_types):
                for index, identifier in enumerate(identifiers[1:]):
                    param_type = cons_type.param_types[index]
                    self.type_environments[-1][identifier] =  param_type
            else:
                raise PeaceTypecheckError("Constructor pattern missing required params")
        except PeaceTypeNotFoundError:
            raise PeaceTypecheckError("Invalid type for constructor pattern: " + ctx.Identifier().getText())


    # Visit a parse tree produced by PeaceParser#ReturnExprStmt.
    def visitReturnExprStmt(self, ctx:PeaceParser.ReturnExprStmtContext):
        given_type = self.visit(ctx.expression())
        if (self.ret_type != given_type):
            raise PeaceTypecheckError("Expected return type: " + self.ret_type.token + " but got: " + given_type.token)


    # Visit a parse tree produced by PeaceParser#ReturnStmt.
    def visitReturnStmt(self, ctx:PeaceParser.ReturnStmtContext):
        if (self.ret_type != PeaceType(PeaceParser.Void, 'void')):
            raise PeaceTypecheckError("Expected return type: " + self.ret_type.token)


    # Visit a parse tree produced by PeaceParser#PrintStmt.
    def visitPrintStmt(self, ctx:PeaceParser.PrintStmtContext):
        l_type = self.visit(ctx.expression())
        if (l_type == PeaceType(PeaceParser.Int, 'int')):
            return l_type
        elif (l_type == PeaceType(PeaceParser.Bool, 'bool')):
            return l_type
        elif (l_type == PeaceType(PeaceParser.String, 'string')):
            return l_type
        elif (l_type == PeaceType(PeaceParser.Float, 'float')):
            return l_type
        else:
            raise PeaceTypecheckError("Unsupported type for print: " + l_type.token)


    # Visit a parse tree produced by PeaceParser#block.
    def visitBlock(self, ctx:PeaceParser.BlockContext):
        self.append_type_environment()
        self.visitChildren(ctx)
        self.type_environments.pop()


    # Visit a parse tree produced by PeaceParser#parameter.
    def visitParameter(self, ctx:PeaceParser.ParameterContext):
        type = self.visit(ctx.atype())
        # If we have a custom type as a param we need to check it's valid
        # in this scope
        if (type.token_type == PeaceParser.Identifier):
            try:
                self.lookup_type(type.token)
            except PeaceTypeNotFoundError:
                raise PeaceTypecheckError("Invalid parameter type: " + type.token)
        self.type_environments[-1][ctx.Identifier().getText()] = type
        return type


    # Visit a parse tree produced by PeaceParser#func_stmt.
    def visitFunc_stmt(self, ctx:PeaceParser.Func_stmtContext):
        func = ctx.Identifier().getText()
        func_type = ctx.atype().getText()
        if func not in self.funcs_prog_env:
            self.funcs_prog_env.update({func: func_type})

            # Set return type for current function as an instance var
            # It's a easy way to typecheck return statements in the function
            # block. We'll also store the ret type in the global type env
            # to typecheck function calls in a different way
            self.ret_type = self.visit(ctx.atype())
            param_types = []
            for param in ctx.parameter():
                param_types.append(self.visit(param))
            signature = self.generate_function_signature(param_types, self.ret_type)
            self.type_environments[-1][func] = PeaceType(PeaceType.FUNCTION, signature, param_types, self.ret_type)

            self.visit(ctx.block())
        elif func in self.funcs_prog_env:
            raise PeaceTypecheckError("Duplicate function definition: " + func + " already defined.")


    # Visit a parse tree produced by PeaceParser#cdef.
    def visitCdef(self, ctx:PeaceParser.CdefContext):
        cdef = ctx.Identifier().getText()
        if cdef not in self.cdefs:
            self.cdefs.append(cdef)
            params = []
            for atype in ctx.atype():
                params.append(self.visit(atype))
            self.type_environments[-1][cdef] =  PeaceType(PeaceType.ENUM_CONSTRUCTOR, cdef, params, self.type_environments[-1][self.enum_flag])
        elif cdef in self.cdefs:
            raise PeaceTypecheckError("Duplicate cdef definition: '" + cdef + "' already exists in '" + self.enum_flag + "'.")


    # Visit a parse tree produced by PeaceParser#enumdef.
    def visitEnumdef(self, ctx:PeaceParser.EnumdefContext):
        self.cdefs = []
        enum = ctx.Identifier().getText()
        self.enum_flag = enum
        if enum not in self.enums_prog_scope:
            self.enums_prog_scope.append(enum)
            self.type_environments[-1][enum] =  PeaceType(PeaceParser.Enum, enum)
        elif enum in self.enums_prog_scope:
            raise PeaceTypecheckError("Duplicate enum definition: " + enum + " already defined.")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#program.
    def visitProgram(self, ctx:PeaceParser.ProgramContext):
        self.enums_prog_scope = []
        self.funcs_prog_env = {}

        #Global Type Environment
        new_type_environment = dict()
        self.type_environments.append(new_type_environment)

        self.visitChildren(ctx)