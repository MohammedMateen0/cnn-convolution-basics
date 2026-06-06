# Week 10 Day 5 - Object Detection Fundamentals

## Overview

Image classification answers:

```text
What is in this image?
```

Object detection answers:

```text
What is in this image?
AND
Where is it located?
```

Unlike image classification, object detection predicts both the class label and the location of objects using bounding boxes.

This project introduces the mathematical foundations behind modern object detection systems such as YOLO, Faster R-CNN, SSD, RetinaNet, and DETR.

---

## Why Object Detection?

Image Classification:

```text
Image
↓
Cat
```

Object Detection:

```text
Image
↓
Cat    (x1,y1,x2,y2)
Dog    (x1,y1,x2,y2)
Person (x1,y1,x2,y2)
```

Applications:

* Self-driving cars
* CCTV surveillance
* Face detection
* Traffic monitoring
* Medical imaging
* Manufacturing inspection

---

# Bounding Boxes

Object detectors locate objects using bounding boxes.

Standard format:

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

Example:

```text
(20,10,80,70)
```

---

## Bounding Box Dimensions

Width:

```text
width = x2 - x1
```

Height:

```text
height = y2 - y1
```

Example:

```text
Box:
(20,10,80,70)

Width:
80 - 20 = 60

Height:
70 - 10 = 60
```

Result:

```text
Width = 60
Height = 60
```

---

# Intersection over Union (IoU)

IoU measures overlap between:

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
Ground Truth Area
+
Predicted Area
-
Intersection Area
```

---

## Example

Ground Truth:

```text
Area = 100
```

Prediction:

```text
Area = 100
```

Intersection:

```text
Area = 50
```

Union:

```text
100 + 100 - 50
=
150
```

IoU:

```text
50 / 150
=
0.333
```

---

## IoU Interpretation

```text
IoU = 0
```

No overlap.

---

```text
IoU = 1
```

Perfect overlap.

---

```text
IoU > 0.5
```

Often considered a valid detection.

---

# Non-Maximum Suppression (NMS)

Object detectors frequently predict multiple boxes for the same object.

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
1 Cat
```

---

## NMS Process

Step 1:

Keep highest confidence box.

```text
Cat : 0.95
```

---

Step 2:

Calculate IoU with remaining boxes.

---

Step 3:

Remove highly overlapping lower-confidence boxes.

Final Result:

```text
Keep:
0.95

Remove:
0.90
0.30
```

---

# Detection Evaluation Metrics

Object detection evaluation uses:

* True Positives
* False Positives
* False Negatives

---

## True Positive (TP)

Correct detection.

Example:

```text
Real Cat
Detected Cat
```

---

## False Positive (FP)

Incorrect detection.

Example:

```text
No Cat Present
Detected Cat
```

---

## False Negative (FN)

Missed object.

Example:

```text
Real Cat Present
No Detection
```

---

# Precision

Measures detection quality.

Formula:

```text
Precision =
TP / (TP + FP)
```

Example:

```text
TP = 2
FP = 1
```

Result:

```text
2 / 3
=
0.67
```

Interpretation:

```text
Of all detections,
how many were correct?
```

---

# Recall

Measures detection completeness.

Formula:

```text
Recall =
TP / (TP + FN)
```

Example:

```text
TP = 2
FN = 0
```

Result:

```text
1.0
```

Interpretation:

```text
Of all real objects,
how many were found?
```

---

# Precision vs Recall Trade-Off

High Precision:

```text
Few False Positives
```

High Recall:

```text
Few False Negatives
```

---

## Medical Example

Detector A:

```text
Precision = 0.95
Recall = 0.40
```

Detector B:

```text
Precision = 0.80
Recall = 0.90
```

Preferred:

```text
Detector B
```

Reason:

```text
Missing a cancer patient
is more dangerous than
a false alarm.
```

Medical systems usually prioritize recall.

---

# Mean Average Precision (mAP)

Modern object detectors are evaluated using:

```text
mAP
```

Mean Average Precision combines:

* Precision
* Recall
* IoU thresholds

into a single metric.

Examples:

```text
mAP@0.5
mAP@0.5:0.95
```

Higher values indicate better object detection performance.

---

# Coding Experiments

## bounding_box_demo.py

Concepts:

* Bounding box coordinates
* Width calculation
* Height calculation

Output:

```text
Width = 60
Height = 60
```

---

## iou_calculator.py

Concepts:

* Intersection area
* Union area
* IoU computation

Output:

```text
IoU = 0.33
```

(Example value)

---

## precision_recall_demo.py

Concepts:

* Precision calculation
* Recall calculation

Output:

```text
Precision = 0.67
Recall = 1.00
```

---

## NMS Intuition Demo

Concepts:

* Confidence scores
* Best box selection
* Duplicate removal

Output:

```text
('Cat', 0.95)
```

---

# Key Learnings

* Object detection predicts class and location.
* Bounding boxes localize objects.
* IoU measures overlap quality.
* NMS removes duplicate detections.
* Precision measures correctness.
* Recall measures completeness.
* Medical applications often prioritize recall.
* mAP is the standard object detection metric.
* IoU and NMS are fundamental to modern detectors.

---

# Project Structure

```text
week10_day5_object_detection_basics/
│
├── bounding_box_demo.py
├── iou_calculator.py
├── precision_recall_demo.py
└── README.md
```

---

# Next Step

Week 10 Day 6:

* R-CNN
* Fast R-CNN
* Faster R-CNN
* Region Proposal Networks (RPN)
* YOLO Architecture
* Single-Stage vs Two-Stage Detectors
* Real-Time Object Detection
* Detection Pipelines
* YOLOv8 Overview
