/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_and_swap.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/22 21:51:38 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/25 22:14:43 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	push(t_list **stack_a, t_list **stack_b)
{
	if (!stack_a || !*stack_a || !stack_b)
		return ;
	if (!*stack_b)
		*stack_b = ft_lstnew((*stack_a)->content, (*stack_a)->placement);
	else
		ft_lstadd_front(stack_b, ft_lstnew((*stack_a)->content,
				(*stack_a)->placement));
	ft_lstdelone(stack_a, *stack_a);
}

void	swap(t_list **stack)
{
	int	stack_tmp;

	stack_tmp = 0;
	if (!(*stack) || !(*stack)->next)
		return ;
	stack_tmp = (*stack)->content;
	(*stack)->content = (*stack)->next->content;
	(*stack)->next->content = stack_tmp;
}

void	swap_both(t_list **stack_a, t_list **stack_b)
{
	int	stack_tmp;

	stack_tmp = 0;
	if (!(*stack_a) || !(*stack_a)->next || !(*stack_b) || !(*stack_b)->next)
		return ;
	stack_tmp = (*stack_a)->content;
	(*stack_a)->content = (*stack_a)->next->content;
	(*stack_a)->next->content = stack_tmp;
	stack_tmp = (*stack_b)->content;
	(*stack_b)->content = (*stack_b)->next->content;
	(*stack_b)->next->content = stack_tmp;
}
