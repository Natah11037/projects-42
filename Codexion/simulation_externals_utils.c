/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simulation_externals_utils.c                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/06 14:07:01 by nweber--          #+#    #+#             */
/*   Updated: 2026/10/06 14:40:07 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include "codexion.h"

t_bool	launching_compil(t_coder coder)
{
	if (coder.config->time_to_compile > coder.config->time_to_burnout)
	{
		printf("coder %d has burnout\n", coder.id);
		return (FALSE);
	}
	printf("coder %d is compiling\n", coder.id);
	usleep(coder.config->time_to_compile * 1000);
	coder.actual_dongle->is_used = FALSE;
	coder.previous_dongle->is_used = FALSE;
	return (TRUE);
}

t_bool	launching_debug(t_coder coder)
{
	if (
		coder.config->time_to_compile
		+ coder.config->time_to_debug > coder.config->time_to_burnout)
	{
		printf("coder %d has burnout\n", coder.id);
		return (FALSE);
	}
	printf("coder %d is debugging\n", coder.id);
	usleep(coder.config->time_to_debug * 1000);
	return (TRUE);
}

t_bool	launching_refactor(t_coder coder)
{
	if (
		coder.config->time_to_compile + coder.config->time_to_debug
		+ coder.config->time_to_refactor > coder.config->time_to_burnout
	)
	{
		printf("coder %d has burnout\n", coder.id);
		return (FALSE);
	}
	printf("coder %d is refactoring\n", coder.id);
	usleep(coder.config->time_to_refactor * 1000);
	return (TRUE);
}
