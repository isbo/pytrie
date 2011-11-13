import unittest
import trie

class TestTrie(unittest.TestCase):

    def testAll(self):
        t = trie.Trie()
        self.assertFalse(t.add("abc", "=abc"))
        self.assertTrue(t.add("abc", "=abc"))
        self.assertFalse(t.add("a", "=a"))
        self.assertFalse(t.add("abd", "=abd"))
        self.assertFalse(t.add("bad", "=bad"))

        self.assertEqual(t.get("abd"), "=abd")
        self.assertFalse(t.get("ab"))
        self.assertEqual(t.lpm("abcd"), "abc")
        self.assertEqual(t.remove("abc"), "=abc")
        self.assertFalse(t.get("abc"))
        self.assertEqual(t.lpm("abcd"), "a")

if __name__ == '__main__':
    unittest.main()
