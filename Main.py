class ReversibleString:
    def __init__(self, text: str):
        self.text = text

    def get_reversed(self) -> str:
        return self.text[::-1]
my_string = ReversibleString("Hello World")
print(my_string.get_reversed()) 
