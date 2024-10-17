import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(201, 46)
        self._button1.TabIndex = 0
        self._button1.Text = "First Name"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(12, 64)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(201, 46)
        self._button2.TabIndex = 1
        self._button2.Text = "Middle Name"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(12, 116)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(201, 46)
        self._button3.TabIndex = 2
        self._button3.Text = "Last Name"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(12, 168)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(201, 46)
        self._button4.TabIndex = 3
        self._button4.Text = "Clear"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.Color.DarkRed
        self._button5.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(219, 168)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(201, 46)
        self._button5.TabIndex = 4
        self._button5.Text = "Exit"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # label1
        # 
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(219, 12)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(201, 46)
        self._label1.TabIndex = 5
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(219, 64)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(201, 46)
        self._label2.TabIndex = 6
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(219, 116)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(201, 46)
        self._label3.TabIndex = 7
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(440, 224)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Make Name"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text="Wyatt"

    def Button2Click(self, sender, e):
        self._label2.Text="Terando"

    def Button3Click(self, sender, e):
        self._label3.Text="Matusewic"

    def Button4Click(self, sender, e):
        self._label1.Text=""
        self._label2.Text=""
        self._label3.Text=""

    def Button5Click(self, sender, e):
        Application.Exit()