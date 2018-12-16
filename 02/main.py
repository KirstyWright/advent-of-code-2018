import collections

# Part 1
file = open("input.txt", "r")
box_list = file.read().split()
duplicate3_count = 0
duplicate2_count = 0

for word in box_list:
    letters = collections.defaultdict(int)
    for character in list(word):
        letters[character] += 1
    values = letters.values()
    if 2 in values:
        duplicate2_count += 1
    if 3 in values:
        duplicate3_count += 1

print(duplicate2_count * duplicate3_count)

# Part 2
final_compare = None
for word in box_list:
    characters = list(word)
    box_list.remove(word)  # Don't want to compare everything twice
    for compare_word in box_list:
        compare_characters = list(compare_word)

        count = 0
        non_matching_count = 0
        while count < len(word):
            if characters[count] != compare_characters[count]:
                if non_matching_count == 1:
                    non_matching_count += 1
                    break  # This is the second mismatch
                non_matching_count += 1  # Found one mismatch

            count += 1
        if (non_matching_count == 1):
            final_compare = [word, compare_word]
            break

if final_compare:
    final_edit = final_compare[0]
    print(final_edit)
    final_compare[0] = list(final_compare[0])
    final_compare[1] = list(final_compare[1])
    while count < len(word[0]):
        if (final_compare[0][count] != final_compare[1][count]):
            final_edit.remove(count)
        count += 1
print(final_edit)
# print(''.join(final_compare[0]))
