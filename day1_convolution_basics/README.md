# Week 10 Day 1 - Convolution Fundamentals

## Overview

This project introduces the core concepts behind Convolutional Neural Networks (CNNs). The goal is to understand how convolution works mathematically, why CNNs are more efficient than fully connected networks for images, and how filters detect spatial patterns.

Unlike a Multi-Layer Perceptron (MLP), which flattens images into a 1D vector, CNNs preserve the spatial structure of images and learn local features such as edges, corners, curves, and textures.

---

## Why CNNs?

In the MNIST MLP project, images were flattened:

```text
28 × 28
↓
784
```

Flattening removes spatial relationships between neighboring pixels.

For image recognition, the arrangement of pixels is important because patterns such as edges and shapes depend on local neighborhoods.

CNNs preserve:

* Height
* Width
* Channels

allowing the network to learn meaningful visual features.

---

## Concepts Covered

### Convolution

A convolution applies a small filter (kernel) to an image.

Process:

1. Place filter on a local region.
2. Multiply corresponding values.
3. Sum the results.
4. Store the output value.
5. Slide the filter and repeat.

This operation produces a feature map.

---

### Filter / Kernel

A filter is a small learnable matrix.

Examples:

```text
3 × 3
5 × 5
```

Filters learn patterns such as:

* Vertical edges
* Horizontal edges
* Curves
* Corners
* Textures

---

### Feature Map

The output of a filter applied across an image.

Example:

```text
Input Image
↓
Filter
↓
Feature Map
```

Each filter produces one feature map.

Multiple filters produce multiple feature maps.

---

### Parameter Sharing

A single filter is reused across the entire image.

Instead of learning separate weights for every location, CNNs share the same weights everywhere.

This dramatically reduces the number of parameters.

---

## CNN vs MLP Parameters

### Fully Connected Layer

```python
nn.Linear(784, 256)
```

Parameters:

```text
784 × 256 + 256
=
200,960
```

---

### Convolution Layer

```python
nn.Conv2d(
    in_channels=1,
    out_channels=32,
    kernel_size=3
)
```

Parameters per filter:

```text
3 × 3 × 1 + 1
=
10
```

Total:

```text
32 × 10
=
320
```

CNNs use far fewer parameters while preserving spatial information.

---

## Output Size Formula

For a convolution layer:

```text
Output Size

= floor((W - F + 2P) / S) + 1
```

Where:

* W = Input Width/Height
* F = Filter Size
* P = Padding
* S = Stride

---

### Example

Input:

```text
28 × 28
```

Filter:

```text
3 × 3
```

Padding:

```text
0
```

Stride:

```text
1
```

Output:

```text
26 × 26
```

---

## Stride

Stride controls how many pixels the filter moves each step.

### Stride = 1

```text
Largest output size
Most detail preserved
```

### Stride = 2

```text
Smaller output size
Faster computation
```

Example:

```text
28 × 28
↓
13 × 13
```

---

## Padding

Padding adds zeros around the border of an image.

Purpose:

* Preserve spatial dimensions
* Allow filters to process edge pixels

Example:

```text
kernel_size = 3
padding = 1
```

Output size remains unchanged.

```text
28 × 28
↓
28 × 28
```

This is called:

```text
Same Padding
```

---

## Channels

### Grayscale Image

```text
Channels = 1
```

Shape:

```text
1 × 28 × 28
```

---

### RGB Image

```text
Channels = 3
```

Shape:

```text
3 × H × W
```

Representing:

* Red
* Green
* Blue

---

## Coding Experiments

### conv_output_shapes.py

Purpose:

* Observe input and output shapes.
* Understand how Conv2D changes tensor dimensions.

Key Result:

```text
Input:
1 × 28 × 28

Output:
32 × 28 × 28
```

---

### conv_parameters.py

Purpose:

* Calculate the number of learnable parameters in a convolution layer.

Key Result:

```text
Conv2d(1, 32, kernel_size=3)

Parameters = 320
```

---

## Key Learnings

* CNNs preserve spatial information.
* Convolution is a sliding-window dot product.
* Filters learn useful visual patterns.
* Each filter produces one feature map.
* Multiple filters create multiple channels.
* Parameter sharing makes CNNs efficient.
* Stride controls output size.
* Padding preserves spatial dimensions.
* Output size can be calculated analytically.
* CNNs require far fewer parameters than fully connected networks.

---

## Files

```text
week10_day1_convolution_basics/
│
├── conv_output_shapes.py
├── conv_parameters.py
└── README.md
```

---

## Next Step

Week 10 Day 2:

* Max Pooling
* Pooling Layers
* Building the First CNN
* Conv2D + ReLU + MaxPool2D
* CNN for MNIST Classification
