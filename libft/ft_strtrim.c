/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 13:31:34 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/07 13:34:23 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	unsigned int	start;
	size_t			strlend;
	char			*strt;

	start = 0;
	if (!s1)
		return (NULL);
	if (!set)
		return ((char *)s1);
	strlend = ft_strlen(s1) - 1;
	while (ft_strchr(set, (int)s1[start]) != NULL)
		start++;
	while (ft_strchr(set, (int)s1[strlend]) != NULL)
		strlend--;
	strt = ft_substr(s1, start, (strlend - start) + 1);
	if (strt == NULL)
		return (NULL);
	return (strt);
}
