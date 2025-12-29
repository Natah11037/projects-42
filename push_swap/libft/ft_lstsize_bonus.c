/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 17:33:56 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/23 14:57:16 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_lstsize(t_list *lst)
{
	size_t	listsize;

	listsize = 0;
	if (lst == NULL)
		return (0);
	if (lst->first_node)
	{
		lst = lst->next;
		++listsize;
	}
	while (!lst->first_node)
	{
		++listsize;
		lst = lst->next;
	}
	return (listsize);
}
