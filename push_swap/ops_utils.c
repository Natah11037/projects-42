/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_utils.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 16:09:34 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/25 13:55:57 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static char	*ft_strndup(const char *s, unsigned int len)
{
	unsigned int	j;
	unsigned int	l_s;
	char			*dup;

	j = 0;
	l_s = ft_strlen(s);
	dup = ft_calloc(len + 1, sizeof dup);
	if (dup == NULL)
		return (NULL);
	while (j < l_s)
	{
		dup[j] = s[j];
		++j;
	}
	dup[j] = '\0';
	return (dup);
}

char	*ft_strnjoin(char *s1, char const *s2, unsigned int keep_index)
{
	char			*joined;
	size_t			lfullstr;

	if (s2 == NULL)
		return (NULL);
	if (!s1)
		return (joined = ft_strndup(s2, ft_strlen(s2)));
	lfullstr = ft_strlen(s1) + keep_index + 1;
	joined = ft_strndup(s1, lfullstr);
	if (joined == NULL)
		return (NULL);
	ft_strlcat(joined, s2, lfullstr);
	free(s1);
	return (joined);
}
