# Generated from c:\Users\nick\Documents\CSUN\COMP430\peace\peace\antlr\Peace.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PeaceParser import PeaceParser
else:
    from PeaceParser import PeaceParser

# This class defines a complete listener for a parse tree produced by PeaceParser.
class PeaceListener(ParseTreeListener):

    # Enter a parse tree produced by PeaceParser#basetype.
    def enterBasetype(self, ctx:PeaceParser.BasetypeContext):
        pass

    # Exit a parse tree produced by PeaceParser#basetype.
    def exitBasetype(self, ctx:PeaceParser.BasetypeContext):
        pass


    # Enter a parse tree produced by PeaceParser#funcpointertype.
    def enterFuncpointertype(self, ctx:PeaceParser.FuncpointertypeContext):
        pass

    # Exit a parse tree produced by PeaceParser#funcpointertype.
    def exitFuncpointertype(self, ctx:PeaceParser.FuncpointertypeContext):
        pass


    # Enter a parse tree produced by PeaceParser#atype.
    def enterAtype(self, ctx:PeaceParser.AtypeContext):
        pass

    # Exit a parse tree produced by PeaceParser#atype.
    def exitAtype(self, ctx:PeaceParser.AtypeContext):
        pass


    # Enter a parse tree produced by PeaceParser#op.
    def enterOp(self, ctx:PeaceParser.OpContext):
        pass

    # Exit a parse tree produced by PeaceParser#op.
    def exitOp(self, ctx:PeaceParser.OpContext):
        pass


    # Enter a parse tree produced by PeaceParser#BoolExpr.
    def enterBoolExpr(self, ctx:PeaceParser.BoolExprContext):
        pass

    # Exit a parse tree produced by PeaceParser#BoolExpr.
    def exitBoolExpr(self, ctx:PeaceParser.BoolExprContext):
        pass


    # Enter a parse tree produced by PeaceParser#IdentExpr.
    def enterIdentExpr(self, ctx:PeaceParser.IdentExprContext):
        pass

    # Exit a parse tree produced by PeaceParser#IdentExpr.
    def exitIdentExpr(self, ctx:PeaceParser.IdentExprContext):
        pass


    # Enter a parse tree produced by PeaceParser#FloatExpr.
    def enterFloatExpr(self, ctx:PeaceParser.FloatExprContext):
        pass

    # Exit a parse tree produced by PeaceParser#FloatExpr.
    def exitFloatExpr(self, ctx:PeaceParser.FloatExprContext):
        pass


    # Enter a parse tree produced by PeaceParser#ArithmeticExpr.
    def enterArithmeticExpr(self, ctx:PeaceParser.ArithmeticExprContext):
        pass

    # Exit a parse tree produced by PeaceParser#ArithmeticExpr.
    def exitArithmeticExpr(self, ctx:PeaceParser.ArithmeticExprContext):
        pass


    # Enter a parse tree produced by PeaceParser#StringLiteralExpr.
    def enterStringLiteralExpr(self, ctx:PeaceParser.StringLiteralExprContext):
        pass

    # Exit a parse tree produced by PeaceParser#StringLiteralExpr.
    def exitStringLiteralExpr(self, ctx:PeaceParser.StringLiteralExprContext):
        pass


    # Enter a parse tree produced by PeaceParser#DigitExpr.
    def enterDigitExpr(self, ctx:PeaceParser.DigitExprContext):
        pass

    # Exit a parse tree produced by PeaceParser#DigitExpr.
    def exitDigitExpr(self, ctx:PeaceParser.DigitExprContext):
        pass


    # Enter a parse tree produced by PeaceParser#CompExpr.
    def enterCompExpr(self, ctx:PeaceParser.CompExprContext):
        pass

    # Exit a parse tree produced by PeaceParser#CompExpr.
    def exitCompExpr(self, ctx:PeaceParser.CompExprContext):
        pass


    # Enter a parse tree produced by PeaceParser#FuncPointCreateExpr.
    def enterFuncPointCreateExpr(self, ctx:PeaceParser.FuncPointCreateExprContext):
        pass

    # Exit a parse tree produced by PeaceParser#FuncPointCreateExpr.
    def exitFuncPointCreateExpr(self, ctx:PeaceParser.FuncPointCreateExprContext):
        pass


    # Enter a parse tree produced by PeaceParser#FuncCallOrEnumExpr.
    def enterFuncCallOrEnumExpr(self, ctx:PeaceParser.FuncCallOrEnumExprContext):
        pass

    # Exit a parse tree produced by PeaceParser#FuncCallOrEnumExpr.
    def exitFuncCallOrEnumExpr(self, ctx:PeaceParser.FuncCallOrEnumExprContext):
        pass


    # Enter a parse tree produced by PeaceParser#AssignExpr.
    def enterAssignExpr(self, ctx:PeaceParser.AssignExprContext):
        pass

    # Exit a parse tree produced by PeaceParser#AssignExpr.
    def exitAssignExpr(self, ctx:PeaceParser.AssignExprContext):
        pass


    # Enter a parse tree produced by PeaceParser#vardec.
    def enterVardec(self, ctx:PeaceParser.VardecContext):
        pass

    # Exit a parse tree produced by PeaceParser#vardec.
    def exitVardec(self, ctx:PeaceParser.VardecContext):
        pass


    # Enter a parse tree produced by PeaceParser#ExprStmt.
    def enterExprStmt(self, ctx:PeaceParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by PeaceParser#ExprStmt.
    def exitExprStmt(self, ctx:PeaceParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by PeaceParser#VarDecStmt.
    def enterVarDecStmt(self, ctx:PeaceParser.VarDecStmtContext):
        pass

    # Exit a parse tree produced by PeaceParser#VarDecStmt.
    def exitVarDecStmt(self, ctx:PeaceParser.VarDecStmtContext):
        pass


    # Enter a parse tree produced by PeaceParser#WhileStmt.
    def enterWhileStmt(self, ctx:PeaceParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by PeaceParser#WhileStmt.
    def exitWhileStmt(self, ctx:PeaceParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by PeaceParser#IfStmt.
    def enterIfStmt(self, ctx:PeaceParser.IfStmtContext):
        pass

    # Exit a parse tree produced by PeaceParser#IfStmt.
    def exitIfStmt(self, ctx:PeaceParser.IfStmtContext):
        pass


    # Enter a parse tree produced by PeaceParser#MatchStmt.
    def enterMatchStmt(self, ctx:PeaceParser.MatchStmtContext):
        pass

    # Exit a parse tree produced by PeaceParser#MatchStmt.
    def exitMatchStmt(self, ctx:PeaceParser.MatchStmtContext):
        pass


    # Enter a parse tree produced by PeaceParser#ReturnExprStmt.
    def enterReturnExprStmt(self, ctx:PeaceParser.ReturnExprStmtContext):
        pass

    # Exit a parse tree produced by PeaceParser#ReturnExprStmt.
    def exitReturnExprStmt(self, ctx:PeaceParser.ReturnExprStmtContext):
        pass


    # Enter a parse tree produced by PeaceParser#ReturnStmt.
    def enterReturnStmt(self, ctx:PeaceParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by PeaceParser#ReturnStmt.
    def exitReturnStmt(self, ctx:PeaceParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by PeaceParser#PrintStmt.
    def enterPrintStmt(self, ctx:PeaceParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by PeaceParser#PrintStmt.
    def exitPrintStmt(self, ctx:PeaceParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by PeaceParser#block.
    def enterBlock(self, ctx:PeaceParser.BlockContext):
        pass

    # Exit a parse tree produced by PeaceParser#block.
    def exitBlock(self, ctx:PeaceParser.BlockContext):
        pass


    # Enter a parse tree produced by PeaceParser#case_.
    def enterCase_(self, ctx:PeaceParser.Case_Context):
        pass

    # Exit a parse tree produced by PeaceParser#case_.
    def exitCase_(self, ctx:PeaceParser.Case_Context):
        pass


    # Enter a parse tree produced by PeaceParser#DigitPattern.
    def enterDigitPattern(self, ctx:PeaceParser.DigitPatternContext):
        pass

    # Exit a parse tree produced by PeaceParser#DigitPattern.
    def exitDigitPattern(self, ctx:PeaceParser.DigitPatternContext):
        pass


    # Enter a parse tree produced by PeaceParser#FloatPattern.
    def enterFloatPattern(self, ctx:PeaceParser.FloatPatternContext):
        pass

    # Exit a parse tree produced by PeaceParser#FloatPattern.
    def exitFloatPattern(self, ctx:PeaceParser.FloatPatternContext):
        pass


    # Enter a parse tree produced by PeaceParser#StringPattern.
    def enterStringPattern(self, ctx:PeaceParser.StringPatternContext):
        pass

    # Exit a parse tree produced by PeaceParser#StringPattern.
    def exitStringPattern(self, ctx:PeaceParser.StringPatternContext):
        pass


    # Enter a parse tree produced by PeaceParser#IdentifierPattern.
    def enterIdentifierPattern(self, ctx:PeaceParser.IdentifierPatternContext):
        pass

    # Exit a parse tree produced by PeaceParser#IdentifierPattern.
    def exitIdentifierPattern(self, ctx:PeaceParser.IdentifierPatternContext):
        pass


    # Enter a parse tree produced by PeaceParser#AnyPattern.
    def enterAnyPattern(self, ctx:PeaceParser.AnyPatternContext):
        pass

    # Exit a parse tree produced by PeaceParser#AnyPattern.
    def exitAnyPattern(self, ctx:PeaceParser.AnyPatternContext):
        pass


    # Enter a parse tree produced by PeaceParser#ConstructorPattern.
    def enterConstructorPattern(self, ctx:PeaceParser.ConstructorPatternContext):
        pass

    # Exit a parse tree produced by PeaceParser#ConstructorPattern.
    def exitConstructorPattern(self, ctx:PeaceParser.ConstructorPatternContext):
        pass


    # Enter a parse tree produced by PeaceParser#parameter.
    def enterParameter(self, ctx:PeaceParser.ParameterContext):
        pass

    # Exit a parse tree produced by PeaceParser#parameter.
    def exitParameter(self, ctx:PeaceParser.ParameterContext):
        pass


    # Enter a parse tree produced by PeaceParser#func_stmt.
    def enterFunc_stmt(self, ctx:PeaceParser.Func_stmtContext):
        pass

    # Exit a parse tree produced by PeaceParser#func_stmt.
    def exitFunc_stmt(self, ctx:PeaceParser.Func_stmtContext):
        pass


    # Enter a parse tree produced by PeaceParser#cdef.
    def enterCdef(self, ctx:PeaceParser.CdefContext):
        pass

    # Exit a parse tree produced by PeaceParser#cdef.
    def exitCdef(self, ctx:PeaceParser.CdefContext):
        pass


    # Enter a parse tree produced by PeaceParser#enumdef.
    def enterEnumdef(self, ctx:PeaceParser.EnumdefContext):
        pass

    # Exit a parse tree produced by PeaceParser#enumdef.
    def exitEnumdef(self, ctx:PeaceParser.EnumdefContext):
        pass


    # Enter a parse tree produced by PeaceParser#program.
    def enterProgram(self, ctx:PeaceParser.ProgramContext):
        pass

    # Exit a parse tree produced by PeaceParser#program.
    def exitProgram(self, ctx:PeaceParser.ProgramContext):
        pass



del PeaceParser