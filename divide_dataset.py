import torchvision
import torchvision.transforms as transforms
import group_dataset


def divide_dataset():

    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

    train_set = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    test_set = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

    groups = [[1, 2, 4, 5, 7], [0, 3, 6, 8, 9]]

    train_d_set = group_dataset.GroupDataset(train_set, groups)
    test_d_set = group_dataset.GroupDataset(test_set, groups)

    return train_d_set, test_d_set
