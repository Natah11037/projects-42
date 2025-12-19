/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 11:18:46 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/11 14:05:29 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strchr(const char *s, int c)
{
	int				i;

	i = 0;
	while (s[i] != '\0')
	{
		if ((char) c == s[i])
			return ((char *) &s[i]);
		++i;
	}
	if ((char) c == s[i])
		return ((char *) &s[i]);
	return (NULL);
}
