import uuid
import time
import copy


class Transaction():

    def __init__(self, senderPublicKey, receiverPublicKey, amount, type):
        self.senderPublicKey = senderPublicKey
        self.receiverPublicKey = receiverPublicKey
        self.amount = amount
        self.type = type
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''

    def toJson(self):
        return self.__dict__ 

    def sign(self, signature):
        self.signature = signature

    def payload(self):
        # consistent representation of signature
        jsonRepresentation = copy.deepcopy(self.toJson())
        jsonRepresentation['signature'] = ''
        return jsonRepresentation
    
    def equals(self, transaction):
        # uuid generates globally unique id
        if self.id == transaction.id:
            return True
        else:
            return False



