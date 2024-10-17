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
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Segoe Marker", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 311)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(114, 82)
        self._button1.TabIndex = 0
        self._button1.Text = "Food"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Segoe Marker", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(132, 311)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(114, 82)
        self._button2.TabIndex = 1
        self._button2.Text = "Shops"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Segoe Marker", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(252, 311)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(114, 82)
        self._button3.TabIndex = 2
        self._button3.Text = "Fun Things"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.Font = System.Drawing.Font("Segoe Marker", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(372, 311)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(114, 82)
        self._button4.TabIndex = 3
        self._button4.Text = "Clear"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.Color.DarkRed
        self._button5.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(492, 311)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(114, 82)
        self._button5.TabIndex = 4
        self._button5.Text = "Exit"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.SteelBlue
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Showcard Gothic", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 17)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(594, 291)
        self._label1.TabIndex = 5
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightBlue
        self.ClientSize = System.Drawing.Size(619, 405)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "phone numbers"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text="Culvers (608-756-2611) \nFive Guys (608-754-8840)"

    def Button2Click(self, sender, e):
        self._label1.Text="Festival Foods (608-563-5841) \nCTR Automotive Center (608-373-9750) "

    def Button3Click(self, sender, e):
        self._label1.Text="Movies 16 (608-743-0200) \nThe Edge Paintball Experience (608-931-3517)"

    def Button4Click(self, sender, e):
        self._label1.Text=""

    def Button5Click(self, sender, e):
        Application.Exit()