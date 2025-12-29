/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing_verifs.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/15 12:58:12 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/29 14:40:36 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	flags_verif(int	*i, int	*sel, char **av)
{
	int	flags_to_check;
	int	max_turns;

	flags_to_check = 1;
	max_turns = 2;
	while (flags_to_check != *sel)
	{
		flags_to_check = *sel;
		if (!av[*i + 1] || max_turns == 0)
			break ;
		if (!ft_strcmp(av[*i], "--simple") && (*sel == 0 || *sel == 10))
			*sel += 1;
		else if (!ft_strcmp(av[*i], "--medium") && (*sel == 0 || *sel == 10))
			*sel += 2;
		else if (!ft_strcmp(av[*i], "--complex") && (*sel == 0 || *sel == 10))
			*sel += 3;
		else if (!ft_strcmp(av[*i], "--adaptive") && (*sel == 0 || *sel == 10))
			*sel += 4;
		else if (!ft_strcmp(av[*i], "--bench") && (*sel < 10))
			*sel += 10;
		if (flags_to_check != *sel)
			*i = *i + 1;
		max_turns--;
	}
	verif_strat_selec(sel);
}

static void	list_verif(char **arguments, int *args_i, int *sing_or_mul)
{
	int	nb_i;
	int	args_ik;

	nb_i = 0;
	args_ik = *args_i;
	while (arguments[*args_i] && arguments[*args_i][nb_i] != '\0')
	{
		if ((arguments[*args_i][nb_i] < 48 || arguments[*args_i][nb_i] > 57) &&
			arguments[*args_i][nb_i] != 32
		&& arguments[*args_i][nb_i] != '-' && arguments[*args_i][nb_i] != '+')
			print_error();
		if ((arguments[*args_i][nb_i] == '-' || arguments[*args_i][nb_i] == '+')
			&& ((arguments[*args_i][nb_i + 1] < 48 ||
				arguments[*args_i][nb_i + 1] > 57) ||
				(nb_i > 0 && arguments[*args_i][nb_i - 1] != 32)))
			print_error();
		++nb_i;
		if (arguments[*args_i][nb_i] == '\0' && *sing_or_mul)
		{
			*args_i += 1;
			nb_i = 0;
		}
	}
	*args_i = args_ik;
}

void	all_verifs(char **arguments, int ac, int *strat_selec, int *sing_or_mul)
{
	int		args_i;

	args_i = 1;
	if (ac < 2)
		exit (0);
	flags_verif(&args_i, strat_selec, arguments);
	if (args_i < ac - 1)
		*sing_or_mul = 1;
	list_verif(arguments, &args_i, sing_or_mul);
}

void	dup_verif(t_list **stack_a, char *ints, int sing_or_mul)
{
	size_t	list_i;
	t_list	*current;
	int		potential_dup;

	list_i = 0;
	current = *stack_a;
	potential_dup = current->content;
	current = current->next;
	while (list_i < ft_lstsize(*stack_a))
	{
		while (!current->first_node)
		{
			if (current->content == potential_dup)
				clear_after_init(stack_a, ints, sing_or_mul, 0);
			current = current->next;
		}
		while (current->prev->content != potential_dup)
			current = current->next;
		potential_dup = current->content;
		current = current->next;
		++list_i;
	}
}
