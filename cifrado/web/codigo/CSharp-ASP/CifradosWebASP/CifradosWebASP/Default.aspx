<%@ Page Title="Home Page" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeFile="Default.aspx.cs" Inherits="_Default" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">

    <div class="jumbotron">
        <h1>.NET</h1>
        <p class="lead">Palabra a Cifrar</p>
        <p>
            <asp:TextBox ID="TextBox1" runat="server"  Height="44px" Width="1795px" ></asp:TextBox>
        </p>
        <asp:Panel ID="Panel1" runat="server" Height="624px" Width="1797px">
            <asp:Label ID="Label1" runat="server"  Font-Size="Large" Text="Cifrado Cesar"></asp:Label>
            <br />
            <asp:DropDownList ID="DropDownList1" runat="server" Height="36px" Width="768px">
            </asp:DropDownList>
            <br />
            <asp:TextBox ID="TextBox2" runat="server" Height="133px" Width="1788px"></asp:TextBox>
            <br />
            <asp:Label ID="Label2" runat="server" Font-Size="Large" Text="Reverse:"></asp:Label>
            <br />
            <asp:TextBox ID="TextBox3" runat="server" Height="156px" Width="1788px"></asp:TextBox>
            <br />
            <asp:Label ID="Label3" runat="server" Font-Size="Large" Text="ReverseGroup:"></asp:Label>
            <br />
            <asp:DropDownList ID="DropDownList2" runat="server" Height="36px" Width="762px">
            </asp:DropDownList>
            <br />
            <asp:TextBox ID="TextBox4" runat="server" Height="171px" Width="1791px"></asp:TextBox>
            <br />
            <asp:Button ID="Button1" runat="server" Font-Size="Large" OnClick="Button1_Click" Text="CIFRAR" />
        </asp:Panel>

    </div>

    <div class="row">
    </div>
</asp:Content>
