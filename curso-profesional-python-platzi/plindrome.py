# Palindromo: Palabra que se lee igual al derecho y al reves

def is_palindrome( string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1] #El mismo string pero al reves


def run():
    print(is_palindrome(1))

if __name__ == '__main__':
    run()