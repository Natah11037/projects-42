/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back_bonus.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 10:48:21 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/11 12:45:16 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*templst;

	if (lst == NULL || new == NULL)
		return ;
	if (!*lst)
		*lst = new;
	else
	{
		templst = ft_lstlast(*lst);
		templst->next = new;
	}
}
