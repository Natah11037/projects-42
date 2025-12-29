/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cyakisan <cyakisan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 15:30:38 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/28 23:30:31 by cyakisan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	based_on_disorder(t_list **stack_a, t_list **stack_b,
		t_data *data)
{
	if (data->disorder < (double) 0.20)
		insertion_sort(stack_a, stack_b, data);
	else if (data->disorder < (double) 0.50)
		chunk_sort(stack_a, stack_b, data);
	else
		radix_sort(stack_a, stack_b, data);
}

static void	algorithm_execution(t_list **stack_a, t_list **stack_b,
		t_data *data)
{
	if (data->strat_selec == 1 || data->strat_selec == 11)
		insertion_sort(stack_a, stack_b, data);
	else if (data->strat_selec == 2 || data->strat_selec == 12)
		chunk_sort(stack_a, stack_b, data);
	else if (data->strat_selec == 3 || data->strat_selec == 13)
		radix_sort(stack_a, stack_b, data);
	else
		based_on_disorder(stack_a, stack_b, data);
	if (data->strat_selec >= 10)
		print_bench(data);
	else
		ft_printf("%s", data->ops);
	ft_lstclear(stack_a);
	free(data->ops);
}

void	push_swap(char **av, int strat_selec, int sing_or_mul)
{
	t_list	*stack_a;
	t_list	*stack_b;
	t_data	data;
	char	*ints;

	stack_a = NULL;
	stack_b = NULL;
	if (sing_or_mul)
		ints = ft_unsplit(av, strat_selec);
	else
		ints = av[ft_dstrlen(av)];
	stack_initializer(&stack_a, ft_split(ints, ' '), ints, sing_or_mul);
	dup_verif(&stack_a, ints, sing_or_mul);
	data_initializer(&data);
	list_normalizer(stack_a);
	data.disorder = extract_disorder(stack_a);
	data.strat_selec = strat_selec;
	if (data.disorder == 0)
	{
		ft_lstclear(&stack_a);
		exit (0);
	}
	algorithm_execution(&stack_a, &stack_b, &data);
	if (sing_or_mul)
		free(ints);
}
