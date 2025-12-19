/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front_bonus.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 16:23:27 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/19 13:42:56 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_front(t_list **lst, t_list *new)
{
	if (lst == NULL || new == NULL)
		return ;
	if (!*lst)
	{
		new->next = new;
		new->prev = new;
		new->first_node = true;
		*lst = new;
	}
	else
	{
		new->prev = ft_lstlast((*lst));
		ft_lstlast((*lst))->next = new;
		(*lst)->first_node = false;
		new->next = *lst;
		new->first_node = true;
		*lst = new;
	}
}

