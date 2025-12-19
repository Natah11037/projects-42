/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 14:14:07 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/07 09:47:55 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	char			*joined;
	size_t			lfullstr;

	if (s1 == NULL || s2 == NULL)
		return (NULL);
	lfullstr = ft_strlen(s1) + ft_strlen(s2) + 1;
	joined = ft_calloc(lfullstr, sizeof (char));
	if (joined == NULL)
		return (NULL);
	ft_strlcpy(joined, s1, lfullstr);
	ft_strlcat(joined, s2, lfullstr);
	return (joined);
}
