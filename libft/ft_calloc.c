/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 16:44:44 by nweber--          #+#    #+#             */
/*   Updated: 2025/10/31 11:52:49 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t nmemb, size_t size)
{
	void	*fullofzero;
	size_t	total_size;

	total_size = nmemb * size;
	if (size && nmemb && nmemb > (size_t)-1 / size)
		return (NULL);
	fullofzero = malloc(total_size);
	if (fullofzero == NULL)
		return (0);
	ft_bzero(fullofzero, total_size);
	return (fullofzero);
}
