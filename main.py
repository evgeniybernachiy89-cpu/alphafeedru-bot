```python
from scout import run as scout_run
from editor import run as editor_run
from publisher import run as publisher_run

def main():
    print("=== Поиск ===")
    scout_run()
    print("=== Редактирование ===")
    editor_run()
    print("=== Публикация ===")
    publisher_run()
    print("=== Готово ===")

if __name__ == "__main__":
    main()
```