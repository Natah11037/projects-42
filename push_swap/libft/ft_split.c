/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 15:34:10 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/22 13:48:50 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdio.h>

static size_t	ft_count_words(const char *s, char c)
{
	unsigned int			i;
	unsigned int			lword;
	size_t					words;

	i = 0;
	words = 0;
	lword = 0;
	while (s[i] != '\0')
	{
		while (s[i] != c && s[i] != '\0')
		{
			++i;
			++lword;
		}
		if (lword > 0)
			++words;
		lword = 0;
		if (s[i] != '\0')
			++i;
	}
	return (words);
}

static	void	*ft_freeall(char **splitted, int j)
{
	while (j >= 0)
	{
		free(splitted[j]);
		--j;
	}
	free(splitted);
	return (NULL);
}

static char	**ft_splitter(const char *s, char c, char **splitted)
{
	unsigned int			i;
	int						j;
	size_t					lword;

	i = 0;
	lword = 0;
	j = 0;
	while (s[i] != '\0')
	{
		while (s[i + lword] != c && s[i + lword] != '\0')
			++lword;
		if (lword > 0)
		{
			splitted[j] = ft_substr(s, i, lword);
			if (splitted[j] == NULL)
				return (ft_freeall(splitted, j));
			j++;
		}
		i = i + lword;
		lword = 0;
		if (s[i] != '\0')
			++i;
	}
	splitted[j] = 0;
	return (splitted);
}

char	**ft_split(char const *s, char c)
{
	char				**splitted;

	if (s == NULL)
		return (NULL);
	splitted = ft_calloc(ft_count_words(s, c) + 1, sizeof(char *));
	if (splitted == NULL)
		return (NULL);
	splitted = ft_splitter(s, c, splitted);
	if (splitted == NULL)
		return (NULL);
	return (splitted);
}
