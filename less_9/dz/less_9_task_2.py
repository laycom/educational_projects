# 2. Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter, namedtuple
import heapq
from binarytree import Node

class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc +'1')
        
class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_encode(s):
    h = []
    code = {}
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    
    count = len(h)
    while len(h) > 1:
        freq_1, _count1, left = heapq.heappop(h)
        freq_2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq_1 + freq_2, count, Node(left, right)))
        count += 1
        for item in h:
            print(item)
        print()
        
    if h:    
        [(_freq, _count, root)] = h
        root.walk(code, '')
        
    return code
    
def huffman_decode(en, code):
    pointer = 0
    encoded_str = ''
    while pointer < len(en):
        for ch in code.keys():
            if en.startswith(code[ch], pointer):
                encoded_str += ch
                pointer += len(code[ch])
    return encoded_str
    
def main():
    s = input('Введите строку: ')
    code = huffman_encode(s)
    encode = ''.join(code[ch] for ch in s)
    print(len(code))
    for ch in sorted(code):
        print('{}: {}'.format(ch, code[ch]))
    print(encode)
    
    print()
    print(huffman_decode(encode, code))
 
if __name__ == "__main__":
    main()

