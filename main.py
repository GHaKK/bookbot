from stats import get_num_words
from stats import get_num_char
from stats import get_sorted_list
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    str_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(str_text)
    num_char = get_num_char(str_text)
    sorted_list = (get_sorted_list(get_num_char(str_text)))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(len(sorted_list)):
        print(f"{sorted_list[i]['char']}: {sorted_list[i]['num']}")
    print("============= END ===============")
    
main()
