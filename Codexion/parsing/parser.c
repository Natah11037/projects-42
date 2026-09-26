/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: root <root@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/26 17:52:58 by root              #+#    #+#             */
/*   Updated: 2026/09/26 18:43:52 by root             ###   ########.fr       */
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

void parser(int ac, char **av)
{
    int i;

    i = 1;

    if (ac != 9)
    {
        fprintf(stderr, "Error: Invalid number of arguments.\n");
        return;
    }
    while (i < 8)
    {
        if (verify_if_valid_int(av[i]) == -1)
        {
            fprintf(stderr, "Error: Invalid argument at position %d: %s\n", i, av[i]);
            return;
        }
    }
}
