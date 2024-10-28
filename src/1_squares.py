from itertools import islice

MIN_LENGTH_RANGE = 200
MAX_LENGTH_RANGE = 10001
MIN_WIDE_RANGE = 500
MAX_WIDE_RANGE = 100_001
COUNT = 100

def calculate_squares(min_length : int = MIN_LENGTH_RANGE, max_length : int = MAX_LENGTH_RANGE,
                      min_wide : int = MIN_WIDE_RANGE, max_wide : int = MAX_WIDE_RANGE, count : int = COUNT):
    squares = list(islice((int(i * j) for i in range(min_length, max_length)
                           for j in range(min_wide, max_wide)), count))
    return squares

def print_squares(squares : list) -> None:
    print(squares)

def process():
    print_squares(calculate_squares())

if __name__ == "__main__":
    process()