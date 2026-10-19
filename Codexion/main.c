/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/28 13:34:07 by root              #+#    #+#             */
/*   Updated: 2026/10/19 13:54:57 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include "codexion.h"
#include "parser.h"
#include "error.h"

int	main(int ac, char **av)
{
	t_config		config;
	t_simulation	simulation;

	if (ac != 9)
		return (print_error(ERROR_NB_ARGS, ac));
	if (parser(ac, av, &config) == 1)
		return (1);
	if (init_simulation(&config, &simulation) != 0)
		return (1);
	if (init_thread(&simulation) != 0)
	{
		pthread_mutex_lock(&simulation.monitor.mutex);
		simulation.monitor.stop = TRUE;
		pthread_mutex_unlock(&simulation.monitor.mutex);
		destroy_simulation(&simulation);
		return (1);
	}
	destroy_simulation(&simulation);
	return (0);
}
