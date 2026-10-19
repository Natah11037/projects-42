/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   compilation.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/19 11:39:46 by nweber--          #+#    #+#             */
/*   Updated: 2026/10/19 14:11:41 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <unistd.h>
#include "codexion.h"

static void	wait_for_dongle_cd(t_coder *coder)
{
	uint64_t	current_time;
	uint64_t	time_to_wait;

	current_time = now_ms();
	if (coder->actual_dongle->last_time_used
		+ coder->config->dongle_cooldown <= current_time
		&& coder->previous_dongle->last_time_used
		+ coder->config->dongle_cooldown <= current_time)
		return ;
	if (coder->actual_dongle->last_time_used
		> coder->previous_dongle->last_time_used)
		time_to_wait = coder->actual_dongle->last_time_used
			+ coder->config->dongle_cooldown - current_time;
	else
		time_to_wait = coder->previous_dongle->last_time_used
			+ coder->config->dongle_cooldown - current_time;
	usleep(time_to_wait * 1000);
}

static void	print_compilation_start(t_coder *coder)
{
	pthread_mutex_lock(coder->mutex_print);
	printf("%llu %d has taken dongle\n",
		(long long unsigned)coder->last_time_compile - coder->start_time,
		coder->id);
	printf("%llu %d has taken dongle\n",
		(long long unsigned)coder->last_time_compile - coder->start_time,
		coder->id);
	printf("%llu %d is compiling\n",
		(long long unsigned)coder->last_time_compile - coder->start_time,
		coder->id);
	pthread_mutex_unlock(coder->mutex_print);
}

static t_bool	start_compilation(t_coder *coder)
{
	uint64_t	current_time;

	pthread_mutex_lock(&coder->monitor->mutex);
	current_time = now_ms();
	if (coder->monitor->stop == TRUE || current_time >= coder->deadline)
	{
		pthread_mutex_unlock(&coder->monitor->mutex);
		return (FALSE);
	}
	coder->last_time_compile = current_time;
	coder->deadline = current_time + coder->config->time_to_burnout;
	pthread_mutex_unlock(&coder->monitor->mutex);
	print_compilation_start(coder);
	return (TRUE);
}

static void	release_compilation_dongles(t_coder *coder)
{
	pthread_mutex_lock(&coder->actual_dongle->mutex);
	pthread_mutex_lock(&coder->previous_dongle->mutex);
	heap_pop(&coder->actual_dongle->heap);
	heap_pop(&coder->previous_dongle->heap);
	coder->actual_dongle->is_used = FALSE;
	coder->previous_dongle->is_used = FALSE;
	coder->actual_dongle->last_time_used = now_ms();
	coder->previous_dongle->last_time_used
		= coder->actual_dongle->last_time_used;
	pthread_mutex_unlock(&coder->actual_dongle->mutex);
	pthread_mutex_unlock(&coder->previous_dongle->mutex);
}

t_bool	launching_compil(t_coder *coder)
{
	if (coder_deadline_expired(coder))
		return (FALSE);
	wait_for_dongle_cd(coder);
	if (start_compilation(coder) == FALSE)
		return (FALSE);
	usleep(coder->config->time_to_compile * 1000);
	release_compilation_dongles(coder);
	return (coder_monitor_is_running(coder->monitor));
}
