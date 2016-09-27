import os
import unittest
from mock import Mock
from blog.servises.logger_decorator import write_error_to_file
from blog.configurations.config import LOGFILENAME


class LoggerWorkAbilityTestCase(unittest.TestCase):

    def setUp(self):
        """
        remove file with logs before each test, if it's exists
        """
        if os.path.isfile(LOGFILENAME):
            os.remove(LOGFILENAME)

    def tearDown(self):
        """
        remove file with logs after each test, if it's exists
        """
        if os.path.isfile(LOGFILENAME):
            os.remove(LOGFILENAME)

    def test_write_to_bug_file_if_good(self):
        """
        Check if everything alright under @, nothing will have happen
        """
        mock = Mock(return_value=3)

        @write_error_to_file
        def everything_works_without_exceptions():
            mock()

        everything_works_without_exceptions()
        self.assertFalse(os.path.isfile(LOGFILENAME))

    def test_write_bug_to_file_if_exception(self):
        """
        Check if logger create .log file and write all required information inside
        """

        mock = Mock(side_effect=KeyError)

        @write_error_to_file
        def error_raising():
            mock()

        error_raising()
        self.assertRaises(KeyError)
        self.assertTrue(os.path.isfile(LOGFILENAME))
        data_in_log_file = open(LOGFILENAME, mode="r").read()
        self.assertIn('There was an exception in  error_raising', data_in_log_file)
        self.assertIn('Traceback', data_in_log_file)
        self.assertIn('KeyError', data_in_log_file)

if __name__ == '__main__':
    unittest.main()
