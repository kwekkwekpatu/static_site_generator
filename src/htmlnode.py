from enum import Enum

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        if self.props is not None:
            props_html = ""
            for prop in self.props:
                props_html += f' {prop}="{self.props[prop]}"'
            return props_html
        return ""
    def __repr__(self) -> str:
        return f"HTMLNODE({self.tag}, {self.value}, children: {self.children}, {self.props})"