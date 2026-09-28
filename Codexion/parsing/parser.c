/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: root <root@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/26 17:52:58 by root              #+#    #+#             */
/*   Updated: 2026/09/28 03:17:22 by root             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>


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
    int result;
    int i;

    result = 0;
    i = 0;

    while (str[i])
    {
        result = result * 10 + (str[i] - '0');
        i++;
    }
    return result;
}

void parser(int ac, char **av)
{
    int i;
    int value;

    i = 1;
    value = 0;

    if (ac != 9)
    {
        fprintf(stderr, "Error: Invalid number of arguments.\n");
        return;
    }
    while (i < ac - 1)
    {
        if (verify_if_valid_int(av[i]) == -1)
        {
            fprintf(stderr, "Error: Invalid argument at position %d: %s\n", i, av[i]);
            return;
        }
        value = convert_to_int(av[i]);
        i++;
    }
}
