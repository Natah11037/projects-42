/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/28 16:01:25 by root              #+#    #+#             */
/*   Updated: 2026/10/21 15:30:37 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef CODEXION_H
# define CODEXION_H
# include "parser.h"
# include <pthread.h>
# include "utils.h"
# include <stdint.h>
# include "monitoring.h"

typedef struct s_coder	t_coder;

typedef struct s_request
{
	t_coder		*coder;
	uint64_t	deadline;
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
	uint64_t		last_time_used;
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
	t_monitor		*monitor;
	pthread_mutex_t	*mutex_print;
}	t_coder;

typedef struct s_simulation
{
	t_config		*config;
	t_coder			*coders;
	t_dongle		*dongles;
	t_monitor		monitor;
	pthread_mutex_t	mutex_print;
	int				initialized_dongles;
	int				monitor_mutex_initialized;
	int				monitor_cond_initialized;
	int				monitor_cond_mutex_initialized;
	int				print_mutex_initialized;
	int				monitor_thread_created;
}	t_simulation;

int			init_simulation(t_config *config, t_simulation *simulation);
void		initialize_coders(t_simulation *simulation, int count);
void		destroy_simulation(t_simulation *simulation);
void		check_to_destroy_simulation(t_simulation *simulation);
void		*launch_coder_threads(void *arg);
int			init_thread(t_simulation *simulation);
void		heap_pop(t_heap *heap);
void		heap_add_back(t_heap *heap, t_request request);
void		heap_add_request(t_coder *coder, t_request coder_request);
t_bool		launching_compil(t_coder *coder);
t_bool		launching_debug(t_coder *coder);
t_bool		launching_refactor(t_coder *coder);
t_bool		coder_monitor_is_running(t_monitor *monitor);
t_bool		coder_deadline_expired(t_coder *coder);
uint64_t	now_ms(void);
void		init_time(t_simulation *simulation);
void		*surveillance(void *arg);
void		wait_for_dongle_cd(t_coder *coder);
t_bool		monitor_is_stopped(t_monitor *monitor);

#endif
