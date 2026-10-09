/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_time.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/09 11:19:03 by nweber--          #+#    #+#             */
/*   Updated: 2026/10/09 14:36:52 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void	init_time(t_simulation *simulation)
{
	int			i;
	uint64_t	time;

	i = 0;
	time = now_ms();
	while (i < simulation->config->nb_coders)
	{
		simulation->coders[i].start_time = time;
		simulation->coders[i].last_time_compile = time;
		simulation->coders[i].deadline = simulation->coders[
			i].last_time_compile + simulation->config->time_to_burnout;
		i++;
	}
}
