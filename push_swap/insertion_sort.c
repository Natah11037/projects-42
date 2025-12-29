/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   insertion_sort.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 16:06:22 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/27 17:54:31 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	putting_min_on_top(size_t *list_i, t_list **stack_b,
		t_data *data)
{
	t_list	*min_node;

	min_node = *stack_b;
	*list_i = min_placement(&min_node);
	if (ft_lstsize(min_node) > (ft_lstsize(*stack_b) / 2))
	{
		while ((*stack_b)->placement != *list_i)
		{
			rotate_stack(stack_b);
			data->ops = ft_strnjoin(data->ops, "rb\n", 3);
			data->rb += 1;
		}
	}
	else
	{
		while ((*stack_b)->placement != *list_i)
		{
			reverse_rotate_stack(stack_b);
			data->ops = ft_strnjoin(data->ops, "rrb\n", 4);
			data->rrb += 1;
		}
	}
}

void	putting_b_in_a(t_list **stack_a, t_list **stack_b,
	t_data *data)
{
	size_t	list_j;
	size_t	list_i;

	list_j = 1;
	while ((*stack_b))
	{
		putting_min_on_top(&list_i, stack_b, data);
		while (list_j < list_i)
		{
			rotate_stack(stack_a);
			data->ops = ft_strnjoin(data->ops, "ra\n", 3);
			data->ra += 1;
			++list_j;
		}
		push(stack_b, stack_a);
		data->ops = ft_strnjoin(data->ops, "pa\n", 3);
		data->pa += 1;
	}
	while ((*stack_a)->placement != 1)
	{
		rotate_stack(stack_a);
		data->ops = ft_strnjoin(data->ops, "ra\n", 3);
		data->ra += 1;
	}
}

void	insertion_sort(t_list **stack_a, t_list **stack_b,
		t_data *data)
{
	size_t	list_j;
	size_t	list_i;

	list_j = ft_lstsize(*stack_a);
	list_i = 1;
	while (list_i <= list_j)
	{
		if ((*stack_a) && list_i == (*stack_a)->placement)
		{
			rotate_stack(stack_a);
			data->ops = ft_strnjoin(data->ops, "ra\n", 3);
			data->ra += 1;
		}
		else
		{
			push(stack_a, stack_b);
			data->ops = ft_strnjoin(data->ops, "pb\n", 3);
			data->pb += 1;
		}
		++list_i;
	}
	list_j = 1;
	putting_b_in_a(stack_a, stack_b, data);
}
