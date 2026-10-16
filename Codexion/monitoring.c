/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   monitoring.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/16 13:12:07 by nweber--          #+#    #+#             */
/*   Updated: 2026/10/16 14:06:46 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <unistd.h>
#include "codexion.h"

static t_coder	*find_expired_coder(t_simulation *simulation,
		t_monitor *monitor)
{
	uint64_t	current_time;
	t_coder		*expired;
	int			i;

	current_time = now_ms();
	expired = NULL;
	pthread_mutex_lock(&monitor->mutex);
	i = 0;
	while (i < simulation->config->nb_coders && monitor->stop == FALSE)
	{
		if (simulation->coders[i].deadline <= current_time)
		{
			expired = &simulation->coders[i];
			monitor->stop = TRUE;
		}
		i++;
	}
	pthread_mutex_unlock(&monitor->mutex);
	return (expired);
}

static t_bool	monitor_is_stopped(t_monitor *monitor)
{
	t_bool	stopped;

	pthread_mutex_lock(&monitor->mutex);
	stopped = monitor->stop;
	pthread_mutex_unlock(&monitor->mutex);
	return (stopped != FALSE);
}

void	*surveillance(void *arg)
{
	t_simulation	*simulation;
	t_monitor		*monitor;
	t_coder			*expired;

	simulation = arg;
	monitor = simulation->coders[0].monitor;
	while (!monitor_is_stopped(monitor))
	{
		expired = find_expired_coder(simulation, monitor);
		if (expired != NULL)
		{
			printf("%llu %d burned out\n",
				(unsigned long long)(now_ms() - expired->start_time),
				expired->id);
			break ;
		}
		usleep(100);
	}
	return (NULL);
}
