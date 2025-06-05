import unittest
from textnode import TextNode, TextType
from inline_markdown import (
    split_nodes_links,
    split_nodes_image,
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images,
)


class TestCode(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("Text is`code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Text is", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("**Bold Text** here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Bold Text", TextType.BOLD),
                TextNode(" here", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_italics(self):
        node = TextNode("_italics here_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALICS)
        self.assertEqual(
            new_nodes,
            [
                TextNode("italics here", TextType.ITALICS),
            ],
        )

    def test_split_node_is_type_bold(self):
        node = TextNode("bold text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("bold text", TextType.BOLD),
            ],
        )

    def test_split_nodes_delimiter_incorrect_syntax(self):
        node = TextNode("hi, **bold text here", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    # FIX: Change tests to assertListEqual()
    def test_extract_markdown_images(self):
        text_images = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertListEqual(
            extract_markdown_images(text_images),
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

    def test_extract_markdown_images_png(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )

    def test_split_images(self):
        node_no_image = TextNode(
            "This is text without an image",
            TextType.TEXT,
        )
        node_image = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )

        old_nodes = []
        old_nodes.append(node_no_image)
        old_nodes.append(node_image)

        nodes_results = split_nodes_image(old_nodes)

        self.assertListEqual(
            [
                TextNode("This is text without an image", TextType.TEXT),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image",
                    TextType.IMAGE,
                    "https://i.imgur.com/3elNhQu.png",
                ),
            ],
            nodes_results,
        )

    def test_split_links(self):
        node_no_link = TextNode(
            "This is text without a link",
            TextType.TEXT,
        )
        node_link = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )

        old_nodes = []
        old_nodes.append(node_no_link)
        old_nodes.append(node_link)

        nodes_results = split_nodes_links(old_nodes)

        self.assertListEqual(
            [
                TextNode("This is text without a link", TextType.TEXT),
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            nodes_results,
        )

    def test_split_one_link(self):
        node_link = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )

        old_nodes = []
        old_nodes.append(node_link)

        nodes_results = split_nodes_links(old_nodes)

        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            ],
            nodes_results,
        )
