# Generated from d:\Github\Peace\antlr\Peace.g4 by ANTLR 4.8
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


    # Enter a parse tree produced by PeaceParser#expression.
    def enterExpression(self, ctx:PeaceParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PeaceParser#expression.
    def exitExpression(self, ctx:PeaceParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PeaceParser#vardec.
    def enterVardec(self, ctx:PeaceParser.VardecContext):
        pass

    # Exit a parse tree produced by PeaceParser#vardec.
    def exitVardec(self, ctx:PeaceParser.VardecContext):
        pass


    # Enter a parse tree produced by PeaceParser#statement.
    def enterStatement(self, ctx:PeaceParser.StatementContext):
        pass

    # Exit a parse tree produced by PeaceParser#statement.
    def exitStatement(self, ctx:PeaceParser.StatementContext):
        pass


    # Enter a parse tree produced by PeaceParser#return_stmt.
    def enterReturn_stmt(self, ctx:PeaceParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by PeaceParser#return_stmt.
    def exitReturn_stmt(self, ctx:PeaceParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by PeaceParser#return_nothing.
    def enterReturn_nothing(self, ctx:PeaceParser.Return_nothingContext):
        pass

    # Exit a parse tree produced by PeaceParser#return_nothing.
    def exitReturn_nothing(self, ctx:PeaceParser.Return_nothingContext):
        pass


    # Enter a parse tree produced by PeaceParser#return_exp.
    def enterReturn_exp(self, ctx:PeaceParser.Return_expContext):
        pass

    # Exit a parse tree produced by PeaceParser#return_exp.
    def exitReturn_exp(self, ctx:PeaceParser.Return_expContext):
        pass


    # Enter a parse tree produced by PeaceParser#print_stmt.
    def enterPrint_stmt(self, ctx:PeaceParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by PeaceParser#print_stmt.
    def exitPrint_stmt(self, ctx:PeaceParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by PeaceParser#match_stmt.
    def enterMatch_stmt(self, ctx:PeaceParser.Match_stmtContext):
        pass

    # Exit a parse tree produced by PeaceParser#match_stmt.
    def exitMatch_stmt(self, ctx:PeaceParser.Match_stmtContext):
        pass


    # Enter a parse tree produced by PeaceParser#func_call.
    def enterFunc_call(self, ctx:PeaceParser.Func_callContext):
        pass

    # Exit a parse tree produced by PeaceParser#func_call.
    def exitFunc_call(self, ctx:PeaceParser.Func_callContext):
        pass


    # Enter a parse tree produced by PeaceParser#match_case.
    def enterMatch_case(self, ctx:PeaceParser.Match_caseContext):
        pass

    # Exit a parse tree produced by PeaceParser#match_case.
    def exitMatch_case(self, ctx:PeaceParser.Match_caseContext):
        pass


    # Enter a parse tree produced by PeaceParser#match_pattern.
    def enterMatch_pattern(self, ctx:PeaceParser.Match_patternContext):
        pass

    # Exit a parse tree produced by PeaceParser#match_pattern.
    def exitMatch_pattern(self, ctx:PeaceParser.Match_patternContext):
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