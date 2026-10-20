/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simulation.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/28 16:36:53 by root              #+#    #+#             */
/*   Updated: 2026/10/20 14:31:54 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <unistd.h>
#include "codexion.h"

static int	monitor_is_running(t_monitor *monitor)
{
	int	running;

	pthread_mutex_lock(&monitor->mutex);
	running = (monitor->stop == FALSE);
	pthread_mutex_unlock(&monitor->mutex);
	return (running);
}

static t_bool	checking_dongles_for_coders(t_coder *coder,
		t_dongle *dongle1, t_dongle *dongle2)
{
	if (dongle1->id == dongle2->id)
		return (FALSE);
	pthread_mutex_lock(&dongle1->mutex);
	pthread_mutex_lock(&dongle2->mutex);
	if (dongle1->is_used == TRUE
		|| dongle2->is_used == TRUE
		|| dongle1->heap.requests[0].coder != coder
		|| dongle2->heap.requests[0].coder != coder)
	{
		pthread_mutex_unlock(&dongle1->mutex);
		pthread_mutex_unlock(&dongle2->mutex);
		return (FALSE);
	}
	else
	{
		wait_for_dongle_cd(coder);
		dongle1->is_used = TRUE;
		dongle2->is_used = TRUE;
	}
	pthread_mutex_unlock(&dongle1->mutex);
	pthread_mutex_unlock(&dongle2->mutex);
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
	pthread_mutex_lock(&coder->monitor->cond_mutex);
	while (coder->config->nb_compiles_required > i
		&& monitor_is_running(coder->monitor))
	{
		usleep(1);
		if (checking_dongles_for_coders(coder,
				coder->actual_dongle, coder->previous_dongle) == TRUE)
		{
			pthread_mutex_unlock(&coder->monitor->cond_mutex);
			if (launching_compilation_debug_refactor(coder, i) == FALSE)
				return (NULL);
			i++;
			if (i < coder->config->nb_compiles_required)
				heap_add_request(coder, coder_request);
		}
		else
		{
			pthread_cond_wait(&coder->monitor->cond,
				&coder->monitor->cond_mutex);
			pthread_mutex_unlock(&coder->monitor->cond_mutex);
		}
		if (monitor_is_running(coder->monitor) == FALSE)
			break ;
	}
	pthread_mutex_unlock(&coder->monitor->cond_mutex);
	return (NULL);
}
