/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/16 13:23:36 by nweber--          #+#    #+#             */
/*   Updated: 2025/12/22 15:58:36 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	push(t_list **stack_a, t_list **stack_b)
{
	if (!stack_a || !*stack_a || !stack_b)
		return ;
	if (!*stack_b)
		*stack_b = ft_lstnew((*stack_a)->content);
	else
		ft_lstadd_front(stack_b, ft_lstnew((*stack_a)->content));
	ft_lstdelone(stack_a, *stack_a);
}

int	main(void)
{
	t_list **a;
	t_list	*new;
	t_list	*new2;
	t_list	**b;

	new = ft_lstnew(45);
	a = &new;
	ft_lstadd_front(a, ft_lstnew(12));
	printf("c'est a %d\n", (*a)->content);
	new2 = ft_lstnew(6);
	b = &new2;
	for (size_t i = 0; i < 3; i++)
	{
		printf("Le noeud de b %zu est a %d\n", i, (*b)->content);
		*b = (*b)->next;
	}
	printf("\n");
	for (size_t i = 0; i < 2; i++)
	{
		printf("Le noeud de a %zu est a %d\n", i, (*a)->content);
		*a = (*a)->next;
	}
	printf("\napres push\n \n");
	push(a, b);
	for (size_t i = 0; i < 3; i++)
	{
		printf("Le noeud de b %zu est a %d\n", i, (*b)->content);
		*b = (*b)->next;
	}
	printf("\n");
	for (size_t i = 0; i < 3; i++)
	{
		printf("Le noeud de a %zu est a %d\n", i, (*a)->content);
		*a = (*a)->next;
	}
	return (0);
}
