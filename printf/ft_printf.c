/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 13:36:52 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/15 14:23:53 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printf(const char *s, ...)
{
	int		i;
	int		final_len;
	va_list	args;

	va_start(args, s);
	i = 0;
	final_len = 0;
	while (s[i] != '\0')
	{
		if (s[i] == '%')
		{
			i++;
			final_len += next_to_percent(s[i], args);
		}
		else
			final_len += ft_putchar_fd(s[i], 1);
		i++;
	}
	va_end(args);
	return (final_len);
}
