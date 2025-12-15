/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 10:26:31 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/11 13:55:39 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	unsigned int	i;
	size_t			lsrc;
	size_t			ldest;

	i = 0;
	if ((dst == NULL || src == NULL) && size == 0)
		return (0);
	lsrc = ft_strlen(src);
	ldest = ft_strlen((const char *) dst);
	if (ldest + i >= size)
		return (size + lsrc);
	while (ldest + i < size - 1 && src[i] != '\0')
	{
		dst[i + ldest] = src[i];
		i++;
	}
	dst[i + ldest] = '\0';
	return (lsrc + ldest);
}
