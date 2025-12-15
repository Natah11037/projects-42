/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 15:35:08 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/07 13:35:04 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	ft_count_words(const char *s, char sep)
{
	unsigned int	nwords;
	unsigned int	isword;
	int				i;
	unsigned int	start;

	i = 0;
	start = 0;
	isword = 0;
	nwords = 0;
	while (s[i] != '\0')
	{
		while (s[i] != sep && s[i] != '\0')
		{
			i++;
			isword++;
		}
		if (isword > 0)
			nwords++;
		isword = 0;
		if (s[i] != '\0')
			i++;
	}
	return (nwords);
}

static void	*ft_free_all(char **split, int j)
{
	while (j >= 0)
	{
		free(split[j]);
		j--;
	}
	free(split);
	return (NULL);
}

static char	**ft_splitter(const char *s, char c, char **split)
{
	unsigned int	i;
	int				j;
	unsigned int	lword;

	i = 0;
	lword = 0;
	j = 0;
	while (s[i] != '\0')
	{
		while (s[i + lword] != c && s[i + lword] != '\0')
			lword++;
		if (lword > 0)
		{
			split[j] = ft_substr(s, i, lword);
			if (split[j] == NULL)
				return (ft_free_all(split, j));
			j++;
		}
		i = i + lword;
		lword = 0;
		if (s[i] != '\0')
			i++;
	}
	split[j] = 0;
	return (split);
}

char	**ft_split(char const *s, char c)
{
	unsigned int	i;
	char			**split;

	i = 0;
	if (s == NULL)
		return (NULL);
	split = ft_calloc(ft_count_words(s, c) + 1, sizeof(char *));
	if (split == NULL)
		return (NULL);
	split = ft_splitter(s, c, split);
	if (split == NULL)
		return (NULL);
	return (split);
}
