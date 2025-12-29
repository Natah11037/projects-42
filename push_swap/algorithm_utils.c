/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algorithm_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 20:25:02 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/27 22:41:24 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	search_for_max(t_list *stack)
{
	int	potential_max;

	potential_max = 0;
	potential_max = stack->content;
	stack = stack->next;
	while (!stack->first_node)
	{
		if (potential_max < stack->content)
			potential_max = stack->content;
		stack = stack->next;
	}
	return (potential_max);
}

size_t	max_placement(t_list *stack)
{
	size_t	potential_max;

	potential_max = 0;
	potential_max = stack->placement;
	stack = stack->next;
	while (!stack->first_node)
	{
		if (potential_max < stack->placement)
			potential_max = stack->placement;
		stack = stack->next;
	}
	return (potential_max);
}

size_t	min_placement(t_list **stack)
{
	size_t	potential_min;

	potential_min = 0;
	potential_min = (*stack)->placement;
	(*stack) = (*stack)->next;
	while (!(*stack)->first_node)
	{
		if (potential_min > (*stack)->placement)
			potential_min = (*stack)->placement;
		(*stack) = (*stack)->next;
	}
	while ((*stack)->placement != potential_min)
		(*stack) = (*stack)->next;
	return (potential_min);
}

size_t	search_placement(t_list *stack, size_t placement)
{
	size_t	i;

	i = 0;
	while (stack->placement != placement)
	{
		stack = stack->next;
		++i;
	}
	return (i);
}
