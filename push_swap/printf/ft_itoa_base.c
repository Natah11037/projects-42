/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 16:08:15 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/15 12:25:49 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static size_t	ft_intlen_base(unsigned long n, const char *base)
{
	size_t				ln;

	ln = 0;
	if (n == 0)
		return (1);
	while (n >= ft_strlen(base))
	{
		n = n / ft_strlen(base);
		++ln;
	}
	if (ln > 0)
		++ln;
	if (ln == 0)
		return (1);
	return (ln);
}

static int	ft_check_base(const char *base)
{
	unsigned int	i;
	unsigned int	j;

	j = 0;
	i = 0;
	if (base[0] == '\0')
		return (0);
	while (base[i] != '\0')
	{
		j = i + 1;
		if (base[i] == '+' || base[i] == '-')
			return (0);
		while (base[j] != '\0' && base[j] != base[i])
			++j;
		if (base[j] == base[i])
			return (0);
		++i;
	}
	return (1);
}

static void	ft_converter(char *str, int i, unsigned long n, const char *base)
{
	long int		keep_mod;

	keep_mod = n;
	while (i >= 0)
	{
		keep_mod = n % ft_strlen(base);
		str[i] = base[keep_mod];
		n = n / ft_strlen(base);
		--i;
	}
}

char	*ft_itoa_base(unsigned long n, const char *base, int iffromp)
{
	char					*str;
	unsigned int			i;

	if (iffromp == 1 && !n)
		return (NULL);
	if (base == NULL)
		return (NULL);
	if (ft_check_base(base) == 0)
		return (NULL);
	i = (int) ft_intlen_base(n, base);
	str = ft_calloc(i + 1, sizeof(char));
	if (str == NULL)
		return (NULL);
	str[i] = '\0';
	--i;
	ft_converter(str, i, n, base);
	return (str);
}
