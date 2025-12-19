/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstiter_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 14:55:48 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/19 14:21:14 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstiter(t_list *lst, void (*f)(int *))
{
	if (lst == NULL || f == NULL)
		return ;
	if (lst->first_node)
	{
		f(&lst->content);
		lst = lst->next;
	}
	while (!lst->first_node)
	{
		f(&lst->content);
		lst = lst->next;
	}
}
