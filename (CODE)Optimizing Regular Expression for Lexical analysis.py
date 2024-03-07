import re
import subprocess
import timeit

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f"Token({self.token_type}, {self.value})"

class Lexer:
    def __init__(self):
        self.tokens = []

    def tokenize(self, input_text):
        self.tokens = []
        position = 0

        while position < len(input_text):
            # Skip whitespaces
            if input_text[position].isspace():
                position += 1
            else:
                # Check for keywords and identifiers
                keyword_identifier_regex = re.compile(r'\b(?:int|float|if|else|return)\b|\b[a-zA-Z_]\w*\b')
                match = keyword_identifier_regex.match(input_text, position)

                if match:
                    value = match.group()
                    token_type = "KEYWORD" if value in ["int", "float", "if", "else", "return"] else "IDENTIFIER"
                    self.tokens.append(Token(token_type, value))
                    position = match.end()
                else:
                    # Check for other single-character tokens
                    token_type = input_text[position]
                    self.tokens.append(Token(token_type, token_type))
                    position += 1

        return self.tokens

def generate_optimized_code(input_code):
    # Split the input code into lines
    lines = input_code.split('\n')
    optimized_lines = []

    # Iterate through each line and remove leading/trailing whitespaces
    for line in lines:
        optimized_line = line.strip()
        optimized_lines.append(optimized_line)

    # Join the optimized lines to form the optimized code
    optimized_code = '\n'.join(optimized_lines)
    return optimized_code

def main():
    # Input code
    input_code = """
    int main() {
    int x=10;float y=3.14;

    if(x>0)
    {
        printf("x is positive\n");
        return x*y;
    }
    else
    {
        printf("x is non-positive\n");
        return 0;
    }
}
    """

    lexer = Lexer()

    # Tokens before optimization
    tokens_before = lexer.tokenize(input_code)
    print("\nTokens Before Optimization:")
    for token in tokens_before:
        print(token)

    # Number of tokens before optimization
    num_tokens_before = len(tokens_before)
    print(f"\nNumber of Tokens Before Optimization: {num_tokens_before}")

    # Measure runtime efficiency before optimization
    runtime_before = timeit.timeit(lambda: lexer.tokenize(input_code), number=10000)
    print(f"\nRuntime Efficiency Before Optimization: {runtime_before:.5f} seconds")

    # Generate and print optimized code
    optimized_code = generate_optimized_code(input_code)
    print("\nOptimized Code:")
    print(optimized_code)

    # Tokens after optimization
    tokens_after = lexer.tokenize(optimized_code)
    print("\nTokens After Optimization:")
    for token in tokens_after:
        print(token)

    # Number of tokens after optimization
    num_tokens_after = len(tokens_after)
    print(f"\nNumber of Tokens After Optimization: {num_tokens_after}")

    # Measure runtime efficiency after optimization
    runtime_after = timeit.timeit(lambda: lexer.tokenize(optimized_code), number=10000)
    print(f"\nRuntime Efficiency After Optimization: {runtime_after:.5f} seconds")

if __name__ == "__main__":
    main()
