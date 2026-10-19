/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion_2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/01 14:41:03 by root              #+#    #+#             */
/*   Updated: 2026/10/16 13:11:48 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <pthread.h>
#include "codexion.h"

static void	set_heaps_beginning(t_simulation *simulation)
{
	int			i;
	int			parity;
	t_request	actual_coder;

	i = 0;
	parity = 0;
	while (parity <= 1)
	{
		i = parity;
		while (simulation->config->nb_coders > i)
		{
			actual_coder.coder = &simulation->coders[i];
			actual_coder.coder->actual_dongle->heap.requests[
				actual_coder.coder->actual_dongle->heap.size] = actual_coder;
			actual_coder.coder->previous_dongle->heap.requests[
				actual_coder.coder->previous_dongle->heap.size] = actual_coder;
			actual_coder.coder->actual_dongle->heap.size++;
			actual_coder.coder->previous_dongle->heap.size++;
			i += 2;
		}
		parity++;
	}
}

int	init_thread(t_simulation *simulation)
{
	int			i;

	i = 0;
	set_heaps_beginning(simulation);
	init_time(simulation);
	if (pthread_create(&simulation->monitor.monitor_thread, NULL,
			&surveillance, simulation) != 0)
		return (1);
	simulation->monitor_thread_created = 1;
	while (i < simulation->config->nb_coders)
	{
		if (pthread_create(&simulation->coders[i].thread, NULL,
				&launch_coder_threads, &simulation->coders[i]) != 0)
			return (1);
		i++;
		simulation->config->created_threads = i;
	}
	return (0);
}
