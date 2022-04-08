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

    def test_function_pointer(self):
        test_input = "let foo: (int*) -> bool = bar;"
        test_expected_rules = [PeaceParser.RULE_statement,
                               PeaceParser.RULE_vardec,
                               PeaceParser.RULE_atype,
                               PeaceParser.RULE_funcpointertype,
                               PeaceParser.RULE_basetype,
                               PeaceParser.RULE_basetype,
                               PeaceParser.RULE_basetype,
                               PeaceParser.RULE_basetype,
                               PeaceParser.RULE_funcpointertype,
                               PeaceParser.RULE_atype,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_vardec, 
                               PeaceParser.RULE_statement] 
        parser = create_parser_for(test_input)
        tree = parser.statement()
        rules_visited = parser_test(tree)
        print(rules_visited)
        assert(rules_visited == test_expected_rules)
    
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

    def test_assign(self):
        test_input = "test = x;"
        test_expected_rules = [PeaceParser.RULE_statement,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_statement] 
        parser = create_parser_for(test_input)
        tree = parser.statement()
        rules_visited = parser_test(tree)
        assert(rules_visited == test_expected_rules)

    def test_while(self):
        test_input = "while (x < 1) { y = 2; }"
        test_expected_rules = [PeaceParser.RULE_statement, #while
                               PeaceParser.RULE_expression, #x < 1
                               PeaceParser.RULE_expression, #x
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression, #1
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_statement,  #y = 2;
                               PeaceParser.RULE_expression, #y = 2
                               PeaceParser.RULE_expression, #y
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression, #2
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_statement, 
                               PeaceParser.RULE_statement] 
        parser = create_parser_for(test_input)
        tree = parser.statement()
        rules_visited = parser_test(tree)
        assert(rules_visited == test_expected_rules)

    def test_if(self):
        test_input = "if (foo >= bar) { baz = x; }"
        test_expected_rules = [PeaceParser.RULE_statement,  #if
                               PeaceParser.RULE_expression, #foo < bar
                               PeaceParser.RULE_expression, #foo
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression, #bar
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_statement,  #bar = x;
                               PeaceParser.RULE_expression, #bar = x
                               PeaceParser.RULE_expression, #bar
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression, #x
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_statement, 
                               PeaceParser.RULE_statement]  #if
        parser = create_parser_for(test_input)
        tree = parser.statement()
        rules_visited = parser_test(tree)
        assert(rules_visited == test_expected_rules)

    def test_if_else(self):
        test_input = "if (foo >= bar) { baz = x; } else { baz = y; }"
        test_expected_rules = [PeaceParser.RULE_statement,  #if
                               PeaceParser.RULE_expression, #foo < bar
                               PeaceParser.RULE_expression, #foo
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression, #bar
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_statement,  #bar = x;
                               PeaceParser.RULE_expression, #bar = x
                               PeaceParser.RULE_expression, #bar
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression, #x
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_statement, 
                               PeaceParser.RULE_statement,  #bar = y;
                               PeaceParser.RULE_expression, #bar = y
                               PeaceParser.RULE_expression, #bar
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression, #y
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_statement, 
                               PeaceParser.RULE_statement]  #if
        parser = create_parser_for(test_input)
        tree = parser.statement()
        rules_visited = parser_test(tree)
        assert(rules_visited == test_expected_rules)

    def test_match(self):
        test_input = "match bar { x => y = x, 2 => y = x };"
        test_expected_rules = [PeaceParser.RULE_statement,  #match
                               PeaceParser.RULE_expression, #bar
                               PeaceParser.RULE_expression, #bar
                               PeaceParser.RULE_case_, #x => y = x
                               PeaceParser.RULE_pattern, #x
                               PeaceParser.RULE_pattern, #x
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression, #y = x;
                               PeaceParser.RULE_expression, #y
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression, #x
                               PeaceParser.RULE_case_, #x => y = x
                               PeaceParser.RULE_case_, #2 => y = x
                               PeaceParser.RULE_pattern, #2
                               PeaceParser.RULE_pattern, #2
                               PeaceParser.RULE_expression, #y = x
                               PeaceParser.RULE_expression, #y
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression, #x
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_expression,
                               PeaceParser.RULE_case_, #2 => y = x
                               PeaceParser.RULE_statement]  #match
        parser = create_parser_for(test_input)
        tree = parser.statement()
        rules_visited = parser_test(tree)
        assert(rules_visited == test_expected_rules)
    
if __name__ == '__main__':
    unittest.main()