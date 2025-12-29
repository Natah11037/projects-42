/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing_verifs2.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/16 13:15:55 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/28 20:53:20 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	print_error(void)
{
	write(2, "Error\n", 6);
	exit (1);
}

void	verif_strat_selec(int *strat_selec)
{
	const int	possible_values[] = {0, 1, 2, 3, 4, 10, 11, 12, 13, 14};
	int			i;

	i = 0;
	while (i <= 9)
	{
		if (*strat_selec == possible_values[i])
			break ;
		++i;
	}
	if (i > 9)
		print_error();
}
