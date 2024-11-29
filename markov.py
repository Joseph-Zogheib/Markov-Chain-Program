initial = 40
second = 10

def calculate():
    global initial, second
    enrolled = 0.90 * initial + 0.20 * second
    switched = 0.10 * initial + 0.80 * second
    print(f"After day {i+1}:")
    print(f"  Enrolled: {enrolled:.2f}")
    print(f"  Switched Out: {switched:.2f}")
    initial = enrolled
    second = switched

print("Initially:")
print("  Enrolled: " + str(initial))
print("  Switched Out: " + str(second))

initial = 40
second = 10


for i in range(30):
    calculate()
