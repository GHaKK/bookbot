def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_characters(text)
    chars_sorted_list = sorted_dict(chars_dict)

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']} character was found {item['num']} times")


def get_book_text(book):
    with open(book) as f:
        return f.read()


def get_num_words(text):
    return text.split()


def get_num_characters(text):
    chars = {}
    for c in text:
        working_text = c.lower()
        if working_text in chars:
            chars[working_text] += 1
        else:
            chars[working_text] = 1
    
    return chars


def sort_on(d):
    return d["num"]


def sorted_dict(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



if __name__ == "__main__":
    main()
