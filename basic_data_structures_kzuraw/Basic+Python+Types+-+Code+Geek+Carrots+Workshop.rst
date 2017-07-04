
Numeryczne
==========

Liczby całkowite - integers
---------------------------

.. code:: python

    integer = 1

.. code:: python

    integer

.. code:: python

    42

Podstawowe operacje:

dodawnie: ``+``

odejmowanie: ``-``

mnożenie: ``*``

dzielenie: ``/``

.. code:: python

    1 + 2

.. code:: python

    3 - 5

.. code:: python

    100 * 44

.. code:: python

    25 / 5

Zadania
~~~~~~~

1 Wykorzystać notebooka jako kalkulator

2 Sprawdzić działanie operatora: ``%``

Liczby całkowite - floaty
-------------------------

.. code:: python

    float_number = 1.0

.. code:: python

    float_number

Podstawowe operacje zostają te same: ``+`` ``-`` ``*`` ``/``

.. code:: python

    1.0 + 2.0

.. code:: python

    3.5 - 5.0

.. code:: python

    100 * 4.5

.. code:: python

    25.5 / 3

.. code:: python

    10 / 4

Zadania
~~~~~~~

1 Sprawdzić wynik działania:

.. code:: python

    50.5 * 45.4 / 2.4 - 5

Obowiązuje kolejność wykonywania działań!

Do jej zmiany można użyć nawiasów: ``()``

2 Sprawdzić wynik działania:

.. code:: python

    50.5 * 45.4 / (2.4 - 5)

3 Czy floaty można wykorzystać do reprezentacji np. pieniędzy?

.. code:: python

    1.1 + 2.2

Boolowskie - boolean
====================

.. code:: python

    True

.. code:: python

    False

Co można z nimi robić?

.. code:: python

    1 is True

.. code:: python

    0 is False

Operatory logiczne

``or`` ``and`` i ``not``

.. code:: python

    True or False

.. code:: python

    True or True

.. code:: python

    False or False

.. code:: python

    True and True

.. code:: python

    True and False

.. code:: python

    False and False

.. code:: python

    not True

.. code:: python

    not False

Zadania
~~~~~~~

1 Sprawdzić czy liczba ``42`` jest ``True`` czy ``False``

2 Sprawdzić jaki będzie wynik tego działania:
``(True and True) or False``

3 Sprawdzić czy liczba ``1.0`` nie jest ``True``

4 Sprawdzić czy liczba ``99.9`` nie jest ``False``

Łańcuchy znaków - stringi
=========================

.. code:: python

    'Ala ma kota'

.. code:: python

    "Ala ma kota"

.. code:: python

    """Ala 
    ma 
    kota"""

.. code:: python

    'Mam ' + 'na ' + 'imię ' + "Krzysiek"

.. code:: python

    'Tutaj jest liczba: {}'.format(1)

.. code:: python

    "Tutaj tez moze być float - {}".format(3.3)

.. code:: python

    'Ale może być też string: {}'.format('Krzysiek')

.. code:: python

    'Chcę być dwa razy ' * 2

Zadania
~~~~~~~

1 Stworzyć string:
``Jestem na warsztatach Code Geek Carrots we Wrocławiu!``

2 Powtórzyć stringa: ``**^**~**`` 5 razy

3 Stworzyć stringa z swoim imieniem i nazwiskiem poprzez: dodawanie

4 ``format``

5 String z pierwszego zadania w kilku liniach

6 Dodać stringa + inta/floata

Listy - lists
=============

.. code:: python

    [1, 2, 3]

.. code:: python

    [1.3,4.5,5.4]

.. code:: python

    ['Wrocław', 'Kraków', 'Warszawa']

.. code:: python

    ['Wrocław', 1, 4.5]

.. code:: python

    lista = [1, 'Super', True, 1.4]

.. code:: python

    lista[0]

.. code:: python

    lista[-1]

.. code:: python

    lista[1:2]

.. code:: python

    lista[1:5:2]

.. code:: python

    [1,2] + ['Tom']

.. code:: python

    nested = [[42], 'Super']

.. code:: python

    nested[0][0]

.. code:: python

    ['Duplikat'] * 2

.. code:: python

    l = [2,3,4]

.. code:: python

    l.append(3.22)

.. code:: python

    l.extend(['String', True])

.. code:: python

    len(l)

Zadania
~~~~~~~

1 Stworzyć listę: ``l`` ``[1,2,3]``

2 Dodać do niej następną listę: ``['Ala', 4.4]`` i zapisać ją jako inna
zmienna

3 Wyciągnąć z nowo powstalej listy pierwszy i ostatni element

4 Zduplikować listę

5 Sprawdzić jak wygląda lista ``l``

6 Wykorzstać \ ``len`` do sprawdzenia długości listy

7 Użyć ``append`` i ``extend``

8 Odwrócić listę

Słowniki - dict
===============

.. code:: python

    {'klucz': 'wartość'}

.. code:: python

    slownik = {'imie': 'Krzysztof', 'wiek': 26, 'pracuje': True}

.. code:: python

    slownik['imie']

.. code:: python

    slownik.get('wzrost', 'nie ma takiego klucza')

.. code:: python

    slownik['nazwisko'] = 'Żuraw'

.. code:: python

    slownik

.. code:: python

    slownik.keys()

.. code:: python

    slownik.values()

.. code:: python

    {'duplikat': 'jego wartość'} * 2

.. code:: python

    {'duplikat': 'jego wartość'} + {'inny': 'jego wartość'}

.. code:: python

    double_dict = {'duplikat': 'jego wartość'}

.. code:: python

    double_dict.update({'inny': 'jego wartość'})

.. code:: python

    double_dict

.. code:: python

    {['1','2']: 'wartość dla listy'}

Zadania
~~~~~~~

1 Stworzyć słownik: ``d``
``{'imie': 'wasze imie', 'nazwisko': 'wasze nazwisko'}``

2 Wyciągnąc ``imie`` i ``nazwisko`` ze słownika

3 Dodać klucz ``zainteresowania`` i dodać listę zainteresowań

4 Zmienić ``imie`` w słowniku

