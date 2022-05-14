import copy
from antlr.generated.PeaceParser import PeaceParser
from antlr.generated.PeaceVisitor import PeaceVisitor

class PeaceType():
    #Extra "Token" Types for the typechecker since they are not defined in the grammar
    FUNCTION = 999
    FUNCTION_POINTER = 998

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
        super().__init__()

    def lookup_type(self, name:str) -> PeaceType:
        if (self.type_environments and name in self.type_environments[-1]):
            return self.type_environments[-1][name]
        raise PeaceTypeNotFoundError("Type not found: " + name)

    # Visit a parse tree produced by PeaceParser#basetype.
    def visitBasetype(self, ctx:PeaceParser.BasetypeContext):
        return PeaceType(PeaceParser.RULE_basetype, 'basetype')


    # Visit a parse tree produced by PeaceParser#funcpointertype.
    def visitFuncpointertype(self, ctx:PeaceParser.FuncpointertypeContext):
        return PeaceType(PeaceParser.RULE_funcpointertype, 'funcpointertype')


    # Visit a parse tree produced by PeaceParser#atype.
    def visitAtype(self, ctx:PeaceParser.AtypeContext):
        return PeaceType(PeaceParser.RULE_atype, 'atype')


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
        types = ctx.expression()
        function_type = self.visit(types[0])
        if (function_type.token_type == PeaceType.FUNCTION or function_type.token_type == PeaceType.ENUM):
            for index, type in enumerate(types[1:]):
                if type.token_type != function_type.param_types[index].token_type:
                    raise PeaceTypecheckError("Invalid param for function call: " + type.token)
            return type.ret_type
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
        l_type = self.visit(ctx.expression())
        r_type = self.visit(ctx.expression())
        if (l_type != r_type):
            raise PeaceTypecheckError("Variable declaration type mismatch: " + l_type.token + " and " + r_type.token)
        return r_type


    # Visit a parse tree produced by PeaceParser#ReturnExprStmt.
    def visitReturnExprStmt(self, ctx:PeaceParser.ReturnExprStmtContext):
        l_type = self.visit(ctx.expression())
        r_type = self.type_environment
        if (l_type == r_type):
            return r_type
        else:
            raise PeaceTypecheckError("Variable declaration type mismatch: " + l_type.token + " and " + r_type.token)


    # Visit a parse tree produced by PeaceParser#ReturnStmt.
    def visitReturnStmt(self, ctx:PeaceParser.ReturnStmtContext):
        l_type = self.visit(ctx.expression())
        r_type = self.type_environment
        if (l_type == r_type):
            return r_type
        else:
            raise PeaceTypecheckError("Variable declaration type mismatch: " + l_type.token + " and " + r_type.token)



    # Visit a parse tree produced by PeaceParser#PrintStmt.
    def visitPrintStmt(self, ctx:PeaceParser.PrintStmtContext):
        l_type = self.visit(ctx.expression())
        r_type = PeaceType(PeaceParser.Int 'int')
        if (l_type == r_type):
            return r_type
        else:
            raise PeaceTypecheckError("Variable declaration type mismatch: " + l_type.token + " and " + r_type.token)






    # Visit a parse tree produced by PeaceParser#block.
    def visitBlock(self, ctx:PeaceParser.BlockContext):
        new_type_environment = dict()
        if (self.type_environments):
            new_type_environment = copy.deepcopy(self.type_environments[-1])
        self.type_environments.append(new_type_environment)
        self.visitChildren(ctx)
        self.type_environments.pop()


    # Visit a parse tree produced by PeaceParser#case_.
    def visitCase_(self, ctx:PeaceParser.Case_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#pattern.
    def visitPattern(self, ctx:PeaceParser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#parameter.
    def visitParameter(self, ctx:PeaceParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#func_stmt.
    def visitFunc_stmt(self, ctx:PeaceParser.Func_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#cdef.
    def visitCdef(self, ctx:PeaceParser.CdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#enumdef.
    def visitEnumdef(self, ctx:PeaceParser.EnumdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#program.
    def visitProgram(self, ctx:PeaceParser.ProgramContext):
        return self.visitChildren(ctx)