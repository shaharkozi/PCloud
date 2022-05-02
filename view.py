import tkinter as tk
from tkinter import ttk, font
from tkinter.font import Font

# try:
#     from ctypes import windll
#     windll.shcore.SetProcessDpiAwareness(1)
# except:
#     pass

COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"


class View:

    def __init__(self, controller):
        self.mycontroller = controller

    class PCloud(tk.Tk):
        def __init__(self, controller, *args, **kwargs):
            super().__init__()
            self.myDict = {}
            self.controller = controller
            style = ttk.Style(self)
            style.theme_use("clam")

            style.configure("PCloud_Window.TFrame", background=COLOUR_LIGHT_BACKGROUND)
            style.configure("PCloud.TFrame", background=COLOUR_PRIMARY)
            style.configure(
                "PCloud_Text.TLabel",
                foreground=COLOUR_LIGHT_TEXT,
                background=COLOUR_DARK_TEXT,
                font="Courier 14"
            )

            style.configure(
                "PCloud_Generic_Text.TLabel",
                foreground=COLOUR_LIGHT_TEXT,
                background=COLOUR_DARK_TEXT,
            )

            style.configure(
                "PCloud.TButton",
                foreground=COLOUR_LIGHT_TEXT,
                background=COLOUR_DARK_TEXT,
            )

            style.map(
                "PCloud.TButton",
                background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_LIGHT_TEXT)]
            )


            self.instaceId = []
            self.region = ""
            self.access_key = ""
            self.secret_key = ""
            self.ami = ""

            self["background"] = COLOUR_LIGHT_BACKGROUND
            self.title("Welcom to PCloud")
            self.geometry("1920x1080")
            instance_id_frame = View.inputUserInstanceId(self)
            instance_id_frame.grid(columnspan=10)
            instance_id_frame.place(height=100, width=1920, y=0)
            self.pick_rule_bar = View.ruleBarFrame(self)
            self.pick_rule_bar.grid(rowspan=10, columnspan=10)
            self.pick_rule_bar.place(height=1000, width=1920, y=100)



        def setInstaceId(self, id):
            self.instaceId.append(id)
            print(self.instaceId)

        def setRegion(self, region):
            self.region = region
            print(self.region)

        def setAccessKey(self, key):
            self.access_key = key
            print(self.access_key)


        def setSecretKey(self, key):
            self.secret_key = key
            print(self.secret_key)

        def setAmi(self, key):
            self.ami = key
            print(self.ami)


        def apply(self):
            rule = self.pick_rule_bar.apply()
            self.controller.addRuleTodict(rule['Type'], rule)
            user_details = { "access_key": self.access_key,
                             "secret_key": self.secret_key,
                             "instance_id": self.instaceId,
                             "region": self.region,
                             "ami": self.ami}
            self.controller.applyRule(rule, user_details)
            print(self.controller.dict)


    class inputUserInstanceId(ttk.Frame):
        def __init__(self, container):
            super().__init__(container)
            self.instance_id = tk.StringVar()
            self.access_key = tk.StringVar()
            self.secret_key = tk.StringVar()
            self.AMI = tk.StringVar()
            self.region = tk.StringVar()
            self["style"] = "PCloud.TFrame"

            # instance id-----------------------------------

            instance_label = ttk.Label(self, text="Instance ID:", style="PCloud_Text.TLabel")
            instance_label.config(font=("Segoe UI", 15))
            instance_label.grid(row=0, column=0)
            instance_entry = ttk.Entry(self, width=20, textvariable=self.instance_id)
            instance_entry.grid(row=0, column=1)
            instance_entry.focus()
            enterID_button = ttk.Button(self, text="Enter", style="PCloud.TButton",
                                        command=lambda: container.setInstaceId(instance_entry.get()))
            enterID_button.grid(row=0, column=2)

            # region-----------------------------------

            region_label = ttk.Label(self, text="Region:", style="PCloud_Text.TLabel")
            region_label.config(font=("Segoe UI", 15))
            region_label.grid(row=0, column=3)
            region_entry = ttk.Entry(self, width=20, textvariable=self.region)
            region_entry.grid(row=0, column=4)
            region_entry.focus()
            region_button = ttk.Button(self, text="Enter", style="PCloud.TButton",
                                        command=lambda: container.setRegion(region_entry.get()))
            region_button.grid(row=0, column=5)

            # access key-----------------------------------

            AWS_ACCESS_KEY_label = ttk.Label(self, text="AWS ACCESS KEY:", style="PCloud_Text.TLabel")
            AWS_ACCESS_KEY_label.config(font=("Segoe UI", 15))
            AWS_ACCESS_KEY_label.grid(row=0, column=6)
            AWS_ACCESS_KEY_entry = ttk.Entry(self, width=20, textvariable=self.access_key)
            AWS_ACCESS_KEY_entry.grid(row=0, column=7)
            AWS_ACCESS_KEY_entry.focus()
            enterAWS_ACCESS_KEY_button = ttk.Button(self, text="Enter", style="PCloud.TButton",
                                                    command=lambda: container.setAccessKey(AWS_ACCESS_KEY_entry.get()))
            enterAWS_ACCESS_KEY_button.grid(row=0, column=8)

            # secret key-----------------------------------

            AWS_Secret_KEY_label = ttk.Label(self, text="AWS Secret KEY:", style="PCloud_Text.TLabel")
            AWS_Secret_KEY_label.config(font=("Segoe UI", 15))
            AWS_Secret_KEY_label.grid(row=0, column=9)
            AWS_Secret_KEY_entry = ttk.Entry(self, width=20, textvariable=self.secret_key)
            AWS_Secret_KEY_entry.grid(row=0, column=10)
            AWS_Secret_KEY_entry.focus()
            enterAWS_Secret_KEY_button = ttk.Button(self, text="Enter", style="PCloud.TButton",
                                                    command=lambda: container.setSecretKey(AWS_Secret_KEY_entry.get()))
            enterAWS_Secret_KEY_button.grid(row=0, column=11)

            # ami-----------------------------------

            AWS_AMI_label = ttk.Label(self, text="AWS AMI ID:", style="PCloud_Text.TLabel")
            AWS_AMI_label.config(font=("Segoe UI", 15))
            AWS_AMI_label.grid(row=0, column=12)
            AWS_AMI_entry = ttk.Entry(self, width=20, textvariable=self.AMI)
            AWS_AMI_entry.grid(row=0, column=13)
            AWS_AMI_entry.focus()
            enterAWS_Secret_KEY_button = ttk.Button(self, text="Enter", style="PCloud.TButton",
                                                    command=lambda: container.setAmi(AWS_AMI_entry.get()))
            enterAWS_Secret_KEY_button.grid(row=0, column=14)

            for children in self.winfo_children():
                children.grid_configure(padx=7, pady=7)

    class ruleBarFrame(ttk.Frame):
        def __init__(self, container):
            super().__init__(container)

            self.pcloud = container

            self["style"] = "PCloud.TFrame"
            # Server type-----------------------------------
            self.server_label = ttk.Label(self, text="Server Type:", style="PCloud_Generic_Text.TLabel")
            self.server_label.config(font=("Segoe UI", 15))
            self.server_label.grid(row=2, column=0, padx=(0, 10))

            self.server_define = ('EC2', 'S3')
            self.servers = tk.StringVar(value=self.server_define)
            self.servers_list = ttk.Combobox(self, width=30, values=self.server_define)
            self.servers_list.grid(row=2, column=1)

            self.servers_list.bind('<<ComboboxSelected>>', )

            # Data type --------------------------------------
            self.dataType_label = ttk.Label(self, text="Data Type:", style="PCloud_Text.TLabel")
            self.dataType_label.config(font=("Segoe UI", 15))
            self.dataType_label.grid(row=2, column=2, padx=(0, 10))

            self.dataTypes = ('CPU ', 'IO')

            datas = tk.StringVar(value=self.dataTypes)
            self.dataType_list = ttk.Combobox(self, width=30, values=self.dataTypes)
            self.dataType_list.grid(row=2, column=3)

            # Action ---------------------------------------
            self.action_label = ttk.Label(self, text="Action:", style="PCloud_Text.TLabel")
            self.action_label.config(font=("Segoe UI", 15))
            self.action_label.grid(row=2, column=4, padx=(0, 10))

            self.action_list = ttk.Combobox(self, width=30, textvariable="Create", values=["Create", "Remove", "Start", "Stop"])
            self.action_list.grid(row=2, column=5)

            # Threshold ----------------------------------------
            self.threshold_label = ttk.Label(self, text="Threshold:", style="PCloud_Text.TLabel")
            self.threshold_label.config(font=("Segoe UI", 15))
            self.threshold_label.grid(row=2, column=6, padx=(0, 10))

            self.initial_threshold = tk.IntVar(value=0)
            self.threshold_spin_box = ttk.Spinbox(
                self,
                from_=0,
                to=100,
                textvariable=self.initial_threshold,
                font=Font(family='Segoe UI', size=15),
                wrap=False
            )
            self.threshold_spin_box.grid(row=2, column=7)

            # apply rule button ----------------------------------------
            self.applyRule_button = ttk.Button(self, text="Apply Rule", style="PCloud.TButton",
                                               command=lambda: container.apply())
            self.applyRule_button.grid(row=2, column=9)

            # machines rules Frame ----------------------------------------
            self.listbox_font = ('Times New Roman', 15)
            self.EC2_label = ttk.Label(self, text="EC2", style="PCloud_Text.TLabel")
            self.EC2_label.config(font=("Segoe UI", 15))
            self.EC2_label.grid(row=4, column=1)

            self.EC2_listbox = tk.Listbox(self, height=20, width=90, font=self.listbox_font)
            self.EC2_listbox.grid(row=5, column=0, sticky=tk.W + tk.E, columnspan=5)

            self.S3_label = ttk.Label(self, text="S3", style="PCloud_Text.TLabel")
            self.S3_label.config(font=("Segoe UI", 15))
            self.S3_label.grid(row=4, column=6)

            self.S3_listbox = tk.Listbox(self, height=20, width=90, font=self.listbox_font)
            self.S3_listbox.grid(row=5, column=5, sticky=tk.W + tk.E, columnspan=5)

            for children in self.winfo_children():
                children.grid_configure(padx=15, pady=15)

        def apply(self):
            server_type = self.servers_list.get()
            data = self.dataType_list.get()
            action = self.action_list.get()
            threshold = self.threshold_spin_box.get()
            Dict = {'Type': server_type, 'Data': data, 'Action': action, 'Threshold': threshold}
            str = ""
            if Dict['Type'] == 'EC2':
                for item in Dict:
                    str += item
                    str += ": " + Dict.get(item) + " "
                self.EC2_listbox.insert(tk.END, str)
            elif Dict['Type'] == 'S3':
                for item in Dict:
                    str += item
                    str += ": " + Dict.get(item) + " "
                self.S3_listbox.insert(tk.END, str)

            return Dict



    def start(self):
        root = self.PCloud(self.mycontroller)

        quit_button = ttk.Button(root, text="Quit", command=root.destroy, style="PCloud.TButton")
        quit_button.grid()
        quit_button.place(y=900, x=1800)

        root.mainloop()