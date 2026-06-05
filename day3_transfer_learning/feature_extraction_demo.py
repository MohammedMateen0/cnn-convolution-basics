from torchvision.models import (
    resnet50,
    ResNet50_Weights
)

import torch.nn as nn

model=resnet50(
    weights=ResNet50_Weights.DEFAULT
)

for param in model.parameters():
    param.requires_grad=False

num_features=model.fc.in_features

model.fc=nn.Linear(
    num_features,
    2
)
trainable_params=sum(
    p.numel()
    for p in model.parameters()
    if p.requires_grad
)
print(f"Trainable Parameters: {trainable_params}")