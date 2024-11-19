import System.Drawing
import System.Windows.Forms
import math
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightSteelBlue
        self._button1.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 295)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(229, 87)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightSteelBlue
        self._button2.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(247, 295)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(101, 87)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkRed
        self._button3.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(358, 295)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(101, 87)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.LightSteelBlue
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Stencil", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 9)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(229, 56)
        self._label2.TabIndex = 4
        self._label2.Text = "Pay:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.LightSteelBlue
        self._listBox1.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 19
        self._listBox1.Location = System.Drawing.Point(247, 9)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(328, 270)
        self._listBox1.TabIndex = 5
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.SlateGray
        self.ClientSize = System.Drawing.Size(587, 394)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog 122 B (hourly pay)"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = "Hourly Pay at 4.00$, per hour"
        self._listBox1.Items.Add(heading)
        pay = 4.00
        hour = 1 
        work = 1
        for hour in range (0, 41):
          
           Money = hour * pay
           
           Time = work * hour
            
            
           line = str(Money) + "                " + str(Time)
            
           line2 = "" 
           self._listBox1.Items.Add(line)
           
          
           
           
           
            
            

    def TextBox1TextChanged(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear(line) 