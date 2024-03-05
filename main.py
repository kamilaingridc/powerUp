# passo a passo
import pyautogui
import time

pyautogui.PAUSE = 0.5

# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa um pouco maior (3s)
time.sleep(3)

# fazer login 
pyautogui.click(x=2076, y=412)
pyautogui.write("pythonimpressionador@gmail.com")

# escrever a senha
pyautogui.press("tab")
pyautogui.write("sua senha aqui")
 
# logar
pyautogui.click(x=2329, y=575)
time.sleep(3)

# importar base de dados 
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# cadastrar um produto


# repetir o processo de cadastro até acabar a base de dados
 