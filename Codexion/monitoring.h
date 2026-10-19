/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   monitoring.h                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/16 11:32:35 by nweber--          #+#    #+#             */
/*   Updated: 2026/10/16 13:04:15 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef MONITORING_H
# define MONITORING_H
# include <pthread.h>
# include "utils.h"

typedef struct s_monitor
{
	pthread_t		monitor_thread;
	t_bool			stop;
	pthread_mutex_t	mutex;
}	t_monitor;

#endif
