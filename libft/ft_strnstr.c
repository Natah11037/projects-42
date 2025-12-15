/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 15:20:46 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/11 10:22:21 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	unsigned int	i;
	unsigned int	y;

	i = 0;
	y = 0;
	if ((big == NULL || little == NULL) && len == 0)
		return (NULL);
	if (little[y] == '\0')
		return ((char *)big);
	while ((big[i] != '\0') && (i < len))
	{
		while (big[i + y] == little[y] && little[y] != '\0' && i + y < len)
		{
			y++;
			if (little[y] == '\0')
				return ((char *) &big[i]);
		}
		y = 0;
		i++;
	}
	return (0);
}
