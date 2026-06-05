from torchvision.models import (
    resnet50,
    ResNet50_Weights
)
import torch
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
for param in model.layer4.parameters():
    param.requires_grad=True

optimizer=torch.optim.AdamW(
    [
        {
            "params":model.layer4.parameters(),
            "lr":1e-5
        },
        {
            "params":model.fc.parameters(),
            "lr":1e-3
        }
    ]
)
print(optimizer)