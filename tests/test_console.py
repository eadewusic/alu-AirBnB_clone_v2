import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        """Set up the HBNBCommand instance for testing."""
        self.console = HBNBCommand()
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        """Tear down after testing."""
        self.patcher.stop()

    def test_quit(self):
        """Test the quit command."""
        with self.assertRaises(SystemExit):
            self.console.onecmd('quit')
        self.assertEqual(self.mock_stdout.getvalue(), '')

    def test_EOF(self):
        """Test the EOF command."""
        with self.assertRaises(SystemExit):
            self.console.onecmd('EOF')
        self.assertEqual(self.mock_stdout.getvalue(), '\n')

    def test_create(self):
        """Test the create command."""
        with patch('sys.stdin', StringIO('create BaseModel\nEOF\n')):
            self.console.cmdloop()
        self.assertIn('0000-0000-0000-0000', self.mock_stdout.getvalue())

    def test_show(self):
        """Test the show command."""
        with patch('sys.stdin', StringIO('create BaseModel\nshow BaseModel 0000-0000-0000-0000\nEOF\n')):
            self.console.cmdloop()
        self.assertIn('BaseModel', self.mock_stdout.getvalue())

    def test_destroy(self):
        """Test the destroy command."""
        with patch('sys.stdin', StringIO('create BaseModel\ndestroy BaseModel 0000-0000-0000-0000\nall\nEOF\n')):
            self.console.cmdloop()
        self.assertNotIn('BaseModel', self.mock_stdout.getvalue())

    def test_all(self):
        """Test the all command."""
        with patch('sys.stdin', StringIO('create BaseModel\nall\nEOF\n')):
            self.console.cmdloop()
        self.assertIn('BaseModel', self.mock_stdout.getvalue())

    def test_count(self):
        """Test the count command."""
        with patch('sys.stdin', StringIO('create BaseModel\ncount BaseModel\nEOF\n')):
            self.console.cmdloop()
        self.assertIn('1', self.mock_stdout.getvalue())

    def test_update(self):
        """Test the update command."""
        with patch('sys.stdin', StringIO('create BaseModel\nupdate BaseModel 0000-0000-0000-0000 name "New Name"\nshow BaseModel 0000-0000-0000-0000\nEOF\n')):
            self.console.cmdloop()
        self.assertIn('New Name', self.mock_stdout.getvalue())

    def test_emptyline(self):
        """Test the emptyline method."""
        with patch('sys.stdin', StringIO('\n')):
            self.console.cmdloop()
        self.assertEqual(self.mock_stdout.getvalue(), '')

if __name__ == '__main__':
    unittest.main()
