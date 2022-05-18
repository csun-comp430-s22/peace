from __future__ import unicode_literals
import sys
import os
import unittest
from antlr4 import *
from antlr4.tree.Trees import Trees

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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
    def test_string_literal(self):
        test_input = 'print("hi this is me");'
        tree_expected = '(statement print ( (expression "hi this is me") ) ;)'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_comment(self):
        test_input = '/*print("hi this is me");*/ print("hi");'
        tree_expected = '(statement print ( (expression "hi") ) ;)'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_function_pointer(self):
        test_input = "let foo: (int*) -> bool = bar;"
        tree_expected = '(statement (vardec let foo : (atype (funcpointertype ( (basetype int) * ) -> (basetype bool))) = (expression bar)) ;)'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_var_declare(self):
        test_input = "let x: int = 20;"
        tree_expected = '(statement (vardec let x : (atype (basetype int)) = (expression 20)) ;)'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_assign(self):
        test_input = "test = x;"
        tree_expected = '(statement (expression (expression test) = (expression x)) ;)'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_while(self):
        test_input = "while (x < 1) { y = 2; }"
        tree_expected = '(statement while ( (expression (expression x) < (expression 1)) ) '\
                            '{ (statement (expression (expression y) = (expression 2)) ;) })'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_if(self):
        test_input = "if (foo >= bar) { baz = x; }"
        tree_expected = '(statement if ( (expression (expression foo) >= (expression bar)) ) '\
                            '{ (statement (expression (expression baz) = (expression x)) ;) })'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_if_else(self):
        test_input = "if (foo >= bar) { baz = x; } else { baz = y; }"
        tree_expected = '(statement if ( (expression (expression foo) >= (expression bar)) ) '\
                            '{ (statement (expression (expression baz) = (expression x)) ;) } '\
                            'else { (statement (expression (expression baz) = (expression y)) ;) })'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_match(self):
        test_input = "match bar { x => y = x, 2 => y = x };"
        tree_expected = '(statement match (expression bar) { (case_ (pattern x) => (expression (expression y) = (expression x))) , '\
                                                            '(case_ (pattern 2) => (expression (expression y) = (expression x))) } ;)'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    
    def test_case_(self):
        test_input = "match x {4 => y = 4}" # case: 4 matcharrow exp
        tree_expected = "(statement match (expression x) { (case_ (pattern 4) => (expression (expression y) = (expression 4))) })"
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_case_multiple(self):
        test_input = "match x {1 => y = 4, 2 => y = 5, 3 => y = 6}" # case: 4 matcharrow exp
        tree_expected = '(statement match (expression x) { (case_ (pattern 1) => (expression (expression y) = (expression 4))) , '\
                                                          '(case_ (pattern 2) => (expression (expression y) = (expression 5))) , '\
                                                          '(case_ (pattern 3) => (expression (expression y) = (expression 6))) })'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_pattern(self):
        test_input = "match toMatch {pie => toMatch = pie, 4 => toMatch = 4}" # pattern: pie and 4 before matcharrow
        tree_expected = '(statement match (expression toMatch) { (case_ (pattern pie) => (expression (expression toMatch) = (expression pie))) , '\
                                                                '(case_ (pattern 4) => (expression (expression toMatch) = (expression 4))) })'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    # https://github.com/antlr/antlr4/issues/118 antlr4 open bug for mismatched input <eof>, safe for now
    # https://stackoverflow.com/questions/17844248/when-is-eof-needed-in-antlr-4
    def test_parameter(self):
        test_input = "bool someFunc(indicator: bool) {}" # param: indicator: bool (name: type)
        tree_expected = '(statement (func_stmt (atype (basetype bool)) someFunc ( (parameter indicator : (atype (basetype bool))) ) { }))'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_parameter_multiple(self):
        test_input = "void person(name: string, age: int) {}" # param: name, age
        tree_expected = '(statement (func_stmt (atype (basetype void)) person ( (parameter name : (atype (basetype string))) , '\
                            '(parameter age : (atype (basetype int))) ) { }))'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_func_stmt(self):
        test_input = "int addition(num1: int, num2: int) { let sum: int = num1 + num2; }" # function creation
        tree_expected = '(statement (func_stmt (atype (basetype int)) addition ( (parameter num1 : (atype (basetype int))) , '\
                                                                                '(parameter num2 : (atype (basetype int))) ) '\
                            '{ (statement (vardec let sum : (atype (basetype int)) = (expression (expression num1) + (expression num2))) ;) }))'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_enumdef(self):
        test_input = "enum cars = { ford: string; }" # enum creation and cdef creation
        tree_expected = '(statement (enumdef enum (expression cars) = { (cdef ford : (atype (basetype string)) ;) }))'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_enumdef_multiple_cdef(self):
        test_input = "enum colors = { blue: int; green: int; violet: int; }" # enum creation and cdef creation
        tree_expected = '(statement (enumdef enum (expression colors) = { (cdef blue : (atype (basetype int)) ;) '\
                                                                         '(cdef green : (atype (basetype int)) ;) '\
                                                                         '(cdef violet : (atype (basetype int)) ;) }))'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_program(self):
        test_input = "enum nums = { one: int; } void main() { print(ok); }"
        tree_expected = '(program (enumdef enum (expression nums) = { (cdef one : (atype (basetype int)) ;) }) '\
                        '(func_stmt (atype (basetype void)) main ( ) { (statement print ( (expression ok) ) ;) }))'
        parser = create_parser_for(test_input)
        tree = parser.program()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_return_exp(self):
        test_input = "return x;"
        tree_expected = '(statement return (expression x) ;)'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_return(self):
        test_input = "return;"
        tree_expected = '(statement return ;)'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual= Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_exp_exp(self):
        test_input = "x(y);"
        tree_expected = '(statement (expression (expression x) ( (expression y) )) ;)'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_print(self):
        test_input = "print(ok);"
        tree_expected = '(statement print ( (expression ok) ) ;)'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_func_call(self):
        test_input = "identifier(ok);"
        tree_expected = '(statement (expression (expression identifier) ( (expression ok) )) ;)'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)
    
if __name__ == '__main__':
    unittest.main()
    