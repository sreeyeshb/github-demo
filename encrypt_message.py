import base64
import logging

class EncryptionError(Exception):
    pass

# Configure logging
logging.basicConfig(filename='encryption.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def encrypt_message(message):
    try:
        logging.debug(f"Encrypting message: {message}")
        encoded_bytes = base64.b64encode(message.encode('utf-8'))
        encrypted_message = encoded_bytes.decode('utf-8')
        logging.debug(f"Encrypted message: {encrypted_message}")
        return encrypted_message
    except Exception as e:
        logging.error(f"An error occurred during encryption: {e}")
        raise EncryptionError(f"An error occurred during encryption: {e}")

message = input("Enter a message: ")

encrypted_message = encrypt_message(message)
print(f"Encrypted message: {encrypted_message}")

