# AI-CODE-GENERATOR
Генератор кода с искусственным интеллектом
# 🤖 Генератор кода с искусственным интеллектом

Этот проект представляет собой простой генератор кода на базе искусственного интеллекта, который принимает подсказки на естественном языке (например, "напишите программу на Python для Fibonacci") и генерирует рабочий код.

✨ Особенности:
- Преобразование английского языка в код
- Запуск и исполнение сгенерированного кода
- Документация, понятная пользователю
- Возможность расширения для большего количества языков

---

## 🚀 как запустить
1. Clone the repo
   ```bash
   git clone https://github.com/Janexus/AI-Code-Generator.git
   cd AI-Code-Generator
   ```

2. Install requirements
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app
   ```bash
   python app.py
   ```

---

## 📂 Структура проекта
- `app.py` → Main runner
- `ai_code_generator/` → Core logic
- `tests/` → Unit tests
- `examples/` → Demo prompts & outputs

---

## 🧪 Пример
**Подсказка:**  
👉 "Напишите программу на Python, которая проверяет, является ли число простым".

**Generated Code:**  
```python
def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
```
---

## 👨‍💻 Автор
Сделано с ❤️ для учебных проектов и колледжей.

## Угостить меня Кофе
![Alt text](https://github.com/nop-74/OPEN-AI-FREE-KEYS/blob/main/100.jpg)
