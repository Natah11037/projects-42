/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: root <root@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/28 13:07:10 by root              #+#    #+#             */
/*   Updated: 2026/10/01 15:35:13 by root             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PARSER_H
#define PARSER_H
# include <stdint.h>
# include <string.h>

typedef struct s_config
{
    int nb_coders;
    uint64_t time_to_burnout;
    uint64_t time_to_compile;
    uint64_t time_to_debug;
    uint64_t time_to_refactor;
    int nb_compiles_required;
    uint64_t dongle_cooldown;
    char *scheduler;
    int created_threads;
} t_config;

int parser(int ac, char **av, t_config *config);

# endif
