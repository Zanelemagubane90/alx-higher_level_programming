#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @a_list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *a_list)
{
	listint_t *trle, *hr;

	if (a_list == NULL || a_list->next == NULL)
		return (0);

	trle = a_list->next;
	hr = a_list->next->next;

	while (trle && hr && hr->next)
	{
		if (trle == hr)
			return (1);

		trle = trle->next;
		hr = hr->next->next;
	}

	return (0);
}
