/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: root <root@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/28 16:01:25 by root              #+#    #+#             */
/*   Updated: 2026/09/28 16:38:42 by root             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef CODEXION_H
#define CODEXION_H
# include "parser.h"
# include <pthread.h>

typedef struct s_coder
{
    int         id;
    t_dongle    *first_dongle;
    t_dongle    *second_dongle;
    t_config    *config;
    pthread_t   thread;
} t_coder;

typedef struct s_dongle
{
    int                 id;
    pthread_mutex_t     mutex;
} t_dongle;

int test(int nb);

# endif
