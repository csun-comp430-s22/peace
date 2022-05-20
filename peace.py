import argparse

from antlr4 import *
from peace.antlr.generated.PeaceLexer import PeaceLexer
from peace.antlr.generated.PeaceParser import PeaceParser
from peace.typechecker.PeaceTypechecker import PeaceTypechecker

def main() -> None:
    parser = argparse.ArgumentParser(
        usage = "%(prog)s [FILE]",
        description = "Eventually compile a Peace program into C, for now just typechecks it"
    )
    parser.add_argument("file")
    args = parser.parse_args()

    if not args.file:
        print("Please provide a valid file path")

    try:
        file_stream = FileStream(args.file)
        lexer = PeaceLexer(file_stream)
        stream = CommonTokenStream(lexer)
        parser = PeaceParser(stream)
        tree = parser.program()
        visitor = PeaceTypechecker()
        visitor.visit(tree)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()