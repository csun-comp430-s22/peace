# Generated from c:\Users\nick\Documents\CSUN\COMP430\peace\antlr\Peace.g4 by ANTLR 4.8
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


    # Enter a parse tree produced by PeaceParser#case.
    def enterCase(self, ctx:PeaceParser.CaseContext):
        pass

    # Exit a parse tree produced by PeaceParser#case.
    def exitCase(self, ctx:PeaceParser.CaseContext):
        pass


    # Enter a parse tree produced by PeaceParser#pattern.
    def enterPattern(self, ctx:PeaceParser.PatternContext):
        pass

    # Exit a parse tree produced by PeaceParser#pattern.
    def exitPattern(self, ctx:PeaceParser.PatternContext):
        pass


    # Enter a parse tree produced by PeaceParser#parameter.
    def enterParameter(self, ctx:PeaceParser.ParameterContext):
        pass

    # Exit a parse tree produced by PeaceParser#parameter.
    def exitParameter(self, ctx:PeaceParser.ParameterContext):
        pass


    # Enter a parse tree produced by PeaceParser#func.
    def enterFunc(self, ctx:PeaceParser.FuncContext):
        pass

    # Exit a parse tree produced by PeaceParser#func.
    def exitFunc(self, ctx:PeaceParser.FuncContext):
        pass


    # Enter a parse tree produced by PeaceParser#enumdef.
    def enterEnumdef(self, ctx:PeaceParser.EnumdefContext):
        pass

    # Exit a parse tree produced by PeaceParser#enumdef.
    def exitEnumdef(self, ctx:PeaceParser.EnumdefContext):
        pass


    # Enter a parse tree produced by PeaceParser#cdef.
    def enterCdef(self, ctx:PeaceParser.CdefContext):
        pass

    # Exit a parse tree produced by PeaceParser#cdef.
    def exitCdef(self, ctx:PeaceParser.CdefContext):
        pass


    # Enter a parse tree produced by PeaceParser#program.
    def enterProgram(self, ctx:PeaceParser.ProgramContext):
        pass

    # Exit a parse tree produced by PeaceParser#program.
    def exitProgram(self, ctx:PeaceParser.ProgramContext):
        pass



del PeaceParser