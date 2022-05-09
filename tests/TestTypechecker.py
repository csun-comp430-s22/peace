from __future__ import unicode_literals
import sys
import os
import unittest
from antlr4 import *
from antlr4.tree.Trees import Trees

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from antlr.generated.PeaceLexer import PeaceLexer
from antlr.generated.PeaceParser import PeaceParser
from typechecker.PeaceTypechecker import PeaceTypechecker, PeaceTypecheckError

from TestParserListener import TestListener

# TEST HELPER FUNCTION
def create_parser_for(input):
    input_stream = InputStream(input)
    lexer = PeaceLexer(input_stream)
    stream = CommonTokenStream(lexer)
    return PeaceParser(stream)

def typecheck_tree(tree):
    visitor = PeaceTypechecker()
    visitor.visit(tree)

class TestParser(unittest.TestCase):
    def test_arithmetic_expression_ints(self):
        test_input = """
        1 + 2
        """
        parser = create_parser_for(test_input)
        tree = parser.expression()
        typecheck_tree(tree)

    def test_arithmetic_expression_floats(self):
        test_input = """
        3.0 + 100.0
        """
        parser = create_parser_for(test_input)
        tree = parser.expression()
        typecheck_tree(tree)

    def test_arithmetic_expression_mixed(self):
        test_input = """
        2 + 10.9
        """
        parser = create_parser_for(test_input)
        tree = parser.expression()
        typecheck_tree(tree)

    def test_arithmetic_expression_invalid(self):
        test_input = """
        2 + true
        """
        parser = create_parser_for(test_input)
        tree = parser.expression()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_assign_arithmetic_expression(self):
        test_input = """
        {
            let a: int = 1;
            let b: int = a + 2;
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        typecheck_tree(tree)

    def test_comparison_expression_ints(self):
        test_input = """
        1 > 2
        """
        parser = create_parser_for(test_input)
        tree = parser.expression()
        typecheck_tree(tree)

    def test_comparison_expression_floats(self):
        test_input = """
        1.9 < 2.1
        """
        parser = create_parser_for(test_input)
        tree = parser.expression()
        typecheck_tree(tree)

    def test_comparison_expression_mixed(self):
        test_input = """
        6 >= 2
        """
        parser = create_parser_for(test_input)
        tree = parser.expression()
        typecheck_tree(tree)

    def test_comparison_expression_invalid(self):
        test_input = """
        foo <= 2
        """
        parser = create_parser_for(test_input)
        tree = parser.expression()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_assign(self):
        test_input = """
        {
            let a: int = 1;
            a = 2;
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        typecheck_tree(tree)

    def test_assign_invalid(self):
        test_input = """
        {
            let a: bool = false;
            a = 3.14;
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

if __name__ == '__main__':
    unittest.main()
    