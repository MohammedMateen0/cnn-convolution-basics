# Object Detection Metrics Simulator

## Overview

Object detection is one of the most important tasks in computer vision. Unlike image classification, object detection must answer two questions:

```text
What object is present?
Where is the object located?
```

Modern object detectors such as YOLO, Faster R-CNN, SSD, RetinaNet, and DETR rely on mathematical concepts like Bounding Boxes, Intersection over Union (IoU), Non-Maximum Suppression (NMS), Precision, and Recall.

This project implements these core concepts from scratch using Python.

---

## Project Goal

Build a simplified object detection evaluation pipeline:

```text
Predicted Bounding Boxes
            ↓
      IoU Calculation
            ↓
 Non-Maximum Suppression
            ↓
   TP / FP / FN Counts
            ↓
 Precision & Recall
```

The objective is to understand the mathematics behind object detection before using advanced frameworks.

---

## Features

### Bounding Box Representation

Store object coordinates and confidence scores.

Example:

```text
(20,10,80,70)
```

Format:

```text
(x1, y1, x2, y2)
```

Where:

```text
x1 = left coordinate
y1 = top coordinate
x2 = right coordinate
y2 = bottom coordinate
```

---

### Bounding Box Properties

Automatically compute:

```text
Width
Height
Area
```

Formulas:

```text
Width  = x2 - x1
Height = y2 - y1

Area = Width × Height
```

---

### Intersection over Union (IoU)

Measures overlap between:

```text
Ground Truth Box
```

and

```text
Predicted Box
```

Formula:

```text
IoU = Intersection / Union
```

Where:

```text
Union =
Area(Box1)
+
Area(Box2)
-
Intersection
```

Interpretation:

```text
IoU = 0.0 → No overlap

IoU = 1.0 → Perfect overlap

IoU > 0.5 → Common detection threshold
```

---

### Non-Maximum Suppression (NMS)

Object detectors often predict multiple boxes for the same object.

Example:

```text
Cat : 0.95

Cat : 0.90

Cat : 0.30
```

Without NMS:

```text
3 Cats Detected
```

Reality:

```text
1 Cat Present
```

NMS:

```text
Keep Highest Confidence Box
↓
Remove Highly Overlapping Boxes
↓
Final Detection
```

---

### Detection Metrics

#### True Positive (TP)

Correct detection.

```text
Real Cat
Detected Cat
```

---

#### False Positive (FP)

Incorrect detection.

```text
No Cat
Detected Cat
```

---

#### False Negative (FN)

Missed object.

```text
Real Cat
No Detection
```

---

### Precision

Measures prediction quality.

Formula:

```text
Precision =
TP / (TP + FP)
```

Example:

```text
TP = 2
FP = 1

Precision = 0.67
```

---

### Recall

Measures prediction completeness.

Formula:

```text
Recall =
TP / (TP + FN)
```

Example:

```text
TP = 2
FN = 0

Recall = 1.00
```

---

## Project Structure

```text
object_detection_metrics/
│
├── bounding_box.py
├── iou.py
├── nms.py
├── metrics.py
├── demo.py
│
└── README.md
```

---

## Module Description

### bounding_box.py

Defines the BoundingBox class.

Responsibilities:

* Store coordinates
* Store confidence scores
* Compute width
* Compute height
* Compute area

---

### iou.py

Implements:

```python
calculate_iou()
```

Responsibilities:

* Calculate intersection area
* Calculate union area
* Return IoU score

---

### nms.py

Implements:

```python
non_max_suppression()
```

Responsibilities:

* Sort boxes by confidence score
* Keep highest confidence box
* Remove overlapping boxes
* Return filtered detections

---

### metrics.py

Implements:

```python
precision()
recall()
```

Responsibilities:

* Detection evaluation
* Performance measurement

---

### demo.py

Demonstrates:

* Bounding Box creation
* IoU calculation
* NMS filtering
* Precision calculation
* Recall calculation

---

## Example Output

```text
IoU: 0.53

Boxes after NMS: 1

Precision: 0.67

Recall: 1.00
```

(Note: IoU may vary depending on box coordinates.)

---

## Learning Outcomes

After completing this project, you should understand:

* Bounding Box Representation
* Bounding Box Dimensions
* Area Calculation
* Intersection Area
* Union Area
* Intersection over Union (IoU)
* Non-Maximum Suppression (NMS)
* True Positives
* False Positives
* False Negatives
* Precision
* Recall

---

## Why This Project Matters

Every modern object detector uses these concepts.

Examples:

```text
YOLO
Faster R-CNN
SSD
RetinaNet
DETR
```

Before training large detection models, it is important to understand the evaluation pipeline and the mathematics behind object detection.

This project provides that foundation.

---

## Future Improvements

Possible extensions:

* Visualize bounding boxes using OpenCV
* Draw detections on images
* Multi-class detection support
* mAP calculation
* IoU threshold tuning
* COCO-style evaluation
* YOLO prediction parser

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* NumPy (optional)
* Computer Vision Fundamentals

---

## Key Takeaway

Object detection is more than classification. A successful detector must:

```text
Find Objects
↓
Locate Objects
↓
Remove Duplicate Detections
↓
Evaluate Detection Quality
```

Understanding IoU, NMS, Precision, and Recall is the foundation for mastering modern object detection systems.
