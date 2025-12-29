/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear_bonus.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 11:15:19 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/22 17:55:35 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst)
{
	t_list	*ntemp;

	if (lst == NULL)
		return ;
	ntemp = (*lst)->next;
	while (!ntemp->first_node)
	{
		ft_lstdelone(lst, ntemp);
		ntemp = (*lst)->next;
	}
	ft_lstdelone(lst, ntemp);
}
