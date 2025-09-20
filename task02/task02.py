from collections import deque        # імпортуємо двосторонню чергу deque — структура з O(1) pop/popleft
import time                          # модуль 'time' дає високоточні лічильники часу для вимірювань

def is_palindrome_while(s: str) -> bool:   # оголошення функції з циклом while; s — вхідний рядок
    dq = deque(ch.lower() for ch in s if not ch.isspace())  # нормалізуємо: до нижнього регістру, прибираємо пробіли, одразу кладемо в deque
    while len(dq) > 1:                    # ітеративно порівнюємо символи з обох кінців, поки залишилось щонайменше 2
        if dq.popleft() != dq.pop():      # беремо лівий і правий символи; якщо різні — не паліндром
            return False                  # достроково завершуємо — невідповідність знайдена
    return True                           # якщо всі пари збіглися (або 0/1 символ) — це паліндром

def is_palindrome_rec(dq: deque) -> bool: # “чиста” рекурсивна функція, працює безпосередньо з deque
    if len(dq) <= 1:                      # базовий випадок: порожньо або один символ — паліндром
        return True
    if dq.popleft() != dq.pop():          # рекурсивний крок: порівнюємо крайні символи
        return False                      # різні — одразу False
    return is_palindrome_rec(dq)          # однакові — рекурсія на "внутрішньому" підрядку (deque уже вкорочений)

def is_palindrome_recursive(s: str) -> bool:   # обгортка над рекурсією, приймає рядок
    return is_palindrome_rec(                  # повертаємо результат рекурсивної перевірки
        deque(ch.lower() for ch in s if not ch.isspace())  # тут теж нормалізуємо: нижній регістр, без пробілів
    )

test = ("A man a plan a canal Panama " * 90)  # створюємо довгий тестовий рядок: фраза помножена на 90 (більше даних — стабільніше вимірювання)

for name, fn in [("while", is_palindrome_while), ("rec", is_palindrome_recursive)]:  # перебираємо дві функції для порівняння
    t0 = time.perf_counter()                 # знімаємо стартовий “мітчик” високоточного таймера (краще за time.time для бенчмарків)
    for _ in range(200):                     # багаторазово викликаємо функцію (90 разів), щоб згладити випадкові коливання часу
        fn(test)                             # власне вимірювана робота — перевірка паліндрома на довгому рядку
    dt = time.perf_counter() - t0            # різниця між поточним часом і стартом — тривалість виконання циклу з 90 викликами
    print(name, dt)                          # друкуємо ім’я варіанта ("while"/"rec") і загальний час у секундах



# from collections import deque

# def is_palindrome_deque(s: str) -> bool:
#     """
#     Повертає True, якщо s — паліндром, інакше False.
#     Ігнорує регістр та пробіли. Використовує двосторонню чергу (deque).
#     """
#     # нормалізація: у нижній регістр, прибрати всі пробільні символи
#     normalized = (ch.lower() for ch in s if not ch.isspace())

#     # заповнюємо deque символами
#     dq = deque(normalized)

#     # порівнюємо символи з обох кінців
#     while len(dq) > 1:
#         if dq.popleft() != dq.pop():
#             return False
#     return True


# # приклади використання
# if __name__ == '__main__':
#     tests = [
#         "Казак азак",          # True
#         "Я несу гусеня",       # True (ігноруємо пробіли й регістр)
#         "A man a plan a canal Panama",  # True
#         "not a palindrome",    # False
#         "Тягни гігант"         # True
#     ]
#     for t in tests:
#         print(f"'{t}' -> {is_palindrome_deque(t)}")

