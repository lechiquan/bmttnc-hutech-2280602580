import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class CaesarCipherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect button click events to methods
        self.ui.btn_encrypt.clicked.connect(self.encrypt_message)
        self.ui.btn_decrypt.clicked.connect(self.decrypt_message)
    
    def encrypt_message(self):
        # Cập nhật URL mới
        url = "http://127.0.0.1:5000/api/Playfail/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.text()
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data["encrypted_message"])
                self.show_message("Encrypted Successfully")
            else:
                self.show_message("Error while calling API")
        except requests.exceptions.RequestException as e:
            self.show_message(f"Error: {e}")
    
    def decrypt_message(self):
        # Cập nhật URL mới
        url = "http://127.0.0.1:5000/api/Playfail/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.text()
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setText(data["decrypted_message"])
                self.show_message("Decrypted Successfully")
            else:
                self.show_message("Error while calling API")
        except requests.exceptions.RequestException as e:
            self.show_message(f"Error: {e}")
    
    def show_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CaesarCipherApp()
    window.show()
    sys.exit(app.exec_())
