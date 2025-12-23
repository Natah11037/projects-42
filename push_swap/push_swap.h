/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/15 14:07:51 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/23 10:35:24 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# define INT_MAX 2147483647
# define INT_MIN -2147483648

# include "libft.h"
# include "ft_printf.h"

typedef struct s_data
{
	double	disorder;
	int		sa;
	int		sb;
	int		ss;
	int		pa;
	int		pb;
	int		ra;
	int		rb;
	int		rr;
	int		rra;
	int		rrb;
	int		rrr;
	int		strat_selec;
}			t_data;

void		verif_strat_selec(int *strat_selec);
int			ft_strcmp(char *s1, char *s2);
long int	ft_long_atoi(const char *nptr, int *int_i, int *sing_or_mul);
void		print_error(void);
int			single_int_verif(int *sing_or_mul, int *args_i, char **arguments);
int			dup_verif_sc(int int_i, char **arguments,
				long int result, int *sng_or_m);
int			integers_verif_sc(char **arguments, int *args_i, int *s_o_m);
int			all_verifs(char **arguments, int ac, int *strat_selec,
				int *sing_or_mul);
void		stack_initializer(t_list **stack_a, char **av, int stra_slc,
				int s_o_m);
void		data_initializer(t_data *data);
double		extract_disorder(t_list *stack_a);
void		push(t_list **stack_a, t_list **stack_b);
void		swap(t_list **stack);
void		swap_both(t_list **stack_a, t_list **stack_b);
void		rotate_stack(t_list **stack);
void		rotate_both(t_list **stack_a, t_list **stack_b);
void		reverse_rotate_both(t_list **stack_a, t_list **stack_b);
void		reverse_rotate_stack(t_list **stack);
void		push_swap(char **av, int strat_selec, int sing_or_mul);
void		print_bench(t_data *data);
void 		print_list(t_list **stack_a);

// METTRE TOUTES LES FONCTIONS EN STATIQUE
// NE PAS OUBLIER DE D'ENLEVER TOUTES LES MAINS ET FONCTIONS DE TESTS ET LES INCLUDES
#endif 