/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_intlen_base.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/15 11:22:11 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/15 11:45:25 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "printf.h"

size_t	ft_intlen_base(unsigned long n, size_t base_len)
{
	size_t			ln;
	unsigned long	tempn;

	tempn = n;
	ln = 0;
	if (tempn == 0)
		return (1);
	while (tempn >= base_len)
	{
		tempn = tempn / base_len;
		++ln;
	}
	if (ln > 0)
		++ln;
	if (ln == 0)
		return (1);
	return (ln);
}
