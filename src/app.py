from secrets import choice

from parse import read_words
from rich import print as rich_print


def main() -> None:
    rich_print("Press Ctrl + C to exit")
    while True:
        try:
            words = read_words("../words.txt")
            word = choice(words)

            if choice((True, False)):
                question = word.question_chinese()
                rich_print(question)
                answer = input()
                result = word.handle_chinese_result(answer)
                rich_print(result)
            else:
                question = word.question_english()
                rich_print(question)
                answer = input()
                result = word.handle_english_result(answer)
                rich_print(result)

            rich_print()
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
