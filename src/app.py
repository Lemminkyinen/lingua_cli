import sys
from secrets import choice

from parse import read_words
from rich import print as rich_print


def words() -> None:
    rich_print("Words mode selected!\n")
    while True:
        words = read_words("../words.txt")
        word = choice(words)

        if choice((True, False)):
            question = word.question_chinese()
            rich_print(question)
            answer = input("> ")
            result = word.handle_chinese_result(answer)
            rich_print(result)
        else:
            question = word.question_english()
            rich_print(question)
            answer = input("> ")
            result = word.handle_english_result(answer)
            rich_print(result)

        rich_print()


def main() -> None:
    start_txt = (
        "[bold]Welcome to LinguaCLI![/bold]\n\n"
        "Please select what mode you would like to play:\n"
        "[cyan]1. Words[/cyan]\n"
        "[cyan]2. Phrases[/cyan]\n"
        "[cyan]3. Sentences[/cyan]\n"
        "[cyan]4. Tones[/cyan]\n"
        "[cyan]5. Random[/cyan]\n\n"
        "Press Ctrl + C to exit\n"
    )
    rich_print(start_txt)
    try:
        match input("> ").lower():
            case "1" | "words":
                words()
            case "2" | "phrases":
                rich_print("[red]Not implemented yet.[/red]")
            case "3" | "sentences":
                rich_print("[red]Not implemented yet.[/red]")
            case "4" | "tones":
                rich_print("[red]Not implemented yet.[/red]")
            case "5" | "random":
                rich_print("[red]Not implemented yet.[/red]")
            case _:
                rich_print("[red]Invalid selection. Please try again.[/red]")
    except KeyboardInterrupt:
        rich_print("[bold]Thank you for playing![/bold]")
        sys.exit(0)


if __name__ == "__main__":
    main()
