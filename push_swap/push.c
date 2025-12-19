/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/16 13:23:36 by nweber--          #+#    #+#             */
/*   Updated: 2025/12/19 15:10:58 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	push(t_list **stack1, t_list **stack2)
{
	if (!stack2)
		return ;
	ft_lstadd_front(stack1, *stack2);
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
	printf("Avant push :\n stack_a : %d%d\n stack_b : %d%d\n", a->content, a->next->content, abis->content, abis->next->content);
	push(&a, &abis);
	printf("Apres push :\n stack_a : %d%d\n stack_b : %d%d\n", a->content, a->next->content, abis->content, abis->next->content);
}