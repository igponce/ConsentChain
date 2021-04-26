from cryptography.fernet import Fernet

"""
Ephemeral (by now) SecretStore.
"""
class SecretStore:

  allkeys = {}

  @staticmethod
  def getkey(id):
    key = SecretStore.allkeys.get(id)
    if key is None:
      key = Fernet.generate_key()
      SecretStore.setkey(id,key)

    return Fernet(key)

  @staticmethod
  def setkey(id, key):
    SecretStore.allkeys[id] = key
