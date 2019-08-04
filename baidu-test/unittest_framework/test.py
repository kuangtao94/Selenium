import tkinter 
import random
class function(object):
    def __init__(self):
        self.window = tkinter.Tk(className=' TEST') 
        self.test = tkinter.Label(self.window)
        self.guess = tkinter.Entry(self.window,width=30)
        self.display_info = tkinter.Listbox(self.window, width=30)
        self.click_button = tkinter.Button(self.window,width=20,command = self.gui_input,text ='确定')
    def gui_arrang(self):
        self.test.pack()
        self.guess.pack()
        self.display_info.pack()
        self.click_button.pack()
        self.a = random.randint(1,100)
        self.display_info.insert(0,'请输入数字')
    def gui_input(self):
        number = self.guess.get()
        number_guess = int(number)
        self.display_info.delete(0,tkinter.END)
        if number_guess !=self.a:
            number_guess = int(number)
            if number_guess < self.a:
                self.display_info.insert(0,'Small')
                self.display_info.insert(1,'again')
            else:
                self.display_info.insert(0,'big')
                self.display_info.insert(1,'again')
        else:
            self.display_info.insert(0,'Yes')
            self.display_info.insert(1,'Over')
def main():
    FC = function()
    FC.gui_arrang()
    tkinter.mainloop()
    pass
if __name__ == "__main__":
    main()