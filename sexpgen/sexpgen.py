import tree_sitter_languages as tslang
from sys import stdout
from pathlib import Path

def from_string(s, lang, fpout=stdout):
    parser = tslang.get_parser(lang)
    tree = parser.parse(s.encode())
    print(tree.root_node.sexp(), file=fpout)

def from_file(path, fpout=stdout):
    path = Path(path)

    langs = [
        (['.c', '.h'], 'c'),
        (['.py'], 'python'),
    ]
    langs = [lang for (exts, lang) in langs if path.suffix in exts]

    if len(langs) > 0 and (lang := langs[0]):
        parser = tslang.get_parser(lang)
        tree = parser.parse(path.read_bytes())
        print(tree.root_node.sexp(), file=fpout)

