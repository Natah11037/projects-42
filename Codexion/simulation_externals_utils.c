/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simulation_externals_utils.c                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/06 14:07:01 by nweber--          #+#    #+#             */
/*   Updated: 2026/10/12 16:17:22 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
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
		time_to_wait = (coder->actual_dongle->last_time_used
				+ coder->config->dongle_cooldown) - current_time;
	else
		time_to_wait = (coder->previous_dongle->last_time_used
				+ coder->config->dongle_cooldown) - current_time;
	usleep(time_to_wait * 1000);
}

t_bool	launching_compil(t_coder *coder)
{
	if (now_ms() >= coder->deadline)
	{
		printf("%llu %d has burnout\n",
			(long long unsigned)now_ms() - coder->start_time, coder->id);
		return (FALSE);
	}
	wait_for_dongle_cd(coder);
	coder->last_time_compile = now_ms();
	printf("%llu %d has taken dongle\n",
		(long long unsigned)coder->last_time_compile - coder->start_time,
		coder->id);
	printf("%llu %d has taken dongle\n",
		(long long unsigned)coder->last_time_compile - coder->start_time,
		coder->id);
	printf("%llu %d is compiling\n",
		(long long unsigned)coder->last_time_compile - coder->start_time,
		coder->id);
	coder->deadline = coder->last_time_compile + coder->config->time_to_burnout;
	usleep(coder->config->time_to_compile * 1000);
	pthread_mutex_lock(&coder->actual_dongle->mutex);
	pthread_mutex_lock(&coder->previous_dongle->mutex);
	heap_pop(&coder->actual_dongle->heap);
	heap_pop(&coder->previous_dongle->heap);
	coder->actual_dongle->is_used = FALSE;
	coder->previous_dongle->is_used = FALSE;
	coder->actual_dongle->last_time_used = now_ms();
	coder->previous_dongle->last_time_used = coder
		->actual_dongle->last_time_used;
	pthread_mutex_unlock(&coder->actual_dongle->mutex);
	pthread_mutex_unlock(&coder->previous_dongle->mutex);
	return (TRUE);
}

t_bool	launching_debug(t_coder *coder)
{
	if (now_ms() >= coder->deadline)
	{
		printf("%llu %d has burnout\n",
			(long long unsigned)now_ms() - coder->start_time, coder->id);
		return (FALSE);
	}
	printf("%llu %d is debugging\n",
		(long long unsigned)now_ms() - coder->start_time, coder->id);
	usleep(coder->config->time_to_debug * 1000);
	return (TRUE);
}

t_bool	launching_refactor(t_coder *coder)
{
	if (now_ms() >= coder->deadline)
	{
		printf("%llu %d has burnout\n",
			(long long unsigned)now_ms() - coder->start_time, coder->id);
		return (FALSE);
	}
	printf("%llu %d is refactoring\n",
		(long long unsigned)now_ms() - coder->start_time, coder->id);
	usleep(coder->config->time_to_refactor * 1000);
	return (TRUE);
}
