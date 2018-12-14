using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class _Default : Page
{
    Gestor gestor = new Gestor();
    protected void Page_Load(object sender, EventArgs e)
    {
        foreach( int i in Enumerable.Range(0,11) )
        {
            DropDownList1.Items.Add(i.ToString());
            DropDownList2.Items.Add(i.ToString());
        }
    }


    protected void Button1_Click(object sender, EventArgs e)
    {
        String salto = DropDownList1.Text;
        String grupo = DropDownList1.Text;
        gestor.cesar.salto = Int32.Parse(salto);
        gestor.reverseG.grupo = Int32.Parse(grupo);

        gestor.cifrar( TextBox1.Text );

        TextBox2.Text = gestor.cesar.resultado;
        TextBox3.Text = gestor.reverse.resultado;
        TextBox4.Text = gestor.reverseG.resultado;
    }
}