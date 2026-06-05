# Week 10 Day 3 - Transfer Learning and Fine-Tuning

## Overview

Training a deep CNN from scratch requires millions of images, large computational resources, and significant training time.

In real-world machine learning projects, models are rarely trained from scratch. Instead, pretrained models such as ResNet, EfficientNet, ConvNeXt, and Vision Transformers are adapted to new tasks through transfer learning.

This project introduces transfer learning, feature extraction, fine-tuning, discriminative learning rates, and the practical workflow used by ML engineers in production.

---

## Why Transfer Learning?

Large datasets such as ImageNet contain over one million labeled images.

Models trained on ImageNet learn useful visual representations that can be reused for new tasks.

Examples:

* Medical image classification
* Traffic camera analysis
* Manufacturing defect detection
* Plant disease recognition
* Satellite image classification

Instead of learning everything from scratch, we reuse previously learned visual features.

---

## Why ImageNet Features Transfer

CNNs learn features hierarchically.

### Early Layers

Learn universal patterns:

```text
Edges
Corners
Lines
Curves
Textures
```

These patterns appear in almost every image domain.

---

### Middle Layers

Learn combinations of low-level features.

Examples:

```text
Shapes
Object parts
Patterns
```

---

### Deep Layers

Learn task-specific concepts.

Examples:

```text
Dog Face
Car Wheel
Bird Wing
```

These features are more specialized and less transferable.

---

## Transfer Learning Workflow

### Phase 1: Feature Extraction

Freeze all pretrained layers.

Train only the classification head.

```text
Pretrained Backbone
↓
Frozen
↓
New Classifier Head
↓
Train
```

Benefits:

* Fast training
* Reduced overfitting
* Requires less data

---

### Phase 2: Fine-Tuning

After the classifier head learns the task:

```text
Unfreeze Layers
↓
Small Learning Rate
↓
Continue Training
```

Benefits:

* Better adaptation to new data
* Higher final accuracy
* Retains useful pretrained knowledge

---

## Feature Extraction

Freeze all pretrained parameters:

```python
for param in model.parameters():
    param.requires_grad = False
```

Only the new classifier head remains trainable.

Example:

```python
model.fc = nn.Linear(
    2048,
    2
)
```

Trainable parameters:

```text
Only FC Layer
```

---

## Fine-Tuning

Unfreeze selected layers.

Example:

```python
for param in model.layer4.parameters():
    param.requires_grad = True
```

Now:

```text
Layer4
FC Layer
```

can learn from the new dataset.

---

## Why Use Small Learning Rates?

Pretrained weights already contain useful information.

Using a large learning rate may destroy these learned features.

Bad:

```text
Large Updates
↓
Forget Useful Features
↓
Performance Drops
```

Good:

```text
Small Updates
↓
Gradual Adaptation
↓
Better Generalization
```

This helps prevent catastrophic forgetting.

---

## Catastrophic Forgetting

A pretrained network contains valuable information learned from ImageNet.

Large parameter updates may overwrite this knowledge.

Example:

```text
Good Edge Detector
↓
Large Gradient Update
↓
Poor Edge Detector
```

Fine-tuning uses small learning rates to preserve useful representations.

---

## Discriminative Learning Rates

Different layers receive different learning rates.

Example:

```python
optimizer = torch.optim.AdamW(
    [
        {
            "params": model.layer4.parameters(),
            "lr": 1e-5
        },
        {
            "params": model.fc.parameters(),
            "lr": 1e-3
        }
    ]
)
```

Reason:

```text
Early Layers
↓
General Features
↓
Small Learning Rate

Late Layers
↓
Task-Specific Features
↓
Larger Learning Rate
```

---

## Replacing the Classification Head

Original ResNet:

```python
nn.Linear(
    2048,
    1000
)
```

Output:

```text
1000 ImageNet Classes
```

For a new task:

```text
Cat
Dog
Rabbit
```

Replace with:

```python
nn.Linear(
    2048,
    3
)
```

Output:

```text
3 Logits
```

The final layer must match the number of target classes.

---

## Data Augmentation

Transfer learning often works with small datasets.

Data augmentation artificially increases data diversity.

Common augmentations:

```text
Random Horizontal Flip
Random Rotation
Random Crop
Color Jitter
Random Resized Crop
```

Benefits:

* Reduces overfitting
* Improves generalization
* Creates more robust models

---

## torchvision Models

PyTorch provides pretrained models through torchvision.

Example:

```python
from torchvision.models import (
    resnet50,
    ResNet50_Weights
)

model = resnet50(
    weights=ResNet50_Weights.DEFAULT
)
```

Popular pretrained models:

```text
ResNet
EfficientNet
MobileNet
ConvNeXt
Vision Transformer (ViT)
```

---

## torch.hub

Community models can be loaded through:

```python
torch.hub.load(...)
```

Common sources:

```text
timm
Hugging Face
Research Repositories
```

Provides access to many state-of-the-art architectures.

---

## Coding Experiments

### pretrained_resnet_demo.py

Demonstrates:

* Loading pretrained ResNet50
* Exploring architecture components

Key Components:

```text
conv1
bn1
layer1
layer2
layer3
layer4
fc
```

---

### feature_extraction_demo.py

Demonstrates:

* Freezing pretrained layers
* Replacing classifier head
* Counting trainable parameters

Key Concept:

```text
Only FC Layer Trains
```

---

### fine_tuning_demo.py

Demonstrates:

* Unfreezing selected layers
* Discriminative learning rates
* Fine-tuning workflow

Key Concept:

```text
layer4 → small LR
fc → larger LR
```

---

## Key Learnings

* Transfer learning is the standard approach for vision tasks.
* Early CNN layers learn universal visual features.
* Feature extraction freezes the pretrained backbone.
* Fine-tuning adapts pretrained features to new tasks.
* Small learning rates preserve useful pretrained knowledge.
* Discriminative learning rates improve optimization.
* Classification heads must match the target classes.
* Data augmentation is critical for small datasets.
* torchvision provides pretrained ImageNet models.
* Fine-tuning is significantly more efficient than training from scratch.

---

## Project Structure

```text
week10_day3_transfer_learning/
│
├── pretrained_resnet_demo.py
├── feature_extraction_demo.py
├── fine_tuning_demo.py
└──  README.md

```

---

## Next Step

Week 10 Day 4:

* Object Detection Fundamentals
* Bounding Boxes
* IoU (Intersection over Union)
* Non-Maximum Suppression (NMS)
* R-CNN Family
* YOLO Architecture
* Detection Metrics (mAP)
* Real-World Detection Pipelines
