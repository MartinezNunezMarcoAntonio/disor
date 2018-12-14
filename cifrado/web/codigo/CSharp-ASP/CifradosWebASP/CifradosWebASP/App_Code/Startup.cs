using Microsoft.Owin;
using Owin;
using System.Web.UI.WebControls;

[assembly: OwinStartupAttribute(typeof(CifradosWebASP.Startup))]
namespace CifradosWebASP
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
