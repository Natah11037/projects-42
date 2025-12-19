/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 11:59:09 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/11 10:13:28 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	unsigned char		*tsrc;
	unsigned char		*tdest;
	unsigned int		i;

	i = 0;
	if (dest == NULL && src == NULL)
		return (NULL);
	tdest = (unsigned char *) dest;
	tsrc = (unsigned char *) src;
	if (dest > src)
	{
		while (0 < n)
		{
			tdest[n - 1] = tsrc[n - 1];
			--n;
		}
	}
	while (i < n)
	{
		tdest[i] = tsrc[i];
		++i;
	}
	return (dest);
}
