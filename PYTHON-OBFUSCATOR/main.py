import ast
import codegen

def obfuscate(src):
    # Parse the input source code and generate an AST
    tree = ast.parse(src)

    # Modify the AST to obfuscate the code
    # For example, this loop renames all function and variable names to shorter,
    # less meaningful names
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Name)):
            node.id = 'x'

    # Use codegen to generate code from the modified AST
    obfuscated_src = codegen.to_source(tree)
    return obfuscated_src

# Read in the source code of the input file
with open('input.py', 'r') as f:
    src = f.read()

# Obfuscate the source code and print the result
obfuscated_src = obfuscate(src)
print(obfuscated_src)