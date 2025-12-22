/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelone_bonus.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 11:01:30 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/22 15:57:45 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstdelone(t_list **lst, t_list *node_del)
{
	if (!lst || !node_del)
		return ;
	if (node_del->next == node_del)
	{
		(*lst) = NULL;
		free(node_del);
		return ;
	}
	node_del->prev->next = node_del->next;
	node_del->next->prev = node_del->prev;
	if ((*lst) == node_del)
	{
		(*lst) = node_del->next;
		node_del->first_node = false;
		(*lst)->first_node = true;
	}
	free(node_del);
}
