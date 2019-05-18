# PoW-introduction
A **simplified** Proof of Work (PoW) algorithm written in Python for demonstration purposes.

## Prerequisites

- Python v3

## Demonstration
In order to mine a single block, execute: `python miner.py`  
You will need to enter a target which represents a number of zeroes with which the mined blockhash needs to start in order for the mining to succeed.
Mining difficulty rises with each zero.
For example, `target=00` will complete faster than `target=000000`.

If you want to mine a whole blockchain, execute: `python blockchain.py`.  
Apart from `target` you will need to enter `desired blockchain height` as well. This represents lenght of the blockchain, i.e. number of blocks in the chain. Higher the number, longer the chain.

## sendtx.py
This script is used to present how easily you can make a transaction on the blockchain.
However in order for this to work you will need Gamecredits client synced and running in the background.
You can clone it from [here](https://github.com/gamecredits-project/GameCredits).

*Note:* Gamecredits client syncing can take a couple of hours.

In order to test it (with fake Gamecredits) you should start the client in regtest mode:
```
{your_location}/gamecredits/src/gamecreditsd -regtest -conf={your_location}/.gamecredits/gamecredits.conf -datadir={your_location}/.gamecredits
```

If you have any questions you can contact me at vuk.simunovic@gmail.com.

# FAQ

1) _What does target represent?_  
Target is simply a number of zeroes with which the mined blockhash needs to start in order for the mining to succeed.

2) _Why are there no zeroes in front of a blockhash then?_  
There are, but they are omitted.

3) _What is nonce?_  
The nonce is a 32-bit field whose value we constantly change until we "win the lottery" and mine a new block (we increment it from 0 in this example).

4) _What happens if 2 miners mine the same block at the same time?_  
When 2 blocks are generated at the same time, the agreement on which block is the "winner" depends on the next block.  
The community agrees on the "longest" chain. Sometimes there are multiple chains of equal length, and that's why it can be important to wait for a number of block confirmations, before considering that a transaction will not be undone by a chain reorganization.

5) _Is target always the same?_  
No, it changes (every x blocks) depending on how fast or slow the network was until that point.

6) _So Python cannot be used with the blockchain?_  
Sure it can, in fact many blockchain applications are written in Python, the most popular being bitcoin electrum wallet.