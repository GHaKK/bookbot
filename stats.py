
def sort_on(dict):
    return dict["num"]


def get_num_words(text):
    return len(text.split())


def get_num_char(text):
    char_dict = {}
    lowered_text = text.lower()

    for i in lowered_text:
        try:
            char_dict[i] += 1
        except KeyError:
            char_dict[i] = 1
    return char_dict


def get_sorted_list(char_dict):
    result_list = []
    for key, value in char_dict.items():
        if key.isalpha():
            result_list.append({'char': key, 'num': value})

    result_list.sort(reverse=True, key=sort_on)
    return result_list


