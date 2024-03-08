using Microsoft.VisualBasic.Logging;
using Python.Runtime;
using System.Reflection.Emit;


namespace DashBoard
{
    public partial class Form_dash_board : Form
    {
        string email { get; set; }
        string password { get; set; }
        dynamic DG { get; set; }
        Bitmap BMP_CORR_MATRIX { get; set; }

        Bitmap BMP_INCOME { get; set; }
        Bitmap BMP_NET_INCOME { get; set; }
        Bitmap BMP_NON_MAIN_INCOME { get; set; }
        Bitmap BMP_MARGIN { get; set; }

        Bitmap BMP_PAYMENT { get; set; }
        Bitmap BMP_RESEARCH_PER_INCOME { get; set; }
        Bitmap BMP_RESEARCH_PER_PAYMENT { get; set; }
        Bitmap BMP_EPS { get; set; }
        ENVS system_path { get; set; }


        public Form_dash_board(List<string> info)
        {
            InitializeComponent();
            start_position();
            component_setting();
            system_path = new ENVS();

            email = info[0];
            password = info[1];
            login();

        }
        private void login()
        {

            Runtime.PythonDLL = system_path.python_dll;

            //string pathToVirtualEnv = "C:/Users/felk/venv39";

            //string path = Environment.GetEnvironmentVariable("PATH")!.TrimEnd(Path.PathSeparator);
            //path = string.IsNullOrEmpty(path) ? pathToVirtualEnv : path + Path.PathSeparator + pathToVirtualEnv;
            //Environment.SetEnvironmentVariable("PATH", path, EnvironmentVariableTarget.Process);
            //Environment.SetEnvironmentVariable("PYTHONHOME", pathToVirtualEnv, EnvironmentVariableTarget.Process);
            //Environment.SetEnvironmentVariable("PYTHONPATH",
            //    $"{pathToVirtualEnv}/Lib/site-packages{Path.PathSeparator}" +
            //    $"{pathToVirtualEnv}/Lib{Path.PathSeparator}", EnvironmentVariableTarget.Process);

            //PythonEngine.PythonPath = PythonEngine.PythonPath + Path.PathSeparator +
            //                          Environment.GetEnvironmentVariable("PYTHONPATH", EnvironmentVariableTarget.Process);
            //PythonEngine.PythonHome = pathToVirtualEnv;
            PythonEngine.Initialize();
            PythonEngine.BeginAllowThreads();
            Py.GIL();

            dynamic sys = Py.Import("sys");
            dynamic os = Py.Import("os");

            sys.path.append(os.getcwd());
            sys.path.append(system_path.sharp_work_dir);
            sys.path.append(system_path.pkg_dog_digger_dir);

            //sys.path.append("X:\\C#\\Dog Digger\\Dog Digger");
            DG = Py.Import("Dog_Digger");

            DG.set_sharp_work_dir(system_path.sharp_work_dir);
            DG.set_accountName(email);
            DG.set_password(password);
            DG.start();


        }

        private void textBox_ticker_input_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                string ticker = textBox_ticker_input.Text;
                this.Invoke((MethodInvoker)delegate ()
                {
                    //label_title.Text = ticker;
                });

                DG.set_ticker(ticker);
                DG.dig();

                BMP_EPS = new Bitmap(ticker + "_EPS.png");
                pictureBox_Left_1.Image = BMP_EPS;

                BMP_PAYMENT = new Bitmap(ticker + "_營業總支出.png");
                pictureBox_Left_2.Image = BMP_PAYMENT;

                BMP_RESEARCH_PER_PAYMENT = new Bitmap(ticker + "_研支比.png");
                pictureBox_Left_3.Image = BMP_RESEARCH_PER_PAYMENT;

                BMP_RESEARCH_PER_INCOME = new Bitmap(ticker + "_研營比.png");
                pictureBox_Left_4.Image = BMP_RESEARCH_PER_INCOME;

                BMP_CORR_MATRIX = new Bitmap("PPMCC_" + ticker + ".png");
                pictureBox_corr_mattrix.Image = BMP_CORR_MATRIX;

                BMP_INCOME = new Bitmap(ticker + "_營收.png");
                pictureBox_Right_1.Image = BMP_INCOME;

                BMP_MARGIN = new Bitmap(ticker + "_毛率.png");
                pictureBox_Right_2.Image = BMP_MARGIN;

                BMP_NET_INCOME = new Bitmap(ticker + "_主業損益.png");
                pictureBox_Right_3.Image = BMP_NET_INCOME;

                BMP_NON_MAIN_INCOME = new Bitmap(ticker + "_業外損益.png");
                pictureBox_Right_4.Image = BMP_NON_MAIN_INCOME;



            }
        }
        private void start_position()
        {
            var size = Screen.FromControl(this).Bounds;
            //this.Width = 2560;
            //this.Height = 1080;

            //this.Width = 1920;
            //this.Height = 1080;

            this.Width = 1440;
            this.Height = 900;

            //this.Width = size.Width;
            //this.Height = size.Height;

            this.Location = new Point(150, 100);

        }
        private void component_setting()
        {
            panel_corr_matrix.Width = Math.Min(this.Width, this.Height - panel_bottom.Height);
            panel_corr_matrix.Height = Math.Min(this.Width, this.Height - panel_bottom.Height);
            pictureBox_corr_mattrix.Width = Math.Min(this.Width, this.Height-panel_bottom.Height);
            pictureBox_corr_mattrix.Height = Math.Min(this.Width, this.Height - panel_bottom.Height);
            pictureBox_corr_mattrix.Dock = DockStyle.Left;
            pictureBox_corr_mattrix.BorderStyle = BorderStyle.None;
            pictureBox_corr_mattrix.SizeMode = PictureBoxSizeMode.StretchImage;
            
            panel_left.Width = (this.Width - pictureBox_corr_mattrix.Width) / 2;
            panel_right.Width = (this.Width - pictureBox_corr_mattrix.Width) / 2;
            panel_left.Height = pictureBox_corr_mattrix.Height;
            panel_right.Height = pictureBox_corr_mattrix.Height;

            pictureBox_Left_1.Width = (this.Width - pictureBox_corr_mattrix.Width) / 2;
            pictureBox_Left_1.Height = pictureBox_corr_mattrix.Height / 4;
            pictureBox_Left_1.BorderStyle = BorderStyle.None;
            pictureBox_Left_1.Dock = DockStyle.Top;
            pictureBox_Left_1.SizeMode = PictureBoxSizeMode.StretchImage;

            pictureBox_Left_2.Width = (this.Width - pictureBox_corr_mattrix.Width) / 2;
            pictureBox_Left_2.Height = pictureBox_corr_mattrix.Height / 4;
            pictureBox_Left_2.BorderStyle = BorderStyle.None;
            pictureBox_Left_2.Dock = DockStyle.Top;
            pictureBox_Left_2.SizeMode = PictureBoxSizeMode.StretchImage;

            pictureBox_Left_3.Width = (this.Width - pictureBox_corr_mattrix.Width) / 2;
            pictureBox_Left_3.Height = pictureBox_corr_mattrix.Height / 4;
            pictureBox_Left_3.BorderStyle = BorderStyle.None;
            pictureBox_Left_3.Dock = DockStyle.Top;
            pictureBox_Left_3.SizeMode = PictureBoxSizeMode.StretchImage;

            pictureBox_Left_4.Width = (this.Width - pictureBox_corr_mattrix.Width) / 2;
            pictureBox_Left_4.Height = pictureBox_corr_mattrix.Height / 4;
            pictureBox_Left_4.BorderStyle = BorderStyle.None;
            pictureBox_Left_4.Dock = DockStyle.Top;
            pictureBox_Left_4.SizeMode = PictureBoxSizeMode.StretchImage;

            pictureBox_Right_1.Width = (this.Width - pictureBox_corr_mattrix.Width) / 2;
            pictureBox_Right_1.Height = pictureBox_corr_mattrix.Height / 4;
            pictureBox_Right_1.BorderStyle = BorderStyle.None;
            pictureBox_Right_1.Dock = DockStyle.Top;
            pictureBox_Right_1.SizeMode = PictureBoxSizeMode.StretchImage;

            pictureBox_Right_2.Width = (this.Width - pictureBox_corr_mattrix.Width) / 2;
            pictureBox_Right_2.Height = pictureBox_corr_mattrix.Height / 4;
            pictureBox_Right_2.BorderStyle = BorderStyle.None;
            pictureBox_Right_2.Dock = DockStyle.Top;
            pictureBox_Right_2.SizeMode = PictureBoxSizeMode.StretchImage;

            pictureBox_Right_3.Width = (this.Width - pictureBox_corr_mattrix.Width) / 2;
            pictureBox_Right_3.Height = pictureBox_corr_mattrix.Height / 4;
            pictureBox_Right_3.BorderStyle = BorderStyle.None;
            pictureBox_Right_3.Dock = DockStyle.Top;
            pictureBox_Right_3.SizeMode = PictureBoxSizeMode.StretchImage;

            pictureBox_Right_4.Width = (this.Width - pictureBox_corr_mattrix.Width) / 2;
            pictureBox_Right_4.Height = pictureBox_corr_mattrix.Height / 4;
            pictureBox_Right_4.BorderStyle = BorderStyle.None;
            pictureBox_Right_4.Dock = DockStyle.Top;
            pictureBox_Right_4.SizeMode = PictureBoxSizeMode.StretchImage;
        }

        private void textBox_ticker_input_KeyPress_1(object sender, KeyPressEventArgs e)
        {
            if (!(e.KeyChar == 8 || (e.KeyChar >= 48 && e.KeyChar <= 57)))
            {
                e.Handled = true;
            }
        }
        public class ENVS
        {
            public string sharp_work_dir;
            public string pkg_dog_digger_dir;
            public string python_dll;

            public ENVS() 
            {
                pkg_dog_digger_dir = "";
                sharp_work_dir = Directory.GetCurrentDirectory();
                python_dll = sharp_work_dir + "/python39.dll";
                set_dog_digger(ref pkg_dog_digger_dir);

            }

            private void set_dog_digger(ref string path)
            {
                int total_terms = sharp_work_dir.Split('\\').Length;
                int remove_terms = 5;
                for (int i =0; i < total_terms - remove_terms; i++)
                {
                    pkg_dog_digger_dir += sharp_work_dir.Split('\\')[i] + "\\";
                }
                pkg_dog_digger_dir += "/Dog Digger/";

            }
        }
    }
}