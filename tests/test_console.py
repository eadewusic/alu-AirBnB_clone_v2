import unittest
from unittest.mock import patch, MagicMock
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

    @patch('sys.stdin', StringIO('quit\n'))
    def test_quit(self):
        """Test the quit command."""
        with self.assertRaises(SystemExit):
            self.console.cmdloop()
        self.assertEqual(self.mock_stdout.getvalue(), '')

    @patch('sys.stdin', StringIO('EOF\n'))
    def test_EOF(self):
        """Test the EOF command."""
        with self.assertRaises(SystemExit):
            self.console.cmdloop()
        self.assertEqual(self.mock_stdout.getvalue(), '\n')

    @patch('sys.stdin', StringIO('create BaseModel\nall\nEOF\n'))
    def test_all(self):
        """Test the all command."""
        self.console.cmdloop()
        self.assertIn('BaseModel', self.mock_stdout.getvalue())

    @patch('sys.stdin', StringIO('create BaseModel\ncount BaseModel\nEOF\n'))
    def test_count(self):
        """Test the count command."""
        self.console.cmdloop()
        self.assertIn('1', self.mock_stdout.getvalue())

    @patch('sys.stdin', StringIO('create BaseModel\n'
                                 'show BaseModel 0000-0000-0000-0000\n'
                                 'EOF\n'))
    def test_show(self):
        """Test the show command."""
        self.console.cmdloop()
        self.assertIn('BaseModel', self.mock_stdout.getvalue())

    @patch('sys.stdin', StringIO('create BaseModel\n'
                                 'destroy BaseModel 0000-0000-0000-0000\n'
                                 'all\n'
                                 'EOF\n'))
    def test_destroy(self):
        """Test the destroy command."""
        self.console.cmdloop()
        self.assertNotIn('BaseModel', self.mock_stdout.getvalue())

    @patch('sys.stdin', StringIO('create BaseModel\n'
                                 'update BaseModel 0000-0000-0000-0000\n'
                                 'name "New Name"\n'
                                 'show BaseModel 0000-0000-0000-0000\n'
                                 'EOF\n'))
    def test_update(self):
        """Test the update command."""
        self.console.cmdloop()
        self.assertIn('New Name', self.mock_stdout.getvalue())

    @patch('sys.stdin', StringIO('\n'))
    def test_emptyline(self):
        """Test the emptyline method."""
        self.console.cmdloop()
        self.assertEqual(self.mock_stdout.getvalue(), '')


if __name__ == '__main__':
    unittest.main()
