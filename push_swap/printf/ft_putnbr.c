/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 16:34:00 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/14 19:52:46 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

void	ft_putnbr(int n, int *printed_ints)
{
	if (n == -2147483648)
	{
		*printed_ints += write(1, "-2147483648", 11);
		return ;
	}
	if (n < 0)
	{
		n = n * -1;
		*printed_ints += write(1, "-", 1);
	}
	if (n >= 0 && n < 10)
		*printed_ints += ft_putchar(n + '0');
	else
	{
		ft_putnbr(n / 10, printed_ints);
		ft_putnbr(n % 10, printed_ints);
	}
}
