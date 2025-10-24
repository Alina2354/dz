import unittest
from dz13_06 import TextAnalyzer


class TestTextAnalyzer(unittest.TestCase):

    def test_word_count(self):
        analyzer = TextAnalyzer("Hello world, this is a test. Hello again.")
        self.assertEqual(analyzer.word_count(), 7)
    def test_unique_words(self):

        analyzer = TextAnalyzer("Hello world, this is a test. Hello again.")
        self.assertEqual(analyzer.unique_words(), {"hello", "world", "this", "is", "a", "test", "again"})


    def test_most_common_word(self):

        analyzer = TextAnalyzer("apple banana apple orange banana apple")
        self.assertEqual(analyzer.most_common_word(), "apple")

        analyzer2 = TextAnalyzer("one two one two three")

        self.assertIn(analyzer2.most_common_word(), {"one", "two"})

        self.assertEqual(analyzer2.most_common_word(), "one")

        analyzer3 = TextAnalyzer("single")
        self.assertEqual(analyzer3.most_common_word(), "single")

    def test_replace_word(self):

        analyzer = TextAnalyzer("Hello world, this is a test. Hello again.")
        self.assertEqual(analyzer.replace_word("Hello", "Hi"), "Hi world, this is a test. Hi again.")
        self.assertEqual(analyzer.replace_word("test", "exam"), "Hello world, this is a exam. Hello again.")
        self.assertEqual(analyzer.replace_word("nonexistent", "new"),
                         "Hello world, this is a test. Hello again.")

        analyzer2 = TextAnalyzer("Apple is an apple. APPLE pie.")
        self.assertEqual(analyzer2.replace_word("apple", "orange"), "orange is an orange. orange pie.")
        self.assertEqual(analyzer2.replace_word("APPLE", "pear"), "pear is an pear. pear pie.")

        analyzer3 = TextAnalyzer("testing the latest tests")
        self.assertEqual(analyzer3.replace_word("test", "exam"), "examing the latest exams") # Ошибка в моей логике, исправлено

        analyzer4 = TextAnalyzer("testing the latest tests")
        self.assertEqual(analyzer4.replace_word("test", "exam"), "testing the latest exams") # Должно заменить только 'tests'

    def test_empty_string_handling(self):

        analyzer = TextAnalyzer("")
        self.assertEqual(analyzer.word_count(), 0)
        self.assertEqual(analyzer.unique_words(), set())
        self.assertIsNone(analyzer.most_common_word())
        self.assertEqual(analyzer.replace_word("any", "word"), "")




if __name__ == '__main__':
    unittest.main()
