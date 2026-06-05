import torch
import torch.nn as nn

x=torch.randn(
    1,
    64,
    7,
    1
)

gap=nn.AdaptiveAvgPool2d(
    (1,1)
)

output=gap(x)

print(output.shape)