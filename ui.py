import sys
import os
import json
import time
from PyQt5 import QtWidgets, uic
from uuid import uuid4

class App:
    def __init__(self) -> None:
        self.data_file = "data.json"
        if not os.path.isfile(self.data_file):
            with open(self.data_file, "w") as jf:
                jf.write("[]")
                self.data = []
        else:
            with open(self.data_file, "r") as jf:
                self.data = json.loads(jf.read())
        
        self.init_main()
        self.launch_main()
    
    def init_main(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.main = uic.loadUi("ui/main.ui")
    
    def launch_main(self):
        self.main.show()

        # main window event handlers
        self.main.newAction.triggered.connect(self.launch_new)

        sys.exit(self.app.exec_())
    
    def load_chord_file(self, uid):
        print(uid)
    
    def clear_new_form(self):
        self.new.bandIpt.setText("")
        self.new.nameIpt.setText("")
    
    def create_song(self):
        uid = str(uuid4())
        band = self.new.bandIpt.text()
        name = self.new.nameIpt.text()
        file = uid + ".txt"
        path = "songs/" + file

        with open(path, "w", encoding="utf-8") as tf:
            tf.write("place your lyrics with chords here ...")
        
        append = {
            "uid": uid,
            "band": band,
            "name": name,
            "created": time.time(),
            "updated": 0
        }

        self.data.append(append)

        self.save()

        self.clear_new_form()
        self.new.hide()

        os.popen("notepad " + path)
    
    def launch_new(self):
        self.new = uic.loadUi("ui/new.ui")
        self.new.show()

        # new window event handlers
        self.new.createBtn.clicked.connect(self.create_song)

    def save(self):
        with open(self.data_file, "w") as jf:
            jf.write(json.dumps(self.data, indent=4))

app = App()