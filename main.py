import testing
import training
import time
import divide_dataset


def mnist_cnn(train, test):

    groups = [[0, 4, 5, 7, 9], [1, 2, 3, 6, 8]]

    start1 = time.time()

    (train_d_set, test_d_set) = divide_dataset.divide_dataset(groups)

    start2 = time.time()

    if train:
        training.train(train_d_set)

    start3 = time.time()

    if test:
        testing.test(test_d_set)

    finish = time.time()

    print(f'Groups: {groups}')

    print('Total seconds passed: %.3f' % (finish - start1))
    print('Seconds passed for dividing: %.3f' % (start2 - start1))
    if train:
        print('Seconds passed for training: %.3f' % (start3 - start2))
    if test:
        print('Seconds passed for testing: %.3f' % (finish - start3))


if __name__ == '__main__':
    mnist_cnn(True, True)
