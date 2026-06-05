import torch.nn as nn

conv=nn.Conv2d(
    in_channels=1,
    out_channels=32,
    kernel_size=3
)

total_params=sum(
    p.numel()
    for p in conv.parameters()
)
print(f"Parameters :{total_params}")