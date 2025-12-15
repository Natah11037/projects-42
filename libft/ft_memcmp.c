/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 14:44:22 by nweber--          #+#    #+#             */
/*   Updated: 2025/10/29 15:04:49 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	unsigned int	i;
	unsigned char	*ts1;
	unsigned char	*ts2;

	i = 0;
	ts1 = (unsigned char *) s1;
	ts2 = (unsigned char *) s2;
	while (i < n)
	{
		if (ts1[i] != ts2[i])
		{
			return (ts1[i] - ts2[i]);
		}
		i++;
	}
	return (0);
}
