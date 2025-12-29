/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   prints.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/22 23:41:47 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/28 21:09:46 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	print_disorder(double disorder)
{
	int	integer;
	int	decimal;

	integer = (int)(disorder * 100);
	decimal = (int)(((disorder * 100) - integer) * 100);
	write(2, "[Disorder]: ", 12);
	ft_putnbr_fd(integer, 2);
	write(2, ".", 1);
	ft_putnbr_fd(decimal, 2);
	write(2, "%\n", 2);
}

static void	print_individual_ops_count(t_data *data)
{
	write(2, "[sa]: ", 6);
	ft_putnbr_fd(data->sa, 2);
	write(2, " [sb]: ", 7);
	ft_putnbr_fd(data->sb, 2);
	write(2, " [ss]: ", 7);
	ft_putnbr_fd(data->ss, 2);
	write(2, " [pa]: ", 7);
	ft_putnbr_fd(data->pa, 2);
	write(2, " [pb]: ", 7);
	ft_putnbr_fd(data->pb, 2);
	write(2, " [ra]: ", 7);
	ft_putnbr_fd(data->ra, 2);
	write(2, " [rb]: ", 7);
	ft_putnbr_fd(data->rb, 2);
	write(2, " [rr]: ", 7);
	ft_putnbr_fd(data->rr, 2);
	write(2, " [rra]: ", 8);
	ft_putnbr_fd(data->rra, 2);
	write(2, " [rrb]: ", 8);
	ft_putnbr_fd(data->rrb, 2);
	write(2, " [rrr]: ", 8);
	ft_putnbr_fd(data->rrr, 2);
}

void	print_bench(t_data *data)
{
	print_disorder(data->disorder);
	write(2, "[Used strategy]: ", 17);
	if (data->strat_selec == 11)
		write(2, "Insertion sort (O(n^2))\n", 24);
	else if (data->strat_selec == 12)
		write(2, "Chunk sort (O(n√n))\n", 22);
	else if (data->strat_selec == 13)
		write(2, "Radix sort (O(n log n))\n", 24);
	else
	{
		if (data->disorder < (double) 0.20)
			write(2, "Adaptive (Insertion sort (O(n^2)))\n", 35);
		else if (data->disorder < (double) 0.50)
			write(2, "Adaptive (Chunk sort (O(n√n)))\n", 33);
		else
			write(2, "Adaptive (Radix sort (O(n log n)))\n", 35);
	}
	write(2, "[Total operations]: ", 20);
	ft_putnbr_fd(data->sa + data->sb + data->ss + data->pa
		+ data->pb + data->ra + data->rb + data->rr + data->rra
		+ data->rrb + data->rrr, 2);
	write(2, "\n", 1);
	print_individual_ops_count(data);
	write(2, "\n", 1);
}
