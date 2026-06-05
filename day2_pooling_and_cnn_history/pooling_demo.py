import torch
import torch.nn as nn

x=torch.tensor([
    [[
        [1.,5.,2.,4.],
        [7.,3.,8.,1.],
        [2.,9.,6.,5.],
        [4.,1.,7.,3.]
    ]]
])

pool=nn.MaxPool2d(
    kernel_size=2,
    stride=2

)

print(pool(x))