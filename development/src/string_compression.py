'''
Implement a method to perform basic string compression
using the counts of repeated characters.
'''


def string_compression(input_string):
    '''
    Perform string compression such that
    the string aabcccccaaa would become a2b1c5a3
    '''
    output = []
    prev_char = input_string[0]
    prev_char_occurrences = 0
    for char in input_string:
        if prev_char == char:
            prev_char_occurrences += 1
        else:
            output.append(f'{prev_char}{prev_char_occurrences}')
            prev_char = char
            prev_char_occurrences = 1
    output.append(f'{prev_char}{prev_char_occurrences}')
    output_string = ''.join(output)
    return input_string if len(output_string) >= len(
        input_string) else output_string


def main():
    '''Main function'''
    assert string_compression('aabcccccaaa') == 'a2b1c5a3'
    assert string_compression('abc') == 'abc'
    assert string_compression('aaaaaaabc') == 'a7b1c1'
    test_input = 'aabcccccaaa'
    print(
        f'String compression of {test_input}: {string_compression(test_input)}')


if __name__ == '__main__':
    main()
