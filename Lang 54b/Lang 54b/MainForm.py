import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Maroon
        self._textBox1.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.Color.White
        self._textBox1.Location = System.Drawing.Point(28, 55)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(181, 38)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.Maroon
        self._textBox2.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.ForeColor = System.Drawing.Color.White
        self._textBox2.Location = System.Drawing.Point(28, 99)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(181, 38)
        self._textBox2.TabIndex = 1
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.Maroon
        self._textBox3.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.ForeColor = System.Drawing.Color.White
        self._textBox3.Location = System.Drawing.Point(28, 143)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(181, 38)
        self._textBox3.TabIndex = 2
        # 
        # textBox4
        # 
        self._textBox4.BackColor = System.Drawing.Color.Maroon
        self._textBox4.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.ForeColor = System.Drawing.Color.White
        self._textBox4.Location = System.Drawing.Point(28, 187)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(181, 38)
        self._textBox4.TabIndex = 3
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Maroon
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Nirmala Text", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(248, 99)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(211, 38)
        self._label1.TabIndex = 4
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.Click += self.Label1Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Maroon
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Nirmala Text", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.White
        self._label2.Location = System.Drawing.Point(248, 143)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(211, 38)
        self._label2.TabIndex = 5
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Showcard Gothic", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(28, 266)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(181, 86)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Showcard Gothic", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(248, 266)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(211, 86)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkRed
        self._button3.Font = System.Drawing.Font("Showcard Gothic", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(29, 358)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(430, 86)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Firebrick
        self.ClientSize = System.Drawing.Size(479, 460)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Lang 54b"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()

    def Label1Click(self, sender, e):
        pass
    def Button1Click(self, sender, e):
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        num3 = int(self._textBox3.Text)
        num4 = int(self._textBox4.Text)




        Sum = num1 + num2 + num3 + num4
        Ave = num1 + num2 + num3 + num4 / 4.0

        self._label1.Text = str(Sum)
        
        self._label2.Text = str(Ave)
    
    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._label1.Text = ""
        self._label2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

   

    def MainFormLoad(self, sender, e):
        pass