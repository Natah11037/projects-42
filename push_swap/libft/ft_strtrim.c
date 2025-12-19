/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 10:55:42 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/07 13:34:23 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdio.h>

char	*ft_strtrim(char const *s1, char const *set)
{
	size_t			start;
	size_t			lmendfullstr;
	char			*trimdstr;

	start = 0;
	if (s1 == NULL)
		return (NULL);
	if (set == NULL)
		return ((char *) s1);
	lmendfullstr = ft_strlen(s1) - 1;
	while (ft_strchr(set, (int) s1[start]) != NULL)
		++start;
	while (ft_strchr(set, (int) s1[lmendfullstr]) != NULL)
		--lmendfullstr;
	trimdstr = ft_substr(s1, start, (lmendfullstr - start) + 1);
	if (trimdstr == NULL)
		return (NULL);
	return (trimdstr);
}
