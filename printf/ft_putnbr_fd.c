/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/14 14:07:21 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/15 15:26:37 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

ssize_t	ft_putnbr_fd(int n, int fd)
{
	long int	nb;
	ssize_t		len;

	nb = n;
	len = 0;
	if (nb < 0)
	{
		len += write(fd, "-", 1);
		nb = nb * -1;
	}
	if (nb > 9)
		len += ft_putnbr_fd((nb / 10), fd);
	len += ft_putchar_fd((nb % 10) + '0', fd);
	return (len);
}
