/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simulation.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/28 16:36:53 by root              #+#    #+#             */
/*   Updated: 2026/10/06 14:37:48 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <unistd.h>
#include "codexion.h"

t_bool	checking_dongles_for_coders(t_dongle dongle1, t_dongle dongle2)
{
	if (dongle1.id == dongle2.id)
		return (FALSE);
	if (dongle1.is_used == TRUE || dongle2.is_used == TRUE)
		return (FALSE);
	else
	{
		dongle1.is_used = TRUE;
		dongle2.is_used = TRUE;
	}
	return (TRUE);
}

t_bool	launching_compilation_debug_refactor(t_coder coder)
{
	printf("coder %d has taken dongle %d\n", coder.id, coder.actual_dongle->id);
	printf("coder %d has taken dongle %d\n",
		coder.id, coder.previous_dongle->id);
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
				*coder->actual_dongle, *coder->previous_dongle) == TRUE)
		{
			launching_compilation_debug_refactor(*coder);
		}
		i++;
	}
	return (NULL);
}
