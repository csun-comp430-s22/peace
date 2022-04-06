from __future__ import unicode_literals
import sys
import os
import unittest
import antlr4

sys.path.append(os.path.dirname(__file__) + "/../")
from antlr.generated.PeaceLexer import PeaceLexer

# TEST HELPER FUNCTION
def lexer_test(input, expected_token_text, expected_token_types):
    input_stream = antlr4.InputStream(input)
    lexer = PeaceLexer(input_stream)
    tokens = lexer.getAllTokens()
    token_text = list(map(lambda x: x.text, tokens))
    token_types = list(map(lambda x: x.type, tokens))
    if token_text == expected_token_text and token_types == expected_token_types:
        return True
    return False

# ALL TOKEN TEST METHODS
class TestLexer(unittest.TestCase):
    
    # SAMPLE TEST
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
        """Test int type token"""
        assert(lexer_test("int", ['int'], [PeaceLexer.Int]))

    def test_type_float_token(self):
        """Test float type token"""
        assert(lexer_test("float", ['float'], [PeaceLexer.Float]))
    
    def test_type_bool_token(self):
        """Test bool type token"""
        assert(lexer_test("bool", ['bool'], [PeaceLexer.Bool]))

    def test_type_void_token(self):
        """Test void type token"""
        assert(lexer_test("void", ['void'], [PeaceLexer.Void]))

    def test_type_string_token(self):
        """Test string type token"""
        assert(lexer_test("string", ['string'], [PeaceLexer.String]))

    # BEGIN TESTS FOR OPERATION TOKENS
    def test_operation_add_token(self):
        """Test equal operation token"""
        assert(lexer_test("+", ['+'], [PeaceLexer.Add]))

    def test_operation_subtract_token(self):
        """Test subtract operation token"""
        assert(lexer_test("-", ['-'], [PeaceLexer.Subtract]))

    def test_operation_multiply_token(self):
        """Test multiply operation token"""
        assert(lexer_test("*", ['*'], [PeaceLexer.Multiply]))

    def test_operation_divide_token(self):
        """Test divide operation token"""
        assert(lexer_test("/", ['/'], [PeaceLexer.Divide]))

    def test_operation_modulo_token(self):
        """Test modulo operation token"""
        assert(lexer_test("%", ['%'], [PeaceLexer.Modulo]))

    def test_operation_less_than_token(self):
        """Test less than operation token"""
        assert(lexer_test("<", ['<'], [PeaceLexer.LessThan]))

    def test_operation_greater_than_token(self):
        """Test greater than operation token"""
        assert(lexer_test(">", ['>'], [PeaceLexer.GreaterThan]))
        
    def test_operation_less_than_or_equal_token(self):
        """Test less than or equal operation token"""
        assert(lexer_test("<=", ['<='], [PeaceLexer.LessThanOrEq]))

    def test_operation_greater_than_or_equal_token(self):
        """Test greater than or equal operation token"""
        assert(lexer_test(">=", ['>='], [PeaceLexer.GreaterThanOrEq]))

    def test_operation_equal_token(self):
        """Test equal operation token"""
        assert(lexer_test("==", ['=='], [PeaceLexer.Equal]))

    def test_operation_not_equal_token(self):
        """Test not equal operation token"""
        assert(lexer_test("!=", ['!='], [PeaceLexer.NotEqual]))

    # BEGIN TESTS FOR KEYWORD TOKENS
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

        #BEGIN TESTS FOR PATTERN MATCHING TOKENS
    def test_type_match_token(self):
        """Test print keyword token"""
        assert(lexer_test("match", ['match'], [PeaceLexer.Match]))
        

    def test_type_match_arrow_token(self):
        """Test print keyword token"""
        assert(lexer_test("=>", ['=>'], [PeaceLexer.MatchArrow]))

    def test_type_any_token(self):
        """Test print keyword token"""
        assert(lexer_test("_", ['_'], [PeaceLexer.Any]))

    def test_type_assign_token(self):
        """Test print keyword token"""
        assert(lexer_test("=", ['='], [PeaceLexer.Assign]))

    def test_type_amp_token(self):
        """Test print keyword token"""
        assert(lexer_test("&", ['&'], [PeaceLexer.Amp]))

    def test_type_colon_token(self):
        """Test print keyword token"""
        assert(lexer_test(":", [':'], [PeaceLexer.Colon]))

    def test_type_semicolon_token(self):
        """Test print keyword token"""
        assert(lexer_test(";", [';'], [PeaceLexer.Semicolon]))

    def test_type_l_paren_token(self):
        """Test print keyword token"""
        assert(lexer_test("(", ['('], [PeaceLexer.LParen]))

    def test_type_r_paren_token(self):
        """Test print keyword token"""
        assert(lexer_test(")", [')'], [PeaceLexer.RParen]))

    def test_type_l_bracket_token(self):
        """Test print keyword token"""
        assert(lexer_test("{", ['{'], [PeaceLexer.LBracket]))

    def test_type_r_bracket_token(self):
        """Test print keyword token"""
        assert(lexer_test("}", ['}'], [PeaceLexer.RBracket]))

    def test_double_quote(self):
        """Test double quote token"""
        assert(lexer_test('"', ['"'], [PeaceLexer.DoubleQuote]))

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
        """Test double quote token"""
        assert(lexer_test('anTlr', ['anTlr'], [PeaceLexer.Identifier]))

    def test_type_digits_token(self):
        """Test double quote token"""
        assert(lexer_test('56', ['56'], [PeaceLexer.Digits]))

    def test_constant_float(self):
        assert(lexer_test("0.12", ['0.12'], [PeaceLexer.FloatConst]))
    
if __name__ == '__main__':
    unittest.main()