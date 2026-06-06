from torchvision import transforms
transform=transforms.RandomErasing(p=1.0)
x=torch.randn(
    3,
    224,
    224
)
output=transform(x)

print(
    x.shape,
    "\n",
    output.shape
)