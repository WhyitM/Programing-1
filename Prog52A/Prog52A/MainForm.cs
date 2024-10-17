
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Prog52A
{
    /// <summary>
    /// Description of MainForm.
    /// </summary>
    public partial class MainForm : Form
    {
        public MainForm()
        {
            //
            // The InitializeComponent() call is required for Windows Forms designer support.
            //
            InitializeComponent();
            
            //
            // TODO: Add constructor code after the InitializeComponent() call.
            //
        }
        
        void Label1Click(object sender, EventArgs e)
        {
            
        }
        
        def Button1Click(self, sender, e):
            length = 143
            width  = 82
            area   = length * width
            perim  = 2 * length + 2 * width
            self._label5.Text = string(area)
            slef._label6.Text = string(perim) 
        
        void MainFormLoad(object sender, EventArgs e)
        {
            
        }
    }
}
