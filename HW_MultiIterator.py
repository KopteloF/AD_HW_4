class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.stack = []

    def __iter__(self):
        self.stack.append(iter(self.nested_list))
        return self

    def __next__(self):
        while self.stack:
            try:
                value = next(self.stack[-1])
                if isinstance(value, list):
                    self.stack.append(iter(value))
                else:
                    return value
            except StopIteration:
                self.stack.pop()

        raise StopIteration


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        print(flat_iterator_item)  # Построчный вывод
        assert flat_iterator_item == check_item

    flat_list = list(FlatIterator(list_of_lists_2))
    print(flat_list)  # Вывод в виде списка
    assert flat_list == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
