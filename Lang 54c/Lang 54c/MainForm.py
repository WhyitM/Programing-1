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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightPink
        self._button1.Font = System.Drawing.Font("Playbill", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 55)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(197, 47)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightPink
        self._button2.Font = System.Drawing.Font("Playbill", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(12, 108)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(197, 76)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkRed
        self._button3.Font = System.Drawing.Font("Playbill", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(12, 187)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(400, 72)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Playbill", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(12, 14)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(197, 35)
        self._textBox1.TabIndex = 3
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Playbill", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(215, 14)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(197, 35)
        self._label1.TabIndex = 4
        self._label1.Text = " "
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Playbill", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(215, 58)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(197, 35)
        self._label2.TabIndex = 5
        self._label2.Text = " Area"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Playbill", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(215, 104)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(197, 35)
        self._label3.TabIndex = 6
        self._label3.Text = " "
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Playbill", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(215, 149)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(197, 35)
        self._label4.TabIndex = 7
        self._label4.Text = " Circumfence"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Pink
        self.ClientSize = System.Drawing.Size(483, 475)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Lang 54c"
        self.ResumeLayout(False)
        self.PerformLayout()


    def TextBox1TextChanged(self, sender, e):
        pass
    

    def Button1Click(self, sender, e):
        radius = float(self._textBox1.Text)
        pi = 3.14159
        Area = pi * radius**2
        Cir = 2 * pi * radius
        Area = round(Area, 3) 
        Cir = round(Cir, 3)
     
        
        self._label1.Text = str(Area)
        self._label3.Text = str(Cir)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label1.Text = ""
        self._label3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()