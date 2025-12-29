/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/15 14:07:51 by cyakisan          #+#    #+#             */
/*   Updated: 2025/12/29 14:39:58 by nweber--         ###   ########.fr       */
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
	char	*ops;
}			t_data;

void		verif_strat_selec(int *strat_selec);
int			ft_strcmp(char *s1, char *s2);
long int	ft_long_atoi(const char *nptr, int *int_i);
size_t		ft_dstrlen(char	**dstr);
void		ft_freeall(char **splitted, int j);
void		print_error(void);
void		all_verifs(char **arguments, int ac, int *strat_selec,
				int *sing_or_mul);
int			pass_flags(int strat_selec, int s_o_m);
void		copying_in_single_string(char **arguments, char *unsplitted,
				unsigned int k, int strat_selec);
char		*ft_unsplit(char **arguments, int strat_selec);
void		stack_initializer(t_list **stack_a, char **ints,
				char *original_ints, int sing_or_mul);
void		clear_after_init(t_list **stack_a, char *ints, int sing_or_mul,
				bool from_disorder_zero);
void		clear_within_init(t_list **stack_a, char *original_ints,
				int sing_or_mul, char **splitted_ints);
void		dup_verif(t_list **stack_a, char *ints, int sing_or_mul);
void		data_initializer(t_data *data);
void		list_normalizer(t_list *stack);
int			search_for_max(t_list *stack);
size_t		max_placement(t_list *stack);
size_t		min_placement(t_list **stack);
size_t		search_placement(t_list *stack, size_t placement);
double		extract_disorder(t_list *stack_a);
void		push(t_list **stack_a, t_list **stack_b);
void		swap(t_list **stack);
void		swap_both(t_list **stack_a, t_list **stack_b);
void		rotate_stack(t_list **stack);
void		rotate_both(t_list **stack_a, t_list **stack_b);
void		reverse_rotate_both(t_list **stack_a, t_list **stack_b);
void		reverse_rotate_stack(t_list **stack);
char		*ft_strnjoin(char *s1, char const *s2, unsigned int keep_index);
void		print_bench(t_data *data);
void		insertion_sort(t_list **stack_a, t_list **stack_b,
				t_data *data);
void		chunk_sort(t_list **stack_a, t_list **stack_b,
				t_data *data);
void		radix_sort(t_list **stack_a, t_list **stack_b,
				t_data *data);
void		push_swap(char **av, int strat_selec, int sing_or_mul);

#endif 