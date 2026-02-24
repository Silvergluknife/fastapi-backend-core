import os
import random

# Список расширений и "фейкового" содержимого для них
langs = {
    "py": "def main():\n    print('Smart Python algorithm running...')\n\nif __name__ == '__main__':\n    main()",
    "js": "console.log('Advanced JavaScript logic initialized');\nconst data = {status: 'ok', value: 42};",
    "html": "<!DOCTYPE html>\n<html>\n<body>\n<h1>Dev Dashboard</h1>\n<p>Loading...</p>\n</body>\n</html>",
    "css": "body { background-color: #2c3e50; color: #ecf0f1; font-family: sans-serif; }"
}

def stuff_repo():
    print("Генерируем файлы для статистики языков...")
    
    # Создаем папку для мусора, чтобы не мешалась в корне
    folder = "src_core_files"
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    for ext, content in langs.items():
        # Создаем по 5-10 файлов каждого типа
        for i in range(random.randint(5, 10)):
            filename = f"{folder}/module_{i}_{random.randint(100, 999)}.{ext}"
            with open(filename, "w") as f:
                f.write(content)
            print(f"Создан файл: {filename}")

    print("\nФайлы готовы! Теперь делай push.")

if __name__ == "__main__":
    stuff_repo()