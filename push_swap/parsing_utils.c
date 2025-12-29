/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing_utils.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 13:59:01 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/28 23:31:29 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i] != '\0' || s2[i] != '\0')
	{
		if (s1[i] != s2[i])
		{
			return (s1[i] - s2[i]);
		}
		++i;
	}
	return (0);
}

long int	ft_long_atoi(const char *nptr, int *int_i)
{
	unsigned int	i;
	int				sign;
	long int		result;

	i = 0;
	sign = 1;
	result = 0;
	while ((nptr[i] <= 13 && nptr[i] >= 9) || nptr[i] == 32)
		++i;
	if (nptr[i] == '-' || nptr[i] == '+')
	{
		if (nptr[i] == '-')
			sign = sign * -1;
		++i;
	}
	while ((nptr[i] >= 48 && nptr[i] <= 57))
	{
		result = result * 10 + (nptr[i] - '0');
		++i;
	}
	*int_i += i;
	return (result * sign);
}

size_t	ft_dstrlen(char	**dstr)
{
	size_t	i;

	i = 0;
	while (dstr[i + 1])
		++i;
	return (i);
}

void	ft_freeall(char **splitted, int j)
{
	while (j >= 0)
	{
		free(splitted[j]);
		--j;
	}
	free(splitted);
}

char	*ft_unsplit(char **arguments, int strat_selec)
{
	char			*unsplitted;
	unsigned int	i;
	unsigned int	j;
	unsigned int	k;

	unsplitted = NULL;
	i = pass_flags(strat_selec, 1);
	j = 0;
	k = 0;
	while (arguments[i])
	{
		while (arguments[i][j] != '\0')
			++j;
		k += j;
		k++;
		++i;
		j = 0;
	}
	unsplitted = ft_calloc(k + 1, sizeof(char));
	if (!unsplitted)
		exit (1);
	copying_in_single_string(arguments, unsplitted, k, strat_selec);
	return (unsplitted);
}
