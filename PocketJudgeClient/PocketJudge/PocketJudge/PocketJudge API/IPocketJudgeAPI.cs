﻿// Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.

namespace PocketJudge
{
    using System;
    using System.Collections.Generic;
    using System.Net.Http;
    using System.Threading;
    using System.Threading.Tasks;
    using Newtonsoft.Json;
    using Microsoft.Rest;
    using Models;

    /// <summary>
    /// </summary>
    public partial interface IPocketJudgeAPI : IDisposable
    {
        /// <summary>
        /// The base URI of the service.
        /// </summary>
        Uri BaseUri { get; set; }

        /// <summary>
        /// Gets or sets json serialization settings.
        /// </summary>
        JsonSerializerSettings SerializationSettings { get; }

        /// <summary>
        /// Gets or sets json deserialization settings.
        /// </summary>
        JsonSerializerSettings DeserializationSettings { get; }

        /// <summary>
        /// Subscription credentials which uniquely identify client
        /// subscription.
        /// </summary>
        ServiceClientCredentials Credentials { get; }


        /// <summary>
        /// Gets the ICompetences.
        /// </summary>
        ICompetences Competences { get; }

        /// <summary>
        /// Gets the IContests.
        /// </summary>
        IContests Contests { get; }

        /// <summary>
        /// Gets the IIsJudge.
        /// </summary>
        IIsJudge IsJudge { get; }

        /// <summary>
        /// Gets the IMarks.
        /// </summary>
        IMarks Marks { get; }

        /// <summary>
        /// Gets the IProjects.
        /// </summary>
        IProjects Projects { get; }

        /// <summary>
        /// Gets the IUsers.
        /// </summary>
        IUsers Users { get; }

    }
}
