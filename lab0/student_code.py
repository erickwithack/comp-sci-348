def order(data):
    # new_data = []

    for i in range(len(data)):
        for j in range(len(data) - 1):
            if (data[j] > data[j + 1]):
                temp_data_j = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp_data_j

    return data
