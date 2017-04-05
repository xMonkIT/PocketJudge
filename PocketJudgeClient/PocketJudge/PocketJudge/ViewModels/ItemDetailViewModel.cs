using PocketJudge.Models;

namespace PocketJudge.ViewModels
{
	public class ItemDetailViewModel : BaseViewModel
	{
		public dynamic Item { get; set; }
		public ItemDetailViewModel(/*dynamic item = null*/)
		{
			//Title = item.Text;
			//Item = item;
		}

		int quantity = 1;
		public int Quantity
		{
			get { return quantity; }
			set { SetProperty(ref quantity, value); }
		}
	}
}