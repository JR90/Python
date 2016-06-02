
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

__author__ = 'Jiwan Rai'

class ItemHireApp(App):
    status_text = StringProperty()

    def __init__(self):
        super(ItemHireApp, self).__init__()
        self.dicDiscp ={}
        self.dicPrice = {}
        self.dicAvail ={}

    def build(self):
        self.title = "ITEM HIRE APP"
        self.root= Builder.load_file('ItemHire.kv')
        self.file_reader()
        self.create_entry_bottons()
        return self.root

    def file_reader(self):
        f= open("items.csv",'r')
        movie= f.readlines()
        n=0


        for i in movie:
            self.movieName = i.strip().split(',')[0]
            self.discp = i.strip().split(',')[1]
            self.dicDiscp [self.movieName] = self.discp
            self.price = float(i.strip().split(',')[2])
            self.dicPrice [self.movieName]= self.price
            self.availablity = i.strip().split(',')[-1]


            if self.availablity== "out":
                self.dicAvail [self.movieName] = "*"

            else:
                self.dicAvail[self.movieName] = ""

    def add_Item(self, added_name, added_desc, added_number):
        f = open("Items.csv", 'a')
        new = added_name+","+added_desc+","+str(added_number)+","+"in\n"
        f.write(new)
        f.close()


    def return_item(self):
        for name in self.dicAvail:
            if self.dicAvail[name] == "*":

                temp_button = Button(text=name)
                temp_button.bind(on_release=self.press_entry_return)
                self.root.ids.entriesBox.add_widget(temp_button)

    def press_entry_return(self, instance):
        name= instance.text
        instance.background_color = (1, 1, 0, 1)
        self.dicAvail[name] = ""
        self.file_updater()



    def hire_item(self):
        for name in self.dicAvail:
            if self.dicAvail[name] == "":

                temp_button = Button(text=name)
                temp_button.bind(on_release=self.press_entry_hire)
                self.root.ids.entriesBox.add_widget(temp_button)

    def press_entry_hire(self, instance):
        name= instance.text
        instance.background_color = (1, 1, 0, 1)
        self.dicAvail[name] = ""
        self.file_updater()




    def create_entry_bottons(self):
        for name in self.dicDiscp:

            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entriesBox.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        self.status_text = "Movie: "+ name + "\nDescription: " + self.dicDiscp[name] + "\nPrice:" + str(self.dicPrice[name])

    def press_add(self):

        self.status_text = "Enter details for new items"

        self.root.ids.popup.open()

    def press_save(self, added_name, added_desc, added_number):

        self.dicPrice[added_name] = added_number
        self.dicDiscp[added_name] = added_desc
        # change the number of columns based on the number of entries (no more than 5 rows of entries)
        self.root.ids.entriesBox.cols = len(self.dicPrice) // 5 + 1
        # add button for new entry (same as in create_entry_buttons())
        temp_button = Button(text=added_name)
        temp_button.background_color = (1, 1, 0, 1)
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.entriesBox.add_widget(temp_button)

        self.root.ids.popup.dismiss()
        self.add_Item(added_name, added_desc, added_number)
        self.clear_fields()

    def file_updater(self):
        f = open('Item.csv','w')
        for name in self.dicDiscp:
            new = name +","+self.dicDiscp[name]+","+str(self.dicPrice[name])+","+self.dicAvail[name]+'\n'
            f.write(new)

        f.close()
        

    def clear_fields(self):

        self.root.ids.addedName.text = ""
        self.root.ids.addedNumber.text = ""

    def press_cancel(self):

        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.status_text = ""

    def exit(self):
        exit()




ItemHireApp().run()




