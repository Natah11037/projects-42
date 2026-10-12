/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   heap_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/12 15:26:28 by nweber--          #+#    #+#             */
/*   Updated: 2026/10/12 15:52:40 by nweber--         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"
#include <unistd.h>

void	heap_pop(t_heap *heap)
{
	if (heap->size == 0)
		return ;
	if (heap->size == 2)
		heap->requests[0] = heap->requests[1];
	heap->size--;
}

void	heap_add_back(t_heap *heap, t_request request)
{
	if (heap->size == 2)
	{
		write(1, "allez ftg", 10);
		return ;
	}
	heap->requests[heap->size++] = request;
}
