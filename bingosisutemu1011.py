import tkinter as tk
from tkinter import messagebox
import random

num = list(range(1, 76))  # 1~75の配列を作成
memo = []  # 履歴保存用配列
text_widgets = []  # 追加されたテキストウィジェットを保存するリスト

def btn_click():  # ボタンがクリックされた時実行する関数
    if num:
        ch = random.choice(num)
        num.remove(ch)
        memo.append(ch)
        result_label.config(text=ch)  # ランダム抽出された数字をラベルに保存

        current_text_widget = text_widgets[-1]
        if int(current_text_widget.index('end-1c').split('.')[0]) >= 15:  #15文字に到達したときに右側にテキストボックスを作成
            new_text_widget = tk.Text(memo_text, height=15, width=4, font=("Helvetica", 16))
            new_text_widget.pack(side=tk.LEFT)
            text_widgets.append(new_text_widget)
            current_text_widget = new_text_widget

            new_text_widget.tag_configure("center", justify='center')# 新しいテキストウィジェットにタグを設定
            new_text_widget.tag_configure("big", font=("Helvetica", 16))

        current_text_widget.insert(tk.END, f"{ch}\n", ("center", "big"))  # 現在のテキストウィジェットに追加
        print(ch)
        print(num)
        print(memo)

    else:  # numが空になった場合
        messagebox.showinfo("終了", "もう番号はないよ！みんなビンゴ出来たかな？？")

# GUI画面作成
tki = tk.Tk() 
tki.geometry('640x700')  #サイズ
tki.title('ビンゴゲーム')  

# ボタン
btn = tk.Button(tki, text='ボタン', command=btn_click)  
btn.place(x=130, y=80)  

# 結果の表示
result_label = tk.Label(tki, text="", font=("Helvetica", 32))  # フォント設定
result_label.pack(pady=100)

# 履歴の表示
memo_text = tk.Frame(tki)
memo_text.pack()

# 最初のテキストウィジェットを作成して追加
initial_text_widget = tk.Text(memo_text, height=15, width=4, font=("Helvetica", 16))
initial_text_widget.pack(side=tk.LEFT)
text_widgets.append(initial_text_widget)

# 最初のテキストウィジェットにタグを設定
initial_text_widget.tag_configure("center", justify='center')
initial_text_widget.tag_configure("big", font=("Helvetica", 16))

# 画面をそのまま表示
tki.mainloop()
