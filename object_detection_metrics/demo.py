from bounding_box import BoundingBox
from iou import calculate_iou
from nms import non_max_suppression
from metrics import (
    precision,
    recall
)

box1=BoundingBox(
    20,
    10,
    80,
    70,
    0.95
)

box2=BoundingBox(
    25,
    15,
    85,
    75,
    0.90
)
print(
    "IoU:",
    calculate_iou(
        box1,
        box2
    )
)

boxes=[
    box1,
    box2
]

filtered=non_max_suppression(
    boxes
)
print(
    "Boxes after NMS:",
    len(filtered)
)
tp=2
fp=1
fn=0

print(
    "Precision:",
    precision(
        tp,
        fp
    ),
    "\nRecall",
    recall(
        tp,
        fn
    )
)