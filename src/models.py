from __future__ import annotations

from functools import partial

from pydantic import BaseModel


class BaseWord(BaseModel):
    english: set[str]
    chinese: set[str]

    @staticmethod
    def parse_from_line(line: str) -> BaseWord:
        """Parse from `bubble; pearl - zhen zhu`"""
        words = line.split("-")
        split_ = partial(str.split, sep=";")
        english_words, chinese_words = map(split_, words)
        english_words = set(map(str.strip, english_words))
        chinese_words = set(map(str.strip, chinese_words))
        return BaseWord(english=english_words, chinese=chinese_words)

    @property
    def _english_str(self) -> str:
        return ", ".join(self.english)

    @property
    def _chinese_str(self) -> str:
        return ", ".join(self.chinese)

    @property
    def _chinese_stripped(self) -> set[str]:
        return {c.replace(" ", "") for c in self.chinese}

    def question_chinese(self) -> str:
        return (
            f"Here's a Chinese word: [cyan]'{self._chinese_str}'[/cyan]. "
            "What is its English translation?"
        )

    def question_english(self) -> str:
        return (
            f"Here's an English word: [cyan]'{self._english_str}'[/cyan]. "
            "What is its Chinese translation?"
        )

    def handle_chinese_result(self, english_word: str) -> str:
        txt = "[red]Wrong![/red]"
        if english_word in self.english:
            txt = "[green]Correct! Well done![/green]"
        return (
            txt + f" The English translation is: [green]'{self._english_str}'[/green]"
        )

    def handle_english_result(self, chinese_word: str) -> str:
        txt = "[red]Wrong![/red]"
        if chinese_word.replace(" ", "") in self._chinese_stripped:
            txt = "[green]Correct! Well done![/green]"
        return (
            txt + f" The Chinese translation is: [green]'{self._chinese_str}'[/green]"
        )


class BasePhrase(BaseModel):
    english: set[str]
    chinese: set[str]
