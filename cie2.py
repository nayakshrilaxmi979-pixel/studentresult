
import sys

m1 = int(sys.argv[1])
m2 = int(sys.argv[2])
m3 = int(sys.argv[3])

total = m1 + m2 + m3
average = total / 3
percentage = (total / 300) * 100

print("Total Marks:", total)
print("Average:", average)
print("Percentage:", percentage)

