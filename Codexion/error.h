/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   error.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/28 15:20:28 by root              #+#    #+#             */
/*   Updated: 2026/10/05 14:09:14 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef ERROR_H
# define ERROR_H
# include <stdio.h>

# define ERROR_NB_ARGS "Error: Invalid number of arguments."
# define ERROR_INVALID_ARG "Error: Invalid argument at position"
# define ERROR_INVALID_SCHEDULER "Error: Invalid scheduler argument"
# define ERROR_OVERFLOW "Error: Integer overflow for argument"

int	print_error(char *message, int arg_position);

#endif
