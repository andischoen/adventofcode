import day6.day6lib as lib
import unittest


class TestDay6(unittest.TestCase):
    def test_getGroupCommonAnswerCount(self):
        group = "abcdef\nbcdk\nabcklmn"
        count = lib.getGroupCommonAnswerCount(group)
        self.assertEqual(count, 2)

        group = "abcdef\nghijk\nlmnopq"
        count = lib.getGroupCommonAnswerCount(group)
        self.assertEqual(count, 0)

        group = "abc\nabc\ncba"
        count = lib.getGroupCommonAnswerCount(group)
        self.assertEqual(count, 3)

    def test_getGroupAnswersCount(self):
        group = "abcdef\nbcdk\nabcklmn"
        count = lib.getGroupAnswersCount(group)
        self.assertEqual(count, 10)

        group = "abcdef\nghijk\nlmnopq"
        count = lib.getGroupAnswersCount(group)
        self.assertEqual(count, 17)

        group = "abc\nabc\ncba"
        count = lib.getGroupAnswersCount(group)
        self.assertEqual(count, 3)

if __name__ == '__main__':
    unittest.main()