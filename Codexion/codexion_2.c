/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion_2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/01 14:41:03 by root              #+#    #+#             */
/*   Updated: 2026/10/06 14:30:44 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <pthread.h>
#include "codexion.h"

int	init_thread(t_simulation simulation)
{
	int	i;

	i = 0;
	while (i < simulation.config->nb_coders)
	{
		if (pthread_create(&simulation.coders[i].thread, NULL,
				&launch_coder_threads, &simulation.coders[i]) != 0)
			return (1);
		i++;
		simulation.config->created_threads = i;
	}
	return (0);
}
