/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/16 09:47:02 by nweber--          #+#    #+#             */
/*   Updated: 2025/12/19 15:07:51 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	swap(t_list **stack)
{
	int	stack_tmp;

	stack_tmp = 0;
	if (!(*stack) || !(*stack)->next)
		exit (1);
	stack_tmp = (*stack)->content;
	(*stack)->content = (*stack)->next->content;
	(*stack)->next->content = stack_tmp;
}

void	swap_both(t_list **stack_a, t_list **stack_b)
{
	int	stack_tmp;

	stack_tmp = 0;
	if (!(*stack_a) || !(*stack_a)->next || !(*stack_b) || !(*stack_b)->next)
		exit (1);
	stack_tmp = (*stack_a)->content;
	(*stack_a)->content = (*stack_a)->next->content;
	(*stack_a)->next->content = stack_tmp;
	stack_tmp = (*stack_b)->content;
	(*stack_b)->content = (*stack_b)->next->content;
	(*stack_b)->next->content = stack_tmp;
}

int	main(void)
{
	t_list	*a;
	t_list	*b;
	t_list	*abis;
	t_list	*bbis;

	a = malloc(sizeof(t_list) * 1);
	b = malloc(sizeof(t_list) * 1);
	abis = malloc(sizeof(t_list) * 1);
	bbis = malloc(sizeof(t_list) * 1);
	a->content = 2;
	b->content = 4;
	abis->content = 9;
	bbis->content = 6;
	a->next = b;
	abis->next = bbis;
	printf("Avant swap :\n stack_a \n%d\n%d\n stack_b \n%d\n%d\n", a->content, a->next->content, abis->content, abis->next->content);
	swap_both(&a, &abis);
	printf("Apres swap :\n stack_a \n%d\n%d\n stack_b \n%d\n%d\n", a->content, a->next->content, abis->content, abis->next->content);
}
