from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

RPC_USER = "user"
RPC_PASSWORD = "pass"

def get_rpc_connection():
    return AuthServiceProxy("http://%s:%s@127.0.0.1:8332" % (RPC_USER, RPC_PASSWORD))

def display_balance(rpc):
    print "Your balance: %s Gamecredits" % rpc.getbalance()

def check_address(rpc, address):
    """
    Check if the Gamecredits address is valid
    """
    res = rpc.validateaddress(address)
    return res["isvalid"]

def send_transaction(rpc, address, amount):
    if check_address(rpc, address):
        try:
            # Balance should be larger and NOT equal to amount we wish to send 
            # because we need to leave some amount for the transaction fee
            # (usually around 0.001 Gamecredits)
            if rpc.getbalance() > amount:
                tx_id = rpc.sendtoaddress(address, amount)
                print "...aaaaand it's gone"
                print "Transaction id: %s" % tx_id
            else:
                print "Not enough Gamecredits"
        except JSONRPCException as json_err:
            print json_err.error["message"]
    else:
        print "Not a valid Gamecredits address"

if __name__ == "__main__":
    rpc_connection = get_rpc_connection()
    # Show us our balance
    display_balance(rpc_connection)

    adr = raw_input("Enter Gamecredits address: ")
    amount = float(raw_input("Enter amount: "))
    send_transaction(rpc_connection, adr, amount)

    # If the transaction passed our balance should decrement by (amount + fee) Gamecredits
    display_balance(rpc_connection)
