/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simulation.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/28 16:36:53 by root              #+#    #+#             */
/*   Updated: 2026/10/09 16:17:25 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <unistd.h>
#include "codexion.h"

t_bool	checking_dongles_for_coders(t_dongle *dongle1, t_dongle *dongle2)
{
	if (dongle1->id == dongle2->id)
		return (FALSE);
	pthread_mutex_lock(&dongle1->mutex);
	pthread_mutex_lock(&dongle2->mutex);
	if (dongle1->is_used == TRUE || dongle2->is_used == TRUE)
	{
		pthread_mutex_unlock(&dongle1->mutex);
		pthread_mutex_unlock(&dongle2->mutex);
		return (FALSE);
	}
	else
	{
		dongle1->is_used = TRUE;
		dongle2->is_used = TRUE;
	}
	pthread_mutex_unlock(&dongle1->mutex);
	pthread_mutex_unlock(&dongle2->mutex);
	return (TRUE);
}

t_bool	launching_compilation_debug_refactor(t_coder *coder)
{
	if (launching_compil(coder) == FALSE)
		return (FALSE);
	if (launching_debug(coder) == FALSE)
		return (FALSE);
	if (launching_refactor(coder) == FALSE)
		return (FALSE);
	return (TRUE);
}

void	*launch_coder_threads(void *arg)
{
	t_coder	*coder;
	int		i;

	coder = arg;
	i = 0;
	while (coder->config->nb_compiles_required > i)
	{
		if (checking_dongles_for_coders(
				coder->actual_dongle, coder->previous_dongle) == TRUE)
		{
			if (launching_compilation_debug_refactor(coder) == FALSE)
				return (NULL);
		}
		i++;
	}
	return (NULL);
}
