﻿// Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.

namespace PocketJudge.Models
{
    using System;
    using System.Linq;
    using System.Collections.Generic;
    using Newtonsoft.Json;
    using Microsoft.Rest;
    using Microsoft.Rest.Serialization;

    public partial class Competence
    {
        /// <summary>
        /// Initializes a new instance of the Competence class.
        /// </summary>
        public Competence() { }

        /// <summary>
        /// Initializes a new instance of the Competence class.
        /// </summary>
        public Competence(int? id = default(int?), string url = default(string), string name = default(string), int? maxMark = default(int?))
        {
            Id = id;
            Url = url;
            Name = name;
            MaxMark = maxMark;
        }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "id")]
        public int? Id { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "url")]
        public string Url { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "name")]
        public string Name { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "max_mark")]
        public int? MaxMark { get; set; }

    }
}
