import torch
import torch.nn as nn
import torch.nn.functional as F


class CifarModel(nn.Module):
    """"
    The ANN build using PyTorch library.
    """

    def __init__(self):
        """
        The class constructor.
        """
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=(3, 3))
        self.conv2 = nn.Conv2d(32, 64, kernel_size=(3, 3))
        self.conv2 = nn.Conv2d(64, 32, kernel_size=(3, 3))
        self.batch_norm = nn.BatchNorm2d(32)
        self.dropout = nn.Dropout(0.25)
        self.leaky_relu = nn.LeakyReLU()
        self.softmax = nn.Softmax()

    def forward(self, x):
        """
        The forward pass.
        :return: None
        """
        x = self.conv1(x)
        x = self.batch_norm(x)
        x = x.view(x.size(0), -1)
        x = self.leaky_relu(x)
        x = x.view(x.size(0), -1)
        x = self.batch_norm(x)
        x = self.dropout(x)
        x = self.softmax(x)

        return x







