/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 10:55:36 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/27 14:48:34 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

size_t	ft_strlcpy(char *dest, const char *src, size_t size)
{
	unsigned int	i;
	size_t			y;

	i = 0;
	y = 0;
	if (size == 0)
		return (ft_strlen(src));
	while (src[y] != '\0')
		y++;
	while (src[i] != '\0' && i < (size - 1))
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = '\0';
	return (y);
}

char	*ft_strnjoin(char *s1, char const *s2, int le_n)
{
	char	*dest;
	int		i;
	int		len_s1;

	i = 0;
	if (!s1)
		s1 = ft_calloc(1, sizeof(char));
	len_s1 = ft_strlen(s1);
	dest = ft_strndup(s1, (le_n + len_s1));
	if (!dest)
		return (NULL);
	while (i < le_n)
	{
		dest[i + len_s1] = s2[i];
		i++;
	}
	dest[i + len_s1] = '\0';
	if (s1)
		free(s1);
	return (dest);
}

static char	*no_nl(char **stock, ssize_t *reader, int fd)
{
	char	*str;

	str = NULL;
	while (!ft_strchr(stock[fd], '\n'))
	{
		str = ft_strnjoin(str, stock[fd], *reader);
		if (!str)
			return (NULL);
		ft_bzero(stock[fd], *reader);
		*reader = read(fd, stock[fd], BUFFER_SIZE);
		if (*reader == 0 && str[0] == '\0')
		{
			free(stock[fd]);
			stock[fd] = NULL;
			return (NULL);
		}
		if (*reader == 0)
		{
			free(stock[fd]);
			stock[fd] = NULL;
			return (str);
		}
	}
	return (str);
}

static char	*get_new_line(char *str, char **stock, ssize_t reader, int fd)
{
	int		i_of_n;
	char	*buffer_t;

	i_of_n = 0;
	buffer_t = NULL;
	str = no_nl(stock, &reader, fd);
	if (reader == 0)
		return (str);
	while (stock[fd][i_of_n] != '\n')
		i_of_n++;
	str = ft_strnjoin(str, stock[fd], i_of_n + 1);
	if (!str)
		return (NULL);
	buffer_t = ft_strndup(stock[fd], reader);
	if (!buffer_t)
		return (NULL);
	ft_bzero(stock[fd], BUFFER_SIZE + 1);
	ft_strlcpy(stock[fd], ft_strchr(buffer_t, '\n') + 1, reader - i_of_n);
	free(buffer_t);
	if (stock[fd][0] == '\0')
	{
		free(stock[fd]);
		stock[fd] = NULL;
	}
	return (str);
}

char	*get_next_line(int fd)
{
	static char		*stock[OPEN_MAX];
	char			*str;
	ssize_t			reader;

	if (fd < 0 || fd >= 1024 || BUFFER_SIZE <= 0)
		return (NULL);
	str = NULL;
	if (!stock[fd])
	{
		stock[fd] = ft_calloc(BUFFER_SIZE + 1, sizeof(char));
		reader = read(fd, stock[fd], BUFFER_SIZE);
		if (reader == -1 || reader == 0)
		{
			free(stock[fd]);
			stock[fd] = NULL;
			return (NULL);
		}
		stock[fd][reader] = '\0';
	}
	else
		reader = ft_strlen(stock[fd]);
	str = get_new_line(str, stock, reader, fd);
	if (!str)
		return (NULL);
	return (str);
}
