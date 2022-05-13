from __future__ import unicode_literals
import sys
import os
from unicodedata import name
import unittest
from antlr4 import *
from antlr4.tree.Trees import Trees
from pyparsing import ParseSyntaxException

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from antlr.generated.PeaceLexer import PeaceLexer
from antlr.generated.PeaceParser import PeaceParser
from antlr.generated.PeaceListener import PeaceListener
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
        3.0 * 100.0
        """
        parser = create_parser_for(test_input)
        tree = parser.expression()
        typecheck_tree(tree)

    def test_arithmetic_expression_mixed(self):
        test_input = """
        2 / 10.9
        """
        parser = create_parser_for(test_input)
        tree = parser.expression()
        typecheck_tree(tree)

    def test_arithmetic_expression_invalid(self):
        test_input = """
        2 % true
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

    def test_invalid_assign(self):
        test_input = """
        {
            let a: int = true;
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        with self.assertRaises(PeaceTypecheckError):
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


    def test_case(self):
        print('testing case:\n')
        test_input = 'void main() { let x: int = 4; match x { 4 => x = true } }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        typecheck_tree(tree)

    def test_param(self):
        print('testing param:\n')
        test_input = 'someVar: string'
        parser = create_parser_for(test_input)
        tree = parser.parameter()
        typecheck_tree(tree)

    def test_func_stmt(self):
        print('testing funcstmt:\n')
        test_input = 'void main(var: string, num: int) { print(ok); }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        typecheck_tree(tree)

    def test_func_stmt_invalid_dup(self):
        print('testing funcstmt invalid:\n')
        test_input = 'void main() { print(ok); } void main() { print (uh); }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_cdef(self):
        print('testing cdef:\n')
        test_input = 'enum nums { one: int; } void main() { }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        typecheck_tree(tree)

    def test_cdef_invalid_dup(self):
        print('testing cdef invalid:\n')
        test_input = 'enum nums { one: int; one: int;} void main() { }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_enumdef(self):
        print('testing enumdef:\n')
        test_input = 'enum nums { one: int; } void main() { }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        typecheck_tree(tree)

    def test_enumdef_invalid_dup(self):
        print('testing enumdef invalid:\n')
        test_input = 'enum nums { one: int; } enum nums { two: int; } void main() { }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_program(self):
        print('testing program:\n')
        test_input = 'enum anEnum { someNum: int; } int addTwo() { let c: int = 2 + 2; return c; }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        typecheck_tree(tree)

if __name__ == '__main__':
    unittest.main()
    