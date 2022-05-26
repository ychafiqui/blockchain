from datetime import datetime
import hashlib

class block():
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = datetime.now()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        ph = str(self.previous_hash)
        t = str(self.timestamp)
        d = str(self.data)
        n = str(self.nonce)
        return hashlib.sha256(str(ph + t + d + n).encode('utf-8')).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[0:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

class blockchain():
    def __init__(self, difficulty):
        self.chain = [block('block0', '0')]
        self.difficulty = difficulty
    
    def add_block(self, data):
        previous_hash = self.chain[-1].hash
        self.chain.append(block(data, previous_hash))

    def print_chain(self):
        for i in range(len(self.chain)):
            print("previous hash:", self.chain[i].previous_hash)
            print("current hash:", self.chain[i].hash)
            print("data:", self.chain[i].data)
            print("timestamp:", self.chain[i].timestamp)
            print("--------------------------------------------------------------------------------------")

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def mine_block(self, index):
        print(f"Mining block {index}...")
        self.chain[index].mine_block(self.difficulty)
        print(f"Block {index} mined: {self.chain[index].hash}")