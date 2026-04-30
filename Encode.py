import bitIO
import PQHeap

f = open("KingJamesBible.txt", "rb") #read file as bits
ftext = f.read()

bitfile = bitIO.BitReader(f)

def make_table(file: str) -> list:
    table = [0]*256
    for elem in file:
        table[elem] += 1
    return table

def make_huffman(table: list) -> list: 
    """huffman = PQHeap.createEmptyPQ()
    for elem in table:
        PQHeap.insert(huffman, elem)
    """



print(make_huffman(make_table(ftext)))