import unittest
import getRestriction

class TestRestriction(unittest.TestCase):

    # Test with restriction - result must be True
    def test_restriction(self):
        self.assertTrue(getRestriction.restriction("PCU-006", "2021-03-10", "16:59"))
        self.assertTrue(getRestriction.restriction("PCU-006", "2021-03-10", "8:15"))
        self.assertTrue(getRestriction.restriction("PCU-003", "2021-03-09", "19:00"))

    # Test without restriction - result must be False
    def test_withoutRestriction(self):
        self.assertFalse(getRestriction.restriction("PCU-006", "2021-03-10", "13:10"))
        self.assertFalse(getRestriction.restriction("PCU-006", "2021-03-10", "10:17"))
        self.assertFalse(getRestriction.restriction("PCU-003", "2021-03-10", "19:00"))
    
if __name__ == '__main__':
    unittest.main()