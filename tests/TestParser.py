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
        #line 1:13 extraneous input '*' expecting {')', ','}
        print('start func pointer')
        test_input = "let foo: (int*) -> bool = bar;"
        tree_expected = '(statement (vardec let foo : (atype (funcpointertype ( (basetype int) * ) -> (basetype bool))) = (expression bar)) ;)'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)
        print('end func pointer')

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
        tree_expected = '(statement while ( (expression (expression x) < (expression 1)) ) (block { (statement (expression (expression y) = (expression 2)) ;) }))'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected == tree_actual)

    def test_if(self):
        test_input = "if (foo >= bar) { }"
        tree_expected = '(statement if((expression(expression foo) >= (expression bar))) (block { }))'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected.replace(" ", "") == tree_actual.replace(" ", ""))

    def test_if_else(self):
        test_input = "if (foo >= bar) { } else { }"
        tree_expected = '(statement if((expression(expression foo) >= (expression bar))) (block { }) else (block { }))'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected.replace(" ", "") == tree_actual.replace(" ", ""))

    def test_match(self):
        test_input = "match x { 3 => { } };"
        tree_expected = '(statement match (expression x) { (case_ (pattern 3) => (block { }))};)'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected.replace(" ", "") == tree_actual.replace(" ", ""))

    
    def test_case_(self):
        test_input = "match x { 4 => {} }" 
        tree_expected = "(statement match (expression x) {(case_ (pattern 4) => (block {})) })"
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected.replace(" ", "") == tree_actual.replace(" ", ""))

    def test_case_multiple(self):
        test_input = "match x { 4 => {}, 5 => {}, 6 => {} }"
        tree_expected = '(statement match (expression x) {(case_ (pattern 4) => (block{})), (case_ (pattern 5) => (block{})), (case_ (pattern 6) => (block{})) })'
        parser = create_parser_for(test_input)
        tree = parser.statement()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected.replace(" ", "") == tree_actual.replace(" ", ""))

    def test_pattern(self):
        test_input = 'caseVar => { }'
        tree_expected = '(case_ (pattern caseVar) => (block { }) )'
        parser = create_parser_for(test_input)
        tree = parser.case_()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected.replace(" ", "") == tree_actual.replace(" ", ""))

    # https://github.com/antlr/antlr4/issues/118 antlr4 open bug for mismatched input <eof>, safe for now
    # https://stackoverflow.com/questions/17844248/when-is-eof-needed-in-antlr-4
    def test_parameter(self):
        test_input = 'void testParam(aBool: bool) { }'
        tree_expected = '(func_stmt(atype(basetype void)) testParam((parameter aBool: (atype(basetype bool)))) (block {}))'
        parser = create_parser_for(test_input)
        tree = parser.func_stmt()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected.replace(" ", "") == tree_actual.replace(" ", ""))

    def test_parameter_multiple(self):
        test_input = 'void testParams(aBool: bool, anInt: int, aString: string) { }'
        tree_expected = '(func_stmt(atype(basetype void)) testParams((parameter aBool: (atype(basetype bool))), (parameter anInt: (atype(basetype int))), (parameter aString: (atype(basetype string)))) (block{}))'
        parser = create_parser_for(test_input)
        tree = parser.func_stmt()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected.replace(" ", "") == tree_actual.replace(" ", ""))

    def test_func_stmt(self):
        test_input = "void printLine(line: string) { print(line); }"
        tree_expected = '(func_stmt (atype(basetype void)) printLine((parameter line: (atype(basetype string)))) (block {(statement print((expression line));) }))'
        parser = create_parser_for(test_input)
        tree = parser.func_stmt()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected.replace(" ", "") == tree_actual.replace(" ", ""))

    def test_enumdef(self):
        test_input = "enum cars { ford: string; }" # enum creation and cdef creation
        tree_expected = '(enumdef enum cars { (cdef ford: (atype(basetype string));) })'
        parser = create_parser_for(test_input)
        tree = parser.enumdef()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected.replace(" ", "") == tree_actual.replace(" ", ""))

    def test_enumdef_multiple_cdef(self):
        test_input = "enum favThings { colors: string, string; food: string; nums: int; }" # enum creation and cdef creation
        tree_expected = '(enumdef enum favThings { (cdef colors: (atype(basetype string)), (atype(basetype string));) (cdef food: (atype(basetype string));) (cdef nums: (atype(basetype int)); )})'
        parser = create_parser_for(test_input)
        tree = parser.enumdef()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected.replace(" ", "") == tree_actual.replace(" ", ""))

    def test_program(self):
        test_input = 'void main() { print("ok"); }'
        tree_expected = '(program(func_stmt(atype(basetype void)) main()(block{(statement print((expression "ok"));)})))'
        parser = create_parser_for(test_input)
        tree = parser.program()
        tree_actual = Trees.toStringTree(tree, None, PeaceParser)
        assert(tree_expected.replace(" ", "") == tree_actual.replace(" ", ""))

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
    