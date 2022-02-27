scores1 = [10, 11, 15, 20, 55, 76, 90, 84]
scores2 = [4, 9, 12, 98, 35, 42, 4, 5, 10]
avg1 = float(sum(scores1) / len(scores1))
avg2 = float(sum(scores2) / len(scores2))
maxNum = max(max(scores1), max(scores2))
maxAvg = max(avg1, avg2)
print("Highest Avg: {0:.0f} ".format(maxAvg))
print("Highest Score: ", maxNum)