import unittest
import kbstatus
from typing import List

class TestKBStatus(unittest.TestCase):
    def test_qwerty_top_movement(self):
        report = kbstatus.keyboard.KeyboardLayoutReport('QWERTY', kbstatus.keyboard.KeyboardFactory.get_layout('qwerty'))
        report.calculate('qweruiop')
        result = self.test_get_report_output(report)
        self.assertListEqual(result, [0, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0])

    def test_get_report_output(self, report: kbstatus.keyboard.KeyboardLayoutReport) -> List[int]:
        return [
            report.moves['none'],
            report.finger_movement_count,
            report.same_finger_use,

            report.moves['top'],
            report.moves['bottom'],
            report.moves['left'],
            report.moves['right'],

            report.moves['top right'],
            report.moves['top left'],
            report.moves['bottom right'],
            report.moves['bottom left']
        ]


if __name__ == '__main__':
    unittest.main()
