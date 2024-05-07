import pyautogui
import time

pyautogui.PAUSE = 1

# pyautogui.click - click do mouse
# pyautogui.write - escrever texto
# pyautogui.press - pressionar tecla do teclado
# pyautogui.hotkey - executar comando ou conjunto de teclas 

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=797, y=453)
pyautogui.write("rabreu@gmail.com")

pyautogui.press("tab")
pyautogui.write("123456")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

import pandas

tabelas = pandas.read_csv("produtos.csv")

for linha in tabelas.index:
    pyautogui.click(x=811, y=341)

    codigo = str(tabelas.loc[linha, "codigo"])
    marca = str(tabelas.loc[linha, "marca"])
    tipo = str(tabelas.loc[linha, "tipo"])
    categoria = str(tabelas.loc[linha, "categoria"])
    preco = str(tabelas.loc[linha, "preco_unitario"])
    custo = str(tabelas.loc[linha, "custo"])
    obs = str(tabelas.loc[linha, "obs"])

    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(marca)
    pyautogui.press("tab")
    pyautogui.write(tipo)
    pyautogui.press("tab")
    pyautogui.write(categoria)
    pyautogui.press("tab")
    pyautogui.write(preco)
    pyautogui.press("tab")
    pyautogui.write(custo)
    pyautogui.press("tab")
    if obs != "NaN":
     pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    time.sleep(3)
    pyautogui.scroll(5000)
