/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   radix_sort.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/27 21:31:59 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/28 12:29:22 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	comparing_bits_to_push_a(t_list **stack_a,
	t_list **stack_b, t_data *data, size_t bit_by_bit)
{
	size_t	current_placement;
	size_t	list_length;
	size_t	list_i;

	list_length = ft_lstsize(*stack_a);
	list_i = 0;
	while (list_i < list_length)
	{
		current_placement = (*stack_a)->placement;
		if (((current_placement >> bit_by_bit) & 1) == 0)
		{
			push(stack_a, stack_b);
			data->ops = ft_strnjoin(data->ops, "pb\n", 3);
			data->pb += 1;
		}
		else
		{
			rotate_stack(stack_a);
			data->ops = ft_strnjoin(data->ops, "ra\n", 3);
			data->ra += 1;
		}
		++list_i;
	}
}

static void	comparing_bits_to_push_b(t_list **stack_a,
	t_list **stack_b, t_data *data, size_t bit_by_bit)
{
	size_t	current_placement;
	size_t	list_length;
	size_t	list_i;

	list_length = ft_lstsize(*stack_b);
	list_i = 0;
	while (list_i < list_length)
	{
		current_placement = (*stack_b)->placement;
		if (((current_placement >> bit_by_bit) & 1) == 1)
		{
			push(stack_b, stack_a);
			data->ops = ft_strnjoin(data->ops, "pa\n", 3);
			data->pa += 1;
		}
		else
		{
			rotate_stack(stack_b);
			data->ops = ft_strnjoin(data->ops, "rb\n", 3);
			data->rb += 1;
		}
		++list_i;
	}
}

void	radix_sort(t_list **stack_a, t_list **stack_b,
		t_data *data)
{
	size_t	max_bits;
	size_t	bit_by_bit;

	max_bits = 0;
	while ((max_placement(*stack_a) >> max_bits) > 0)
		max_bits++;
	bit_by_bit = 0;
	while (bit_by_bit < max_bits)
	{
		comparing_bits_to_push_a(stack_a, stack_b,
			data, bit_by_bit);
		++bit_by_bit;
		if (bit_by_bit < max_bits)
			comparing_bits_to_push_b(stack_a, stack_b,
				data, bit_by_bit);
		else
		{
			while (*stack_b)
			{
				push(stack_b, stack_a);
				data->ops = ft_strnjoin(data->ops, "pa\n", 3);
				data->pa += 1;
			}
		}
	}
}
