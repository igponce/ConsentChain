"""
Simple test for in-memory blob
"""

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, hmac

"""
Ephemeral (by now) SecretStore.
"""
class SecretStore:

  allkeys = {}

  @staticmethod
  def _getkey(id):
    key = SecretStore.allkeys.get(id)
    if key is None:
      key = Fernet.generate_key()
      SecretStore.setkey(id,key)
    return key

  @staticmethod
  def getkey(id):
    return Fernet(SecretStore._getkey(id))

  @staticmethod
  def setkey(id, key):
    SecretStore.allkeys[id] = key

class EncryptedBlob:

  def __init__ (self, data, keyid, encrypt=True):
    """
    :param data: Data to store
    :param keyid: symmetric encryption/decryption key id (from secret store)
    :param encrypt: should I encrypts that data for you (True by default)
    """

    key = SecretStore.getkey(keyid)
    self.encrypt = encrypt

    if encrypt:
      self.content = self._encrypt(data, key)
    else:
      self.content = data


  @staticmethod
  def _encrypt(data, key=None):
    """
    Encrypt data with the given fernet key (from a secrets store)
    :param data: bytes data to store
    :param key: Fernet Key retrieved from store

    Returns bytes with encrypted data (or None) if that could not be possible.
    """
    
    if key is not None:
      if isinstance(data, str):
        return key.encrypt(data.encode('utf8'))
      elif isinstance(data, bytes):
         return key.encrypt(data)

    return b''

  @staticmethod
  def _decrypt(data, key):
    """
    Decrypt the data
    :param data: Data (bytes) to decrypt
    :param key: Fernet Key to use (from a secrets store)
    """

    if the_key is None:
       return data
    else:
       return key.decrypt(data, the_key)
  
  def hmac(self, keyid=None):
    key = SecretStore._getkey(keyid)
    return self._hmac(key)

  def _hmac(self, key):
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(self.content)
    self.hmac = h.finalize()
    return self.hmac

  def rekey(self,newkeyid, oldkeyid):
    """
    Rekey (re-encrypt) data with the given key.
    This operation makes possible to store keep fresh data
    in the consent chain.
    :param keyid: Key id (from a secrets store)
    """
    self.blob = _encrypt(self._decrypt(self.blob, self.key), keyid)
    self.keyid = keyid

