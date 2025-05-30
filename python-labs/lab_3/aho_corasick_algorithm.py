from collections import deque
from typing import Dict, List, Optional, Tuple


class AhoCorasickNode:
    def __init__(self):
        self.children: Dict[str, AhoCorasickNode] = {}
        self.fail: Optional[AhoCorasickNode] = None
        self.output: List[str] = []


class AhoCorasick:
    def __init__(self, patterns: List[str]):
        self.root = AhoCorasickNode()
        self.patterns = [p for p in patterns if p]  # usuń puste wzorce
        self._build_trie()
        self._build_failure_links()

    def _build_trie(self):
        for pattern in self.patterns:
            node = self.root
            for char in pattern:
                if char not in node.children:
                    node.children[char] = AhoCorasickNode()
                node = node.children[char]
            node.output.append(pattern)

    def _build_failure_links(self):
        queue = deque()
        # Poziom 1 – dzieci korzenia mają fail ustawiony na root
        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)

        while queue:
            current_node = queue.popleft()
            for char, child in current_node.children.items():
                # Znajdź fail link dla dziecka
                fail_node = current_node.fail
                while fail_node and char not in fail_node.children:
                    fail_node = fail_node.fail
                child.fail = fail_node.children[char] if fail_node and char in fail_node.children else self.root
                child.output += child.fail.output  # propagacja wzorców
                queue.append(child)

    def search(self, text: str) -> List[Tuple[int, str]]:
        result = []
        node = self.root

        for i, char in enumerate(text):
            while node and char not in node.children:
                node = node.fail
            if not node:
                node = self.root
                continue
            node = node.children[char]
            for pattern in node.output:
                result.append((i - len(pattern) + 1, pattern))
        return result

