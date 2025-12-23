/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing_initializer.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 15:12:16 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/23 10:02:36 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	pass_flags(int strat_selec)
{
	int	i;

	i = 1;
	if (strat_selec == 0)
		return (i);
	else if (strat_selec >= 1 && strat_selec <= 10)
		return (i = 2);
	else
		return (i = 3);
}

void	stack_initializer(t_list **stack_a, char **av, int stra_slc, int s_o_m)
{
	int	sing_i;
	int	int_i;

	sing_i = 0;
	int_i = pass_flags(stra_slc);
	while (av[int_i] && av[int_i][sing_i] != '\0')
	{
		if (!s_o_m)
			ft_lstadd_back(stack_a, ft_lstnew((int)
					ft_long_atoi(&av[int_i][sing_i], &sing_i, &s_o_m)));
		else
			ft_lstadd_back(stack_a, ft_lstnew((int) ft_long_atoi(av[int_i],
						&int_i, &s_o_m)));
		if (s_o_m)
			++int_i;
	}
}
// ft_bzero(data, sizeof(data))

void	data_initializer(t_data *data)
{
	data->sa = 0;
	data->sb = 0;
	data->ss = 0;
	data->pa = 0;
	data->pb = 0;
	data->ra = 0;
	data->rb = 0;
	data->rr = 0;
	data->rra = 0;
	data->rrb = 0;
	data->rrr = 0;
}

double	extract_disorder(t_list *stack_a)
{
	int		mistakes;
	int		total_pairs;
	int		fullcheck;
	t_list	*temp;

	mistakes = 0;
	total_pairs = 0;
	temp = stack_a;
	fullcheck = 0;
	stack_a = stack_a->next;
	while (fullcheck == 0)
	{
		while (!stack_a->first_node)
		{
			++total_pairs;
			if (temp->content > stack_a->content)
				++mistakes;
			stack_a = stack_a->next;
		}
		temp = temp->next;
		stack_a = temp->next;
		if (temp->first_node)
			fullcheck = 1;
	}
	return ((double) mistakes / (double) total_pairs);
}
