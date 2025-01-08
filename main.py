def main():
    print(create_report())

def read_file():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words():
    file_text = read_file()
    return len(file_text.split())

def count_chars():
    charCounter = {}
    file_content = read_file()
    for char in file_content:
        lower_char = char.lower()
        if not lower_char in charCounter.keys():
            charCounter[lower_char] = 0
        charCounter[lower_char] += 1
    return charCounter

def create_report():
    report = ""
    report += "--- Begin report of books/frankenstein.txt ---\n"
    report += f"{count_words()} words found in the document\n\n"
    counted_chars = count_chars()
    for counter in counted_chars:
        report += f"The '{counter}' character was found {counted_chars[counter]} times\n"
    report += "\n\n --- End of report ---"
    return report



main()