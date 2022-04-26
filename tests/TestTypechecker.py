from __future__ import unicode_literals
import sys
import os
import unittest
from antlr4 import *
from antlr4.tree.Trees import Trees

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from antlr.generated.PeaceLexer import PeaceLexer
from antlr.generated.PeaceParser import PeaceParser
from typechecker import PeaceTypechecker

from TestParserListener import TestListener

# TEST HELPER FUNCTION
def create_parser_for(input):
    input_stream = InputStream(input)
    lexer = PeaceLexer(input_stream)
    stream = CommonTokenStream(lexer)
    return PeaceParser(stream)

def parser_test(tree):
    listener = PeaceTypechecker()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.rules_visited

class TestParser(unittest.TestCase):
    def test_arithmetic_expression(self):
        test_input = """
enum foo {
    int bar,
    int baz
}

void main() {
    
}
        """
        tree_expected = ''
        parser = create_parser_for(test_input)
        tree = parser.program()
        #assert(tree_expected == tree_actual)

if __name__ == '__main__':
    unittest.main()
    