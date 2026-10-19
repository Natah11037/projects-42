/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/30 15:34:36 by root              #+#    #+#             */
/*   Updated: 2026/10/19 14:03:31 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"
#include <stdlib.h>

static int	allocate_simulation(t_config *config, t_simulation *simulation)
{
	simulation->config = config;
	simulation->coders = NULL;
	simulation->dongles = NULL;
	simulation->initialized_dongles = 0;
	simulation->monitor_mutex_initialized = 0;
	simulation->print_mutex_initialized = 0;
	simulation->monitor_thread_created = 0;
	simulation->coders = malloc(sizeof(t_coder) * config->nb_coders);
	if (!simulation->coders)
		return (1);
	simulation->dongles = malloc(sizeof(t_dongle) * config->nb_coders);
	if (!simulation->dongles)
		return (1);
	if (pthread_mutex_init(&simulation->monitor.mutex, NULL) != 0)
		return (1);
	simulation->monitor_mutex_initialized = 1;
	if (pthread_mutex_init(&simulation->mutex_print, NULL) != 0)
		return (1);
	simulation->print_mutex_initialized = 1;
	simulation->monitor.stop = FALSE;
	return (0);
}

static int	init_dongles(t_simulation *simulation, int count)
{
	int	i;

	i = 0;
	while (i < count)
	{
		simulation->dongles[i].id = i + 1;
		if (pthread_mutex_init(&simulation->dongles[i].mutex, NULL) != 0)
			return (1);
		simulation->initialized_dongles++;
		simulation->dongles[i].is_used = FALSE;
		simulation->dongles[i].heap = (t_heap){0};
		i++;
	}
	return (0);
}

int	init_simulation(t_config *config, t_simulation *simulation)
{
	if (allocate_simulation(config, simulation) != 0
		|| init_dongles(simulation, config->nb_coders) != 0)
	{
		destroy_simulation(simulation);
		return (1);
	}
	initialize_coders(simulation, config->nb_coders);
	return (0);
}
