
def main():
    path = "books/frankenstein.txt"
    book = get_book(path)
    word_num = get_num_words(book)
    count_letter = count_letters(book)
    get_report(path, book)

def get_num_words(book):
    words = book.split()
    return len(words)

def get_book(path):
    with open(path) as f:
        return f.read()

def count_letters(book):
    cl = {}

    for c in book.lower():
        if c in cl:
            cl[c] += 1
        else:
            cl[c] = 1

    return cl

def get_report(path, book):

    number_words = get_num_words(book)
    count_letter = list(count_letters(book).items())
    sorted_count_letter = count_letter.sort(reverse=True, key=lambda x: x[1])

    print(f"--- Begin report of {path} ---")
    print(f"{number_words} words found in the document")

    for c in count_letter:
        if c[0].isalpha():
            print(f"The '{c[0]}' character was found {c[1]} times")

    print(f"--- End Report ---")

main()