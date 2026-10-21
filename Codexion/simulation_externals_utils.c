/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simulation_externals_utils.c                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/06 14:07:01 by nweber--          #+#    #+#             */
/*   Updated: 2026/10/21 13:14:10 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include "codexion.h"

t_bool	coder_monitor_is_running(t_monitor *monitor)
{
	t_bool	running;

	pthread_mutex_lock(&monitor->mutex);
	running = (monitor->stop == FALSE);
	pthread_mutex_unlock(&monitor->mutex);
	return (running);
}

t_bool	coder_deadline_expired(t_coder *coder)
{
	t_bool	expired;

	pthread_mutex_lock(&coder->monitor->mutex);
	expired = now_ms() >= coder->deadline;
	pthread_mutex_unlock(&coder->monitor->mutex);
	return (expired);
}

t_bool	launching_debug(t_coder *coder)
{
	if (coder_monitor_is_running(coder->monitor) == FALSE
		|| coder_deadline_expired(coder))
		return (FALSE);
	pthread_mutex_lock(coder->mutex_print);
	printf("%llu %d is debugging\n",
		(long long unsigned)now_ms() - coder->start_time, coder->id);
	pthread_mutex_unlock(coder->mutex_print);
	usleep(coder->config->time_to_debug * 1000);
	return (coder_monitor_is_running(coder->monitor));
}

t_bool	launching_refactor(t_coder *coder)
{
	if (coder_monitor_is_running(coder->monitor) == FALSE
		|| coder_deadline_expired(coder))
		return (FALSE);
	pthread_mutex_lock(coder->mutex_print);
	printf("%llu %d is refactoring\n",
		(long long unsigned)now_ms() - coder->start_time, coder->id);
	pthread_mutex_unlock(coder->mutex_print);
	usleep(coder->config->time_to_refactor * 1000);
	return (coder_monitor_is_running(coder->monitor));
}

void	check_to_destroy_simulation(t_simulation *simulation)
{
	if (simulation->monitor_mutex_initialized)
	{
		pthread_mutex_destroy(&simulation->monitor.mutex);
		simulation->monitor_mutex_initialized = 0;
	}
	if (simulation->monitor_cond_initialized)
	{
		pthread_cond_destroy(&simulation->monitor.cond);
		simulation->monitor_cond_initialized = 0;
	}
	if (simulation->monitor_cond_mutex_initialized)
	{
		pthread_mutex_destroy(&simulation->monitor.cond_mutex);
		simulation->monitor_cond_mutex_initialized = 0;
	}
	if (simulation->print_mutex_initialized)
	{
		pthread_mutex_destroy(&simulation->mutex_print);
		simulation->print_mutex_initialized = 0;
	}
}
