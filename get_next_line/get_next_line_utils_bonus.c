/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils_bonus.c                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 10:56:07 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/27 13:25:12 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

size_t	ft_strlen(const char *s)
{
	size_t	i;

	if (!s)
		return (0);
	i = 0;
	while (s[i] != '\0')
		i++;
	return (i);
}

void	*ft_calloc(size_t nmemb, size_t size)
{
	void			*fullofzero;
	size_t			total_size;
	unsigned int	i;
	unsigned char	*temp;

	total_size = nmemb * size;
	if (size && nmemb && nmemb > (size_t)-1 / size)
		return (NULL);
	fullofzero = malloc(total_size);
	if (fullofzero == NULL)
		return (0);
	temp = fullofzero;
	i = 0;
	while (i != size)
	{
		temp[i] = '\0';
		i++;
	}
	return (fullofzero);
}

char	*ft_strndup(const char *s, size_t len)
{
	size_t		i;
	size_t		len_s;
	char		*dup;

	len_s = ft_strlen(s);
	i = 0;
	dup = ft_calloc(len + 1, sizeof (char));
	if (dup == NULL)
		return (NULL);
	while (i < len_s)
	{
		dup[i] = s[i];
		i++;
	}
	dup[i] = '\0';
	return (dup);
}

void	ft_bzero(void *s, size_t n)
{
	unsigned int	i;
	unsigned char	*temp;

	temp = s;
	i = 0;
	while (i != n)
	{
		temp[i] = '\0';
		i++;
	}
}

char	*ft_strchr(const char *s, int c)
{
	int		i;

	i = 0;
	while (s[i] != '\0')
	{
		if (s[i] == (char) c)
			return ((char *) &s[i]);
		i++;
	}
	if (c == s[i])
		return ((char *) &s[i]);
	return (NULL);
}
