/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_next_to_percent.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 15:18:29 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/15 15:53:14 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static void	if_itoa_base(va_list args, int *l, char *base)
{
	char	*s;

	s = ft_itoa_base(va_arg(args, unsigned int), base, 0);
	*l += ft_putstr(s);
	free(s);
}

void	next_to_percent(const char *to_print, va_list args, int *l)
{
	char	*str;

	if (to_print[0] == 'c')
		*l += ft_putchar(va_arg(args, unsigned int));
	else if (to_print[0] == 's')
		*l += ft_putstr(va_arg(args, char *));
	else if (to_print[0] == 'p')
	{
		str = ft_itoa_base((size_t) va_arg(args, void *), HEX_MIN, 1);
		*l += ft_putadress(str);
		free(str);
	}
	else if (to_print[0] == 'd' || to_print[0] == 'i')
		ft_putnbr(va_arg(args, int), l);
	else if (to_print[0] == 'u')
		if_itoa_base(args, l, DEC);
	else if (to_print[0] == 'x')
		if_itoa_base(args, l, HEX_MIN);
	else if (to_print[0] == 'X')
		if_itoa_base(args, l, HEX_MAJ);
	else if (to_print[0] == '%')
		*l += ft_putchar('%');
}
