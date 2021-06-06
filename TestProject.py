import unittest
import Project
class TestProject(unittest.TestCase):
    def test_make(self):
        self.assertEqual(Project.Make(0, 71907805), (11.99, 'Musaka', 1200))
        self.assertEqual(Project.Make(0, 28947983), (1.99, 'Voda', 0))
        self.assertEqual(Project.Make(0, 0), (0, 0, 0))
if __name__ == "__main__":
    unittest.main()