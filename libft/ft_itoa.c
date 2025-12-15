/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 11:44:19 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/07 14:23:14 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	ft_intlen(long int n)
{
	long int	i;

	i = 0;
	if (n == 0)
		return (1);
	if (n < 0)
	{
		n = n * -1;
		++i;
	}
	while (n != 0)
	{
		n = n / 10;
		i++;
	}
	return (i);
}

char	*ft_itoa(int n)
{
	char		*str;
	int			size;
	long int	nb;

	nb = n;
	size = (int) ft_intlen(nb);
	str = ft_calloc(size + 1, sizeof(char));
	if (str == NULL)
		return (NULL);
	if (nb < 0)
	{
		nb = nb * -1;
		str[0] = '-';
	}
	str[size] = '\0';
	--size;
	while (size >= 0)
	{
		str[size] = nb % 10 + '0';
		nb = nb / 10;
		size--;
		if (size == 0 && n < 0)
			--size;
	}
	return (str);
}
