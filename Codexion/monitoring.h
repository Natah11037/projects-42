/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   monitoring.h                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/16 11:32:35 by nweber--          #+#    #+#             */
/*   Updated: 2026/10/20 13:38:25 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef MONITORING_H
# define MONITORING_H
# include <pthread.h>
# include "utils.h"

typedef struct s_monitor
{
	pthread_t				monitor_thread;
	t_bool					stop;
	pthread_mutex_t			mutex;
	pthread_cond_t			cond;
	pthread_mutex_t			cond_mutex;
}	t_monitor;

#endif
