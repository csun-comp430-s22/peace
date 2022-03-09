from __future__ import unicode_literals
import sys
import unittest
import antlr4

sys.path.append("../")
from antlr.generated.PeaceLexer import PeaceLexer

class TestLexer(unittest.TestCase):
    
    def test_declare(self):
        test_input = "let x: int = 20;"
        test_expected_text = ['let', 'x', ':', 'int', '=', '20', ';']
        test_expected_types = [17, 38, 30, 1, 28, 40, 31] 
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    # BEGIN TESTS FOR TYPE TOKENS
    def test_type_int_token(self):
        test_input = "int"
        test_expected_text = ['int']
        test_expected_types = [1]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_float_token(self):
        test_input = "float"
        test_expected_text = ['float']
        test_expected_types = [2]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)
    
    def test_type_bool_token(self):
        test_input = "bool"
        test_expected_text = ['bool']
        test_expected_types = [3]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_void_token(self):
        test_input = "void"
        test_expected_text = ['void']
        test_expected_types = [4]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_string_token(self):
        test_input = "string"
        test_expected_text = ['string']
        test_expected_types = [5]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_string_token(self):
        test_input = "string"
        test_expected_text = ['string']
        test_expected_types = [5]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    # BEGIN TESTS FOR OPERATION TOKENS
    def test_operation_add_token(self):
        test_input = "+"
        test_expected_text = ['+']
        test_expected_types = [6]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_operation_subtract_token(self):
        test_input = "-"
        test_expected_text = ['-']
        test_expected_types = [7]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_operation_multiply_token(self):
        test_input = "*"
        test_expected_text = ['*']
        test_expected_types = [8]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_operation_divide_token(self):
        test_input = "/"
        test_expected_text = ['/']
        test_expected_types = [9]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_operation_modulo_token(self):
        test_input = "%"
        test_expected_text = ['%']
        test_expected_types = [10]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_operation_less_than_token(self):
        test_input = "<"
        test_expected_text = ['<']
        test_expected_types = [11]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_operation_greater_than_token(self):
        test_input = ">"
        test_expected_text = ['>']
        test_expected_types = [12]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_operation_less_than_or_equal_token(self):
        test_input = "<="
        test_expected_text = ['<=']
        test_expected_types = [13]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_operation_greater_than_or_equal_token(self):
        test_input = ">="
        test_expected_text = ['>=']
        test_expected_types = [14]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_operation_equal_token(self):
        test_input = "=="
        test_expected_text = ['==']
        test_expected_types = [15]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_operation_not_equal_token(self):
        test_input = "!="
        test_expected_text = ['!=']
        test_expected_types = [16]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

if __name__ == '__main__':
    unittest.main()