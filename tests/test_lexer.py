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


        #17 - 24 



        #pattern matching tests
    def test_type_match_token(self):
        test_input = "match"
        test_expected_text = ['match']
        test_expected_types = [25]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_match_arrow_token(self):
        test_input = "=>"
        test_expected_text = ['=>']
        test_expected_types = [26]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_any_token(self):
        test_input = "_"
        test_expected_text = ['_']
        test_expected_types = [27]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_assign_token(self):
        test_input = "="
        test_expected_text = ['=']
        test_expected_types = [28]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_amp_token(self):
        test_input = "&"
        test_expected_text = ['&']
        test_expected_types = [29]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_colon_token(self):
        test_input = ":"
        test_expected_text = [':']
        test_expected_types = [30]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_semicolon_token(self):
        test_input = ";"
        test_expected_text = [';']
        test_expected_types = [31]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_l_paren_token(self):
        test_input = "("
        test_expected_text = ['(']
        test_expected_types = [32]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_r_paren_token(self):
        test_input = ")"
        test_expected_text = [')']
        test_expected_types = [33]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_l_bracket_token(self):
        test_input = "{"
        test_expected_text = ['{']
        test_expected_types = [34]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_r_bracket_token(self):
        test_input = "}"
        test_expected_text = ['}']
        test_expected_types = [35]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_ws_token(self):
        test_input = ""
        test_expected_text = ['']
        test_expected_types = [36]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_new_line_token(self):
        test_input = " "
        test_expected_text = [' ']
        test_expected_types = [37]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_identifier_token(self):
        test_input = "anTlr"
        test_expected_text = ['anTlr']
        test_expected_types = [38]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_digit_token(self):
        test_input = "9"
        test_expected_text = ['9']
        test_expected_types = [39]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_digits_token(self):
        test_input = "56"
        test_expected_text = ['56']
        test_expected_types = [40]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)
    


if __name__ == '__main__':
    unittest.main()