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

if __name__ == '__main__':
    unittest.main()