import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Gainsboro
        self._label1.Location = System.Drawing.Point(56, 38)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Length"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopRight
        self._label1.Click += self.Label1Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Gainsboro
        self._label2.Location = System.Drawing.Point(56, 112)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "Widith"
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Gainsboro
        self._label3.Location = System.Drawing.Point(56, 198)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 2
        self._label3.Text = "Area"
        self._label3.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Gainsboro
        self._label4.Location = System.Drawing.Point(56, 279)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 3
        self._label4.Text = "Perimiter"
        self._label4.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Maroon
        self._label5.ForeColor = System.Drawing.Color.White
        self._label5.Location = System.Drawing.Point(326, 198)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(288, 23)
        self._label5.TabIndex = 4
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Maroon
        self._label6.ForeColor = System.Drawing.Color.White
        self._label6.Location = System.Drawing.Point(326, 279)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(288, 23)
        self._label6.TabIndex = 5
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(56, 364)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 23)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(326, 364)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(75, 23)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(594, 364)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(75, 23)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit "
        self._button3.UseVisualStyleBackColor = True
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(326, 40)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(288, 20)
        self._textBox1.TabIndex = 9
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(326, 109)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(288, 20)
        self._textBox2.TabIndex = 10
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DimGray
        self.ClientSize = System.Drawing.Size(828, 421)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog 52a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        length = int(self._textBox1.Text)
        width  = int(self._textBox2.Text)
        area   = length*width
        perim  = 2 * length + 2 * width
        self._label5.Text=str(area)
        self._label6.Text=str(perim)
        # = - * / % ** pow      // divide & round down
        #int (Interger): a whole number; pos/neg
        #Float (Floating Point Number): any number w/ a decimal
        #str (string): a string of text 

    def Button2Click(self, sender, e):
        self._textBox1.Text= ""
        self._textBox2.Text=""
        self._label5.Text=""
        self._label6.Text=""

    def Label1Click(self, sender, e):
        pass