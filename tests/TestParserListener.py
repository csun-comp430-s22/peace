from dataclasses import InitVar
from multiprocessing.pool import INIT
from peace.antlr.generated.PeaceParser import PeaceParser
from peace.antlr.generated.PeaceListener import PeaceListener

class TestListener(PeaceListener):
    def __init__(self):
        self.rules_visited = []

    # Enter a parse tree produced by PeaceParser#basetype.
    def enterBasetype(self, ctx:PeaceParser.BasetypeContext):
        self.rules_visited.append(ctx.getRuleIndex());

    # Exit a parse tree produced by PeaceParser#basetype.
    def exitBasetype(self, ctx:PeaceParser.BasetypeContext):
        self.rules_visited.append(ctx.getRuleIndex());


    # Enter a parse tree produced by PeaceParser#funcpointertype.
    def enterFuncpointertype(self, ctx:PeaceParser.FuncpointertypeContext):
        self.rules_visited.append(ctx.getRuleIndex());

    # Exit a parse tree produced by PeaceParser#funcpointertype.
    def exitFuncpointertype(self, ctx:PeaceParser.FuncpointertypeContext):
        self.rules_visited.append(ctx.getRuleIndex());


    # Enter a parse tree produced by PeaceParser#atype.
    def enterAtype(self, ctx:PeaceParser.AtypeContext):
        self.rules_visited.append(ctx.getRuleIndex());

    # Exit a parse tree produced by PeaceParser#atype.
    def exitAtype(self, ctx:PeaceParser.AtypeContext):
        self.rules_visited.append(ctx.getRuleIndex());


    # Enter a parse tree produced by PeaceParser#expression.
    def enterExpression(self, ctx:PeaceParser.ExpressionContext):
        self.rules_visited.append(ctx.getRuleIndex());

    # Exit a parse tree produced by PeaceParser#expression.
    def exitExpression(self, ctx:PeaceParser.ExpressionContext):
        self.rules_visited.append(ctx.getRuleIndex());


    # Enter a parse tree produced by PeaceParser#vardec.
    def enterVardec(self, ctx:PeaceParser.VardecContext):
        self.rules_visited.append(ctx.getRuleIndex());

    # Exit a parse tree produced by PeaceParser#vardec.
    def exitVardec(self, ctx:PeaceParser.VardecContext):
        self.rules_visited.append(ctx.getRuleIndex());


    # Enter a parse tree produced by PeaceParser#statement.
    def enterStatement(self, ctx:PeaceParser.StatementContext):
        self.rules_visited.append(ctx.getRuleIndex());

    # Exit a parse tree produced by PeaceParser#statement.
    def exitStatement(self, ctx:PeaceParser.StatementContext):
        self.rules_visited.append(ctx.getRuleIndex());


    # Enter a parse tree produced by PeaceParser#case.
    def enterCase_(self, ctx:PeaceParser.Case_Context):
        self.rules_visited.append(ctx.getRuleIndex());

    # Exit a parse tree produced by PeaceParser#case.
    def exitCase_(self, ctx:PeaceParser.Case_Context):
        self.rules_visited.append(ctx.getRuleIndex());


    # Enter a parse tree produced by PeaceParser#pattern.
    def enterPattern(self, ctx:PeaceParser.PatternContext):
        self.rules_visited.append(ctx.getRuleIndex());

    # Exit a parse tree produced by PeaceParser#pattern.
    def exitPattern(self, ctx:PeaceParser.PatternContext):
        self.rules_visited.append(ctx.getRuleIndex());


    # Enter a parse tree produced by PeaceParser#parameter.
    def enterParameter(self, ctx:PeaceParser.ParameterContext):
        self.rules_visited.append(ctx.getRuleIndex());

    # Exit a parse tree produced by PeaceParser#parameter.
    def exitParameter(self, ctx:PeaceParser.ParameterContext):
        self.rules_visited.append(ctx.getRuleIndex());

    """
    # Enter a parse tree produced by PeaceParser#func.
    def enterFunc(self, ctx:PeaceParser.FuncContext):
        self.rules_visited.append(ctx.getRuleIndex());

    # Exit a parse tree produced by PeaceParser#func.
    def exitFunc(self, ctx:PeaceParser.FuncContext):
        self.rules_visited.append(ctx.getRuleIndex());
    """


    # Enter a parse tree produced by PeaceParser#enumdef.
    def enterEnumdef(self, ctx:PeaceParser.EnumdefContext):
        self.rules_visited.append(ctx.getRuleIndex());

    # Exit a parse tree produced by PeaceParser#enumdef.
    def exitEnumdef(self, ctx:PeaceParser.EnumdefContext):
        self.rules_visited.append(ctx.getRuleIndex());

    # Enter a parse tree produced by PeaceParser#cdef.
    def enterCdef(self, ctx:PeaceParser.CdefContext):
        self.rules_visited.append(ctx.getRuleIndex());

    # Exit a parse tree produced by PeaceParser#cdef.
    def exitCdef(self, ctx:PeaceParser.CdefContext):
        self.rules_visited.append(ctx.getRuleIndex());

    # Enter a parse tree produced by PeaceParser#program.
    def enterProgram(self, ctx:PeaceParser.ProgramContext):
        self.rules_visited.append(ctx.getRuleIndex());

    # Exit a parse tree produced by PeaceParser#program.
    def exitProgram(self, ctx:PeaceParser.ProgramContext):
        self.rules_visited.append(ctx.getRuleIndex());