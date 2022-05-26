from blockchain import blockchain

bc = blockchain(difficulty=5)

bc.mine_block(0)
bc.add_block("block1")
bc.mine_block(1)
bc.add_block("block2")
bc.mine_block(2)
bc.add_block("block3")
bc.mine_block(3)

print("##############################################################################")

bc.print_chain()