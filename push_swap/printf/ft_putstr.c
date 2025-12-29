/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 16:30:16 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/14 19:50:45 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putstr(char *s)
{
	int	i;
	int	printed_chrs;

	printed_chrs = 0;
	i = 0;
	if (s == NULL)
	{
		printed_chrs += write(1, "(null)", 6);
		return (printed_chrs);
	}
	while (s[i] != '\0')
	{
		printed_chrs += write(1, &s[i], 1);
		++i;
	}
	return (printed_chrs);
}
