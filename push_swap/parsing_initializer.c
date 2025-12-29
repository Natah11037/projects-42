/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing_initializer.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 15:12:16 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/29 14:53:18 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	pass_flags(int strat_selec, int s_o_m)
{
	if (!s_o_m)
		return (0);
	else if (strat_selec == 0)
		return (1);
	else if (strat_selec >= 1 && strat_selec <= 10)
		return (2);
	else
		return (3);
}

void	stack_initializer(t_list **stack_a, char **ints,
		char *original_ints, int sing_or_mul)
{
	int			sing_i;
	int			ints_i;
	long int	result;

	sing_i = 0;
	ints_i = 0;
	while (ints[ints_i] && ints[ints_i][sing_i] != '\0')
	{
		result = ft_long_atoi(&ints[ints_i][sing_i], &sing_i);
		if (result > INT_MAX || result < INT_MIN)
			clear_within_init(stack_a, original_ints, sing_or_mul,
				ints);
		ft_lstadd_back(stack_a, ft_lstnew(((int)result), 1));
		while (ints[ints_i] && ints[ints_i][sing_i] == '\0')
		{
			sing_i = 0;
			++ints_i;
		}
	}
	ft_freeall(ints, ft_dstrlen(ints));
	if ((*stack_a)->next == (*stack_a))
		clear_after_init(stack_a, original_ints, sing_or_mul,
			0);
}

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
	data->ops = NULL;
}

void	list_normalizer(t_list *stack)
{
	int		max_int;
	size_t	list_l;
	size_t	list_i;

	max_int = search_for_max(stack);
	list_l = ft_lstsize(stack);
	list_i = ft_lstsize(stack);
	while (list_l > 0)
	{
		while (list_i > 0)
		{
			if (max_int == stack->content)
			{
				stack->placement = list_l;
				--list_l;
			}
			stack = stack->next;
			--list_i;
		}
		list_i = ft_lstsize(stack);
		--max_int;
	}
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
