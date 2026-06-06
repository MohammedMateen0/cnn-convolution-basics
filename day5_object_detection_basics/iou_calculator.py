def calculate_iou(
    box1,
    box2
):
    x1=max(
        box1[0],
        box2[0]
    )
    y1=max(
        box1[1],
        box2[1]
    )
    x2=min(
        box1[2],
        box2[2]
    )
    y2=min(
        box1[3],
        box2[3]
    )
    intrsection=max(
        0,
        x2-x1
    )* max(
        0,
        y2-y1
    )
    area1=(
        box1[2]-box1[0]
    )*(
        box1[3]-box1[1]
    )
    area2=(
        box2[2]-box2[0]
    )*(
        box2[3]-box2[1]
    )
    union=(area1+area2-intrsection)

    return intrsection/union

box1=(20,10,80,70)
box2=(40,20,90,80)

print(calculate_iou(
    box1,
    box2
))