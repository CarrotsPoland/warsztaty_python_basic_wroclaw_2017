
# coding: utf-8

# # Numeryczne

# ## Liczby całkowite - integers

# In[ ]:

integer = 1


# In[ ]:

integer


# In[ ]:

42


# Podstawowe operacje:

# dodawnie: `+`

# odejmowanie: `-`

# mnożenie: `*`

# dzielenie: `/`

# In[ ]:

1 + 2


# In[ ]:

3 - 5


# In[ ]:

100 * 44


# In[ ]:

25 / 5


# ### Zadania

# 1 Wykorzystać notebooka jako kalkulator

# 2 Sprawdzić działanie operatora: `%`

# ## Liczby całkowite - floaty

# In[ ]:

float_number = 1.0


# In[ ]:

float_number


# Podstawowe operacje zostają te same: `+` `-` `*` `/`

# In[ ]:

1.0 + 2.0


# In[ ]:

3.5 - 5.0


# In[ ]:

100 * 4.5


# In[ ]:

25.5 / 3


# In[ ]:

10 / 4


# ### Zadania

# 1 Sprawdzić wynik działania:

# In[ ]:

50.5 * 45.4 / 2.4 - 5


# Obowiązuje kolejność wykonywania działań!

# Do jej zmiany można użyć nawiasów: `()`

# 2 Sprawdzić wynik działania:

# In[ ]:

50.5 * 45.4 / (2.4 - 5)


# 3 Czy floaty można wykorzystać do reprezentacji np. pieniędzy?

# In[ ]:

1.1 + 2.2


# # Boolowskie - boolean

# In[ ]:

True


# In[ ]:

False


# Co można z nimi robić?

# In[ ]:

1 is True


# In[ ]:

0 is False


# Operatory logiczne

# `or` `and` i `not`

# In[ ]:

True or False


# In[ ]:

True or True


# In[ ]:

False or False


# In[ ]:

True and True


# In[ ]:

True and False


# In[ ]:

False and False


# In[ ]:

not True


# In[ ]:

not False


# ### Zadania

# 1 Sprawdzić czy liczba `42` jest `True` czy `False`

# 2 Sprawdzić jaki będzie wynik tego działania: `(True and True) or False`

# 3 Sprawdzić czy liczba `1.0` nie jest `True`

# 4 Sprawdzić czy liczba `99.9` nie jest `False`

# # Łańcuchy znaków - stringi

# In[ ]:

'Ala ma kota'


# In[ ]:

"Ala ma kota"


# In[ ]:

"""Ala 
ma 
kota"""


# In[ ]:

'Mam ' + 'na ' + 'imię ' + "Krzysiek"


# In[ ]:

'Tutaj jest liczba: {}'.format(1)


# In[ ]:

"Tutaj tez moze być float - {}".format(3.3)


# In[ ]:

'Ale może być też string: {}'.format('Krzysiek')


# In[ ]:

'Chcę być dwa razy ' * 2


# ### Zadania

# 1 Stworzyć string: `Jestem na warsztatach Code Geek Carrots we Wrocławiu!`

# 2 Powtórzyć stringa: `**^**~**` 5 razy

# 3 Stworzyć stringa z swoim imieniem i nazwiskiem poprzez: dodawanie

# 4 `format`

# 5 String z pierwszego zadania w kilku liniach

# 6 Dodać stringa + inta/floata

# # Listy - lists

# In[ ]:

[1, 2, 3]


# In[ ]:

[1.3,4.5,5.4]


# In[ ]:

['Wrocław', 'Kraków', 'Warszawa']


# In[ ]:

['Wrocław', 1, 4.5]


# In[ ]:

lista = [1, 'Super', True, 1.4]


# In[ ]:

lista[0]


# In[ ]:

lista[-1]


# In[ ]:

lista[1:2]


# In[ ]:

lista[1:5:2]


# In[ ]:

[1,2] + ['Tom']


# In[ ]:

nested = [[42], 'Super']


# In[ ]:

nested[0][0]


# In[ ]:

['Duplikat'] * 2


# In[ ]:

l = [2,3,4]


# In[ ]:

l.append(3.22)


# In[ ]:

l.extend(['String', True])


# In[ ]:

len(l)


# ### Zadania

# 1 Stworzyć listę: `l` `[1,2,3]`

# 2 Dodać do niej następną listę: `['Ala', 4.4]` i zapisać ją jako inna zmienna

# 3 Wyciągnąć z nowo powstalej listy pierwszy i ostatni element

# 4 Zduplikować listę

# 5 Sprawdzić jak wygląda lista `l`

# 6 Wykorzstać `len` do sprawdzenia długości listy

# 7 Użyć `append` i `extend`

# 8 Odwrócić listę

# # Słowniki - dict

# In[ ]:

{'klucz': 'wartość'}


# In[ ]:

slownik = {'imie': 'Krzysztof', 'wiek': 26, 'pracuje': True}


# In[ ]:

slownik['imie']


# In[ ]:

slownik.get('wzrost', 'nie ma takiego klucza')


# In[ ]:

slownik['nazwisko'] = 'Żuraw'


# In[ ]:

slownik


# In[ ]:

slownik.keys()


# In[ ]:

slownik.values()


# In[ ]:

{'duplikat': 'jego wartość'} * 2


# In[ ]:

{'duplikat': 'jego wartość'} + {'inny': 'jego wartość'}


# In[ ]:

double_dict = {'duplikat': 'jego wartość'}


# In[ ]:

double_dict.update({'inny': 'jego wartość'})


# In[ ]:

double_dict


# In[ ]:

{['1','2']: 'wartość dla listy'}


# ### Zadania

# 1 Stworzyć słownik: `d` `{'imie': 'wasze imie', 'nazwisko': 'wasze nazwisko'}`

# 2 Wyciągnąc `imie` i `nazwisko` ze słownika

# 3 Dodać klucz `zainteresowania` i dodać listę zainteresowań

# 4 Zmienić `imie` w słowniku

# In[ ]:



