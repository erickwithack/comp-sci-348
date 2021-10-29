class constants:
    PI = 3.14159
    TRAINING_SIZE = 1000
    TEST_SIZE = 100
    NUM_CLASSES = 10
    NUM_FEATURES = 3
    DATA_DIM = 2


def init_data(items, columns):
    return [[0 for x in range(columns)] for x in range(items)]
