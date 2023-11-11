import types

def flat_generator(nested_list):
    for sublist in nested_list:
        for item in sublist:
            yield item


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    # Тестируем обход элементов в генераторе
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        print(flat_iterator_item)  # Построчный вывод
        assert flat_iterator_item == check_item

    # Тестируем преобразование в список
    flat_list = list(flat_generator(list_of_lists_1))
    print(flat_list)  # Вывод в виде списка
    assert flat_list == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    # Проверяем является ли возвращаемый тип генератором
    is_generator = isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    print(is_generator)
    assert is_generator

if __name__ == '__main__':
    test_2()
