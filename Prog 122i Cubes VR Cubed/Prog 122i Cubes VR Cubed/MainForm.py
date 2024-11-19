﻿import System.Drawing
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
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 374)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(176, 93)
        self._button1.TabIndex = 0
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(194, 374)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(117, 93)
        self._button2.TabIndex = 1
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(317, 374)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(117, 93)
        self._button3.TabIndex = 2
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = True
        # 
        # listBox1
        # 
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(12, 33)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(421, 290)
        self._listBox1.TabIndex = 3
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(446, 479)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog 122i Cubes VR Cubed"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = "Number Cubed"
        self._listBox1.Items.Add(heading)
        heading2 = "Cube Root"
        self._listBox1.Items.Add(heading2)