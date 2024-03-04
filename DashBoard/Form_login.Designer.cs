namespace DashBoard
{
    partial class Form_login
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.textBox_user_name = new System.Windows.Forms.TextBox();
            this.label_user_name = new System.Windows.Forms.Label();
            this.label_user_password = new System.Windows.Forms.Label();
            this.textBox_user_password = new System.Windows.Forms.TextBox();
            this.button_submit = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // textBox_user_name
            // 
            this.textBox_user_name.Location = new System.Drawing.Point(198, 41);
            this.textBox_user_name.Margin = new System.Windows.Forms.Padding(5);
            this.textBox_user_name.Name = "textBox_user_name";
            this.textBox_user_name.Size = new System.Drawing.Size(266, 27);
            this.textBox_user_name.TabIndex = 0;
            this.textBox_user_name.Text = "chobit19968535@gmail.com";
            // 
            // label_user_name
            // 
            this.label_user_name.AutoSize = true;
            this.label_user_name.Location = new System.Drawing.Point(27, 48);
            this.label_user_name.Margin = new System.Windows.Forms.Padding(5, 0, 5, 0);
            this.label_user_name.Name = "label_user_name";
            this.label_user_name.Size = new System.Drawing.Size(109, 20);
            this.label_user_name.TabIndex = 1;
            this.label_user_name.Text = "User-Email";
            // 
            // label_user_password
            // 
            this.label_user_password.AutoSize = true;
            this.label_user_password.Location = new System.Drawing.Point(27, 89);
            this.label_user_password.Margin = new System.Windows.Forms.Padding(5, 0, 5, 0);
            this.label_user_password.Name = "label_user_password";
            this.label_user_password.Size = new System.Drawing.Size(139, 20);
            this.label_user_password.TabIndex = 2;
            this.label_user_password.Text = "User-Password";
            // 
            // textBox_user_password
            // 
            this.textBox_user_password.Location = new System.Drawing.Point(198, 82);
            this.textBox_user_password.Margin = new System.Windows.Forms.Padding(5);
            this.textBox_user_password.Name = "textBox_user_password";
            this.textBox_user_password.PasswordChar = '*';
            this.textBox_user_password.Size = new System.Drawing.Size(266, 27);
            this.textBox_user_password.TabIndex = 3;
            this.textBox_user_password.Text = "zapdAj-pepbe4-bykzuf";
            // 
            // button_submit
            // 
            this.button_submit.Font = new System.Drawing.Font("Fira Code", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.button_submit.Location = new System.Drawing.Point(389, 126);
            this.button_submit.Name = "button_submit";
            this.button_submit.Size = new System.Drawing.Size(75, 35);
            this.button_submit.TabIndex = 4;
            this.button_submit.Text = "Login";
            this.button_submit.UseVisualStyleBackColor = true;
            this.button_submit.Click += new System.EventHandler(this.button_submit_Click);
            // 
            // Form_login
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Control;
            this.ClientSize = new System.Drawing.Size(501, 173);
            this.Controls.Add(this.button_submit);
            this.Controls.Add(this.textBox_user_password);
            this.Controls.Add(this.label_user_password);
            this.Controls.Add(this.label_user_name);
            this.Controls.Add(this.textBox_user_name);
            this.Font = new System.Drawing.Font("Fira Code", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.ForeColor = System.Drawing.SystemColors.ControlText;
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Margin = new System.Windows.Forms.Padding(5);
            this.Name = "Form_login";
            this.Text = "Form_login";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private TextBox textBox_user_name;
        private Label label_user_name;
        private Label label_user_password;
        private TextBox textBox_user_password;
        private Button button_submit;
    }
}