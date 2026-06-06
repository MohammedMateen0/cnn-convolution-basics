TP=2
FP=1
FN=0

precision=TP/(
    TP+FP
)

recall=TP/(
    TP+FN
)

print(
    f"Precision={precision:.2f}"
)

print(
    f"Recall={recall:.2f}"
)