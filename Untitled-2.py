import tkinter as tk

# Початкове значення кліків
clicks = 0

# Функція, яка збільшує кількість кліків
def click():
    global clicks
    clicks += 1
    label.config(text = clicks)

# Створення вікна
window = tk.Tk()
window.title("Клікер")

# Створення напису
label = tk.Label(window, text=clicks, font=("Arial", 24),)
label.pack(pady=10)

# Створення кнопки
button = tk.Button(window, text="Клікни мене!", font=("Arial", 18), command=click)
button.pack(pady=10)

# Запуск програми
window.mainloop()
