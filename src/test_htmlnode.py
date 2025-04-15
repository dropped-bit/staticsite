import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        html_node_1 = HTMLNode(
            "p",
            "here is some paragraph text",
            "<p>here is an embedded paragraph<p>",
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            html_node_1.props_to_html(),
            'href="https://www.google.com" target="_blank"',
        )

        self.assertEqual(
            html_node_1.__repr__(),
            "HTMLNode('p', here is some paragraph text, children: <p>here is an embedded paragraph<p>, {'href': 'https://www.google.com', 'target': '_blank'})",
        )


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        leaf_node_1 = LeafNode("p", "This is a paragraph")
        leaf_node_2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf_node_1.to_html(), "<p>This is a paragraph</p>")
        self.assertEqual(
            leaf_node_2.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )


if __name__ == "__main__":
    unittest.main()
