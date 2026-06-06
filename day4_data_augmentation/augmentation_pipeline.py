from torchvision import transforms
transform=transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),

    transforms.ColorJitter(
        brightness=0.2,
        contrast=0.2
    ),
    transforms.ToTensor(),
    transforms.RandomErasing(p=1.0),
    transforms.Normalize(
        mean=[0.5],
        std=[0.5]
    )
])