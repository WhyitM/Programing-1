import System.Drawing
import math
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
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightSteelBlue
        self._button1.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 279)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(212, 78)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightSteelBlue
        self._button2.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(12, 363)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(103, 78)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkRed
        self._button3.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(121, 363)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(103, 78)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.AliceBlue
        self._textBox1.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(12, 47)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(90, 26)
        self._textBox1.TabIndex = 3
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.AliceBlue
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 99)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(212, 21)
        self._label1.TabIndex = 4
        self._label1.Text = " "
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.AliceBlue
        self._textBox2.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(134, 47)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(90, 26)
        self._textBox2.TabIndex = 5
        self._textBox2.TextChanged += self.TextBox2TextChanged
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.LightSteelBlue
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 76)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(212, 21)
        self._label2.TabIndex = 6
        self._label2.Text = " Change"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.LightSteelBlue
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 23)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(90, 21)
        self._label3.TabIndex = 7
        self._label3.Text = " Price"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.LightSteelBlue
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(134, 23)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(90, 21)
        self._label4.TabIndex = 8
        self._label4.Text = "Payment"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.LightSteelBlue
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label5.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 120)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(90, 21)
        self._label5.TabIndex = 9
        self._label5.Text = " Bills"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.LightSteelBlue
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label6.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(12, 151)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(90, 21)
        self._label6.TabIndex = 10
        self._label6.Text = " Quarter"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.LightSteelBlue
        self._label7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label7.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(12, 182)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(90, 21)
        self._label7.TabIndex = 11
        self._label7.Text = " Nickels"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.LightSteelBlue
        self._label8.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label8.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(12, 213)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(90, 21)
        self._label8.TabIndex = 12
        self._label8.Text = " Dimes"
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.LightSteelBlue
        self._label9.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label9.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(12, 245)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(90, 21)
        self._label9.TabIndex = 13
        self._label9.Text = " Pennies"
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.AliceBlue
        self._label10.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label10.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(134, 120)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(90, 21)
        self._label10.TabIndex = 14
        self._label10.Text = " "
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.AliceBlue
        self._label11.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label11.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(134, 151)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(90, 21)
        self._label11.TabIndex = 15
        self._label11.Text = " "
        self._label11.Click += self.Label11Click
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.AliceBlue
        self._label12.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label12.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(134, 182)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(90, 21)
        self._label12.TabIndex = 16
        self._label12.Text = " "
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.AliceBlue
        self._label13.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label13.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(134, 213)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(90, 21)
        self._label13.TabIndex = 17
        self._label13.Text = " "
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.AliceBlue
        self._label14.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label14.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(134, 245)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(90, 21)
        self._label14.TabIndex = 18
        self._label14.Text = " "
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightSlateGray
        self.ClientSize = System.Drawing.Size(290, 453)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Lang 58T"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        
        amountdue = float (self._textBox1.Text)
      
        amountgiven = float (self._textBox2.Text)
      
        changedue = amountgiven - amountdue
        self._label1.Text = str(changedue)
       
        dollarvalue = int(changedue)
        self._label10.Text = str(dollarvalue)
        decimalchange = changedue - dollarvalue
       
        quartervalue = float(decimalchange) // .25
        quarterliteralvalue = float(quartervalue) * .25
      
        rcaq = float(decimalchange) - float(quarterliteralvalue)
        self._label11.Text = str(quartervalue)
      
        dimevalue = float(rcaq) // .10
        self._label13.Text = str(dimevalue)
      
        dimeliteralvalue = float(dimevalue) * .10
        rcad = float(rcaq) - dimeliteralvalue
       
        nickelvalue = float(rcad) // .05
        self._label12.Text = str(nickelvalue)
       
        nickelliteralvalue = float(nickelvalue) * .05
        rcan = float(rcad) - nickelliteralvalue
       
        pennyvalue = float(rcan) // .01
        self._label14.Text = str(pennyvalue)


    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label1.Text = ""
        self._label10.Text = ""
        self._label11.Text = ""
        self._label12.Text = ""
        self._label13.Text = ""
        self._label14.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def TextBox2TextChanged(self, sender, e):
        pass

    def Label11Click(self, sender, e):
        pass