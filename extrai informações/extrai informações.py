import requests
from bs4 import BeautifulSoup
import tkinter as tk

# A criação do extrator
def extrair_manchetes():
    url = url_entry.get()
    
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    manchetes = soup.find_all('h3', class_='gs-c-promo-heading__title')

    resultados_text.delete('1.0', tk.END)
    resultados_text.insert(tk.END, "Manchetes:\n")
    for manchete in manchetes:
        resultados_text.insert(tk.END, manchete.text.strip() + "\n")

# Configuração Tkinter
root = tk.Tk()
root.title("Extrator de Manchetes Web")

url_label = tk.Label(root, text="Insira a URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

extrair_button = tk.Button(root, text="Extrair Manchetes", command=extrair_manchetes)
extrair_button.pack()

resultados_text = tk.Text(root, width=60, height=40)
resultados_text.pack()

root.mainloop()
