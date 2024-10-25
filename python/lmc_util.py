# 엑셀 파일을 선택하여 읽어 들이고, treeview 에 보여주는 프로그램

import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import pandas as pd

class LmcUtil:
    def __init__(self, root):
        self.root = root
        self.root.title("Letsmilan - Windows")
        self.root.geometry("1600x480") 
        
        self.tree = None  # Treeview를 저장할 변수
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        self.scrollbar_y = Scrollbar(self.root, orient=VERTICAL)
        self.scrollbar_y.pack(side="right", fill="y")

        self.scrollbar_x = Scrollbar(self.root, orient=HORIZONTAL)
        self.scrollbar_x.pack(side="bottom", fill="x")

        self.txt = Text(self.root, yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)
        self.txt.pack(side="left", fill="both", expand=True)
        self.scrollbar_y.config(command=self.txt.yview)
        self.scrollbar_x.config(command=self.txt.xview)

    def create_menu(self):
        menu = Menu(self.root)

        menu_file = Menu(menu, tearoff=0)        
        menu_file.add_command(label="열기", command=self.open_file_dialog)
        menu_file.add_separator()
        menu_file.add_command(label="끝내기", command=self.root.quit)

        menu.add_cascade(label="파일", menu=menu_file)

        menu_edit = Menu(menu, tearoff=0)
        menu_edit.add_command(label="삭제", command=self.delete_text_and_show_grid)

        menu.add_cascade(label="편집", menu=menu_edit)

        self.root.config(menu=menu)  

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(
            title="파일 열기", 
            filetypes=(("엑셀 파일", "*.xlsx"), ("모든 파일", "*.*"))
        )

        if file_path:                        
            print(f"선택한 파일: {file_path}")            
            self.read_excel(file_path)            

    def read_excel(self, file_path):
        try:
            df = pd.read_excel(file_path)
            data_list = df.values.tolist()
            messagebox.showinfo("성공", "엑셀 파일을 성공적으로 읽었습니다.")
            self.df = df
            self.data_list = data_list
            self.delete_text_and_show_grid()
        except Exception as e:
            messagebox.showerror("에러", f"엑셀 파일을 읽는 중 오류가 발생했습니다: {e}")                    

    def delete_text_and_show_grid(self):
        # 기존 Treeview가 있으면 삭제합니다.
        if self.tree:
            self.tree.destroy()

        # Text 위젯과 스크롤바를 삭제합니다.
        self.txt.pack_forget()
        self.scrollbar_y.pack_forget()
        self.scrollbar_x.pack_forget()

        # Treeview를 생성합니다.
        columns = list(self.df.columns)
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings', yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)

        # 컬럼 헤더를 설정합니다.
        for col in columns:
            self.tree.heading(col, text=col)

        # 데이터 삽입
        for row in self.data_list:
            self.tree.insert("", "end", values=row)

        self.tree.pack(fill="both", expand=True)
        self.scrollbar_y.config(command=self.tree.yview)
        self.scrollbar_x.config(command=self.tree.xview)

        self.scrollbar_y.pack(side="right", fill="y")
        self.scrollbar_x.pack(side="bottom", fill="x")

if __name__ == "__main__":
    root = Tk()
    notepad = LmcUtil(root)
    root.mainloop()
