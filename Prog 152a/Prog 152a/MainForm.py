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
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightSteelBlue
        self._button1.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 219)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(176, 96)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightSteelBlue
        self._button2.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(194, 219)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(96, 96)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkRed
        self._button3.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(296, 219)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(96, 96)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # listBox1
        # 
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(12, 43)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(379, 121)
        self._listBox1.TabIndex = 3
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.SlateGray
        self.ClientSize = System.Drawing.Size(404, 327)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog 152a"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._listBox1.Items.Add(Heading)
        Heading = "Sum of the multiples of 3"
        
        summed = 3
       
            
        for summed in range (0, 9669):
            repeat(3 + 3)
            
            line = summed
            
        self._listBox1.Items.Add(line)
            
            
            

            

    def Button2Click(self, sender, e):
        self._listBox1.Items.Add(line)

    def Button3Click(self, sender, e):
        Application.Exit()

    def Label1Click(self, sender, e):
        pass