/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   heap_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber-- <nweber--@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/12 15:26:28 by nweber--          #+#    #+#             */
/*   Updated: 2026/10/21 14:33:11 by nweber--         ###   ########.fr       */
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
	if (heap->size == 1
		&& strcmp(request.coder->config->scheduler, "edf") == 0
		&& request.deadline < heap->requests[0].deadline)
	{
		heap->requests[1] = heap->requests[0];
		heap->requests[0] = request;
	}
	else
		heap->requests[heap->size] = request;
	heap->size++;
}

void	heap_add_request(t_coder *coder, t_request coder_request)
{
	pthread_mutex_lock(&coder->monitor->cond_mutex);
	pthread_mutex_lock(&coder->monitor->mutex);
	coder_request.deadline = coder->deadline;
	pthread_mutex_unlock(&coder->monitor->mutex);
	pthread_mutex_lock(&coder->actual_dongle->mutex);
	pthread_mutex_lock(&coder->previous_dongle->mutex);
	heap_add_back(&coder->actual_dongle->heap, coder_request);
	heap_add_back(&coder->previous_dongle->heap, coder_request);
	pthread_mutex_unlock(&coder->previous_dongle->mutex);
	pthread_mutex_unlock(&coder->actual_dongle->mutex);
	pthread_cond_broadcast(&coder->monitor->cond);
	pthread_mutex_unlock(&coder->monitor->cond_mutex);
}
