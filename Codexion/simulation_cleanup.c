/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simulation_cleanup.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/19 11:39:46 by nweber--          #+#    #+#             */
/*   Updated: 2026/10/21 13:07:30 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "codexion.h"

static void	join_coder_threads(t_simulation *simulation)
{
	int	i;

	i = 0;
	while (i < simulation->config->created_threads)
	{
		pthread_join(simulation->coders[i].thread, NULL);
		i++;
	}
}

static void	stop_monitor_thread(t_simulation *simulation)
{
	if (!simulation->monitor_thread_created)
		return ;
	pthread_mutex_lock(&simulation->monitor.mutex);
	simulation->monitor.stop = TRUE;
	pthread_mutex_unlock(&simulation->monitor.mutex);
	pthread_join(simulation->monitor.monitor_thread, NULL);
	simulation->monitor_thread_created = 0;
}

static void	destroy_simulation_mutexes(t_simulation *simulation)
{
	int	i;

	i = 0;
	while (i < simulation->initialized_dongles)
	{
		pthread_mutex_destroy(&simulation->dongles[i].mutex);
		i++;
	}
	check_to_destroy_simulation(simulation);
}

static void	free_simulation_arrays(t_simulation *simulation)
{
	free(simulation->coders);
	free(simulation->dongles);
	simulation->coders = NULL;
	simulation->dongles = NULL;
	simulation->initialized_dongles = 0;
}

void	destroy_simulation(t_simulation *simulation)
{
	join_coder_threads(simulation);
	stop_monitor_thread(simulation);
	destroy_simulation_mutexes(simulation);
	free_simulation_arrays(simulation);
}
