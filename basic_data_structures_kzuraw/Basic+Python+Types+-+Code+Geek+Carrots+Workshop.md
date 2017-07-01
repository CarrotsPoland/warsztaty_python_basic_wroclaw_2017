
# Numeryczne

## Liczby całkowite - integers


```python
integer = 1
```


```python
integer
```


```python
42
```

Podstawowe operacje:

dodawnie: `+`

odejmowanie: `-`

mnożenie: `*`

dzielenie: `/`


```python
1 + 2
```


```python
3 - 5
```


```python
100 * 44
```


```python
25 / 5
```

### Zadania

1 Wykorzystać notebooka jako kalkulator

2 Sprawdzić działanie operatora: `%`

## Liczby całkowite - floaty


```python
float_number = 1.0
```


```python
float_number
```

Podstawowe operacje zostają te same: `+` `-` `*` `/`


```python
1.0 + 2.0
```


```python
3.5 - 5.0
```


```python
100 * 4.5
```


```python
25.5 / 3
```


```python
10 / 4
```

### Zadania

1 Sprawdzić wynik działania:


```python
50.5 * 45.4 / 2.4 - 5
```

Obowiązuje kolejność wykonywania działań!

Do jej zmiany można użyć nawiasów: `()`

2 Sprawdzić wynik działania:


```python
50.5 * 45.4 / (2.4 - 5)
```

3 Czy floaty można wykorzystać do reprezentacji np. pieniędzy?


```python
1.1 + 2.2
```

# Boolowskie - boolean


```python
True
```


```python
False
```

Co można z nimi robić?


```python
1 is True
```


```python
0 is False
```

Operatory logiczne

`or` `and` i `not`


```python
True or False
```


```python
True or True
```


```python
False or False
```


```python
True and True
```


```python
True and False
```


```python
False and False
```


```python
not True
```


```python
not False
```

### Zadania

1 Sprawdzić czy liczba `42` jest `True` czy `False`

2 Sprawdzić jaki będzie wynik tego działania: `(True and True) or False`

3 Sprawdzić czy liczba `1.0` nie jest `True`

4 Sprawdzić czy liczba `99.9` nie jest `False`

# Łańcuchy znaków - stringi


```python
'Ala ma kota'
```


```python
"Ala ma kota"
```


```python
"""Ala 
ma 
kota"""
```


```python
'Mam ' + 'na ' + 'imię ' + "Krzysiek"
```


```python
'Tutaj jest liczba: {}'.format(1)
```


```python
"Tutaj tez moze być float - {}".format(3.3)
```


```python
'Ale może być też string: {}'.format('Krzysiek')
```


```python
'Chcę być dwa razy ' * 2
```

### Zadania

1 Stworzyć string: `Jestem na warsztatach Code Geek Carrots we Wrocławiu!`

2 Powtórzyć stringa: `**^**~**` 5 razy

3 Stworzyć stringa z swoim imieniem i nazwiskiem poprzez: dodawanie

4 `format`

5 String z pierwszego zadania w kilku liniach

6 Dodać stringa + inta/floata

# Listy - lists


```python
[1, 2, 3]
```


```python
[1.3,4.5,5.4]
```


```python
['Wrocław', 'Kraków', 'Warszawa']
```


```python
['Wrocław', 1, 4.5]
```


```python
lista = [1, 'Super', True, 1.4]
```


```python
lista[0]
```


```python
lista[-1]
```


```python
lista[1:2]
```


```python
lista[1:5:2]
```


```python
[1,2] + ['Tom']
```


```python
nested = [[42], 'Super']
```


```python
nested[0][0]
```


```python
['Duplikat'] * 2
```


```python
l = [2,3,4]
```


```python
l.append(3.22)
```


```python
l.extend(['String', True])
```


```python
len(l)
```

### Zadania

1 Stworzyć listę: `l` `[1,2,3]`

2 Dodać do niej następną listę: `['Ala', 4.4]` i zapisać ją jako inna zmienna

3 Wyciągnąć z nowo powstalej listy pierwszy i ostatni element

4 Zduplikować listę

5 Sprawdzić jak wygląda lista `l`

6 Wykorzstać `len` do sprawdzenia długości listy

7 Użyć `append` i `extend`

8 Odwrócić listę

# Słowniki - dict


```python
{'klucz': 'wartość'}
```


```python
slownik = {'imie': 'Krzysztof', 'wiek': 26, 'pracuje': True}
```


```python
slownik['imie']
```


```python
slownik.get('wzrost', 'nie ma takiego klucza')
```


```python
slownik['nazwisko'] = 'Żuraw'
```


```python
slownik
```


```python
slownik.keys()
```


```python
slownik.values()
```


```python
{'duplikat': 'jego wartość'} * 2
```


```python
{'duplikat': 'jego wartość'} + {'inny': 'jego wartość'}
```


```python
double_dict = {'duplikat': 'jego wartość'}
```


```python
double_dict.update({'inny': 'jego wartość'})
```


```python
double_dict
```


```python
{['1','2']: 'wartość dla listy'}
```

### Zadania

1 Stworzyć słownik: `d` `{'imie': 'wasze imie', 'nazwisko': 'wasze nazwisko'}`

2 Wyciągnąc `imie` i `nazwisko` ze słownika

3 Dodać klucz `zainteresowania` i dodać listę zainteresowań

4 Zmienić `imie` w słowniku


```python

```
