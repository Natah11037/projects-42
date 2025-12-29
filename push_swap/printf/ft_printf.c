/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 14:15:14 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/15 15:53:29 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printf(const char *to_print, ...)
{
	unsigned int	i;
	int				printed_chrs;
	va_list			args;

	va_start(args, to_print);
	i = 0;
	printed_chrs = 0;
	while (to_print[i] != '\0')
	{
		if (to_print[i] == '%')
		{
			++i;
			next_to_percent(&to_print[i], args, &printed_chrs);
			++i;
		}
		else
		{
			ft_putchar(to_print[i]);
			++i;
			++printed_chrs;
		}
	}
	va_end(args);
	return (printed_chrs);
}
