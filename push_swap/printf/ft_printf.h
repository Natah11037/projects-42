/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 13:28:08 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/15 15:27:02 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H
# define DEC "0123456789"
# define HEXA_MIN "0123456789abcdef"
# define HEXA_MAX "0123456789ABCDEF"

# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>

int		ft_printf(const char *s, ...);
int		next_to_percent(char c, va_list args);
int		ft_putchar_fd(char c, int fd);
ssize_t	ft_putnbr_fd(int n, int fd);
int		ft_putstr_fd(char *s, int fd);
void	*ft_calloc(size_t nmemb, size_t size);
size_t	ft_strlen(const char *s);
char	*ft_itoa_base(unsigned long n, const char *base);
void	ft_bzero(void *s, size_t n);
size_t	ft_intlen_base(unsigned long n, size_t base_len);

#endif