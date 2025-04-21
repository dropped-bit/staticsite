from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for node in old_nodes:
        current_nodes = []
        split_strings = []
        if node.text_type is not TextType.TEXT:
            current_nodes.append(node)
        if node.text_type is TextType.TEXT:
            split_strings.extend(node.text.split(delimiter))
            for i in range(0, len(split_strings)):
                if i == 1:
                    current_nodes.append(TextNode(split_strings[i], text_type))
                else:
                    current_nodes.append(TextNode(split_strings[i], TextType.TEXT))
        new_nodes.append(current_nodes)

    return new_nodes


# TODO: Iterate over the list of split text and identiy which text type it is
# TODO: Append to new list of TextNodes
node = TextNode("This is text with a `code block` word", TextType.TEXT)
print(split_nodes_delimiter([node], "`", TextType.CODE))
