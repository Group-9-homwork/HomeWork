import json
from PyQt5.QtWidgets import QInputDialog,QLineEdit,QWidget

def read_json(file_path):
    with open(file_path, 'r') as f:
            content = json.load(f)
    return content


class RemarkModule():
    def __init__(self, ui, file_path):
        self.ui = ui
        self.LabelClassDict = {}
        self.getLabel(file_path)
        self.load_label_ComboBox()
        #print(self.LabelClassDict)


    def remarkStart(self):
        # 添加信号和槽。
        self.ui.remark_cB_class.currentIndexChanged.connect(self.comboBox_label_choose)

    def getLabel(self,file_path):
        self.LabelClassDict = read_json(file_path)


    #读取标签类选择选项
    def load_label_ComboBox(self):
        for keys in self.LabelClassDict.keys():
            self.ui.remark_cB_class.addItem(keys)

    #选择标签类时，更新标签显示列表
    def comboBox_label_choose(self):
        test_choose = self.ui.remark_cB_class.currentText()
        print(test_choose)
        if test_choose != "" :
            self.ui.remark_lW_label.clear()
            new_label = self.LabelClassDict[test_choose]
            self.ui.remark_lW_label.addItems(new_label)






