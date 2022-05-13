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
    
    def test_WhileStmt(self):
        test_input = """
        {
            let x: int = 0;
            let y: int = 1;
            while (x < 1) { y = 2; }
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        typecheck_tree(tree)

    def test_WhileStmt_invalid(self):
        test_input = """
        {
             let y: int = 0;
            let x: bool = true;
            while (x < 1) { y = 2; }
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_IfStmt(self):
        test_input = """
        {
            let x: int = 2;
            let y: int = 1;
            let baz: int = 1;
            let foo: int = 2;
            let bar: int = 1;
            if (foo >= bar) { baz = x; }
            if (foo <= bar) { baz = x; } else { baz = y; }
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        typecheck_tree(tree)

    def test_IfStmt_invalid(self):
        test_input = """
        {
            let x: int = 2;
            let y: int = 1;
            let baz: int = 1;
            let foo: bool = true;
            let bar: int = 1;
            if (foo >= bar) { baz = x; }
            if (foo <= bar) { baz = x; } else { baz = y; }
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_MatchStmt(self):
        test_input = """
        {
            let x: int = 3;
            let y: int = 1;
            match bar { x => y = x, 2 => y = x };
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        typecheck_tree(tree)

    def test_MatchStmt_invalid(self): #how to make invalid
        test_input = """
        {
            let x: bool = false;
            let y: int = 1;
            match bar { x => y = x, 2 => y = x };
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_ReturnStmt(self):
        test_input = """
        {
            let a: int = 1;
            let b: int = 1;
            if(a > b) { return; }
            else { return; }
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        typecheck_tree(tree)

    def test_ReturnStmt_invalid(self): #how to make invalid
        test_input = """
        {
            let a: int = 1;
            let b: int = 1;
            if(a > b) { return; }
            else { return; }
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_ReturnExprStmt(self):
        test_input = """
        {
            let a: int = 2;
            let b: int = 1;
            if(a > b) { return a; }
            else { return a; }
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        typecheck_tree(tree)

    def test_ReturnExprStmt_invalid(self): #how to make invalid
        test_input = """
        {
            let a: int = 2;
            let b: int = 1;
            if(a > b) { return y; }
            else { return y; }
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)


    def test_PrintStmt(self):
        test_input = """
        {
            let a: int = 1;
            print( a );
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        typecheck_tree(tree)

    def test_PrintStmt_invalid(self): #how to make invalid
        test_input = """
        {
            print( a );
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    

if __name__ == '__main__':
    unittest.main()
    