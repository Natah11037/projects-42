/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 15:00:55 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/13 14:06:19 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*firstnode;
	t_list	*transfolst;

	if (lst == NULL || f == NULL || del == NULL)
		return (NULL);
	transfolst = ft_lstnew(f(lst->content));
	if (transfolst == NULL)
		return (NULL);
	firstnode = transfolst;
	while (lst->next != NULL)
	{
		lst = lst->next;
		transfolst->next = ft_lstnew(f(lst->content));
		if (transfolst == NULL)
		{
			ft_lstclear(&firstnode, del);
			return (NULL);
		}
		transfolst = transfolst->next;
	}
	return (firstnode);
}
