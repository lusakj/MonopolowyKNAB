from tkinter import *

from Domain import Model

class CounterApplication(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.model = Model()
        self.create_widgets()

    def presentProducts(self, products):
        result = ""
        for product in products:
            result += '\t' + product.name + product.price + "\n"
        return result

    def presentProduct(self, product):
        return '    ' + product.name + "    " + product.price

    def presentShop(self, shop):
        return shop.name + "\n" + str(shop.coordinates.calculate_distance(0, 0))

    def create_widgets(self):
        self.master.geometry("500x500")

        self.Lb1 = Listbox(self.master, width=100, height=50)
        shops = self.model.search("")
        idx = 1
        for shop in shops:
            self.Lb1.insert(idx, self.presentShop(shop))
            idx += 1
            for product in shop.products:
                self.Lb1.insert(idx, self.presentProduct(product))
                idx += 1

        self.Lb1.pack()
        self.search = Button(self)
        self.create_button("Wyszukaj", self.clear, self.search)
        self.tbox = Entry(self)
        self.tbox.pack()

    def clear(self):
        self.Lb1.delete(0, END)
        shops = self.model.search(self.tbox.get())
        idx = 1
        for shop in shops:
            self.Lb1.insert(idx, self.presentShop(shop))
            idx += 1
            for product in shop.products:
                self.Lb1.insert(idx, self.presentProduct(product))
                idx += 1


    def create_button(self, label, action, button):
        button["text"] = label
        button["command"] = action
        button.pack(side="top")

root = Tk()
app = CounterApplication(master=root)
app.mainloop()








