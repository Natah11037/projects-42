/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing_verifs.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/15 12:58:12 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/19 16:57:33 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include "push_swap.h"
#include "libft.h"

static void	flags_verif(int	*i, int	*strat_selec, char **arguments)
{
	int	flags_to_check;

	flags_to_check = 1;
	while (flags_to_check != *strat_selec)
	{
		flags_to_check = *strat_selec;
		if (!ft_strcmp(arguments[*i], "--simple"))
			*strat_selec += 1;
		else if (!ft_strcmp(arguments[*i], "--medium"))
			*strat_selec += 2;
		else if (!ft_strcmp(arguments[*i], "--complex"))
			*strat_selec += 3;
		else if (!ft_strcmp(arguments[*i], "--adaptive"))
			*strat_selec += 4;
		else if (!ft_strcmp(arguments[*i], "--bench"))
			*strat_selec += 10;
		if (!arguments[*i + 1])
			break ;
		else if (flags_to_check != *strat_selec)
			*i = *i + 1;
	}
	verif_strat_selec(strat_selec);
}

static int	list_verif(char **arguments, int *args_i, int *sing_or_mul)
{
	int	nb_i;
	int	args_ik;

	nb_i = 0;
	args_ik = *args_i;
	while (arguments[*args_i] && arguments[*args_i][nb_i] != '\0')
	{
		if ((arguments[*args_i][nb_i] < 48 || arguments[*args_i][nb_i] > 57) &&
		arguments[*args_i][nb_i] != 10 && arguments[*args_i][nb_i] != 32)
			print_error();
		++nb_i;
		if (arguments[*args_i][nb_i] == '\0' && *sing_or_mul)
		{
			*args_i += 1;
			nb_i = 0;
		}
	}
	*args_i = args_ik;
	single_int_verif(sing_or_mul, args_i, arguments);
	return (1);
}

static int	dup_verif_mc(int int_i, char **arguments,
			long int result, int *sng_or_m)
{
	int			str_i;
	long int	duplicate;

	duplicate = 0;
	str_i = 1;
	while (arguments[str_i])
	{
		duplicate = ft_long_atoi(arguments[str_i], &int_i, sng_or_m);
		if (duplicate == result)
			print_error();
		++str_i;
	}
	return (1);
}

static int	integers_verif_mc(char **arguments, int *args_i, int *s_o_m)
{
	long int		result;
	int				int_i;

	int_i = 0;
	while (arguments[*args_i])
	{
		result = ft_long_atoi(arguments[*args_i], &int_i, s_o_m);
		if (result > INT_MAX || result < INT_MIN)
			print_error();
		dup_verif_mc(int_i, &arguments[*args_i], result, s_o_m);
		*args_i += 1;
	}
	return (1);
}

int	all_verifs(char **arguments, int ac, int *strat_selec, int *sing_or_mul)
{
	int		args_i;

	args_i = 1;
	if (ac < 2)
		exit (0);
	flags_verif(&args_i, strat_selec, arguments);
	if (args_i < ac - 1)
		*sing_or_mul = 1;
	list_verif(arguments, &args_i, sing_or_mul);
	if (*sing_or_mul)
		integers_verif_mc(arguments, &args_i, sing_or_mul);
	else
		integers_verif_sc(arguments, &args_i, sing_or_mul);
	return (1);
}
