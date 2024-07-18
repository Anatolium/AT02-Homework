def count_vowels(text: str) -> int:
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for char in text if char in vowels)
