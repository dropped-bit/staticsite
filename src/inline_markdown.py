import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid Markdown, please close the bold or italics text")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)

    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"\[(.*?)\]\((.*?\.gif|.*?\.jpeg|.*?\.png)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((https:\/\/.*?)\)", text)


def split_nodes_image(old_nodes):
    # make a list of text nodes
    new_nodes = []

    # we accept a list of text nodes.
    for old_node in old_nodes:

        # e.g. old_node.text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        # for each node extract images text using function "images"
        # image data contains a list of tuples.
        # e.g. [("to boot dev", "https://www.boot.dev"),("to youtube", "https://www.youtube.com/@bootdotdev")]
        images_data = extract_markdown_images(old_node.text)

        # check for no image data
        if not images_data:
            new_nodes.append(old_node)
        else:
            # e.g. ("to boot dev", "https://www.boot.dev")
            alt, url = images_data[0]
            before_split, after_split = old_node.text.split(f"![{alt}]({url})", 1)
            new_nodes.extend(
                [
                    TextNode(before_split, TextType.TEXT),
                    TextNode(alt, TextType.IMAGE, url),
                ]
            )

            # if there is text in after_split, then run following recurssion, **extending** new_nodes.
            if after_split:
                new_nodes.extend(
                    split_nodes_image([TextNode(after_split, TextType.TEXT)])
                )
    return new_nodes


def split_nodes_links(old_nodes):
    # make a list of text nodes
    new_nodes = []

    # we accept a list of text nodes.
    for old_node in old_nodes:

        # e.g. old_node.text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        # for each node extract images text using function "images"
        # image data contains a list of tuples.
        # e.g. [("to boot dev", "https://www.boot.dev"),("to youtube", "https://www.youtube.com/@bootdotdev")]
        links_data = extract_markdown_links(old_node.text)

        # check for no image data
        if not links_data:
            new_nodes.append(old_node)
        else:
            # e.g. ("to boot dev", "https://www.boot.dev")
            text, url = links_data[0]
            # e.g. ["This is text with a link ", " and [to youtube](https://www.youtube.com/@bootdotdev)",
            before_split, after_split = old_node.text.split(f"[{text}]({url})", 1)
            new_nodes.extend(
                [
                    TextNode(before_split, TextType.TEXT),
                    TextNode(text, TextType.LINK, url),
                ]
            )

            # if there is text in after_split, then run following recurssion, **extending** new_nodes.
            if after_split:
                new_nodes.extend(
                    split_nodes_links([TextNode(after_split, TextType.TEXT)])
                )
    return new_nodes

