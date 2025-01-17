def main ():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lower_text = text.lower()
    char_histogram = get_char_dist(lower_text)

    print(f"{get_num_words(text)} words found in the document")
    print()
    sorted_histogram = sorted(char_histogram, key=char_histogram.get, reverse=True)
    for char in sorted_histogram:
        if char >= 'a' and char <= 'z':
            print(f"The '{char}' character was found {char_histogram[char]} times")

def get_char_dist(text):
    c_histogram = {}
    for char in text:
        if char not in c_histogram:
            c_histogram[char] = 1
        else:
            c_histogram[char] += 1
    return c_histogram

def get_num_words(text):
    words = text.lower().split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

