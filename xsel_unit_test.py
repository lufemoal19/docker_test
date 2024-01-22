import subprocess
import unittest
from unittest.mock import patch
from xsel_test import copy_to_clipboard, paste_text

class TestClipboardOperations(unittest.TestCase):

    @patch('subprocess.run')
    def test_copy_to_clipboard(self, mock_run):
        # Mock the subprocess.run method
        copy_to_clipboard("Test Text")
        
        # Assert that subprocess.run was called with the correct arguments
        mock_run.assert_called_once_with(['xsel', '-i'], input="Test Text".encode(), check=True)

    @patch('subprocess.run')
    def test_paste_text(self, mock_run):
        # Mock the subprocess.run method
        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = b'Test Text\n'
        result = paste_text()

        # Assert that subprocess.run was called with the correct arguments
        mock_run.assert_called_once_with(['xsel', '-o'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Assert that the returned result is correct
        self.assertEqual(result, b'Test Text')

if __name__ == '__main__':
    unittest.main()