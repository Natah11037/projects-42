/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 16:10:16 by nweber--          #+#    #+#             */
/*   Updated: 2025/11/27 11:07:14 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

int	main(void)
{
	char	*str;
	int		fd;
	int		lines;

	lines = 0;
	fd = open("fichier.text", O_RDWR);
	while (lines++ < 10)
	{
		str = get_next_line(fd);
		printf("%s", str);
		free(str);
	}
}
