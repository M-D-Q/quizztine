# importing libraries
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import sys
from scraper import scrap_exam


class Window(QDialog):

    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Let's get started!")

        # Not necessary yet
        # self.setGeometry(0, 0, 500, 600)

        self.form_group_box = QGroupBox("Scrapping info")

        self.size_spinbar = QSpinBox()

        self.link_line_edit = QLineEdit()
        self.name_line_edit = QLineEdit()
        self.file_name_edit = QLineEdit()

        self.txt_box = QCheckBox("Export to txt file", self)
        self.txt_box.setChecked(True)
        self.pdf_box = QCheckBox("Export to pdf file", self)
        self.pdf_box.setChecked(True)

        self.christine_label = QLabel(self)
        pixmap = QPixmap('christine.png')
        self.christine_label.setPixmap(pixmap)

        self.link_label = QLabel("Link to the discussion?")
        self.pages_label = QLabel("Number of pages to scrap?")
        self.name_label = QLabel("Exam name? Format example: exam-101-500:")
        self.file_label = QLabel("Choose a file name to export the links to:")

        self.log_links_found = QTextEdit()
        self.log_links_found.setReadOnly(True)
        self.log_links_found.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        font = self.log_links_found.font()
        font.setFamily("Courier")
        font.setPointSize(10)

        self.create_form()

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.button_box.accepted.connect(self.get_links)

        self.button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()

        main_layout.addWidget(self.form_group_box)

        main_layout.addWidget(self.button_box)

        self.setLayout(main_layout)

    def get_links(self):
        forum_link = self.link_line_edit.text()
        size = int(self.size_spinbar.text())
        exam_name = self.name_line_edit.text()

        file_name = self.file_name_edit.text()

        list_link = scrap_exam(forum_link, size, exam_name, file_name)
        for link in list_link:
            self.log_links_found.append(link)

    def create_form(self):
        layout = QFormLayout()

        layout.addRow(self.christine_label)
        layout.addRow(self.link_label, self.link_line_edit)
        layout.addRow(self.name_label, self.name_line_edit)
        layout.addRow(self.pages_label, self.size_spinbar)
        layout.addRow(self.file_label, self.file_name_edit)
        layout.addRow(self.txt_box)
        layout.addRow(self.pdf_box)

        layout.addRow(QLabel("Links found:"))
        layout.addRow(self.log_links_found)

        self.form_group_box.setLayout(layout)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec())
