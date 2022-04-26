from antlr.generated.PeaceParser import PeaceParser
from antlr.generated.PeaceListener import PeaceListener

class PeaceTypecheckError(Exception):
    def __init__(self, message):
        self.message = message

class PeaceTypechecker(PeaceListener):
    def __init__(self) -> None:
        super().__init__()

    # Enter a parse tree produced by PeaceParser#ArithmeticExpr.
    def exitArithmeticExpr(self, ctx:PeaceParser.ArithmeticExprContext):
        print(ctx.op().getType())


    # Enter a parse tree produced by PeaceParser#DigitExpr.
    def exitDigitExpr(self, ctx:PeaceParser.DigitExprContext):
        pass

    # Enter a parse tree produced by PeaceParser#IdentExpr.
    def exitIdentExpr(self, ctx:PeaceParser.IdentExprContext):
        ctx.getToken().toString()

        
