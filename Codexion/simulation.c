/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simulation.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/28 16:36:53 by root              #+#    #+#             */
/*   Updated: 2026/10/21 13:00:12 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <unistd.h>
#include "codexion.h"

static t_bool	dongles_available_for_coder(t_coder *coder,
		t_dongle *dongle1, t_dongle *dongle2, uint64_t current_time)
{
	if (dongle1->heap.size == 0 || dongle2->heap.size == 0
		|| dongle1->is_used == TRUE
		|| dongle2->is_used == TRUE
		|| dongle1->heap.requests[0].coder != coder
		|| dongle2->heap.requests[0].coder != coder
		|| dongle1->last_time_used + coder->config->dongle_cooldown
		> current_time
		|| dongle2->last_time_used + coder->config->dongle_cooldown
		> current_time)
		return (FALSE);
	return (TRUE);
}

static t_bool	checking_dongles_for_coders(t_coder *coder,
		t_dongle *dongle1, t_dongle *dongle2)
{
	uint64_t	current_time;

	if (dongle1->id == dongle2->id)
		return (FALSE);
	pthread_mutex_lock(&dongle1->mutex);
	pthread_mutex_lock(&dongle2->mutex);
	current_time = now_ms();
	if (dongles_available_for_coder(coder, dongle1, dongle2, current_time)
		== FALSE)
	{
		pthread_mutex_unlock(&dongle1->mutex);
		pthread_mutex_unlock(&dongle2->mutex);
		return (FALSE);
	}
	dongle1->is_used = TRUE;
	dongle2->is_used = TRUE;
	pthread_mutex_unlock(&dongle1->mutex);
	pthread_mutex_unlock(&dongle2->mutex);
	return (TRUE);
}

static t_bool	wait_for_coder_dongles(t_coder *coder)
{
	pthread_mutex_lock(&coder->monitor->cond_mutex);
	while (coder_monitor_is_running(coder->monitor)
		&& checking_dongles_for_coders(coder,
			coder->actual_dongle, coder->previous_dongle) == FALSE)
		wait_for_dongle_cd(coder);
	if (coder_monitor_is_running(coder->monitor) == FALSE)
	{
		pthread_mutex_unlock(&coder->monitor->cond_mutex);
		return (FALSE);
	}
	pthread_mutex_unlock(&coder->monitor->cond_mutex);
	return (TRUE);
}

t_bool	launching_compilation_debug_refactor(t_coder *coder, int i)
{
	if (launching_compil(coder) == FALSE)
		return (FALSE);
	if (i + 1 == coder->config->nb_compiles_required)
		return (TRUE);
	if (launching_debug(coder) == FALSE)
		return (FALSE);
	if (launching_refactor(coder) == FALSE)
		return (FALSE);
	return (TRUE);
}

void	*launch_coder_threads(void *arg)
{
	t_request	coder_request;
	t_coder		*coder;
	int			i;

	coder = arg;
	i = 0;
	coder_request.coder = coder;
	while (coder->config->nb_compiles_required > i
		&& coder_monitor_is_running(coder->monitor))
	{
		if (wait_for_coder_dongles(coder) == FALSE)
			break ;
		if (launching_compilation_debug_refactor(coder, i) == FALSE)
			return (NULL);
		i++;
		if (i < coder->config->nb_compiles_required)
			heap_add_request(coder, coder_request);
	}
	return (NULL);
}
