/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear_bonus.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 11:15:19 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/19 11:52:59 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(int *))
{
	t_list	*ntemp;

	if (lst == NULL)
		return ;
	if ((*lst)->first_node)
		(*lst) = (*lst)->next;
	while (!(*lst)->first_node)
	{
		ntemp = (*lst)->next;
		ft_lstdelone((*lst), del);
		(*lst) = ntemp;
	}
	ft_lstdelone((*lst), del);
}
