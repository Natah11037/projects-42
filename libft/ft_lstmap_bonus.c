/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 15:02:09 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/11 14:00:37 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*flst;
	t_list	*firstlst;

	if (!lst || f == NULL)
		return (NULL);
	flst = ft_lstnew(f(lst->content));
	if (!flst)
		return (NULL);
	firstlst = flst;
	while (lst->next != NULL)
	{
		lst = lst->next;
		flst->next = ft_lstnew(f(lst->content));
		if (flst->next == NULL)
		{
			ft_lstclear(&firstlst, del);
			free(lst);
			return (NULL);
		}
		flst = flst->next;
	}
	return (firstlst);
}
