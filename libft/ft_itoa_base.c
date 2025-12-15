/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 13:07:32 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/14 14:56:59 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdio.h>

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

static void	ft_converter(char *s, int i, unsigned long n, const char *base)
{
	while (i >= 0)
	{
		s[i] = base[n % ft_strlen(base)];
		n /= ft_strlen(base);
		i--;
	}
}

char	*ft_itoa_base(unsigned long n, const char *base)
{
	int				i;
	unsigned long	nbr;
	size_t			base_len;
	char			*s;

	i = 0;
	nbr = n;
	if (verif_base(base) == 0)
		return (NULL);
	base_len = ft_strlen(base);
	while (nbr != 0)
	{
		i++;
		nbr /= base_len;
	}
	s = ft_calloc(i + 1, sizeof(char));
	if (!n)
		return (NULL);
	s[i + 1] = '\0';
	ft_converter(s, i, n, base);
	return (s);
}
