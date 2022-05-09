import copy
from antlr.generated.PeaceParser import PeaceParser
from antlr.generated.PeaceVisitor import PeaceVisitor

class PeaceType():
    def __init__(self, token_type, token):
        self.token_type = token_type
        self.token = token

    def __eq__(self, other) -> bool:
        return (self.token_type == other.token_type and self.token == other.token)

class PeaceTypecheckError(Exception):
    def __init__(self, message):
        self.message = message

class PeaceTypechecker(PeaceVisitor):
    def __init__(self) -> None:
        self.type_environments = []
        super().__init__()

    # Visit a parse tree produced by PeaceParser#basetype.
    def visitBasetype(self, ctx:PeaceParser.BasetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#funcpointertype.
    def visitFuncpointertype(self, ctx:PeaceParser.FuncpointertypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#atype.
    def visitAtype(self, ctx:PeaceParser.AtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#op.
    def visitOp(self, ctx:PeaceParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#EnumExpr.
    def visitEnumExpr(self, ctx:PeaceParser.EnumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#BoolExpr.
    def visitBoolExpr(self, ctx:PeaceParser.BoolExprContext):
        return PeaceType(PeaceParser.Bool, 'bool')


    # Visit a parse tree produced by PeaceParser#IdentExpr.
    def visitIdentExpr(self, ctx:PeaceParser.IdentExprContext):
        if (self.type_environments and
            ctx.Identifier().getText() in self.type_environments[-1]):
            return self.type_environments[-1][ctx.Identifier().getText()]
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#AssignExpr.
    def visitAssignExpr(self, ctx:PeaceParser.AssignExprContext):
        l_type = self.visit(ctx.expression(0))
        r_type = self.visit(ctx.expression(1))
        if (l_type != r_type):
            raise PeaceTypecheckError("Assignment type mismatch: " + l_type.token + " and " + r_type.token)
        return l_type


    # Visit a parse tree produced by PeaceParser#FuncCallExpr.
    def visitFuncCallExpr(self, ctx:PeaceParser.FuncCallExprContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#IfStmt.
    def visitIfStmt(self, ctx:PeaceParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#MatchStmt.
    def visitMatchStmt(self, ctx:PeaceParser.MatchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#ReturnExprStmt.
    def visitReturnExprStmt(self, ctx:PeaceParser.ReturnExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#ReturnStmt.
    def visitReturnStmt(self, ctx:PeaceParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#PrintStmt.
    def visitPrintStmt(self, ctx:PeaceParser.PrintStmtContext):
        return self.visitChildren(ctx)


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