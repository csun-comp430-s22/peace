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

class TestParser(unittest.TestCase):
    
    # SAMPLE TEST
    def test_declare(self):
        test_input = "let x: int = 20;"
        test_expected_text = ['let', 'x', ':', 'int', '=', '20', ';']
        test_expected_types = [PeaceLexer.Let, PeaceLexer.Identifier,
                               PeaceLexer.Colon, PeaceLexer.Int,
                               PeaceLexer.Assign, PeaceLexer.Digits, 
                               PeaceLexer.Semicolon] 
        assert(lexer_test(test_input, test_expected_text, test_expected_types))
    
if __name__ == '__main__':
    unittest.main()