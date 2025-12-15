/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 16:03:32 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/28 15:48:39 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_atoi(const char *nptr)
{
	unsigned int	i;
	int				sign;
	int				result;

	i = 0;
	sign = 1;
	result = 0;
	while ((nptr[i] <= 13 && nptr[i] >= 9) || (nptr[i] == 32))
		i++;
	if ((nptr[i] == '-') || (nptr[i] == '+'))
	{
		if (nptr[i] == '-')
			sign = sign * -1;
		i++;
	}
	while ((nptr[i] <= 57) && (nptr[i] >= 48))
	{
		result = result * 10 + (nptr[i] - '0');
		i++;
	}
	return (result * sign);
}
