import pytest

from string_utils import StringUtils

utils = StringUtils()

""" Capitilize """

@pytest.mark.parametrize('string, result', [("alexandr", "Alexandr"), ("moskva", "Moskva"), ("lenin", "Lenin"), ("", ""), ("  ", "  "), ("123", "123")])
def test_capitilize(string, result):
    assert utils.capitilize(string) == result

""" Trim """

@pytest.mark.parametrize('string, result', [(" alexandr", "alexandr"), ("  moskva", "moskva"), ("   lenin", "lenin"), ("", ""), ("  ", ""), (" 123", "123")])
def test_trim(string, result):
    assert utils.trim(string) == result

""" To list """

@pytest.mark.parametrize('string, result', [("a,b,c,d", ["a", "b", "c", "d"]), ("1,2,3,4", ["1", "2", "3", "4"]), ("odin,dva,tri,chetyre", ["odin", "dva", "tri", "chetyre"]), ("", []), (" ", [])])
def test_to_list(string, result):
    assert utils.to_list(string) == result

""" Contains """

@pytest.mark.parametrize(('string', 'letter', 'result'), [('Alexandr', 'A', True), ('Moskva', 'k', True), ('Lenin', 'd', False), ('', '', True), (' ', ' ', True), ('', 'a', False)])
def test_contains(string, letter, result):
    assert utils.contains(string, letter) == result

""" Delete symbol """

@pytest.mark.parametrize(('string', 'letter', 'result'), [('Alexandr', 'A', 'lexandr'), ('Moskva', 'k', 'Mosva'), ('Lenin', 'e', 'Lnin'), ('1234', '2', '134'), ('', '', ''), (' ', ' ', '')])
def test_delete_symbol(string, letter, result):
    assert utils.delete_symbol(string, letter) == result

""" Starts with """

@pytest.mark.parametrize(('string', 'letter', 'result'), [('Alexandr', 'E', False), ('Moskva', 'M', True), ('Lenin', 'L', True), ('123', '1', True), ('', '', True), (' ', ' ', True)])
def test_starts_with(string, letter, result):
    assert utils.starts_with(string, letter) == result

""" End with """

@pytest.mark.parametrize(('string', 'letter', 'result'), [('Alexandr', 'r', True), ('Moskva', 'e', False), ('Lenin', 'n', True), ('123', '3', True), ('', '', True), (' ', ' ', True)])
def test_end_with(string, letter, result):
    assert utils.end_with(string, letter) == result

""" Is empty """

@pytest.mark.parametrize(('string', 'result'), [('', True), ('   ', True), ('Lenin', False), ('1234', False)])
def test_is_empty(string, result):
    assert utils.is_empty(string) == result

""" List to string """

@pytest.mark.parametrize(('string', 'letter', 'result'), [('Alexandr', 'A', 'lexandr'), ('Moskva', 'k', 'Mosva'), ('Lenin', 'e', 'Lnin'), ('1234', '3', '124'), ("", "", ""), (" ", " ", "")])
def test_list_to_string(string, letter, result):
    assert utils.delete_symbol(string, letter) == result
