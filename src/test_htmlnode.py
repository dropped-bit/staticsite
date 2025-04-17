import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
            ' href="https://www.google.com" target="_blank"',
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
            leaf_node_1.__repr__(), "LeafNode(p, This is a paragraph, None)"
        )
        self.assertEqual(
            leaf_node_2.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_raises(self):
        leaf_node_1_raises = LeafNode("p", None)

        with self.assertRaises(ValueError):
            leaf_node_1_raises.to_html()


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        parent_node_1 = ParentNode("p", "<p>hello me</p>")
        self.assertEqual(
            parent_node_1.__repr__(), "ParentNode('p', <p>hello me</p>, None)"
        )

        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


# TODO:
# Add more tests for html parentnode with nested leafnodes. Especially with props
if __name__ == "__main__":
    unittest.main()
