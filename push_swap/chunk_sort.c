/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   chunk_sort.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/26 16:46:08 by root              #+#    #+#             */
/*   Updated: 2025/12/28 12:44:55 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static size_t	sqrt_ceil(size_t n)
{
	size_t	i;

	i = 0;
	while (i * i < n)
		i++;
	return (i);
}

static void	rotating_chunk_in_b(size_t max_placement_chunk,
		t_list **stack_b, t_data *data)
{
	size_t	list_i;

	list_i = search_placement(*stack_b, max_placement_chunk);
	if (list_i < (ft_lstsize(*stack_b) / 2))
	{
		while ((*stack_b)->placement != max_placement_chunk)
		{
			rotate_stack(stack_b);
			data->ops = ft_strnjoin(data->ops, "rb\n", 3);
			data->rb += 1;
		}
	}
	else
	{
		while ((*stack_b)->placement != max_placement_chunk)
		{
			reverse_rotate_stack(stack_b);
			data->ops = ft_strnjoin(data->ops, "rrb\n", 4);
			data->rrb += 1;
		}
	}
}

static t_list	*pushing_by_chunk_in_a(size_t max_placement_chunk,
		t_list **stack_b, t_data *data)
{
	t_list	*stack_a;

	stack_a = NULL;
	while (*stack_b)
	{
		rotating_chunk_in_b(max_placement_chunk, stack_b,
			data);
		push(stack_b, &stack_a);
		data->ops = ft_strnjoin(data->ops, "pa\n", 3);
		data->pa += 1;
		--max_placement_chunk;
	}
	return (stack_a);
}

static void	pushing_by_chunk_in_b(t_list **stack_a, t_list **stack_b,
		t_data *data, size_t max_placement_chunk)
{
	static size_t	push_counter;

	if (push_counter == 0)
		push_counter = 1;
	while ((*stack_a) && push_counter <= max_placement_chunk)
	{
		if ((*stack_a)->placement <= max_placement_chunk)
		{
			push(stack_a, stack_b);
			data->ops = ft_strnjoin(data->ops, "pb\n", 3);
			data->pb += 1;
			++push_counter;
		}
		else
		{
			rotate_stack(stack_a);
			data->ops = ft_strnjoin(data->ops, "ra\n", 3);
			data->ra += 1;
		}
	}
}

void	chunk_sort(t_list **stack_a, t_list **stack_b,
		t_data *data)
{
	size_t	stack_a_size;
	size_t	nb_chunk;
	size_t	chunk_l;
	size_t	max_placement_chunk;

	stack_a_size = ft_lstsize(*stack_a);
	nb_chunk = (sqrt_ceil(stack_a_size) * 45) / 100;
	if (!nb_chunk)
		nb_chunk = 1;
	chunk_l = stack_a_size / nb_chunk;
	max_placement_chunk = chunk_l;
	while (nb_chunk > 0)
	{
		if (nb_chunk == 1)
		{
			chunk_l = ft_lstsize(*stack_a);
			max_placement_chunk = stack_a_size;
		}
		pushing_by_chunk_in_b(stack_a, stack_b, data, max_placement_chunk);
		if ((*stack_a))
			max_placement_chunk += chunk_l;
		nb_chunk--;
	}
	*stack_a = pushing_by_chunk_in_a(max_placement_chunk, stack_b, data);
}
