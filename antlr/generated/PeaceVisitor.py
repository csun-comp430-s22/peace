# Generated from c:\Users\nick\Documents\CSUN\COMP430\peace\antlr\Peace.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PeaceParser import PeaceParser
else:
    from PeaceParser import PeaceParser

# This class defines a complete generic visitor for a parse tree produced by PeaceParser.

class PeaceVisitor(ParseTreeVisitor):

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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#IdentExpr.
    def visitIdentExpr(self, ctx:PeaceParser.IdentExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#FloatExpr.
    def visitFloatExpr(self, ctx:PeaceParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#ArithmeticExpr.
    def visitArithmeticExpr(self, ctx:PeaceParser.ArithmeticExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#DigitExpr.
    def visitDigitExpr(self, ctx:PeaceParser.DigitExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#CompExpr.
    def visitCompExpr(self, ctx:PeaceParser.CompExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#FuncPointCreateExpr.
    def visitFuncPointCreateExpr(self, ctx:PeaceParser.FuncPointCreateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#AssignExpr.
    def visitAssignExpr(self, ctx:PeaceParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#FuncCallExpr.
    def visitFuncCallExpr(self, ctx:PeaceParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#vardec.
    def visitVardec(self, ctx:PeaceParser.VardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#ExprStmt.
    def visitExprStmt(self, ctx:PeaceParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeaceParser#VarDecStmt.
    def visitVarDecStmt(self, ctx:PeaceParser.VarDecStmtContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)


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



del PeaceParser