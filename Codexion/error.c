/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   error.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/28 14:48:19 by root              #+#    #+#             */
/*   Updated: 2026/10/05 14:09:14 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	print_error(char *message, int arg_position)
{
	fprintf(stderr, "%s: %d\n", message, arg_position);
	return (1);
}
