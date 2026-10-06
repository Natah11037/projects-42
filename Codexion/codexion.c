/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/30 15:34:36 by root              #+#    #+#             */
/*   Updated: 2026/10/06 12:32:07 by nweber--         ###   ########.fr       */
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
	simulation->coders = malloc(sizeof(t_coder) * config->nb_coders);
	simulation->dongles = malloc(sizeof(t_dongle) * config->nb_coders);
	if (!simulation->coders || !simulation->dongles)
		return (1);
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
		i++;
	}
	return (0);
}

static void	init_coders(t_simulation *simulation, int count)
{
	int	i;

	i = 0;
	while (i < count)
	{
		if (i == count - 1)
		{
			simulation->coders[i].id = i + 1;
			simulation->coders[i].config = simulation->config;
			simulation->coders[i].actual_dongle
				= &simulation->dongles[(i + count - 1) % count];
			simulation->coders[i].previous_dongle = &simulation->dongles[i];
		}
		else
		{
			simulation->coders[i].id = i + 1;
			simulation->coders[i].config = simulation->config;
			simulation->coders[i].actual_dongle = &simulation->dongles[i];
			simulation->coders[i].previous_dongle
				= &simulation->dongles[(i + count - 1) % count];
		}
		i++;
	}
}

int	init_simulation(t_config *config, t_simulation *simulation)
{
	if (allocate_simulation(config, simulation) != 0
		|| init_dongles(simulation, config->nb_coders) != 0)
	{
		destroy_simulation(simulation);
		return (1);
	}
	init_coders(simulation, config->nb_coders);
	return (0);
}

void	destroy_simulation(t_simulation *simulation)
{
	int	i;

	i = 0;
	while (i < simulation->config->created_threads)
	{
		pthread_join(simulation->coders[i].thread, NULL);
		i++;
	}
	i = 0;
	while (i < simulation->initialized_dongles)
	{
		pthread_mutex_destroy(&simulation->dongles[i].mutex);
		i++;
	}
	free(simulation->coders);
	free(simulation->dongles);
	simulation->coders = NULL;
	simulation->dongles = NULL;
	simulation->initialized_dongles = 0;
}
