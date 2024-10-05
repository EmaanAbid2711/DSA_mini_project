import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QGridLayout, QLabel, QSizePolicy, QHeaderView, QLineEdit
from PyQt5.QtCore import Qt
import pandas as pd
import time
from Algos import BubbleSort, SelectionSort, MergeSort, QuickSort, InsertionSort, CountingSort, RadixSort, BucketSort

dataList = []
df = pd.read_csv("D:\\semester 3\\DSA Lab\\mini project\\maan\\rings(final).csv")
dataList = df.values.tolist()


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Mini Projects')
        self.setGeometry(0, 0, 566, 366)

        self.setStyleSheet("background-color: #e6ccff;")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.title_label = QLabel("Mini Project")
        self.title_label.setStyleSheet("""
                                      font-size: 24px;
                                      font-weight: bold;
                                      color: purple;  
                                      padding: 10px;
                                      """)
        self.title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.title_label)

        # Sorting buttons
        button_layout = QGridLayout()
        self.add_sorting_button(button_layout, "Bubble Sort", self.bubble_sort, 0, 0)
        self.add_sorting_button(button_layout, "Selection Sort", self.selection_sort, 0, 1)
        self.add_sorting_button(button_layout, "Insertion Sort", self.insertion_sort, 0, 2)
        self.add_sorting_button(button_layout, "Merge Sort", self.Merge_sort, 0, 3)
        self.add_sorting_button(button_layout, "Quick Sort", self.Quick_sort, 1, 0)
        self.add_sorting_button(button_layout, "Counting Sort", self.counting_sort, 1, 1)
        self.add_sorting_button(button_layout, "Radix Sort", self.radix_sort, 1, 2)
        self.add_sorting_button(button_layout, "Bucket Sort", self.bucket_sort, 1, 3)
        main_layout.addLayout(button_layout)

        # text box
        self.column_input = QLineEdit()
        self.column_input.setPlaceholderText("Column Name") 
        self.column_input.setStyleSheet("""
                                        QLineEdit{
                                            font-size: 16px;
                                            border: 2px solid black;
                                            color: black;
                                            padding: 12px;  
                                            width: 150%;
                                        }
                                        QLineEdit::placeholder {
                                            color: black;
                                        }""")
        self.column_input.setMaximumWidth(280)
        main_layout.addWidget(self.column_input, alignment=Qt.AlignCenter)

        # table to display data
        self.table = QTableWidget()
        self.table.setRowCount(len(dataList))
        self.table.setColumnCount(6) 
        self.table.setHorizontalHeaderLabels(
            ['Type', "Price", "Discount", "Rating", "Sold", "Overseas"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        main_layout.addWidget(self.table)
        self.load_data()

        # table style sheet
        self.table.setStyleSheet("""
                                QTableWidget{
                                    font-size: 16px;
                                    border: 2px solid black; 
                                    background-color: #f3e6ff;
                                }
                                QHeaderView::section{
                                    background-color: #787a80;
                                    padding: 7px;
                                    font-size: 20px;
                                    font-family: Arial, Helvetica, sans-serif;
                                    width: 13px;
                                    border: 1px solid black;
                                }
                                QTableWidget QTableCornerButton::section {
                                    background-color: #404040;
                                    border: 1px solid black;
                                }
                               """)

        # label to display sorting time
        self.time_Label = QLabel("Sorting Time: No sort")
        self.time_Label.setStyleSheet("""
                                      font-size: 20px;
                                      color: purple; 
                                      font-weight: bold;
                                      padding-top: 10;
                                      """)
        main_layout.addWidget(self.time_Label, alignment=Qt.AlignCenter)  

        # Reset button
        self.Button_reset = QPushButton("Reset")
        self.Button_reset.clicked.connect(self.reset)
        self.Button_reset.setFixedSize(100, 40)
        self.Button_reset.setStyleSheet("""
                            QPushButton {
                                font-size: 23px;
                                background-color: black; 
                                color: white;
                                border-radius: 5px;
                            }
                            QPushButton:hover {
                                background-color: #ffb3ff;
                            }
            """)
        main_layout.addWidget(self.Button_reset, alignment=Qt.AlignCenter)

    def add_sorting_button(self, layout, name, func, row, col):
        button = QPushButton(name)
        button.clicked.connect(func)
        button.setStyleSheet("""
                             QPushButton {
                                font-size: 18px;
                                background-color: black; 
                                color: white; 
                                border-radius: 3px;
                                padding: 10px;
                                margin: 5px;
                             }
                             QPushButton:hover {
                                background-color: #ffb3ff;
                             }
        """)
        layout.addWidget(button, row, col)

    def load_data(self):
           
        for row_index,row_data in enumerate(dataList):
            for col_index,item in enumerate(row_data):
                self.table.setItem(row_index,col_index,QTableWidgetItem(str(item)))

      
            
    # When Insertion Button clicks ,Insertion Sorting Apply
    def insertion_sort(self):
        column_Name=self.column_input.text().strip()
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name")
            return
        start_time = time.time()
        InsertionSort(dataList,column_index)
        end_time=time.time()
        self.load_data()
        self.time_Label.setText(f"Sorting Time: {end_time-start_time}")

    # When selection Button clicks ,selection Sorting Apply
    def selection_sort(self):
        column_Name=self.column_input.text().strip()
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name")
            return
        start_time = time.time()
        SelectionSort(dataList,column_index)
        end_time=time.time()
        self.load_data()
        self.time_Label.setText(f"Sorting Time: {end_time-start_time}")
    
    # When bubble Button clicks ,bubble Sorting Apply
    def bubble_sort(self):

        column_Name=self.column_input.text().strip()
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name")
            return
        start_time = time.time()
        BubbleSort(dataList,column_index)
        end_time=time.time()
        self.load_data()
        self.time_Label.setText(f"Sorting Time: {end_time-start_time}")

    def Merge_sort(self):
        column_Name=self.column_input.text().strip()
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name")
            return
        start_time = time.time()
        MergeSort(dataList,column_index)
        end_time=time.time()
        self.load_data()
        self.time_Label.setText(f"Sorting Time: {end_time-start_time}")

    def Quick_sort(self):
        global dataList
        column_Name=self.column_input.text().strip()
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name")
            return
        start_time = time.time()
        dataList=QuickSort(dataList,column_index)
        end_time=time.time()
        self.load_data()
        self.time_Label.setText(f"Sorting Time: {end_time-start_time}")

    def counting_sort(self):
        column_Name=self.column_input.text().strip()
        if column_Name=="Type" or column_Name=="Overseas":
            self.time_Label.setText(f"Counting Sort is not applicable for {column_Name} column ")
            self.time_Label.setStyleSheet("color:Black;"
                                          "font-size:13px;"
                                          "font-weight:bold;"
                                      "padding-left:150;"
                                      "padding-top:20;")
            return
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid")
            return
        start_time = time.time()
        CountingSort(dataList,column_index)
        end_time=time.time()
        self.load_data()
        self.time_Label.setText(f"Sorting Time: {end_time-start_time}")

    def radix_sort(self):
        column_Name=self.column_input.text().strip()
        if column_Name=="Type" or column_Name=="Overseas":
            self.time_Label.setText(f"Radix Sort is not applicable for {column_Name} column ")
            self.time_Label.setStyleSheet("color:Black;"
                                          "font-size:13px;"
                                          "font-weight:bold;"
                                      "padding-left:150;"
                                      "padding-top:20;")
            return
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name")
            return
        start_time = time.time()
        RadixSort(dataList,column_index)
        end_time=time.time()
        self.load_data()
        self.time_Label.setText(f"Sorting Time: {end_time-start_time}")

    def bucket_sort(self):
        global dataList
        column_Name=self.column_input.text().strip()
        if column_Name=="Type" or column_Name=="Overseas":
            self.time_Label.setText(f"Bucket Sort is not applicable for {column_Name} column ")
            self.time_Label.setStyleSheet("color:Black;"
                                          "font-size:13px;"
                                          "font-weight:bold;"
                                      "padding-left:150;"
                                      "padding-top:20;")
            return
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name")
            return
        start_time = time.time()
        dataList=BucketSort(dataList,column_index)
        end_time=time.time()
        self.load_data()
        self.time_Label.setText(f"Sorting Time: {end_time-start_time}")

    def reset(self):
        global dataList
        df = pd.read_csv("D:\\semester 3\\DSA Lab\\mini project\\maan\\rings(final).csv")
        dataList = df.values.tolist()
        self.load_data()
        self.time_Label.setText("Sorting Time: No sort")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = App()
    exe.show()
    sys.exit(app.exec_())
