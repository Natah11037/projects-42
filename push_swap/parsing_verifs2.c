/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing_verifs2.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/16 13:15:55 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/17 15:45:03 by cyakisan         ###   ########.fr       */
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

int	single_int_verif(int *sing_or_mul, int *args_i, char **arguments)
{
	int	nb_i;

	nb_i = 0;
	ft_long_atoi(arguments[*args_i], &nb_i, sing_or_mul);
	if (arguments[*args_i][nb_i] == '\0' && !arguments[*args_i + 1])
		print_error();
	return (1);
}

int	dup_verif_sc(int int_i, char **arguments, long int result, int *sng_or_m)
{
	long int	duplicate;
	int			sint_i;

	duplicate = 0;
	sint_i = 0;
	while (arguments[0][int_i + sint_i] != '\0')
	{
		duplicate = ft_long_atoi(&arguments[0][int_i + sint_i],
				&sint_i, sng_or_m);
		if (duplicate == result)
			print_error();
	}
	return (1);
}

int	integers_verif_sc(char **arguments, int *args_i, int *s_o_m)
{
	long int	result;
	int			int_i;

	int_i = 0;
	result = 0;
	while (arguments[*args_i][int_i] != '\0')
	{
		result = ft_long_atoi(&arguments[*args_i][int_i], &int_i, s_o_m);
		if (result > INT_MAX || result < INT_MIN)
			print_error();
		dup_verif_sc(int_i, &arguments[*args_i], result, s_o_m);
	}
	return (1);
}
