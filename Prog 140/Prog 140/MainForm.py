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
        self._button6 = System.Windows.Forms.Button()
        self._button7 = System.Windows.Forms.Button()
        self._button8 = System.Windows.Forms.Button()
        self._button9 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightSteelBlue
        self._button1.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(268, 60)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(146, 46)
        self._button1.TabIndex = 0
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = False
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightSteelBlue
        self._button2.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(268, 117)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(146, 46)
        self._button2.TabIndex = 1
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightSteelBlue
        self._button3.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(268, 169)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(146, 46)
        self._button3.TabIndex = 2
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = False
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.Color.LightSteelBlue
        self._button4.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(420, 60)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(146, 46)
        self._button4.TabIndex = 3
        self._button4.Text = "button4"
        self._button4.UseVisualStyleBackColor = False
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.Color.LightSteelBlue
        self._button5.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(420, 117)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(146, 46)
        self._button5.TabIndex = 4
        self._button5.Text = "button5"
        self._button5.UseVisualStyleBackColor = False
        # 
        # button6
        # 
        self._button6.BackColor = System.Drawing.Color.LightSteelBlue
        self._button6.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button6.Location = System.Drawing.Point(420, 169)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(146, 46)
        self._button6.TabIndex = 5
        self._button6.Text = "button6"
        self._button6.UseVisualStyleBackColor = False
        # 
        # button7
        # 
        self._button7.BackColor = System.Drawing.Color.LightSteelBlue
        self._button7.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button7.Location = System.Drawing.Point(420, 240)
        self._button7.Name = "button7"
        self._button7.Size = System.Drawing.Size(146, 46)
        self._button7.TabIndex = 6
        self._button7.Text = "button7"
        self._button7.UseVisualStyleBackColor = False
        # 
        # button8
        # 
        self._button8.BackColor = System.Drawing.Color.LightSteelBlue
        self._button8.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button8.Location = System.Drawing.Point(420, 292)
        self._button8.Name = "button8"
        self._button8.Size = System.Drawing.Size(146, 46)
        self._button8.TabIndex = 7
        self._button8.Text = "button8"
        self._button8.UseVisualStyleBackColor = False
        # 
        # button9
        # 
        self._button9.BackColor = System.Drawing.Color.LightSteelBlue
        self._button9.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button9.Location = System.Drawing.Point(420, 353)
        self._button9.Name = "button9"
        self._button9.Size = System.Drawing.Size(146, 46)
        self._button9.TabIndex = 8
        self._button9.Text = "button9"
        self._button9.UseVisualStyleBackColor = False
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LightSteelBlue
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 117)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(104, 46)
        self._label1.TabIndex = 9
        self._label1.Text = "label1"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.LightSteelBlue
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 169)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(104, 46)
        self._label2.TabIndex = 10
        self._label2.Text = "label2"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.LightSteelBlue
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 292)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(104, 46)
        self._label3.TabIndex = 11
        self._label3.Text = "label3"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.LightSteelBlue
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Stencil", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 353)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(104, 46)
        self._label4.TabIndex = 12
        self._label4.Text = "label4"
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(578, 496)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button9)
        self.Controls.Add(self._button8)
        self.Controls.Add(self._button7)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog 140"
        self.ResumeLayout(False)


    def Label1Click(self, sender, e):
        pass