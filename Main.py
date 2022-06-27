# implementing transaction class

from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool

if __name__ == '__main__':

    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'

    # transaction = Transaction(sender, receiver, amount, type)

    # # print(transaction.toJson())

    # wallet = Wallet()
    # signature = wallet.sign(transaction.toJson())
    # # print(signature)
    # #appends sign to json first empty then append data inconsistent hence False
    # transaction.sign(signature)
    # # print(transaction.toJson())

    # # check signature
    # signatureValid = wallet.signatureValid(
    #     transaction.payload(), signature, wallet.publicKeyString())
    # print(signatureValid)


    # final part
    wallet = Wallet()
    fraudulentWallet = Wallet()
    pool = TransactionPool()

    transaction = wallet.createTransaction(receiver, amount, type)
    # print(transaction.payload())

    # signatureValid = Wallet.signatureValid(transaction.payload(), transaction.signature, fraudulentWallet.publicKeyString())
    # print(signatureValid)

    if pool.transactionExists(transaction) == False:
        pool.addTrans