#!/usr/bin/env python3

print("Bewannacry Tool \N{Snake}")

name = input("Geben Sie Ihren Namen ein: ")
alter = input("Geben Sie Ihr Alter ein: ")
stadt = input("Geben Sie Ihre Stadt ein: ")
handynummer = input("Geben Sie Ihre Handynummer ein:")


person = {'Name': name, 'Alter': alter, 'Stadt': stadt, 'Handynummer': handynummer}

banner = '''
 _______                       __        __           
/       \                     /  |      /  |          
$$$$$$$  |  ______   __    __ $$ |____  $$/  _______  
$$ |  $$ | /      \ /  \  /  |$$      \ /  |/       \ 
$$ |  $$ |/$$$$$$  |$$  \/$$/ $$$$$$$  |$$ |$$$$$$$  |
$$ |  $$ |$$ |  $$ | $$  $$<  $$ |  $$ |$$ |$$ |  $$ |
$$ |__$$ |$$ \__$$ | /$$$$  \ $$ |__$$ |$$ |$$ |  $$ |
$$    $$/ $$    $$/ /$$/ $$  |$$    $$/ $$ |$$ |  $$ |
$$$$$$$/   $$$$$$/  $$/   $$/ $$$$$$$/  $$/ $$/   $$/

'''
print(banner)

print("Name =", person['Name'])

print("Alter =", person['Alter'])

print("Stadt =", person['Stadt'])

print("Handynummer =", person['Handynummer'])

print("Drücken sie eine Taste das Programm zu beenden")