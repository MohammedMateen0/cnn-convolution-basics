from iou import calculate_iou

def non_max_suppression(
        boxes,
        threshold=0.5
):
    boxes=sorted(
        boxes,
        key=lambda x:x.score,
        reverse=True
    )
    keep=[]

    while boxes:
        best=boxes.pop(0)
        keep.append(best)

        boxes=[
            box
            for box in boxes
            if calculate_iou(
                best,
                box
            ) < threshold
        ]
    return keep