/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 16:10:11 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/05 16:18:23 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	long int	nb;

	nb = n;
	if (nb < 0)
	{
		write(fd, "-", 1);
		nb = nb * -1;
	}
	if (nb <= 9 && nb >= 0)
	{
		ft_putchar_fd((nb + '0'), fd);
		return ;
	}
	ft_putnbr_fd((nb / 10), fd);
	ft_putnbr_fd((nb % 10), fd);
}
