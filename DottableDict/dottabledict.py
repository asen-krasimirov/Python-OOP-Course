

class DotableDict(dict):

    def __getitem__(self, item):
        items = {item: False for item in item.split('.')}

        result = self
        for item in items:
            for key, value in result.items():

                if key == item:
                    result = value
                    items[item] = True
                    break

        if all([items[item] for item in items]):
            return result

    def __contains__(self, item):
        return not self[item] is None
    #
    # def __get_all_sub_keys(self, key):
    #     array = self[key]
    #     if array is None:
    #         return key
    #
    #     keys = [self.__get_all_sub_keys(key) for key in self[key]]
    #     return keys

    def keys(self):
        # TODO: return the keys in format -> x.y.z, x.y, x
        all_keys = []
        for key in self:
            # loc_keys = [key for key in self[key]]
            loc_keys = self.__get_all_sub_keys(key)
            all_keys.append(loc_keys)
        return all_keys


def all_tests():

    def searching_by_dot_test():
        dotted_dict = DotableDict({'test1': {'test2': {'test3': 'passed'}}})
        assert dotted_dict['test1'] == {'test2': {'test3': 'passed'}}
        assert dotted_dict['test1.test2'] == {'test3': 'passed'}
        assert dotted_dict['test1.test2.test3'] == "passed"
        assert dotted_dict['test2.test3'] is None
        print('searching_by_dot Test passed')

    def content_test():
        data = DotableDict(x={'y': {'z': 1}})
        assert ('x.y.z' in data) is True, 'x.y.z' in data  # True
        assert ('x.y' in data) is True, 'x.y' in data  # True
        assert ('x' in data) is True, 'x' in data  # True
        assert ('x.y.t' in data) is False, 'x.y.t' in data  # False
        assert ('x.z' in data) is False, 'x.z' in data  # False
        assert ('y' in data) is False, 'y' in data  # False
        print('test_two Test passed')

    def keys_test():
        data = DotableDict(x={'y': {'z': 1}})
        data2 = DotableDict({'test1': {'test2': {'test3': 'passed'}}})
        assert list(data.keys()) == ['x.y.z', 'x.y', 'x'], list(data.keys())
        assert list(data.keys()) == ['test1.test2.test3', 'test1.test2', 'test1'], list(data2.keys())

    searching_by_dot_test()
    content_test()
    # keys_test()


if __name__ == '__main__':
    all_tests()
    # data = DotableDict(x={'y': {'z': 1}})
    # print(list(daa.keys()))