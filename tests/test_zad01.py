import unittest
from unittest import mock
from unittest.mock import *
from src.zadanie1.zad01 import File


class TestFile(unittest.TestCase):

    def setUp(self):
        self.temp = File()

    def test_open(self):
        path = "plik.txt"
        mock = mock_open(read_data="test")
        with patch('builtins.open', mock):
            self.assertEqual(self.temp.open(path), "test")


    def test_edit(self):
        path = "plik.txt"
        mock = mock_open(read_data="test")
        with patch('builtins.open', mock):
            self.temp.edit(path, "aaa")
        mock.assert_called_once_with(path, "w")

    @mock.patch('src.zadanie1.zad01.os.path')
    @mock.patch('src.zadanie1.zad01.os')
    def test_delete_file(self, mock_os, mock_path):
        path = "plik.txt"
        mock_path.exists.return_value = True
        self.temp.delete(path)
        mock_os.remove.assert_called_with(path)


    def tearDown(self):
        self.temp = None



if __name__ == '__main__':
    unittest.main()