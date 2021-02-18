"""
Simple test for in-memory blob
"""

class EncryptedBlob:

  self.keyid = None # 
  self.payload = b''

  def __init__ (self, key, data, encrypt=True):
    """
    :param key: symmetric encryption/decryption key id (from secrets)
    :param data: Data to store
    :param encrypt: should I encrypts that data for you (True by default)
    """

    self.keyid = key # From a secrets store, not the acual key

    if encrypt:
      self.blob = _encrypt(blod)


  @staticmethod
  def _encrypt(data, keyid):
    """
    Encrypt data with the given keyid (from a secrets store)
    :param data: bytes data to store
    :param keyid: Key ID to use from secrets store
    """

    the_key = secrets.get(keyid)
    
    if the_key is None:
      # not found, use random key
      the_key = 123 # for test
     
    return encrypt(data, the_key)

  def _decrypt(data, keyid):
    """
    Decrypt the data
    :param data: Data (bytes) to decrypt
    :param key: Key id to use (from a secrets store)
    """

    if key is None:
       return data
    else:
       return decrypt(data, keyid)

  def self.rekey(keyid):
    """
    Rekey (re-encrypt) data with the given key.
    This operation makes possible to store keep fresh data
    in the consent chain.
    :param keyid: Key id (from a secrets store)
    """
    self.blob = _encrypt( self._decrypt(), self.key), keyid)
    self.keyid = keyid
