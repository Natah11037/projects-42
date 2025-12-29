/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 15:16:55 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/28 18:42:44 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	main(int ac, char **av)
{
	int	sing_or_mul;
	int	strat_selec;

	sing_or_mul = 0;
	strat_selec = 0;
	all_verifs(av, ac, &strat_selec, &sing_or_mul);
	push_swap(av, strat_selec, sing_or_mul);
	return (0);
}
