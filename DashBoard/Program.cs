namespace DashBoard
{
    internal static class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            // To customize application configuration such as set high DPI settings or default font,
            // see https://aka.ms/applicationconfiguration.
            ApplicationConfiguration.Initialize();

            string email = "N/A";
            string password = "N/A";

            using (var form = new Form_login()) 
            {
                if (DialogResult.OK == form.ShowDialog()) 
                {
                    email = form.email;
                    password = form.password;
                }
                else
                {
                    Application.Exit();
                }
            }

            List<string> info = new List<string>() { email, password};
            Application.Run(new Form_dash_board(info));
        }
    }
}