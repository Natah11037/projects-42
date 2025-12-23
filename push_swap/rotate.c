/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/22 20:22:22 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/23 13:06:42 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	rotate_stack(t_list **stack)
{
	if (!stack || !*stack)
		return ;
	(*stack)->first_node = false;
	(*stack)->next->first_node = true;
	*stack = (*stack)->next;
}

void	rotate_both(t_list **stack_a, t_list **stack_b)
{
	if (!stack_a || !*stack_a || !stack_b || !*stack_b)
		return ;
	rotate_stack(stack_a);
	rotate_stack(stack_b);
}

void	reverse_rotate_stack(t_list **stack)
{
	if (!stack || !*stack)
		return ;
	(*stack)->first_node = false;
	(*stack)->prev->first_node = true;
	*stack = (*stack)->prev;
}

void	reverse_rotate_both(t_list **stack_a, t_list **stack_b)
{
	if (!stack_a || !*stack_a || !stack_b || !*stack_b)
		return ;
	reverse_rotate_stack(stack_a);
	reverse_rotate_stack(stack_b);
}
