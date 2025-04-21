class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError(f"Do not call this method directly")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}{f'</{self.tag}>' if self.tag is not "img" else ''}"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


#
# Create another child class of HTMLNode called ParentNode. Its constructor should differ from HTMLNode in that:
# The tag and children arguments are not optional
# It doesn't take a value argument
# props is optional
# (It's the exact opposite of the LeafNode class)


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def __repr__(self):
        return f"ParentNode('{self.tag}', {self.children}, {self.props})"

    # Add a .to_html method.
    # If the object doesn't have a tag, raise a ValueError.
    # If children is a missing value, raise a ValueError with a different message.
    # Otherwise, return a string representing the HTML tag of the node and its children.
    # This should be a recursive method (each recursion being called on a nested child node).
    # I iterated over all the children and called to_html on each,
    # concatenating the results and injecting them between the opening and closing tags of the parent.

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no nested html available")
        # if self.props is None:
        #     return None
        children_concat = ""
        for node in self.children:
            children_concat += node.to_html()
        return f"<{self.tag}{f' {self.props}' if self.props else ''}>{children_concat}</{self.tag}>"
