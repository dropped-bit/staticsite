import unittest
from textnode import TextNode, TextType
from code_func import split_nodes_delimiter


class TestCode(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("Text is`code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                [
                    TextNode("Text is", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" word", TextType.TEXT),
                ]
            ],
        )


# TODO: Additional Cases:
# node_1 = TextNode("`code block` at the beginning", TextType.TEXT)
# node_2 = TextNode("**only bold text here**", TextType.BOLD)
