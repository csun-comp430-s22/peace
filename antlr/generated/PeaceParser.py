# Generated from c:\Users\nick\Documents\CSUN\COMP430\peace\antlr\Peace.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-")
        buf.write("\37\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5")
        buf.write("\2\17\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\32\n")
        buf.write("\3\f\3\16\3\35\13\3\3\3\2\3\4\4\2\4\2\4\3\2\b\f\3\2\r")
        buf.write("\20\2\37\2\16\3\2\2\2\4\20\3\2\2\2\6\7\5\4\3\2\7\b\7#")
        buf.write("\2\2\b\17\3\2\2\2\t\n\7+\2\2\n\13\7 \2\2\13\f\5\4\3\2")
        buf.write("\f\r\7#\2\2\r\17\3\2\2\2\16\6\3\2\2\2\16\t\3\2\2\2\17")
        buf.write("\3\3\2\2\2\20\21\b\3\1\2\21\22\7+\2\2\22\33\3\2\2\2\23")
        buf.write("\24\f\5\2\2\24\25\t\2\2\2\25\32\5\4\3\6\26\27\f\4\2\2")
        buf.write("\27\30\t\3\2\2\30\32\5\4\3\5\31\23\3\2\2\2\31\26\3\2\2")
        buf.write("\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\5\3\2")
        buf.write("\2\2\35\33\3\2\2\2\5\16\31\33")
        return buf.getvalue()


class PeaceParser ( Parser ):

    grammarFileName = "Peace.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'bool'", "'void'", 
                     "'string'", "'+'", "'-'", "'*'", "'/'", "'%'", "'<'", 
                     "'>'", "'<='", "'>='", "'=='", "'!='", "'let'", "'true'", 
                     "'false'", "'->'", "'while'", "'if'", "'else'", "'return'", 
                     "'func'", "'print'", "'match'", "'=>'", "'_'", "'='", 
                     "'&'", "':'", "';'", "'('", "')'", "'{'", "'}'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "Int", "Float", "Bool", "Void", "String", 
                      "Add", "Subtract", "Multiply", "Divide", "Modulo", 
                      "LessThan", "GreaterThan", "LessThanOrEq", "GreaterThanOrEq", 
                      "Equal", "NotEqual", "Let", "BoolTrue", "BoolFalse", 
                      "Arrow", "While", "If", "Else", "Return", "Function", 
                      "Print", "Match", "MatchArrow", "Any", "Assign", "Amp", 
                      "Colon", "Semicolon", "LParen", "RParen", "LBracket", 
                      "RBracket", "DoubleQuote", "WS", "Newline", "Identifier", 
                      "Digits", "FloatConst" ]

    RULE_statement = 0
    RULE_expression = 1

    ruleNames =  [ "statement", "expression" ]

    EOF = Token.EOF
    Int=1
    Float=2
    Bool=3
    Void=4
    String=5
    Add=6
    Subtract=7
    Multiply=8
    Divide=9
    Modulo=10
    LessThan=11
    GreaterThan=12
    LessThanOrEq=13
    GreaterThanOrEq=14
    Equal=15
    NotEqual=16
    Let=17
    BoolTrue=18
    BoolFalse=19
    Arrow=20
    While=21
    If=22
    Else=23
    Return=24
    Function=25
    Print=26
    Match=27
    MatchArrow=28
    Any=29
    Assign=30
    Amp=31
    Colon=32
    Semicolon=33
    LParen=34
    RParen=35
    LBracket=36
    RBracket=37
    DoubleQuote=38
    WS=39
    Newline=40
    Identifier=41
    Digits=42
    FloatConst=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PeaceParser.ExpressionContext,0)


        def Semicolon(self):
            return self.getToken(PeaceParser.Semicolon, 0)

        def Identifier(self):
            return self.getToken(PeaceParser.Identifier, 0)

        def Assign(self):
            return self.getToken(PeaceParser.Assign, 0)

        def getRuleIndex(self):
            return PeaceParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PeaceParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_statement)
        try:
            self.state = 12
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.expression(0)
                self.state = 5
                self.match(PeaceParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.match(PeaceParser.Identifier)
                self.state = 8
                self.match(PeaceParser.Assign)
                self.state = 9
                self.expression(0)
                self.state = 10
                self.match(PeaceParser.Semicolon)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(PeaceParser.Identifier, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PeaceParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PeaceParser.ExpressionContext,i)


        def Add(self):
            return self.getToken(PeaceParser.Add, 0)

        def Subtract(self):
            return self.getToken(PeaceParser.Subtract, 0)

        def Multiply(self):
            return self.getToken(PeaceParser.Multiply, 0)

        def Divide(self):
            return self.getToken(PeaceParser.Divide, 0)

        def Modulo(self):
            return self.getToken(PeaceParser.Modulo, 0)

        def LessThan(self):
            return self.getToken(PeaceParser.LessThan, 0)

        def GreaterThan(self):
            return self.getToken(PeaceParser.GreaterThan, 0)

        def LessThanOrEq(self):
            return self.getToken(PeaceParser.LessThanOrEq, 0)

        def GreaterThanOrEq(self):
            return self.getToken(PeaceParser.GreaterThanOrEq, 0)

        def getRuleIndex(self):
            return PeaceParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PeaceParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(PeaceParser.Identifier)
            self._ctx.stop = self._input.LT(-1)
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 23
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = PeaceParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 17
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 18
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PeaceParser.Add) | (1 << PeaceParser.Subtract) | (1 << PeaceParser.Multiply) | (1 << PeaceParser.Divide) | (1 << PeaceParser.Modulo))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 19
                        self.expression(4)
                        pass

                    elif la_ == 2:
                        localctx = PeaceParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 20
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 21
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PeaceParser.LessThan) | (1 << PeaceParser.GreaterThan) | (1 << PeaceParser.LessThanOrEq) | (1 << PeaceParser.GreaterThanOrEq))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 22
                        self.expression(3)
                        pass

             
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




