import blockchain
import socket

import hash
import datetime


class Block:
    index: int  
    time_stamp: str 
    transactions: []  
    proof: int 
    previous_hash: str 
    hash: str 

    def calc_hash(self) -> str:
        transactions_str = ""
        for string in self.transactions:
            transactions_str += string
        hash_string = (self.index.to_bytes(8, byteorder='big') +
                       str(self.time_stamp).encode('utf-8') + str(transactions_str).encode('utf-8') +
                       self.proof.to_bytes(8, byteorder='big') + self.previous_hash.encode('utf-8'))
        hash_obj = hash.new('streebog256', data=hash_string)
        hash_result = hash_obj.hexdigest()
        return hash_result

    def __init__(self):
        self.index = 0
        self.time_stamp = str(datetime.datetime.now())
        self.transactions = ["Hello", "world"]
        self.proof = 0
        self.previous_hash = "1"
        self.hash = ""

    def init(self, index_in, in_transactions):
        self.index = index_in
        self.time_stamp = str(datetime.datetime.now())
        self.transactions = in_transactions
        self.proof = 0
        self.previous_hash = ""
        self.hash = ""

    def mine_block(self, diff):
        zero_str = '0' * diff
        while self.hash[:diff] != zero_str:
            self.hash = self.calc_hash()
            self.proof += 1
        return self.hash

    def set_previous_hash(self, in_previous_hash):
        self.previous_hash = in_previous_hash

    def get_hash(self):
        return self.hash


class Blockchain:
    def __init__(self, diff):
        self.diff = diff
        self.chain = []
        self.mempool = []
        self.max_size_mempool = 10

    def add_genesis_block(self, new_block: Block):
        hash = new_block.calc_hash()
        new_block.hash = hash
        self.chain.append(new_block)

    def add_block(self, new_block):
        new_block.set_previous_hash(self.get_last_block().get_hash())
        hash = new_block.calc_hash()
        new_block.hash = hash
        new_block.mine_block(self.diff)
        self.chain.append(new_block)

    def get_last_block(self):
        return self.chain[-1]

    def clear_mempool(self):
        self.mempool = []
        

block_chain = blockchain.Blockchain(2)
genesis_block = blockchain.Block()
block_chain.add_genesis_block(genesis_block)
block_index = 0

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5001))
server_socket.listen()

print("Узел блокчейна запущен и прослушивает порт 5000...")

while True:
    client_socket, address = server_socket.accept()
    print(f"Подключение от {address}")
    data = client_socket.recv(1024).decode()

    if data:
        block_chain.mempool.append(data)
        client_socket.send(b"0")
        if len(block_chain.mempool) == block_chain.max_size_mempool:
            block = blockchain.Block()
            block_index = block_index + 1
            block.init(block_index, block_chain.mempool)
            block_chain.add_block(block)
            block_chain.clear_mempool()
    client_socket.close()
