# PoW-introduction
A **simplified** Proof of Work (PoW) algorithm written in Python for demonstration purposes.

## Prerequisites

- Python v3

## Demonstration
In order to mine a single block, execute: `python miner.py`  
You will need to enter a target which represents a number of zeroes with which the mined blockhash needs to start in order for the mining to succeed.

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
