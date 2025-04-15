import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode(
            "This is a text node", TextType.BOLD, "[url text](www.google.com)"
        )
        node4 = TextNode(
            "This is a text node", TextType.BOLD, "[url text](www.google.com)"
        )
        test_cases = ((node, node2), (node3, node4))
        for a, b in test_cases:
            self.assertEqual(a, b)

    def test_noteq(self):
        node = TextNode("Text is 1 version", TextType.ITALICS)
        node2 = TextNode("Text is 2 version", TextType.ITALICS)
        node3 = TextNode("Text is same version", TextType.ITALICS)
        node4 = TextNode("Text is same version", TextType.TEXT)
        test_cases = ((node, node2), (node3, node4))
        for a, b in test_cases:
            self.assertNotEqual(a, b)


if __name__ == "__main__":
    unittest.main()
