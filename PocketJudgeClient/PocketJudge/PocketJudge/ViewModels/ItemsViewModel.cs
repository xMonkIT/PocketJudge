using System;
using System.Diagnostics;
using System.Threading.Tasks;

using PocketJudge.Helpers;
using PocketJudge.Models;
using PocketJudge.Views;

using Xamarin.Forms;

namespace PocketJudge.ViewModels
{
	public class ItemsViewModel : BaseViewModel
	{
		public ObservableRangeCollection<dynamic> Items { get; set; }
		public Command LoadItemsCommand { get; set; }

		public ItemsViewModel()
		{
			Title = "Browse";
			Items = new ObservableRangeCollection<dynamic>();
			LoadItemsCommand = new Command(() => ExecuteLoadItemsCommand());

			MessagingCenter.Subscribe<NewItemPage, dynamic>(this, "AddItem", (obj, item) =>
			{
				//var _item = item as Item;
				//Items.Add(item);
				//await DataStore.AddItemAsync(_item);
			});
		}

		void ExecuteLoadItemsCommand()
		{
			if (IsBusy)
				return;

			IsBusy = true;

			try
			{
				Items.Clear();
				//var items = await DataStore.GetItemsAsync(true);
				Items.ReplaceRange(new[] { new { Title = "asd" } });
			}
			catch (Exception ex)
			{
				Debug.WriteLine(ex);
			}
			finally
			{
				IsBusy = false;
			}
		}
	}
}