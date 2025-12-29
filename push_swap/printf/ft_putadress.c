/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putadress.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/14 11:04:22 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/14 15:55:32 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putadress(char *s)
{
	int	i;
	int	printed_chrs;

	printed_chrs = 0;
	i = 0;
	if (s == NULL)
	{
		printed_chrs += write(1, "(nil)", 5);
		return (printed_chrs);
	}
	printed_chrs += write(1, "0x", 2);
	while (s[i] != '\0')
	{
		printed_chrs += write(1, &s[i], 1);
		++i;
	}
	return (printed_chrs);
}
