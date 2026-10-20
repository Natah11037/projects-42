/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   compilation.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/19 11:39:46 by nweber--          #+#    #+#             */
/*   Updated: 2026/10/20 14:00:18 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include "codexion.h"

void	wait_for_dongle_cd(t_coder *coder)
{
	struct timespec	deadline;
	uint64_t		wake_at;

	pthread_mutex_lock(&coder->actual_dongle->mutex);
	if (coder->actual_dongle != coder->previous_dongle)
		pthread_mutex_lock(&coder->previous_dongle->mutex);
	wake_at = coder->actual_dongle->last_time_used
		+ coder->config->dongle_cooldown;
	if (coder->previous_dongle->last_time_used
		+ coder->config->dongle_cooldown > wake_at)
		wake_at = coder->previous_dongle->last_time_used
			+ coder->config->dongle_cooldown;
	if (coder->actual_dongle != coder->previous_dongle)
		pthread_mutex_unlock(&coder->previous_dongle->mutex);
	pthread_mutex_unlock(&coder->actual_dongle->mutex);
	if (wake_at <= now_ms())
		pthread_cond_wait(&coder->monitor->cond,
			&coder->monitor->cond_mutex);
	else
	{
		deadline.tv_sec = wake_at / 1000;
		deadline.tv_nsec = (wake_at % 1000) * 1000000;
		pthread_cond_timedwait(&coder->monitor->cond,
			&coder->monitor->cond_mutex, &deadline);
	}
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
	pthread_mutex_lock(&coder->monitor->cond_mutex);
	pthread_mutex_lock(&coder->actual_dongle->mutex);
	pthread_mutex_lock(&coder->previous_dongle->mutex);
	heap_pop(&coder->actual_dongle->heap);
	heap_pop(&coder->previous_dongle->heap);
	coder->actual_dongle->is_used = FALSE;
	coder->previous_dongle->is_used = FALSE;
	coder->actual_dongle->last_time_used = now_ms();
	coder->previous_dongle->last_time_used
		= coder->actual_dongle->last_time_used;
	pthread_cond_broadcast(&coder->monitor->cond);
	pthread_mutex_unlock(&coder->actual_dongle->mutex);
	pthread_mutex_unlock(&coder->previous_dongle->mutex);
	pthread_mutex_unlock(&coder->monitor->cond_mutex);
}

t_bool	launching_compil(t_coder *coder)
{
	if (coder_deadline_expired(coder))
		return (FALSE);
	if (start_compilation(coder) == FALSE)
		return (FALSE);
	usleep(coder->config->time_to_compile * 1000);
	release_compilation_dongles(coder);
	return (coder_monitor_is_running(coder->monitor));
}
