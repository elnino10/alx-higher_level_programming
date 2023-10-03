#include "lists.h"

/**
 * check_cycle - checks if list contains a cycle
 * @list: pointer to list
 *
 * Return:  0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;

	if (!list)
		return (0);
	if (fast->next && fast->next->next)
	{
		list = list->next;
		fast = fast->next->next;
		if (fast == list)
			return (1);
	}

	return (0);
}
