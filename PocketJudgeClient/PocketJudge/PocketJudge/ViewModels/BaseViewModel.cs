using Microsoft.Rest;
using PocketJudge.Helpers;
using PocketJudge.Models;
using System;
using Xamarin.Forms;

namespace PocketJudge.ViewModels
{
	public class BaseViewModel : ObservableObject
	{
        public PocketJudgeAPI APIClient = new PocketJudgeAPI(
            new Uri(""),
            new BasicAuthenticationCredentials
            {
                UserName = "krochev",
                Password = "Password123"
            }
        );

		bool isBusy = false;
		public bool IsBusy
		{
			get { return isBusy; }
			set { SetProperty(ref isBusy, value); }
		}
		/// <summary>
		/// Private backing field to hold the title
		/// </summary>
		string title = string.Empty;
		/// <summary>
		/// Public property to set and get the title of the item
		/// </summary>
		public string Title
		{
			get { return title; }
			set { SetProperty(ref title, value); }
		}
	}
}

