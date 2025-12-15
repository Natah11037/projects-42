/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 11:46:56 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/11 12:51:26 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	int		i;
	char	ctochar;

	ctochar = c;
	if (ft_isascii(ctochar) == 0)
		return ((char *) s);
	i = ft_strlen(s);
	while (i >= 0)
	{
		if (s[i] == ctochar)
			return ((char *) &s[i]);
		--i;
	}
	return (0);
}
