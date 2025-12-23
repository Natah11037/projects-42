/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   prints.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/22 23:41:47 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/23 10:46:17 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	print_disorder(double disorder)
{
	int	integer;
	int	decimal;

	integer = (int)(disorder * 100);
	decimal = (int)(((disorder * 100) - integer) * 100);
	write(2, "[Disorder] ", 11);
	ft_putnbr_fd(integer, 2);
	write(2, ".", 1);
	ft_putnbr_fd(decimal, 2);
	write(2, "\n", 1);
}

void	print_bench(t_data *data)
{
	print_disorder(data->disorder);
	write(2, "[Used strategy] ", 16);
	if (data->strat_selec == 11)
		write(2, " (O(n2))", 5);
	else if (data->strat_selec == 12)
		write(2, "Error", 6);
}
