
using Microsoft.Rest;
using Newtonsoft.Json;
using PocketJudge.Models;
using System;
using System.Collections.Generic;
using Xamarin.Forms;

namespace PocketJudge.Views
{
	public partial class AboutPage : ContentPage
	{
		public AboutPage()
		{
			InitializeComponent();

            var client = new PocketJudgeAPI(
                new Uri("https://a6a76f48.ngrok.io"),
                new BasicAuthenticationCredentials
                {
                    UserName = "krochev",
                    Password = "Password123"
                }
            );

            var response = client.Competences.ListWithHttpMessagesAsync().GetAwaiter().GetResult().Response;
            var competences = JsonConvert.DeserializeObject<List<Competence>>(response.Content.ReadAsStringAsync().GetAwaiter().GetResult());
        }
	}
}
