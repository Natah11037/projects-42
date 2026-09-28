/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: root <root@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/26 17:52:58 by root              #+#    #+#             */
/*   Updated: 2026/09/28 15:28:45 by root             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include "parser.h"
#include "error.h"


int verify_if_valid_int(char *str)
{
    int i;

    i = 0;

    while (str[i])
    {
        if (str[i] < '0' || str[i] > '9')
            return -1;
        i++;
    }
    return 0;
}

int convert_to_int(char *str)
{
    long result;
    int i;

    result = 0;
    i = 0;

    while (str[i])
    {
        result = result * 10 + (str[i] - '0');
        i++;
        if (result > 2147483647)
        {
            fprintf(stderr, "Error: Integer overflow for argument: %s\n", str);
            return -1;
        }
    }
    return (int)result;
}

void save_config(int value, int i, t_config *config)
{
    if (i == 1)
        config->nb_coders = value;
    else if (i == 2)
        config->time_to_burnout = value;
    else if (i == 3)
        config->time_to_compile = value;
    else if (i == 4)
        config->time_to_debug = value;
    else if (i == 5)
        config->time_to_refactor = value;
    else if (i == 6)
        config->nb_compiles_required = value;
    else if (i == 7)
        config->dongle_cooldown = value;
}

int parser(int ac, char **av, t_config *config)
{
    int i;
    int value;

    i = 1;
    value = 0;

    while (i < ac - 1)
    {
        if (verify_if_valid_int(av[i]) == -1)
            return (print_error(ERROR_INVALID_ARG, i));
        value = convert_to_int(av[i]);
        if (value == -1)
            return (1);
        save_config(value, i, config);
        i++;
    }
    if ((strcmp(av[i], "fifo") == 0) || (strcmp(av[i], "edf") == 0))
        config->scheduler = av[i];
    else
        return (print_error(ERROR_INVALID_SCHEDULER, i));
    return (0);
}
