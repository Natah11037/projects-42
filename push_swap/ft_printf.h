/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 14:13:52 by cyakisan          #+#    #+#             */
/*   Updated: 2025/11/15 15:23:23 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H
# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>
# define HEX_MIN "0123456789abcdef"
# define HEX_MAJ "0123456789ABCDEF"
# define DEC "0123456789"

void	next_to_percent(const char *to_print, va_list args, int *l, int *i);
int		ft_putchar(char c);
int		ft_putstr(char *s);
void	ft_putnbr(int n, int *printed_ints);
int		ft_putadress(char *s);
size_t	ft_strlen(const char *s);
void	ft_bzero(void *s, size_t n);
void	*ft_calloc(size_t nmemb, size_t size);
char	*ft_itoa_base(unsigned long n, const char *base, int iffromp);
int		ft_printf(const char *to_print, ...);

#endif