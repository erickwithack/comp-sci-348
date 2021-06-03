import common

PI = common.constants.PI
TRAINING_SIZE = common.constants.TRAINING_SIZE
TEST_SIZE = common.constants.TEST_SIZE
NUM_CLASSES = common.constants.NUM_CLASSES
NUM_FEATURES = common.constants.NUM_FEATURES
DATA_DIM = common.constants.DATA_DIM


def part_one_classifier(data_train, data_test):
    # Initialize constants
    weights = common.init_data(1, 3)[0]
    part = 'one'
    accuracy = 0
    data_train_length = len(data_train)

    while accuracy / data_train_length < .95:
        # Initialize accuracy after every epoch
        accuracy = 0

        # Predict the class
        for i in range(data_train_length):
            x, y, values = data_train[i]
            prediction = part_one_prediction(x, y, weights)

            # Update weights
            if prediction != values:
                update = 0.01 * (values - prediction)
                weights[0] += update
                weights[1] += update * x
                weights[2] += update * y

            # Update accuracy
            else:
                accuracy += 1

    # Evaluate the results
    evaluation(data_test, weights, part)
    return


def part_two_classifier(data_train, data_test):
    # Initialize constants
    weights = common.init_data(10, 2)
    part = 'two'
    accuracy = 0
    data_train_length = len(data_train)

    while accuracy / data_train_length < .95:
        # Initialize accuracy after every epoch
        accuracy = 0

        # Predict the class
        for i in range(data_train_length):
            x, y, values = data_train[i]
            values = int(values)
            prediction = part_two_prediction(x, y, weights)

            # Update weights
            if prediction != values:
                weights[values][0] += 0.01 * x
                weights[values][1] += 0.01 * y
                weights[prediction][0] -= 0.01 * x
                weights[prediction][1] -= 0.01 * y

            # Update accuracy
            else:
                accuracy += 1

    # Evaluate the results
    evaluation(data_test, weights, part)
    return


def part_one_prediction(x, y, weights):
    tot_weights = weights[0] + weights[1] * x + weights[2] * y
    if tot_weights >= 0:
        prediction = 1
    else:
        prediction = 0

    return prediction


def part_two_prediction(x, y, weights):
    max_val = 0
    max_index = -1

    for i in range(NUM_CLASSES):
        output = weights[i][0] * x + weights[i][1] * y
        if output > max_val:
            max_val = output
            max_index = i

    return max_index


def evaluation(data_test, weights, part):
    for index, data in enumerate(data_test):
        x, y, _ = data

        if part == 'one':
            prediction = part_one_prediction(x, y, weights)
        else:
            prediction = part_two_prediction(x, y, weights)

        # Update the third column of the “data_test” structure with the prediction
        data_test[index][2] = prediction
