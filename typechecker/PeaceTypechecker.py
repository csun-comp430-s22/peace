from antlr.generated.PeaceParser import PeaceParser
from antlr.generated.PeaceListener import PeaceListener

class PeaceTypecheckError(Exception):
    def __init__(self, message):
        self.message = message

class PeaceTypechecker(PeaceListener):
    def __init__(self) -> None:
        super().__init__()

    # Enter a parse tree produced by PeaceParser#ArithmeticExpr.
    def enterArithmeticExpr(self, ctx:PeaceParser.ArithmeticExprContext):
        print(ctx.op().getType())

    # Exit a parse tree produced by PeaceParser#ArithmeticExpr.
    def exitArithmeticExpr(self, ctx:PeaceParser.ArithmeticExprContext):
        pass
