import unittest
import HTMLTestRunner

suite = unittest.defaultTestLoader.discover('./', pattern='test_ddt.py')

if __name__ == '__main__':
    runner = HTMLTestRunner.HTMLTestRunner(open('.report.html', 'wb'), title='hahha', description='haha')
    runner.run(suite)
