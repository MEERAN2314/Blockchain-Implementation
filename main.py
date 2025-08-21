from fastapi import FastAPI, Request, responses
from fastapi.templating import Jinja2Templates
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
import hashlib

app = FastAPI()

import datetime

class Block:

    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        digest = hashes.Hash(hashes.SHA256())
        digest.update(str(self.index).encode() + self.timestamp.encode() + str(self.transactions).encode() + self.previous_hash.encode())
        return digest.finalize().hex()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now().isoformat(), ["Genesis Block"], "0")

    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_block = Block(previous_block.index + 1, datetime.datetime.now().isoformat(), transactions, previous_block.hash)
        self.chain.append(new_block)

blockchain = Blockchain()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "chain": blockchain.chain})


@app.post("/add_transaction")
async def add_transaction(transaction: dict):
    blockchain.add_block([transaction])
    return {"message": f"Transaction added: {transaction}"}

@app.get("/chain")
async def get_chain():
    return {"chain": blockchain.chain}
