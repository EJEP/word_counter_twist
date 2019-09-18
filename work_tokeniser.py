import argparse

def read_the_file(fname):

    with open(fname) as the_file:
        lines = the_file.readlines()

    return lines

def count_words(lines):

    words = {}
    previous_word = ''
    numbers = {'two':2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
               'seven': 7, 'eight': 8, 'nine': 9}

    for line in lines:
        for word in line:
            word = word.lower()
            if word in numbers:
                words[previous_word] += numbers[word] - 1
            else:
                if word not in words:
                    words[word] = 1
                else:
                    words[word] += 1
            previous_word = word
    return words

def get_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('in_fname', help='Input filename')

    return parser.parse_args()

def main():

    args = get_args()
    lines = read_the_file(args.in_fname)

    lines = [line.strip().split(' ') for line in lines]

    counted_words = count_words(lines)

    counted_words = [(word, count) for word, count in counted_words.items()]

    counted_words.sort(key=lambda x: x[0])
    counted_words.sort(key=lambda x: x[1], reverse=True)

    for word_count in counted_words[:5]:
        print(word_count[0] + ': ' + str(word_count[1]))
if __name__ == '__main__':
    main()
