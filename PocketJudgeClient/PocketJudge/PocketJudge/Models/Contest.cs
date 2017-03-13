﻿// Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.

namespace App2.Models
{
    using System;
    using System.Linq;
    using System.Collections.Generic;
    using Newtonsoft.Json;
    using Microsoft.Rest;
    using Microsoft.Rest.Serialization;

    public partial class Contest
    {
        /// <summary>
        /// Initializes a new instance of the Contest class.
        /// </summary>
        public Contest() { }

        /// <summary>
        /// Initializes a new instance of the Contest class.
        /// </summary>
        public Contest(int? id = default(int?), string name = default(string), IList<Competence> competences = default(IList<Competence>), IList<Project> projects = default(IList<Project>))
        {
            Id = id;
            Name = name;
            Competences = competences;
            Projects = projects;
        }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "id")]
        public int? Id { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "name")]
        public string Name { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "competences")]
        public IList<Competence> Competences { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "projects")]
        public IList<Project> Projects { get; set; }

    }
}
