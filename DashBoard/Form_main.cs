using Python.Runtime;
using System.Reflection.Emit;


namespace DashBoard
{
    public partial class Form_dash_board : Form
    {
        string email { get; set; }
        string password { get; set; }
        dynamic DG { get; set; }

        public Form_dash_board(List<string> info)
        {
            InitializeComponent();
            start_position();
            email = info[0];
            password = info[1];
            login();

        }
        private void login()
        {
            PythonEngine.Initialize();
            PythonEngine.BeginAllowThreads();
            Py.GIL();

            dynamic sys = Py.Import("sys");
            dynamic os = Py.Import("os");
            sys.path.append(os.getcwd());
            sys.path.append("X:\\C#\\Dog Digger\\Dog Digger");
            DG = Py.Import("Dog_Digger");

            DG.set_accountName(email);
            DG.set_password(password);
            DG.start();
        }

        private void textBox_ticker_input_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                string ticker = textBox_ticker_input.Text;
                label_ticker.Text = ticker;
                DG.set_ticker(ticker);
                DG.dig();
            }
        }
        private void start_position()
        {
            var size = Screen.FromControl(this).Bounds;
            this.Width = size.Width / 2;
            this.Height = size.Height;
            this.Location = new Point(size.Width / 2, 0);
        }
    }
}