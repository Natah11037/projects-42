/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 15:30:38 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/23 13:07:35 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void print_list(t_list **stack_a)
{
	size_t len_stack_a;
	len_stack_a = ft_lstsize(*stack_a);
	while (len_stack_a > 0)
	{
		ft_printf("%d\n", (*stack_a)->content);
		(*stack_a) = (*stack_a)->next;
		len_stack_a--;
	}
}

// static void	algorithm_execution(t_list **stack_a, t_list **stack_b,
// 		t_data *data, char *ops)
// {
// 	if (data->strat_selec == 1 || data->strat_selec == 11)
// 		// ALGO SIMPLE
// 	// else if (data->strat_selec == 2 || data->strat_selec == 12)
// 	// 	// ALGO MEDIUM
// 	// else if (data->strat_selec == 3 || data->strat_selec == 13)
// 	// 	// ALGO COMPLEX
// 	// else
// 	// 	based_on_disorder();
// 	if (data->strat_selec >= 10)
// 		print_bench(data);
// 	// else
// 	// 	print_ops();
// }

void	push_swap(char **av, int strat_selec, int sing_or_mul)
{
	t_list	*stack_a;
	t_list	*stack_b; 
	t_data	data;
	char	*ops;

	stack_a = NULL;
	stack_b = NULL;
	ops = NULL;
	stack_initializer(&stack_a, av, strat_selec, sing_or_mul);
	data_initializer(&data);
	data.disorder = extract_disorder(stack_a);
	data.strat_selec = strat_selec;
	if (data.disorder == 0)
	{
		ft_lstclear(&stack_a);
		exit (0);
	}
	// algorithm_execution(&stack_a, &stack_b, &data, ops);
	reverse_rotate_stack(&stack_a);
	print_list(&stack_a);
	
	// ft_lstclear(&stack_a);
	// ft_lstclear(&stack_b);
	// free(ops);
}
