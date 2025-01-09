def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    #get_word_count(text)
    count_characters(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    count = len(words)
    print(f"\n The amount of words in the text is: {count}")

def count_characters(text):
    amount = {}
    lowercase = text.lower()
    for character in lowercase:
        if (character in amount):
            amount[character] += 1
        else:
            amount[character] = 1
    print(amount)

main()