from __future__ import unicode_literals
import sys
import unittest
import antlr4

sys.path.append("../")
from antlr.generated.PeaceLexer import PeaceLexer

def lexer_test(input, expected_token_text, expected_token_types):
    input_stream = antlr4.InputStream(input)
    lexer = PeaceLexer(input_stream)
    tokens = lexer.getAllTokens()
    token_text = list(map(lambda x: x.text, tokens))
    token_types = list(map(lambda x: x.type, tokens))
    if token_text == expected_token_text and token_types == expected_token_types:
        return True
    return False

class TestLexer(unittest.TestCase):
    
    def test_declare(self):
        test_input = "let x: int = 20;"
        test_expected_text = ['let', 'x', ':', 'int', '=', '20', ';']
        test_expected_types = [PeaceLexer.Let, PeaceLexer.Identifier,
                               PeaceLexer.Colon, PeaceLexer.Int,
                               PeaceLexer.Assign, PeaceLexer.Digits, 
                               PeaceLexer.Semicolon] 
        assert(lexer_test(test_input, test_expected_text, test_expected_types))

    # BEGIN TESTS FOR TYPE TOKENS
    def test_type_int_token(self):
        test_input = "int"
        test_expected_text = ['int']
        test_expected_types = [PeaceLexer.Int]
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
        test_expected_types = [PeaceLexer.Float]
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
        test_expected_types = [PeaceLexer.Bool]
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
        test_expected_types = [PeaceLexer.Void]
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
        test_expected_types = [PeaceLexer.String]
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
        test_expected_types = [PeaceLexer.Add]
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
        test_expected_types = [PeaceLexer.Subtract]
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
        test_expected_types = [PeaceLexer.Multiply]
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
        test_expected_types = [PeaceLexer.Divide]
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
        test_expected_types = [PeaceLexer.Modulo]
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
        test_expected_types = [PeaceLexer.LessThan]
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
        test_expected_types = [PeaceLexer.GreaterThan]
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
        test_expected_types = [PeaceLexer.LessThanOrEq]
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
        test_expected_types = [PeaceLexer.GreaterThanOrEq]
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
        test_expected_types = [PeaceLexer.Equal]
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
        test_expected_types = [PeaceLexer.NotEqual]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_keyword_let(self):
        """Test let keyword token"""
        assert(lexer_test("let", ['let'], [PeaceLexer.Let]))

    def test_keyword_true(self):
        """Test true keyword token"""
        assert(lexer_test("true", ['true'], [PeaceLexer.BoolTrue]))

    def test_keyword_false(self):
        """Test false keyword token"""
        assert(lexer_test("false", ['false'], [PeaceLexer.BoolFalse]))

    def test_keyword_arrow(self):
        """Test arrow (->) token"""
        assert(lexer_test("->", ['->'], [PeaceLexer.Arrow]))

    def test_keyword_while(self):
        """Test while keyword token"""
        assert(lexer_test("while", ['while'], [PeaceLexer.While]))

    def test_keyword_if(self):
        """Test if keyword token"""
        assert(lexer_test("if", ['if'], [PeaceLexer.If]))

    def test_keyword_else(self):
        """Test else keyword token"""
        assert(lexer_test("else", ['else'], [PeaceLexer.Else]))

    def test_keyword_return(self):
        """Test Return keyword token"""
        assert(lexer_test("return", ['return'], [PeaceLexer.Return]))

    def test_keyword_func(self):
        """Test func keyword token"""
        assert(lexer_test("func", ['func'], [PeaceLexer.Function]))

    def test_keyword_print(self):
        """Test print keyword token"""
        assert(lexer_test("print", ['print'], [PeaceLexer.Print]))

        #pattern matching tests
    def test_type_match_token(self):
        test_input = "match"
        test_expected_text = ['match']
        test_expected_types = [PeaceLexer.Match]
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
        test_expected_types = [PeaceLexer.MatchArrow]
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
        test_expected_types = [PeaceLexer.Any]
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
        test_expected_types = [PeaceLexer.Assign]
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
        test_expected_types = [PeaceLexer.Amp]
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
        test_expected_types = [PeaceLexer.Colon]
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
        test_expected_types = [PeaceLexer.Semicolon]
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
        test_expected_types = [PeaceLexer.LParen]
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
        test_expected_types = [PeaceLexer.RParen]
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
        test_expected_types = [PeaceLexer.LBracket]
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
        test_expected_types = [PeaceLexer.RBracket]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_type_ws_token(self):
        test_input = " "
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        assert(len(tokens) == 0)

    def test_type_new_line_token(self):
        test_input = "\n"
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        assert(len(tokens) == 0)

    def test_type_identifier_token(self):
        test_input = "anTlr"
        test_expected_text = ['anTlr']
        test_expected_types = [PeaceLexer.Identifier]
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
        test_expected_types = [PeaceLexer.Digits]
        input_stream = antlr4.InputStream(test_input)
        lexer = PeaceLexer(input_stream)
        tokens = lexer.getAllTokens()
        token_text = list(map(lambda x: x.text, tokens))
        token_types = list(map(lambda x: x.type, tokens))
        assert(token_text == test_expected_text)
        assert(token_types == test_expected_types)

    def test_constant_float(self):
        assert(lexer_test("0.12", ['0.12'], [PeaceLexer.FloatConst]))
    
if __name__ == '__main__':
    unittest.main()