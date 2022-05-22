import sys
import os
import unittest
from antlr4 import *
from antlr4.tree.Trees import Trees

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from peace.antlr.generated.PeaceLexer import PeaceLexer
from peace.antlr.generated.PeaceParser import PeaceParser
from peace.typechecker.PeaceTypechecker import PeaceTypechecker, PeaceTypecheckError

# TEST HELPER FUNCTION
def create_parser_for(input):
    input_stream = InputStream(input)
    lexer = PeaceLexer(input_stream)
    stream = CommonTokenStream(lexer)
    return PeaceParser(stream)

def typecheck_tree(tree):
    visitor = PeaceTypechecker()
    visitor.visit(tree)

class TestTypechecker(unittest.TestCase):
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

    def test_arithmetic_expression_left_invalid(self):
        test_input = """
        false % 3.14
        """
        parser = create_parser_for(test_input)
        tree = parser.expression()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_arithmetic_expression_right_invalid(self):
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

    def test_comparison_expression_left_invalid(self):
        test_input = """
        foo <= 2
        """
        parser = create_parser_for(test_input)
        tree = parser.expression()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_comparison_expression_right_invalid(self):
        test_input = """
        5 <= "5"
        """
        parser = create_parser_for(test_input)
        tree = parser.expression()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_comparison_expression_equal_invalid(self):
        test_input = """
        foo == 2
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
        enum ColorType {
            RGB8: int, int, int;
            RGBA8: int, int, int, int;
            HSVF: float, float, float; 
        }

        void main()
        {
            let darkgreen: ColorType = RGB8(128, 128, 128);
            let sum: int = 0;
            match darkgreen {
                RGB8(r, g, b) => { sum = r + g + b; }, 
                RGBA8(r, g, b, a) => { sum = r * a + g * a + b * a; }, 
                _ => { print("Only RGB(A)8 supported"); }
            };
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.program()
        typecheck_tree(tree)

    def test_MatchStmt_invalid(self): 
        test_input = """
        {
            let x: int = 8;
            let y: bool = true;
            match bar {
                x => { y = x; },
                2 => { y = x; }
            };
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_MatchStmt_Cdef_invalid(self): 
        test_input = """
        {
            let x: int = 8;
            let y: bool = true;
            match bar {
                Foo(x) => { y = x; },
                2 => { y = x; }
            };
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_ReturnStmt(self):
        test_input = """
        void main()
        {
            return;
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.program()
        typecheck_tree(tree)

    def test_ReturnStmt_invalid(self):
        test_input = """
        void main()
        {
            return true;
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.program()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_ReturnExprStmt(self):
        test_input = """
        int main()
        {
            let a: int = 2 + 3;
            return a;
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.program()
        typecheck_tree(tree)

    def test_ReturnExprStmt_invalid(self): #how to make invalid
        test_input = """
        bool main()
        {
            let foo: int = 2;
            return foo;
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.program()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)


    def test_PrintStmt(self):
        test_input = """
        {
            let t: int = 2;
            let tt: bool = true;
            print( t );
            print( tt );
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        typecheck_tree(tree)

    def test_PrintStmt_invalid(self): 
        test_input = """
        {
            print( a );
        }
        """
        parser = create_parser_for(test_input)
        tree = parser.block()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)


    def test_case_reach_invalid_expression(self):
        test_input = '{ let x: int = 3; match x { 3 => { x = true; } } }'
        parser = create_parser_for(test_input)
        tree = parser.block()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_case(self):
        test_input = '{ let x: int = 3; match x { 3 => { x = 4; } } }'
        parser = create_parser_for(test_input)
        tree = parser.block()
        typecheck_tree(tree)

    def test_param_invalid_type(self):
        test_input = 'someVar: 459hj'
        parser = create_parser_for(test_input)
        tree = parser.parameter()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_param(self):
        test_input = 'someVar: int'
        parser = create_parser_for(test_input)
        tree = parser.parameter()
        typecheck_tree(tree)

    def test_func_stmt(self):
        test_input = 'void main(var: string, num: int) { print(10); }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        typecheck_tree(tree)

    def test_func_stmt_invalid_dup(self):
        test_input = 'void main() { print(ok); } void main() { print (uh); }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_func_pointer(self):
        test_input = 'int add(x: int, y: int) { return x + y; }; void main(var: string, num: int) { let addptr: (int, int) -> int = &add; addptr(10, 20); }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        typecheck_tree(tree)


    def test_func_pointer_type_invalid(self):
        test_input = 'void main(var: string, num: int) { let sumptr: (int, int) -> int = &var; sumptr(10, 20); }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)


    def test_func_pointer_missing_invalid(self):
        test_input = 'void main(var: string, num: int) { let sumptr: (int, int) -> int = &sum; sumptr(10, 20); }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_cdef(self):
        test_input = 'enum nums { one: int; } void main() { }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        typecheck_tree(tree)

    def test_cdef_invalid_dup(self):
        test_input = 'enum nums { one: int; one: int;} void main() { }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_enumdef(self):
        test_input = 'enum nums { one: int; } void main() { }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        typecheck_tree(tree)

    def test_enumdef_invalid_dup(self):
        test_input = 'enum nums { one: int; } enum nums { two: int; } void main() { }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        with self.assertRaises(PeaceTypecheckError):
            typecheck_tree(tree)

    def test_program(self):
        test_input = 'enum anEnum { someNum: int; } int addTwo() { let c: int = 2 + 2; return c; }'
        parser = create_parser_for(test_input)
        tree = parser.program()
        typecheck_tree(tree)

if __name__ == '__main__':
    unittest.main(verbosity=2)
    