/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 14:13:36 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/06 10:20:40 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	size_t	lenall;
	char	*dest;

	if (!s1 || !s2)
		return (NULL);
	lenall = ft_strlen(s1) + ft_strlen(s2) + 1;
	dest = ft_calloc(lenall, sizeof(char));
	if (!dest)
		return (NULL);
	ft_strlcpy(dest, s1, lenall);
	ft_strlcat(dest, s2, lenall);
	return (dest);
}
