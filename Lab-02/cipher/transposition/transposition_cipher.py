class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        rows = len(text) // key
        decrypted_text = [''] * rows
        
        index = 0
        for col in range(key):
            for row in range(rows):
                decrypted_text[row] += text[index]
                index += 1

        return ''.join(decrypted_text)




