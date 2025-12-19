/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back_bonus.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 10:48:37 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/19 14:36:23 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdio.h>

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*templst;

	if (lst == NULL || new == NULL)
		return ;
	if (*lst == NULL)
	{
		new->next = new;
		new->prev = new;
		new->first_node = true;
		*lst = new;
	}
	else
	{
		templst = ft_lstlast(*lst);
		templst->next = new;
		new->prev = templst;
		new->next = *lst;
		new->first_node = false;
	}
}
