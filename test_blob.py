import unittest
from blob import EncryptedBlob
from secrets import SecretStore

def test_Secrets_setkey():
    key = '123'
    value = b'123123'
    SecretStore.setkey(key,b'00000')
    SecretStore.setkey(key,value)
    assert SecretStore.allkeys.get(key) == value

def test_EncryptedBlob_cryptdecrypt():
    plaintext = "Simple plaintext"
    testkey = 123
    b = EncryptedBlob(plaintext, testkey)
    assert b is not None
    assert b.content != plaintext

def test_EncryptedBlob_hash():
    plaintext = "Simple plaintext"
    testkey = 'test123'
    SecretStore.setkey(testkey, testkey.encode('utf8'))

    print(SecretStore.allkeys)

    b = EncryptedBlob(plaintext, testkey)

    print(SecretStore.allkeys)

    bhash = b.hmac(testkey)

    assert bhash is not None
    assert bhash[0:5] ==  b'v\xbd\xdfD\x1c\x1d'  # Flaky test.

