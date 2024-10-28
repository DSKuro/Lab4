def user_input() -> tuple:
    first_array = [int(x) for x in input("Введите первый список: ").split()]
    second_array = [int(x) for x in input("Введите второй список: ").split()]
    return first_array, second_array

def calculate_result(first : list, second : list) -> list:
    numbers = set(first) & set(second)
    odd_numbers = list(filter(lambda x : True if x % 2 == 0 else False, numbers))
    return odd_numbers

def print_result(numbers : list) -> None:
    print(numbers)

def process():
    first, second = user_input()
    print(calculate_result(first, second))

if __name__ == "__main__":
    process()