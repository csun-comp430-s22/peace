from __future__ import unicode_literals
import sys
import os
import unittest
from antlr4 import *

sys.path.append(os.path.dirname(__file__) + "/../")
from antlr.generated.PeaceLexer import PeaceLexer
from antlr.generated.PeaceParser import PeaceParser
from antlr.generated.PeaceListener import PeaceListener

from TestParserListener import TestListener

# TEST HELPER FUNCTION
def create_parser_for(input):
    input_stream = InputStream(input)
    lexer = PeaceLexer(input_stream)
    stream = CommonTokenStream(lexer)
    return PeaceParser(stream)

def parser_test(tree):
    listener = TestListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.rules_visited

class TestParser(unittest.TestCase):
    
    # SAMPLE TEST
    def test_var_declare(self):
        test_input = "let x: int = 20;"
        test_expected_rules = [PeaceParser.RULE_statement,
                               PeaceParser.RULE_vardec,
                               PeaceParser.RULE_atype,
                               PeaceParser.RULE_basetype,
                               PeaceParser.RULE_basetype,
                               PeaceParser.RULE_atype,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_vardec, 
                               PeaceParser.RULE_statement] 
        parser = create_parser_for(test_input)
        tree = parser.statement()
        rules_visited = parser_test(tree)
        assert(rules_visited == test_expected_rules)
    
if __name__ == '__main__':
    unittest.main()