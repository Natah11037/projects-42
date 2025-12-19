/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 11:22:49 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/07 09:57:29 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdio.h>

static size_t	ft_intlen(int n)
{
	size_t			ln;
	long int		posnbr;	

	ln = 0;
	posnbr = n;
	if (posnbr == 0)
		return (1);
	if (posnbr < 0)
	{
		posnbr = posnbr * -1;
		++ln;
	}
	while (posnbr > 0)
	{
		posnbr = posnbr / 10;
		++ln;
	}
	return (ln);
}

char	*ft_itoa(int n)
{
	char		*str;
	long int	tempn;
	int			i;

	i = (int) ft_intlen(n);
	str = ft_calloc(ft_intlen(n) + 1, sizeof(char));
	if (str == NULL)
		return (NULL);
	tempn = n;
	if (tempn < 0)
	{
		tempn = tempn * -1;
		str[0] = '-';
	}
	str[i] = '\0';
	--i;
	while (i >= 0)
	{
		str[i] = (tempn % 10) + '0';
		tempn = tempn / 10;
		--i;
		if (n < 0 && i == 0)
			--i;
	}
	return (str);
}
