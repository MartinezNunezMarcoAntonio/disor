using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace CifradosGenerico
{
    internal class CifradoComponente
    {
        List<String> requirements_to_each_encrypt { get; set; }
        String result { get; set; }

        CifradoComponente()
        {
            requirements_to_each_encrypt = new List<string>();
            result = "";
        }
    }
}