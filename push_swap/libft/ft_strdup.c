/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 11:03:46 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/11 10:22:37 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	unsigned int	i;
	unsigned int	j;
	char			*dup;

	i = ft_strlen(s);
	j = 0;
	dup = ft_calloc(i + 1, sizeof(char));
	if (dup == NULL)
		return (NULL);
	while (s[j] != '\0')
	{
		dup[j] = s[j];
		++j;
	}
	dup[j] = '\0';
	return (dup);
}
