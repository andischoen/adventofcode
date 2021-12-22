import day18.day18lib as lib
import unittest


class TestDay18(unittest.TestCase):
    def test_caclulateLine(self):
        line = list("5+3")
        res = lib.calculateLine(line)
        self.assertEqual(res, 8)

        line = list("2*(3+(4*5*6)+3)")
        res = lib.calculateLine(line)
        self.assertEqual(res, 252)

        line = list("2*3+(4*5)")
        res = lib.calculateLine(line)
        self.assertEqual(res, 26)

        line = list("5+(8*3+9+3*4*3)")
        res = lib.calculateLine(line)
        self.assertEqual(res, 437)

        line = list("5*9*(7*3*3+9*3+(8+6*4))")
        res = lib.calculateLine(line)
        self.assertEqual(res, 12240)

        line = list("((2+4*9)*(6+9*8+6)+6)+2+4*2")
        res = lib.calculateLine(line)
        self.assertEqual(res, 13632)

        line = list("1+(2*3)+(4*(5+6))")
        res = lib.calculateLine(line)
        self.assertEqual(res, 51)

        line = list("2+((3*4*4*4*8+7)*5)+(5+5+2*4)*(3*9+(6+7*3+4*3*5)+(7+9*9*7*8+9)+7)*3*2")
        res = lib.calculateLine(line)
        self.assertEqual(res, 407755680)

        line = list("2+((3*4)*2)+5*2")
        res = lib.calculateLine(line)
        self.assertEqual(res, 62)

        line = list("2+((3*4)*2)")
        res = lib.calculateLine(line)
        self.assertEqual(res, 26)

    def test_caclulateLineAdvanced(self):
        line = list("5+3")
        res = lib.calculateLineAdvanced(line)
        self.assertEqual(res, 8)

        line = list("2*(3+(4*5*6)+3)")
        res = lib.calculateLineAdvanced(line)
        self.assertEqual(res, 252)

        line = list("2*3+(4*5)")
        res = lib.calculateLineAdvanced(line)
        self.assertEqual(res, 46)

        line = list("5+(8*3+9+3*4*3)")
        res = lib.calculateLineAdvanced(line)
        self.assertEqual(res, 1445)

        line = list("5*9*(7*3*3+9*3+(8+6*4))")
        res = lib.calculateLineAdvanced(line)
        self.assertEqual(res, 669060)

        line = list("((2+4*9)*(6+9*8+6)+6)+2+4*2")
        res = lib.calculateLineAdvanced(line)
        self.assertEqual(res, 23340)

        line = list("1+(2*3)+(4*(5+6))")
        res = lib.calculateLineAdvanced(line)
        self.assertEqual(res, 51)

        line = list("2+((3*4*4*4*8+7)*5)+(5+5+2*4)*(3*9+(6+7*3+4*3*5)+(7+9*9*7*8+9)+7)*3*2")
        res = lib.calculateLineAdvanced(line)
        self.assertEqual(res, 4816271700)

        line = list("2+((3*4)*2)+5*2")
        res = lib.calculateLineAdvanced(line)
        self.assertEqual(res, 62)

        line = list("2+((3*4)*2)")
        res = lib.calculateLineAdvanced(line)
        self.assertEqual(res, 26)

if __name__ == '__main__':
    unittest.main()