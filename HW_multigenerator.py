import types

def flat_generator(nested_list):
    for values in nested_list:
        if isinstance(values, list):
            yield from flat_generator(values)
        else:
            yield values


def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        print(flat_iterator_item)  # Построчный вывод
        assert flat_iterator_item == check_item

    flat_list = list(flat_generator(list_of_lists_2))
    print(flat_list)  # Вывод в списке
    assert flat_list == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

	# Проверяем является ли возвращаемый тип генератором
    is_generator = isinstance(flat_generator(list_of_lists_2), types.GeneratorType)
    print(is_generator) 
    assert is_generator


if __name__ == '__main__':
    test_4()
