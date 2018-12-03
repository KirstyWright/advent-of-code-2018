import itertools

# Part 1
file = open("input.txt", "r")
action_list = file.read().split()

frequency = 0
for line in action_list:
    frequency += int(line)

print(frequency)

# Part 2
frequency = 0
results = {0}
for line in itertools.cycle(action_list):
    frequency += int(line)
    if frequency in results:
        print(frequency)
        break
    results.add(frequency)
