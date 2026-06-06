def calculate_iou(
    box1,
    box2
):
    x1=max(
        box1.x1,
        box2.x1
    )
    y1=max(
        box1.y1,
        box2.y1
    )
    x2=min(
        box1.x2,
        box2.x2
    )
    y2=min(
        box1.y2,
        box2.y2
    )
    intersection=max(
        0,
        x2-x1
    )*max(
        0,
        y2-y1
    )

    union=(
        box1.area+
        box2.area-
        intersection
    )

    return intersection/union