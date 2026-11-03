
import heapq
from collections import Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_encoding(text):
    frequencies = Counter(text)
    heap = []

    for char, freq in frequencies.items():
        heapq.heappush(heap, Node(char, freq))

    if len(heap) == 1:
        only = heap[0]
        return {only.char: "0"}

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right

        heapq.heappush(heap, parent)

    codes = {}

    def generate_codes(node, code):
        if node.char is not None:
            codes[node.char] = code
            return

        generate_codes(node.left, code + "0")
        generate_codes(node.right, code + "1")

    generate_codes(heap[0], "")

    return codes


text = input("Enter text to encode: ")

if not text:
    print("Please enter some text.")
else:
    codes = huffman_encoding(text)

    print("\nCharacter frequencies and Huffman codes:")

    for char, code in sorted(codes.items()):
        display = repr(char)
        print(f"{display}: {code}")

    encoded = "".join(codes[char] for char in text)

    print("\nEncoded bit string:")
    print(encoded)
