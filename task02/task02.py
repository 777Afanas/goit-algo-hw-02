from collections import deque

def is_palindrome_deque(s: str) -> bool:
    """
    Повертає True, якщо s — паліндром, інакше False.
    Ігнорує регістр та пробіли. Використовує двосторонню чергу (deque).
    """
    # нормалізація: у нижній регістр, прибрати всі пробільні символи
    normalized = (ch.lower() for ch in s if not ch.isspace())

    # заповнюємо deque символами
    dq = deque(normalized)

    # порівнюємо символи з обох кінців
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


# приклади використання
if __name__ == "__main__":
    tests = [
        "Казак азак",          # True
        "Я несу гусеня",       # True (ігноруємо пробіли й регістр)
        "A man a plan a canal Panama",  # True
        "not a palindrome",    # False
        "Тягни гігант"         # True
    ]
    for t in tests:
        print(f"'{t}' -> {is_palindrome_deque(t)}")