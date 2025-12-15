/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 17:04:27 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/10 10:30:19 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_lstsize(t_list *lst)
{
	int	lenlst;

	lenlst = 0;
	while (lst != NULL)
	{
		lst = lst->next;
		++lenlst;
	}
	return (lenlst);
}
