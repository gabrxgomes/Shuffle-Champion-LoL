from tkinter import *
import random
import tkinter

Main_window = Tk()

mylist_mid = ["Ahri", "Akali", "Akshan", "Anivia", "Annie", "Aurelion Sol", "Azir", "Cassiopeia", "Corki", "Ekko", "Fizz", "Galio", "Heimerdinger", "Irelia", "Kai'Sa",
"Kassasin", "Katarina", "LeBlanc", "Lissandra", "Lux", "Malzahar", "Neeko", "Orianna", "Qianna", "Ryse", "Sylas", "Syndra", "Talon", "Twisted of Fate", "Veigar", 
"Vex", "Viktor", "Vladmir", "Xeraath", "Yasuo", "Yone", "Zed", "Zoe"]
mylist_top = ["Aatrox", "Akali", "Camile","Cho'Gath", "Darius", "Dr Mundo", "Fiora", "Gangplank", "Garen", "Gnar", "Gragas,", "Graves", "Gwen", "Heimerdinger",
 "Illaoi", "Irelia", "Jax", "Jayce", "Kayle", "Kennen", "Kled", "Malphite", "Mordekaiser", "Nasus", "Orn", "Quinn", "Renekton", "Rengar", "Riven", 
"Rumble", "Sett", "Shen", "Singed", "Sion", "Tahm Kench", "Teemo", "Tryndamere", "Urgot", "Vayne", "Volibear", "Wukong", "Yasuo", "Yone", "Yorick"]
mylist_jungle = ["Amumu", "Diana", "Ekko", "Elise", "Evelynn", "Fiddlesticks", "Graves", "Hecarim", "Ivern", "Jarvan IV", "Karthus", "Kayn", "Kha'Zix",
"Kindred", "Lee Sin", "Lilia", "Master Yi", "Nidalee", "Nocturne", "Nunu e Willump", "Olaf", "Poppy", "Rammus", "Rek'Sai", "Rengar", "Sejuani", "Shaco", "Shyvana", "Skarner",
"Taliah", "Talon", "Trundle", "Udyr", "Vi", "Viego", "Volibear", "Warwick", "Wukong", "Xin Zhao", "Zac", "Zed"]
mylist_adc = ["Aphelios", "Ashe", "Caitlyn", "Draven", "Ezreal", "Jhin", "Kai'Sa", "Kalista", "Kog'Maw", "Lucian", "Miss Fortune", "Samira", "Sivir", "Tristana", "Twitch", "Varus",
"Vayne", "Xaya", "Yasuo", "Zeri", "Ziggs"]
mylist_sup = ["Alistar", "Bardo", "Blitzcrank", "Brand", "Braum", "Galio", "Janna", "Karma", "Leona", "Lulu", "Lux", "Maokai", "Morgana", "Nami", "Nautilus", "Pantheon",
"Pyke", "Rakan","Rell","Renata Glasc", "Senna", "Sona", "Soraka", "Seraphine", "Swain", "Taric", "Thresh", "Vel'Koz", "Xerath", "Yummi", "Zilean", "Zyra"]

Main_window.title('Shuffle Champions LoL')
Main_window.geometry("350x250")
Main_window.iconbitmap("icon.ico")
Main_window.resizable(False, False) 



def top():
    my_string_var.set(random.choice(mylist_top))

def mid():
    my_string_var.set(random.choice(mylist_mid))

def jungle():
    my_string_var.set(random.choice(mylist_jungle))

def adc():
    my_string_var.set(random.choice(mylist_adc))

def sup():
    my_string_var.set(random.choice(mylist_sup))
 


btn_1 = Button(Main_window,
               text = "TOP",
               command = top)

btn_2 = Button(Main_window,
               text = "JUNGLE",
               command = jungle)

btn_3 = Button(Main_window,
               text = "MID",
               command = mid)

btn_4 = Button(Main_window,
               text = "ADC",
               command = adc)

btn_5 = Button(Main_window,
               text = "SUPORTE",
               command = sup)
 

my_string_var = StringVar()
my_string_var1 = StringVar()
my_string_var2 = StringVar()

my_string_var.set("Randomize sua lane e duvirta-se" 
"com seus amigos!")
my_string_var1.set("Programa em fase inicial, espero que seja de grande utilidade!")
my_string_var2.set("Link GitHub: github.com/gabrxgomes")

my_label = Label(Main_window,
                 textvariable = my_string_var)
my_label2 = Label(Main_window,
                 textvariable = my_string_var1)

my_label3 = Label(Main_window,
                 textvariable = my_string_var2)


 

btn_1.pack()
btn_2.pack()
btn_3.pack()
btn_4.pack()
btn_5.pack()

my_label.pack()
my_label2.pack()
my_label3.pack()
 

Main_window.mainloop()