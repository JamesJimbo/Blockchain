import datetime
import hashlib

class Block:
    data = None
    next = None
    hash = None
    blockNo = 0
    nonce = 0
    previousHash = 0
    timestamp = datetime.datetime.now()


    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previousHash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlock Number: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\nPrevious Hash: " + str(self.previousHash) + "\n--------------"

class Blockchain:

    diff = 15
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):

        block.previousHash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()

while True:
    try: 
        chainLen = int(input("How long would you like the blockchain to be? "))
        break
    except ValueError:
        print("Invalid input")
        
print(blockchain.head)

for n in range(chainLen):
    blockchain.mine(Block("Block " + str(n+1)))

while blockchain.head != None:
    blockchain.head = blockchain.head.next
