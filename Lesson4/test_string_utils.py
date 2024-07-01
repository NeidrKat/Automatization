import pytest
from string_utilis import StringUtils

s_utilis = StringUtils()

# Принимает на вход текст, делает первую букву заглавной и возвращает этот же
# текст: 'test_capitilize'


def test_capitilize():
    # possitive
    assert s_utilis.capitilize('pice') == 'Pice'
    assert s_utilis.capitilize('мир') == 'Мир'
    assert s_utilis.capitilize('annMary') == 'Annmary'
    assert s_utilis.capitilize('lion king') == 'Lion king'
    assert s_utilis.capitilize('berserk2') == 'Berserk2'
    # negative_test
    assert s_utilis.capitilize('') == ''
    assert s_utilis.capitilize('.') == '.'

# Принимает на вход текст и удаляет пробелы в начале, если они есть:
# 'test_trim'


def test_trim_positive():
    assert s_utilis.trim(' pice') == 'pice'
    assert s_utilis.trim(' PICE') == 'PICE'
    assert s_utilis.trim(' pice ') == 'pice '


@pytest.mark.xfail
def test_negative_trim():
    assert s_utilis.trim(123456) == '123456'

# Принимает на вход текст с разделителем и возвращает список строк:
# 'test_to_list'
# Параметры:
# `string` - строка для обработки
# `delimeter` - разделитель строк. По умолчанию запятая (",")


@pytest.mark.parametrize('string, delimeter, result', [
    # positive :
    ('dog,cat,bird', ',', ['dog', 'cat', 'bird']),
    ('flower,tree,forest', ',', ['flower', 'tree', 'forest']),
    ('pen;pencil;marker', ';', ['pen', 'pencil', 'marker']),
    ('1,2,3,4,5', None, ['1', '2', '3', '4', '5']),
    ('@^%^&^!^*', '^', ['@', '%', '&', '!', '*']),
    ('1/n2/n3', '/n', ['1', '2', '3']),
    # negative :
    ('', None, []),
    ])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = s_utilis.to_list(string)
    else:
        res = s_utilis.to_list(string, delimeter)
    assert res == result

# Возвращает `True`, если строка содержит искомый символ и `False` -
# если нет : 'test_contains
# Параметры:
# `string` - строка для обработки
# `symbol` - искомый символ


@pytest.mark.parametrize('string, symbol, result', [
  # positive :
  ('dog', 'o', True),
  ('flower', 'w', True),
  ('Red', 'r', False),
  ('pice', 'l', False),
  ('rain', '1', False),
  ('12345', 'j', False),
  # negative :
  ('', 'p', False),
  # ('love', '', False)        # defect
])
def test_contains(string, symbol, result):
    res = s_utilis.contains(string, symbol)
    assert res == result

# Удаляет все подстроки из переданной строки:'delete_symbol'
#  Параметры:
# `string` - строка для обработки
# `symbol` - искомый символ для удаления


@pytest.mark.parametrize('string, symbol, result', [
  # positive :
  ('dog', 'o', 'dg'),
  ('flower', 'f', 'lower'),
  ('Marry-Ann', '-', 'MarryAnn'),
  # negative :
  ('', '', ''),
  ('', 'b', ''),
  ('miss', '', 'miss')
])
def test_delete_symbol(string, symbol, result):
    res = s_utilis.delete_symbol(string, symbol)
    assert res == result

# Возвращает `True`, если строка начинается с заданного символа и 'False'
# - если нет: 'test_starts_with'
# Параметры:
# `string` - строка для обработки
# `symbol` - искомый символ


@pytest.mark.parametrize('string, symbol, result', [
    # positive :
    ('pice', 'p', True),
    ('', '', True),
    ('Love', 'L', True),
    (' bubble', '', True),
    ('Mary - Ann', 'M', True),
    ('Josh Bush', 'J', True),
    ('987', '9', True),
    # negative :
    ('Love', 'l', False),
    ('tea', 'T', False),
    ("", "v", False),
    ("eleven", "n", False)
])
def test_starts_with(string, symbol, result):
    res = s_utilis.starts_with(string, symbol)
    assert res == result


# Возвращает `True`, если строка заканчивается заданным символом и
# `False` - если нет: 'test_end_with'
# Параметры:
# `string` - строка для обработки
# `symbol` - искомый символ


@pytest.mark.parametrize('string, symbol, result', [
    # positive :
    ('pice', 'e', True),
    ('', '', True),
    ('LOVE', 'E', True),
    ('bubble ', '', True),
    ('Mary - Ann', 'n', True),
    ('Josh Bush', 'h', True),
    ('987', '7', True),
    # negative :
    ('Love', 'l', False),
    ('TEA', 'a', False),
    ("", "v", False),
    ("eleven", "e", False)
])
def test_end_with(string, symbol, result):
    res = s_utilis.end_with(string, symbol)
    assert res == result


# Возвращает `True`, если строка пустая и `False` - если нет: 'test_is_empty'
# Пример 1: `is_empty("") -> True`
# Пример 2: `is_empty(" ") -> True`
# Пример 3: `is_empty("SkyPro") -> False`

@pytest.mark.parametrize('string, result', [
    # positive :
    ('', True),
    (' ', True),
    ('               ', True),
    # negative :
    ('pice', False),
    (' pice', False),
    ('pice ', False)
])
def test_is_empty(string, result):
    res = s_utilis.is_empty(string)
    assert res == result


# Преобразует список элементов в строку с указанным разделителем
# Параметры:
# `lst` - список элементов
# `joiner` - разделитель элементов в строке. По умолчанию запятая
# (", ")
# Пример 1: `list_to_string([1,2,3,4]) -> "1, 2, 3, 4"`
# Пример 2: `list_to_string(["Sky", "Pro"]) -> "Sky, Pro"`
# Пример 3: `list_to_string(["Sky", "Pro"], "-") -> "Sky-Pro"`


@pytest.mark.parametrize('lst, joiner, result', [
    # positive :
    (['a', 'b', 'c'], ',', 'a,b,c'),
    ([1, 2, 3, 4, 5], None, '1, 2, 3, 4, 5'),
    (['a', 'b', 'c'], '', 'abc'),
    (['Mary', 'Ann'], '-', 'Mary-Ann'),
    # negative :
    ([], None, ''),
    ([], '*', '')
])
def test_list_to_string(lst, joiner, result):
    if joiner is None:
        res = s_utilis.list_to_string(lst)
    else:
        res = s_utilis.list_to_string(lst, joiner)
    assert res == result
