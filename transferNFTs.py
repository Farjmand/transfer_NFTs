class WalletHandler(object):

        web3 = Web3(Web3.HTTPProvider(INFURA_API_URL))

        fromAddress = SENDER_WALLET_ADDRESS
        private_key = PRIVATE_KEY_OF_SENDER_WALLET
        toAddress = RECEIVER_WALLET_ADDRESS
     
        nonce = web3.eth.getTransactionCount(fromAddress)
        abi = NFT_CONTRACT_ABI

        contract_address = NFT_CONTRACT_ADDRESS

        contract = web3.eth.contract(address=contract_address, abi=abi)
        id = ID_OF_NFT
        amount = NUMBER_OF_SHARES
        mint_txn = contract.functions.safeTransferFrom(fromAddress, toAddress, id, amount, data ).buildTransaction(
        {
        'from': fromAddress,
        'nonce': nonce,
        'gas': 1000000,
        'gasPrice': web3.toWei("70", "gwei"),

        }
        )

        signed_txn = web3.eth.account.sign_transaction(mint_txn, 
        private_key=private_key)
        result =  web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print('result,' + result)
       



