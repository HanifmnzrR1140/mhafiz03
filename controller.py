from PySide6.QtWidgets import QMainWindow
from calculator_ui import Ui_Form  # Pastikan ini sesuai dengan kelas UI yang dikompilasi dari file .ui

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        # Koneksi tombol sesuai nama widget di file UI
        self.ui.btn1.clicked.connect(lambda: self.button_clicked("1"))  # Tombol '1'
        self.ui.btn2.clicked.connect(lambda: self.button_clicked("2"))
        self.ui.btn3.clicked.connect(lambda: self.button_clicked("3"))
        self.ui.btn4.clicked.connect(lambda: self.button_clicked("4"))
        self.ui.btn5.clicked.connect(lambda: self.button_clicked("5"))
        self.ui.btn6.clicked.connect(lambda: self.button_clicked("6"))
        self.ui.btn7.clicked.connect(lambda: self.button_clicked("7"))
        self.ui.btn8.clicked.connect(lambda: self.button_clicked("8"))
        self.ui.btn9.clicked.connect(lambda: self.button_clicked("9"))
        self.ui.btn0.clicked.connect(lambda: self.button_clicked("0"))
        self.ui.btnadd.clicked.connect(lambda: self.button_clicked("+"))
        self.ui.btnsum.clicked.connect(lambda: self.button_clicked("-"))
        self.ui.btnmul.clicked.connect(lambda: self.button_clicked("*"))
        self.ui.btnDiv.clicked.connect(lambda: self.button_clicked("/"))
        self.ui.btnEquals.clicked.connect(self.calculate_result)
        self.ui.btnClear.clicked.connect(self.clear_input)

        self.current_input = ""  # Menyimpan input sementara

    def button_clicked(self, value):
        self.current_input += value
        self.ui.textEdit.setText(self.current_input)  # Update teks di QTextEdit

    def calculate_result(self):
        try:
            result = str(eval(self.current_input))  # Evaluasi input matematika
            self.ui.textEdit.setText(result)
            self.current_input = result  # Simpan hasil sebagai input berikutnya
        except Exception:
            self.ui.textEdit.setText("Error")
            self.current_input = ""

    def clear_input(self):
        self.current_input = ""
        self.ui.textEdit.clear()
