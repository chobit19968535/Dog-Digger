namespace DashBoard
{
    partial class Form_dash_board
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label_ticker = new System.Windows.Forms.Label();
            this.textBox_ticker_input = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // label_ticker
            // 
            this.label_ticker.AutoSize = true;
            this.label_ticker.Location = new System.Drawing.Point(12, 9);
            this.label_ticker.Name = "label_ticker";
            this.label_ticker.Size = new System.Drawing.Size(69, 20);
            this.label_ticker.TabIndex = 0;
            this.label_ticker.Text = "Ticker";
            // 
            // textBox_ticker_input
            // 
            this.textBox_ticker_input.Location = new System.Drawing.Point(403, 350);
            this.textBox_ticker_input.Name = "textBox_ticker_input";
            this.textBox_ticker_input.Size = new System.Drawing.Size(64, 27);
            this.textBox_ticker_input.TabIndex = 1;
            this.textBox_ticker_input.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.textBox_ticker_input.KeyDown += new System.Windows.Forms.KeyEventHandler(this.textBox_ticker_input_KeyDown);
            // 
            // Form_dash_board
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(479, 389);
            this.Controls.Add(this.textBox_ticker_input);
            this.Controls.Add(this.label_ticker);
            this.Font = new System.Drawing.Font("Fira Code", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D;
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Form_dash_board";
            this.Text = "Dog Digger";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Label label_ticker;
        private TextBox textBox_ticker_input;
    }
}