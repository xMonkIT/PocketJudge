using System;

using PocketJudge.Models;

using Xamarin.Forms;

namespace PocketJudge.Views
{
	public partial class NewItemPage : ContentPage
	{
		public dynamic Item { get; set; }

		public NewItemPage()
		{
			InitializeComponent();

			Item = new 
			{
				Text = "Item name",
				Description = "This is a nice description"
			};

			BindingContext = this;
		}

		async void Save_Clicked(object sender, EventArgs e)
		{
			//MessagingCenter.Send(this, "AddItem", Item);
			await Navigation.PopToRootAsync();
		}
	}
}