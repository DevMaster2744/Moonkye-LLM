import tiktoken

class Tokenizer():
    def __init__(self):
        print("Starting <TOKENIZER>")
        self.encoder = tiktoken.get_encoding("cl100k_base")
        print(self.encoder.encode("Forgotten World"))
        print("<TOKENIZER LOADED>")

Tokenizer()