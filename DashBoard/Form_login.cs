﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.ListView;

namespace DashBoard
{
    public partial class Form_login : Form
    {
        public string email    {get;set;}
        public string password {get;set;}

        public Form_login()
        {
            InitializeComponent();
            start_position();
            email = string.Empty;
            password = string.Empty;

        }

        private void button_submit_Click(object sender, EventArgs e)
        {
            email = textBox_user_name.Text;
            password = textBox_user_password.Text;
            this.DialogResult = DialogResult.OK;
        }

        private void start_position()
        {
            var size =  Screen.FromControl(this).Bounds;
            this.Location = new Point(size.Width/2 - this.Width/2, size.Height/2 - this.Height/2);


        }
    }
}
