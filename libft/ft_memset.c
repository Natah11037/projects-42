/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 16:59:19 by nweber--          #+#    #+#             */
/*   Updated: 2025/10/28 17:17:42 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

void	*ft_memset(void *s, int c, size_t n)
{
	unsigned int	i;
	unsigned char	*temp;

	temp = s;
	i = 0;
	while (i != n)
	{
		temp[i] = c;
		i++;
	}
	return (s);
}
