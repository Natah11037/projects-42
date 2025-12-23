/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   next_to_percent.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 13:39:48 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/15 15:22:32 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static void	for_itoa_base(va_list args, char c, ssize_t *len)
{
	char		*str;
	void		*ptr;

	str = NULL;
	if (c == 'u')
		str = ft_itoa_base(va_arg(args, unsigned int), DEC);
	else if (c == 'x')
		str = ft_itoa_base(va_arg(args, unsigned int), HEXA_MIN);
	else if (c == 'X')
		str = ft_itoa_base(va_arg(args, unsigned int), HEXA_MAX);
	else if (c == 'p')
	{
		ptr = va_arg(args, void *);
		if (ptr == NULL)
		{
			*len += ft_putstr_fd("(nil)", 1);
			return ;
		}
		str = ft_itoa_base((size_t)ptr, HEXA_MIN);
		*len += ft_putstr_fd("0x", 1);
	}
	*len += ft_putstr_fd(str, 1);
	free(str);
}

int	next_to_percent(char c, va_list args)
{
	char		*str;
	ssize_t		len;

	len = 0;
	if (c == '%')
		len += ft_putchar_fd('%', 1);
	else if (c == 'c')
		len += ft_putchar_fd(va_arg(args, unsigned int), 1);
	else if (c == 's')
	{
		str = va_arg(args, char *);
		if (str == NULL)
			len += ft_putstr_fd("(null)", 1);
		else
			len += ft_putstr_fd(str, 1);
	}
	else if (c == 'i' || c == 'd')
		len += ft_putnbr_fd(va_arg(args, int), 1);
	else if (c == 'u' || c == 'x' || c == 'X' || c == 'p')
		for_itoa_base(args, c, &len);
	return (len);
}
