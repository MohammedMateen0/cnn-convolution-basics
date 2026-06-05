import torch
import torch.nn as nn

x=torch.randn(
    1,
    1,
    28,
    28
)

conv=nn.Conv2d(
    in_channels=1,
    out_channels=32,
    kernel_size=3,
    padding=1
)

output=conv(x)

print("Input Shape:",x.shape,
      "\nOutput Shape:",output.shape)