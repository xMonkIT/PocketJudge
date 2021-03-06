﻿// Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.

namespace PocketJudge
{
    using System;
    using System.Collections;
    using System.Collections.Generic;
    using System.Threading;
    using System.Threading.Tasks;
    using Microsoft.Rest;
    using Models;

    /// <summary>
    /// Extension methods for Contests.
    /// </summary>
    public static partial class ContestsExtensions
    {
            /// <param name='operations'>
            /// The operations group for this extension method.
            /// </param>
            /// <param name='page'>
            /// </param>
            /// <param name='judges'>
            /// </param>
            public static void List(this IContests operations, string page = default(string), string judges = default(string))
            {
                Task.Factory.StartNew(s => ((IContests)s).ListAsync(page, judges), operations, CancellationToken.None, TaskCreationOptions.None, TaskScheduler.Default).Unwrap().GetAwaiter().GetResult();
            }

            /// <param name='operations'>
            /// The operations group for this extension method.
            /// </param>
            /// <param name='page'>
            /// </param>
            /// <param name='judges'>
            /// </param>
            /// <param name='cancellationToken'>
            /// The cancellation token.
            /// </param>
            public static async Task ListAsync(this IContests operations, string page = default(string), string judges = default(string), CancellationToken cancellationToken = default(CancellationToken))
            {
                await operations.ListWithHttpMessagesAsync(page, judges, null, cancellationToken).ConfigureAwait(false);
            }

            /// <param name='operations'>
            /// The operations group for this extension method.
            /// </param>
            /// <param name='id'>
            /// </param>
            public static void Read(this IContests operations, string id)
            {
                Task.Factory.StartNew(s => ((IContests)s).ReadAsync(id), operations, CancellationToken.None, TaskCreationOptions.None, TaskScheduler.Default).Unwrap().GetAwaiter().GetResult();
            }

            /// <param name='operations'>
            /// The operations group for this extension method.
            /// </param>
            /// <param name='id'>
            /// </param>
            /// <param name='cancellationToken'>
            /// The cancellation token.
            /// </param>
            public static async Task ReadAsync(this IContests operations, string id, CancellationToken cancellationToken = default(CancellationToken))
            {
                await operations.ReadWithHttpMessagesAsync(id, null, cancellationToken).ConfigureAwait(false);
            }

    }
}
