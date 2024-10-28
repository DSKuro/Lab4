from random import choice

p = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

def generate_notes(n : int):
    for i in range(0, n):
        yield choice(p)

def create_two_dimensional_array(n : int, a: int, b : int) -> list:
    array = [[list(generate_notes(n)) for j in range(b)] for i in range(a)]
    return array

def print_array(array : list) -> None:
    print(array)

def process(n : int, a : int, b : int):
    print_array(create_two_dimensional_array(n, a, b))

if __name__ == "__main__":
    process(5, 10, 10)
