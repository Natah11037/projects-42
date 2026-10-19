/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   coder_init.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/19 11:39:46 by nweber--          #+#    #+#             */
/*   Updated: 2026/10/19 14:06:58 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	initialize_coder(t_simulation *simulation, int index, int count)
{
	t_coder	*coder;

	coder = &simulation->coders[index];
	coder->id = index + 1;
	coder->config = simulation->config;
	coder->monitor = &simulation->monitor;
	coder->mutex_print = &simulation->mutex_print;
	if (index == count - 1)
	{
		coder->actual_dongle
			= &simulation->dongles[(index + count - 1) % count];
		coder->previous_dongle = &simulation->dongles[index];
	}
	else
	{
		coder->actual_dongle = &simulation->dongles[index];
		coder->previous_dongle
			= &simulation->dongles[(index + count - 1) % count];
	}
}

void	initialize_coders(t_simulation *simulation, int count)
{
	int	i;

	i = 0;
	simulation->monitor.stop = FALSE;
	while (i < count)
	{
		initialize_coder(simulation, i, count);
		i++;
	}
}
