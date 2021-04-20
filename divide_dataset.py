import group_dataset


def divide_dataset(groups, train_set, test_set):

    train_d_set = group_dataset.GroupDataset(train_set, groups)
    test_d_set = group_dataset.GroupDataset(test_set, groups)

    return train_d_set, test_d_set
