#!/usr/bin/env python3
'''
just a testing driver
'''

import unittest
import report_process


class HTMLProcessingTest(unittest.TestCase):
    def test_reg(self):
        print(report_process.get_studentId_percentage(
            "./judge/lab8/TANGB/ggg,_WANG_Shuxin(11611815)/Judgement.java (94%)"))



if __name__ == '__main__':
    unittest.main()
