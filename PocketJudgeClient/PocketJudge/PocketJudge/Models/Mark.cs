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

    public partial class Mark
    {
        /// <summary>
        /// Initializes a new instance of the Mark class.
        /// </summary>
        public Mark() { }

        /// <summary>
        /// Initializes a new instance of the Mark class.
        /// </summary>
        public Mark(string competence, string project, int markProperty, string url = default(string), string judge = default(string))
        {
            Url = url;
            Competence = competence;
            Project = project;
            Judge = judge;
            MarkProperty = markProperty;
        }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "url")]
        public string Url { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "competence")]
        public string Competence { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "project")]
        public string Project { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "judge")]
        public string Judge { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "mark")]
        public int MarkProperty { get; set; }

        /// <summary>
        /// Validate the object. Throws ValidationException if validation fails.
        /// </summary>
        public virtual void Validate()
        {
            if (Competence == null)
            {
                throw new ValidationException(ValidationRules.CannotBeNull, "Competence");
            }
            if (Project == null)
            {
                throw new ValidationException(ValidationRules.CannotBeNull, "Project");
            }
        }
    }
}