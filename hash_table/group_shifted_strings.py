import string


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        letter_value = {}
        value = 0
        for letter in string.ascii_lowercase:
            value += 1
            letter_value[letter] = value
        sequence_strings = {}
        for my_str in strings:
            length = len(my_str)
            distance = []
            str_list = list(my_str)
            for i in range(length - 1):
                distance.append((letter_value[str_list[i + 1]] - letter_value[str_list[i]]) % 26)
            shift_sequence = (length, tuple(distance))
            sequence_strings.setdefault(shift_sequence, []).append(my_str)
        return list(sequence_strings.values())
