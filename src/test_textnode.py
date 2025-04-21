import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_html_node_TEXT_eq(self):
        textnode = TextNode("here is some text", TextType.TEXT)
        leafnode_from_textnode = text_node_to_html_node(textnode)
        test = leafnode_from_textnode.to_html()
        self.assertEqual(test, "here is some text")

    def test_text_to_html_node_BOLD_eq(self):
        textnode = TextNode("here is some bold text", TextType.BOLD)
        leafnode_from_textnode = text_node_to_html_node(textnode)
        test = leafnode_from_textnode.to_html()
        self.assertEqual(test, "<b>here is some bold text</b>")

    def test_text_to_html_node_ITALICS_eq(self):
        textnode = TextNode("here is some italics text", TextType.ITALICS)
        leafnode_from_textnode = text_node_to_html_node(textnode)
        test = leafnode_from_textnode.to_html()
        self.assertEqual(test, "<i>here is some italics text</i>")

    def test_text_to_html_node_CODE_eq(self):
        textnode = TextNode("x = x + y;", TextType.CODE)
        leafnode_from_textnode = text_node_to_html_node(textnode)
        test = leafnode_from_textnode.to_html()
        self.assertEqual(test, "<code>x = x + y;</code>")

    def test_text_to_html_node_LINK_eq(self):
        textnode_link = TextNode("link text", TextType.LINK, "https://google.com")
        htmlnode_link = text_node_to_html_node(textnode_link)
        self.assertEqual(
            htmlnode_link.to_html(), '<a href="https://google.com">link text</a>'
        )

    def test_text_to_html_node_IMAGE_eq(self):
        textnode_link = TextNode("Smiley face", TextType.IMAGE, "smiley.gif")
        htmlnode_link = text_node_to_html_node(textnode_link)
        self.assertEqual(
            htmlnode_link.to_html(), '<img src="smiley.gif" alt="Smiley face">'
        )


if __name__ == "__main__":
    unittest.main()
