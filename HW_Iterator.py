class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = iter(nested_list)
        self.current_list = iter([])

    def __iter__(self):
        return self

    def __next__(self):
        while True: 
            try:
                return next(self.current_list)
            except StopIteration:
                self.current_list = iter(next(self.nested_list))


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        print(flat_iterator_item)  
        assert flat_iterator_item == check_item

    # Создаем и выводим результат преобразования в список
    flat_list = list(FlatIterator(list_of_lists_1))
    print(flat_list)
    assert flat_list == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

