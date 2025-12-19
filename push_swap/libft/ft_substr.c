/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 13:16:17 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/07 13:23:24 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char			*sub;
	size_t			lfromstart;
	unsigned int	i;

	i = 0;
	lfromstart = 0;
	if (s == NULL || s[0] == '\0' || ft_strlen(s) < start)
		return (sub = ft_calloc(1, sizeof(char)));
	lfromstart = ft_strlen(&s[start]);
	if (lfromstart >= len)
		sub = ft_calloc(len + 1, sizeof(char));
	else
		sub = ft_calloc(lfromstart + 1, sizeof(char));
	if (sub == NULL)
		return (NULL);
	if (len > lfromstart)
		len = lfromstart;
	while (i < len)
	{
		sub[i] = s[start];
		++i;
		++start;
	}
	sub[i] = '\0';
	return (sub);
}
