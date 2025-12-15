/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 13:52:11 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/11 10:12:54 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t size)
{
	unsigned int			i;
	unsigned char			*tsrc;
	unsigned char			*tdest;

	tdest = (unsigned char *)dest;
	tsrc = (unsigned char *)src;
	i = 0;
	if (dest == NULL && src == NULL)
		return (NULL);
	if (dest > src)
	{
		while (size > 0)
		{
			tdest[size - 1] = tsrc[size - 1];
			size--;
		}
	}
	while (i < size)
	{
		tdest[i] = tsrc[i];
		i++;
	}
	return (dest);
}
