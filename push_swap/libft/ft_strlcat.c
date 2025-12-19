/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 14:54:48 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/11 10:20:36 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	unsigned int		i;
	size_t				lsrc;
	size_t				ldst;

	i = 0;
	if ((dst == NULL || src == NULL) && size == 0)
		return (0);
	lsrc = ft_strlen(src);
	ldst = ft_strlen(dst);
	if (ldst >= size)
		return (size + lsrc);
	while (ldst + i < size - 1 && src[i] != '\0')
	{
		dst[i + ldst] = src[i];
		++i;
	}
	dst[i + ldst] = '\0';
	return (ldst + lsrc);
}
