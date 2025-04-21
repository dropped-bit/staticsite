import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, World!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(), ' class="greeting" href="https://boot.dev"'
        )

    def test_to_html_props_no_values(self):

        node = HTMLNode(
            "div",
            "Hello, World!",
            None,
            None,
        )
        self.assertEqual(node.props_to_html(), "")

    def test_values(self):
        node = HTMLNode("div", "I wish I could read")

        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("p", "Here is a string", None, {"class": "primary"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, Here is a string, children: None, {'class': 'primary'})",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "this is a leaf paragraph")
        self.assertEqual(node.to_html(), "<p>this is a leaf paragraph</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "click here!", {"href": "https://boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://boot.dev">click here!</a>')

    def test_leaf_to_html_notag(self):
        node = LeafNode(None, "no tag")
        self.assertEqual(node.to_html(), "no tag")

    def test_raises_value_error_leaf(self):
        node = LeafNode("p", None)

        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_node_many_children(self):
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
