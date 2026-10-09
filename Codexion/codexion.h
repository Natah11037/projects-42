/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/28 16:01:25 by root              #+#    #+#             */
/*   Updated: 2026/10/09 16:12:07 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef CODEXION_H
# define CODEXION_H
# include "parser.h"
# include <pthread.h>
# include "utils.h"
# include <stdint.h>

typedef struct s_request
{
	t_coder	*coder;
}	t_request;

typedef struct s_heap
{
	t_request	requests[2];
	int			size;
}	t_heap;

typedef struct s_dongle
{
	int				id;
	pthread_mutex_t	mutex;
	t_bool			is_used;
	t_heap			heap;
}	t_dongle;

typedef struct s_coder
{
	int				id;
	t_dongle		*actual_dongle;
	t_dongle		*previous_dongle;
	t_config		*config;
	pthread_t		thread;
	uint64_t		start_time;
	uint64_t		last_time_compile;
	uint64_t		deadline;
}	t_coder;

typedef struct s_simulation
{
	t_config		*config;
	t_coder			*coders;
	t_dongle		*dongles;
	int				initialized_dongles;
}	t_simulation;

int			init_simulation(t_config *config, t_simulation *simulation);
void		destroy_simulation(t_simulation *simulation);
void		*launch_coder_threads(void *arg);
int			init_thread(t_simulation simulation);
t_bool		launching_compil(t_coder *coder);
t_bool		launching_debug(t_coder *coder);
t_bool		launching_refactor(t_coder *coder);
uint64_t	now_ms(void);
void		init_time(t_simulation *simulation);

#endif
