scores = [87, 45, 92, 58, 76, 100, 64, 73, 89, 34, 51, 68, 95, 81, 49, 62, 77, 90, 43, 56, 85, 70, 94, 37, 88, 66, 99, 48, 60, 72]

print(sum(scores))

print(max(scores))
max = scores[0]
for score in scores:
    if score > max:
        max = score
print(max)