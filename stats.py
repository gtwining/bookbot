def count_words(text):
    wordcount = 0
    words = text.split()
    for word in words:
        wordcount +=1
    
    return wordcount

def count_characters(book):
    char_count = {}
    lower_book = book.lower()
    for char in lower_book:
        if char not in char_count:
            char_count[char] = 1 
        else: 
            char_count[char] +=1
    return char_count

def sort_on(item):
    return item['num']

def sort_dict(dictionary):
    sorted_list  =[]

    for key in dictionary:
         new_dict = {"char":key, "num":dictionary[key]}
         sorted_list.append(new_dict)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list