def main():
    book_path = "books/frankenstein.txt"
    make_a_report(book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    count = len(words)
    #print(f"\n The amount of words in the text is: {count}")
    return count

def get_char_dict(text):
    amount = {}
    lowercase = text.lower()
    for character in lowercase:
        if (character in amount):
            amount[character] += 1
        else:
            amount[character] = 1
    return amount

def sort_on(dictionary):
    return dictionary["num"]

def make_a_report(path):
    text = get_book_text(path)
    count = get_word_count(text)
    dictionary = get_char_dict(text)
    print(f"--- Begin report of {path} ---")
    print(f"{count} words were found in the document \n")
    
    entries = []
    for key in dictionary:
        entries.append({"name":key, "num":dictionary[key]})
    entries.sort(reverse=True, key=sort_on)

    for character in entries:
        if (character["name"].isalpha()):
            print(f"The {character["name"]} character was found {character["num"]} times")
    
    print("--- End report ---")

    #If you wanna read the book, delete the commentary:
    #print(text)

    
main()