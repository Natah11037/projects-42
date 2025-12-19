/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 15:22:28 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/11 10:22:04 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	unsigned int	i;
	unsigned int	o;

	i = 0;
	o = 0;
	if ((big == NULL || little == NULL) && len == 0)
		return (NULL);
	if (little[o] == '\0')
		return ((char *) big);
	while (big[i] != '\0' && i < len)
	{
		while ((big[i + o] == little[o]) && (little[o] != '\0') && i + o < len)
		{
			++o;
			if (little[o] == '\0')
				return ((char *) &big[i]);
		}
		o = 0;
		++i;
	}
	return (NULL);
}
