from ai_code_generator.generator import generate_code
from ai_code_generator.executor import execute_code

def main():
    print("🤖 Добро пожаловать в генератор искусственного интеллекта!")
    prompt = input("👉 Введите свой запрос:")

    code = generate_code(prompt)
    print("\n✨ Generated Code:\n")
    print(code)

    run = input("\n▶️ Хотите ли вы выполнить этот код? (y/n): ")
    if run.lower() == 'y':
        execute_code(code)

if __name__ == "__main__":
    main()
