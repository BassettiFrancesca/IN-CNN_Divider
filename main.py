import testing
import training
import time
import divide_dataset
import prepare_dataset
import find_pairings
import matplotlib.pyplot as plt


def mnist_cnn():
    start = time.time()

    groups = find_pairings.find_pairings()

    groups_a_l = {}
    acc = []
    losses = []

    for g in groups:
        print(f'Groups: {g}')
        digits = []
        for i in g:
            for k in i:
                digits.append(k)
        (tr_d, te_d) = prepare_dataset.prepare_dataset(digits)
        (train_d_set, test_d_set) = divide_dataset.divide_dataset(g, tr_d, te_d)
        loss = training.train(train_d_set)
        accuracy = testing.test(test_d_set)
        groups_a_l[str(g)] = [accuracy]
        groups_a_l[str(g)].append(loss)
        acc.append(accuracy)
        losses.append(loss)

    acc.sort()
    acc.reverse()

    losses.sort()

    for i in groups_a_l:
        if groups_a_l[i][0] == acc[0]:
            print(f'Highest accuracy: {acc[0]}, groups: {i}\n')
        if groups_a_l[i][0] == acc[1]:
            print(f'Second highest accuracy: {acc[1]}, groups: {i}\n')
        if groups_a_l[i][0] == acc[len(acc) - 1]:
            print(f'Lowest accuracy: {acc[len(acc) - 1]}, groups: {i}\n')
        if groups_a_l[i][0] == acc[len(acc) - 2]:
            print(f'Second lowest accuracy: {acc[len(acc) - 2]}, groups: {i}\n')

    for i in groups_a_l:
        if groups_a_l[i][1] == losses[0]:
            print(f'Lowest loss: {losses[0]}, groups: {i}\n')
        if groups_a_l[i][1] == losses[1]:
            print(f'Second lowest loss: {losses[1]}, groups: {i}\n')
        if groups_a_l[i][1] == losses[len(losses) - 1]:
            print(f'Highest loss: {losses[len(losses) - 1]}, groups: {i}\n')
        if groups_a_l[i][1] == losses[len(losses) - 2]:
            print(f'Second highest loss: {losses[len(losses) - 2]}, groups: {i}\n')

    finish = time.time()

    print(groups_a_l)

    print('Total seconds passed: %.3f' % (finish - start))

    x = losses
    y = []

    for i in x:
        for j in groups_a_l:
            if groups_a_l[j][1] == i:
                y.append(groups_a_l[j][0])

    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    mnist_cnn()
