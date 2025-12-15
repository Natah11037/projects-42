/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/15 11:22:47 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/15 14:42:05 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	verif_base(const char *base)
{
	int	i;
	int	j;

	i = 0;
	j = 0;
	if (base[i] == '\0')
		return (0);
	while (base[i] != '\0')
	{
		j = i + 1;
		while (base[j] != '\0')
		{
			if (base[i] == base [j])
			{
				return (0);
			}
			j++;
		}
		i++;
	}
	return (1);
}

char	*ft_itoa_base(unsigned long nbr, const char *base)
{
	int				i;
	size_t			base_len;
	char			*s;

	i = 0;
	if (verif_base(base) == 0)
		return (NULL);
	base_len = ft_strlen(base);
	i = ft_intlen_base(nbr, base_len);
	s = ft_calloc(i + 1, sizeof(char));
	if (!s)
		return (NULL);
	s[i] = '\0';
	i--;
	while (i >= 0)
	{
		s[i] = base[nbr % base_len];
		nbr /= base_len;
		--i;
	}
	return (s);
}
