from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([])
win = QWidget()
win.resize(700,500)
win.setWindowTitle('Easy Editor')
lb_imege = QLabel("Картина")

win.show()
app.exec()

btn_dir = QPushButton("Папка")
lw_files = QListWidget()
btn_left = QPushButton("вліво")
btn_right = QPushButton("Вправо")
btn_Flip = QPushButton("Дзеркало")
btn_bw = QPushButton("Ч/Б")


row = QHBoxLayuoy()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_imege, 95)
row_tools = QHBoxLayuoy()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_Flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)


row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)


win.show()


workdir = ''


def filer(files, extensions):
    result = []
    for  filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def chooseWorkdir():
    global workdir
    workdir = QfileDialog.getExistingDirectory()



def showFilenamesList():
    extension = ['.jpg','jpeg','png','gif','bmp']
    chooseWorkdir()
    filenames = filer(os.lister(workir), extensions)
    lw_files.clear()
    for filename in filnames:
        lw_files.addItem(filename)


        btn_dir.clicked.connect(showFilenamesList)
        app.exec()