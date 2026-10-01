/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: root <root@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/28 16:01:25 by root              #+#    #+#             */
/*   Updated: 2026/10/01 14:55:53 by root             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef CODEXION_H
#define CODEXION_H
# include "parser.h"
# include <pthread.h>

typedef struct s_dongle
{
    int                 id;
    pthread_mutex_t     mutex;
} t_dongle;

typedef struct s_coder
{
    int             id;
    t_dongle       *actual_dongle;
    t_dongle       *previous_dongle;
    t_config       *config;
    pthread_t       thread;
} t_coder;

typedef struct s_simulation
{
    t_config       *config;
    t_coder        *coders;
    t_dongle       *dongles;
    int             initialized_dongles;
} t_simulation;

int init_simulation(t_config *config, t_simulation *simulation);
void destroy_simulation(t_simulation *simulation);
void *test(void *arg);
int init_thread(t_simulation simulation);

# endif
