import testing
import training
import time
import divide_dataset
import prepare_dataset


def mnist_cnn():
    start = time.time()

    (tr_d, te_d) = prepare_dataset.prepare_dataset([2, 3, 5, 7])

    groups = [[[2, 3], [5, 7]], [[2, 5], [3, 7]], [[2, 7], [3, 5]]]

    #groups = [[[0, 1, 2, 3], [4, 5, 6, 7]], [[0, 1, 2, 4], [3, 5, 6, 7]], [[0, 1, 2, 5], [3, 4, 6, 7]],
     #         [[0, 1, 2, 6], [3, 4, 5, 7]], [[0, 1, 2, 7], [3, 4, 5, 6]], [[0, 1, 3, 4], [2, 5, 6, 7]],
      #        [[0, 1, 3, 5], [2, 4, 6, 7]], [[0, 1, 3, 6], [2, 4, 5, 7]], [[0, 1, 3, 7], [2, 4, 5, 6]],
       #       [[0, 1, 4, 5], [2, 3, 6, 7]], [[0, 1, 4, 6], [2, 3, 5, 7]], [[0, 1, 4, 7], [2, 3, 5, 6]],
        #      [[0, 1, 5, 6], [2, 3, 4, 7]], [[0, 1, 5, 7], [2, 3, 4, 6]], [[0, 1, 6, 7], [2, 3, 4, 5]],
         #     [[0, 2, 3, 4], [1, 5, 6, 7]], [[0, 2, 3, 5], [1, 4, 6, 7]], [[0, 2, 3, 6], [1, 4, 5, 7]],
          #    [[0, 2, 3, 7], [1, 4, 5, 6]], [[0, 2, 4, 5], [1, 3, 6, 7]], [[0, 2, 4, 6], [1, 3, 5, 7]],
           #   [[0, 2, 4, 7], [1, 3, 5, 6]], [[0, 2, 5, 6], [1, 3, 4, 7]], [[0, 2, 5, 7], [1, 3, 4, 6]],
            #  [[0, 2, 6, 7], [1, 3, 4, 5]], [[0, 3, 4, 5], [1, 2, 6, 7]], [[0, 3, 4, 6], [1, 2, 5, 7]],
             # [[0, 3, 4, 7], [1, 2, 5, 6]], [[0, 3, 5, 6], [1, 2, 4, 7]], [[0, 3, 5, 7], [1, 2, 4, 6]],
              #[[0, 3, 6, 7], [1, 2, 4, 5]], [[0, 4, 5, 6], [1, 2, 3, 7]], [[0, 4, 5, 7], [1, 2, 3, 6]],
              #[[0, 4, 6, 7], [1, 2, 3, 5]], [[0, 5, 6, 7], [1, 2, 3, 4]]]

    d = {}
    a = []

    for g in groups:
        print(f'Groups: {g}')
        (train_d_set, test_d_set) = divide_dataset.divide_dataset(g, tr_d, te_d)
        training.train(train_d_set)
        accuracy = testing.test(test_d_set)
        d[str(g)] = accuracy
        a.append(accuracy)

    a.sort()
    a.reverse()

    for i in d:
        if d[i] == a[0]:
            print(f'Highest accuracy: {a[0]}, groups: {i}\n')
        if d[i] == a[1]:
            print(f'Second highest accuracy: {a[1]}, groups: {i}\n')

    finish = time.time()

    print('Total seconds passed: %.3f' % (finish - start))


if __name__ == '__main__':
    mnist_cnn()
