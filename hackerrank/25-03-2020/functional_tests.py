import unittest
import nested_functions

class TestingNestedLists(unittest.TestCase):
    def test_01_input_works_properly(self):
        given = [["simon", 1.3], ["john", 3.7], ["margaret", 4.5]]
        expected = [["simon", 1.3], ["john", 3.7], ["margaret", 4.5]]
        # intentionally broken expected data - to fire some dummy smoke test
        # expected = [["simon", 1.5], ["john", 3.7], ["margaret", 4.5]]
        actual = nested_functions.get_nested_scores(len(given), given)
        self.assertListEqual(expected, actual)

    def test_02_list_is_sorted_by_scores_ascending(self):
        given = [["margaret", 4.5], ["simon", 1.3], ["john", 3.7], ["harry", 2.2]]
        expected = [["simon", 1.3], ["harry", 2.2], ["john", 3.7], ["margaret", 4.5]]

        actual = nested_functions.sorted_by_score_ascending(len(given), given)
        self.assertListEqual(expected, actual)

    def test_03_find_second_lowest_score(self):
        given = [["margaret", 4.5], ["simon", 1.3], ["john", 3.7], ["harry", 2.2]]
        expected = ["harry", 2.2]

        actual = nested_functions.find_second_lowest_ordered_by_name(given)
        self.assertListEqual(expected, actual)

    def test_04_finds_all_second_lowest_scores_ordered_by_name(self):
        # intentionally broken given and expected to observe alphabetical order sorting
        #given = [["margaret", 4.5], ["simon", 1.3], ["john", 3.7], ["A_harry", 2.2], ["C_second_someone", 2.2], ["B_third_someone",2.2]]
        #expected = [["A_harry", 2.2], ["C_second_someone", 2.2], ["B_third_someone", 2.2]]

        given = [["margaret", 4.5], ["simon", 1.3], ["john", 3.7], ["harry", 2.2], ["second_someone", 2.2],
                 ["third_someone", 2.2]]
        expected = [["harry", 2.2], ["second_someone", 2.2], ["third_someone", 2.2]]

        actual = nested_functions.find_second_lowest_ordered_by_name(given)
        self.assertListEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()


