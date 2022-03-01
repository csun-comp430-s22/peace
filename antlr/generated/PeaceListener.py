# Generated from c:\Users\nick\Documents\CSUN\COMP430\peace\antlr\Peace.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PeaceParser import PeaceParser
else:
    from PeaceParser import PeaceParser

# This class defines a complete listener for a parse tree produced by PeaceParser.
class PeaceListener(ParseTreeListener):

    # Enter a parse tree produced by PeaceParser#statement.
    def enterStatement(self, ctx:PeaceParser.StatementContext):
        pass

    # Exit a parse tree produced by PeaceParser#statement.
    def exitStatement(self, ctx:PeaceParser.StatementContext):
        pass


    # Enter a parse tree produced by PeaceParser#expression.
    def enterExpression(self, ctx:PeaceParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PeaceParser#expression.
    def exitExpression(self, ctx:PeaceParser.ExpressionContext):
        pass



del PeaceParser