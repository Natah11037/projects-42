/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear_bonus.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 11:17:16 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/11 13:56:31 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*actuallst;
	t_list	*nextlst;

	if (!lst)
		return ;
	actuallst = *lst;
	while (actuallst != NULL)
	{
		nextlst = actuallst->next;
		ft_lstdelone(actuallst, del);
		actuallst = nextlst;
	}
	*lst = NULL;
}
