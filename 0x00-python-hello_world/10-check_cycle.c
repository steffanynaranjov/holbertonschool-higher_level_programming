#include "lists.h"
/**
* check_cycle - checks if a singly linked list has a cycle in
*
* @list: single linked list
* Return: 0 or 1.
*/
int check_cycle(listint_t *list)
{
	listint_t *tmp = list;
	listint_t *node = list;

	while (tmp && node && node->next)
{
		tmp = tmp->next;
		node = node->next->next;

			if (tmp == node)
			{
				return (1);
			}
	}
	/* Return 0 to indeciate that ther is no loop*/
	return (0);
}
