/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: root <root@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/28 13:34:07 by root              #+#    #+#             */
/*   Updated: 2026/09/30 15:59:37 by root             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include "codexion.h"
#include "parser.h"
#include "error.h"


int main(int ac, char **av)
{
    t_config config;
    t_simulation simulation;

    if (ac != 9)
        return (print_error(ERROR_NB_ARGS, ac));
    if (parser(ac, av, &config) == 1)
        return (1);
    if (init_simulation(&config, &simulation) != 0)
        return (1);
    printf("Number of coders: %d\n", config.nb_coders);
    printf("Time to burnout: %ld\n", config.time_to_burnout);
    printf("Time to compile: %ld\n", config.time_to_compile);
    printf("Time to debug: %ld\n", config.time_to_debug);
    printf("Time to refactor: %ld\n", config.time_to_refactor);
    printf("Number of compiles required: %d\n", config.nb_compiles_required);
    printf("Dongle cooldown: %ld\n", config.dongle_cooldown);
    printf("Scheduler: %s\n", config.scheduler);
    destroy_simulation(&simulation);
    return (0);
}
