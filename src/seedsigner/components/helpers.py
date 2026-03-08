from dataclasses import replace

from seedsigner.loopyUI import Component, Rect, Text, Node


def _offset_node(node: Node, dx: int, dy: int) -> Node:
    if node is None:
        return None

    if isinstance(node, Rect):
        return replace(node, x=node.x + dx, y=node.y + dy)

    if isinstance(node, Text):
        return replace(node, x=node.x + dx, y=node.y + dy)

    if isinstance(node, Component):
        return _offset_node(node.render(), dx, dy)

    if isinstance(node, list):
        return [_offset_node(child, dx, dy) for child in node]

    if isinstance(node, tuple):
        return [_offset_node(child, dx, dy) for child in node]

    raise ValueError(f"unrecognized node: {node}")
