#include "lists.h"

/**
 * check_cycle - Checks for cycle in a singly linked list
 * @list: List to be to be checked
 * Return: Returns 0 if there is no cycle or 1 if a cycle exist and 0 on error
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	hare = list;
	tortoise = list;
	if (list == NULL)
		return (-1);
	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
