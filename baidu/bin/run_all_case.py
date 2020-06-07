import unittest

suite = unittest.defaultTestLoader.discover('./../case_mange', pattern='test_baidu_*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)
