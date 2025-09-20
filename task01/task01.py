import queue
import time
import random

# Створюємо чергу
request_queue = queue.Queue()

# Лічильник для унікальних ідентифікаторів заявок
request_id = 1

def generate_request():
    """Генерує нову заявку та додає її до черги"""
    global request_id
    request = f"Заявка #{request_id}"
    request_queue.put(request)
    print(f"[+] Додано {request} до черги")
    request_id += 1

def process_request():
    """Обробляє заявку, якщо черга не пуста"""
    if not request_queue.empty():
        request = request_queue.get()
        print(f"[~] Обробка {request}...")
        time.sleep(random.uniform(0.5, 1.5))  # імітація часу обробки
        print(f"[✓] {request} оброблено")
    else:
        print("[!] Черга порожня, немає заявок для обробки")

def main():
    print("Система приймання заявок запущена. Натисніть Ctrl+C для виходу.")
    try:
        while True:
            # Імітуємо генерацію нових заявок
            if random.random() < 0.7:  # 70% ймовірність, що прийде нова заявка
                generate_request()

            # Імітуємо обробку заявок
            process_request()

            # Затримка для більш реалістичної роботи
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем.")

if __name__ == '__main__':
    main()