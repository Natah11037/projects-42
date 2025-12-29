/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing_utils_2.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/28 22:39:58 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/29 14:39:26 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	copying_in_single_string(char **arguments, char *unsplitted,
			unsigned int k, int strat_selec)
{
	unsigned int	i;
	unsigned int	j;
	unsigned int	l;

	i = pass_flags(strat_selec, 1);
	j = 0;
	l = 0;
	while (l < k)
	{
		while (arguments[i] && arguments[i][j] != '\0')
		{
			unsplitted[l] = arguments[i][j];
			++j;
			++l;
		}
		unsplitted[l] = ' ';
		++l;
		++i;
		j = 0;
	}
}

void	clear_after_init(t_list **stack_a, char *ints, int sing_or_mul,
	bool from_disorder_zero)
{
	ft_lstclear(stack_a);
	if (sing_or_mul)
		free(ints);
	if (!from_disorder_zero)
		print_error();
}

void	clear_within_init(t_list **stack_a, char *original_ints,
	int sing_or_mul, char **splitted_ints)
{
	if (*stack_a)
		ft_lstclear(stack_a);
	if (splitted_ints)
		ft_freeall(splitted_ints, ft_dstrlen(splitted_ints));
	if (sing_or_mul)
		free(original_ints);
	print_error();
}
