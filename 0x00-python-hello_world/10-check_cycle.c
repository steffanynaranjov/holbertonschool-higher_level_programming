#include "lists.h"
/**
* check_cycle - checks if a singly linked list has a cycle in
*
* @list: single linked list
* Return: 0 or 1.
*/
int check_cycle(listint_t *list)
{
	listint_t *slow_p = list;
	listint_t *fast_p = list;

	while (slow_p && fast_p && fast_p->next)
{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;

			if (slow_p == fast_p)
			{
				return (1);
			}
	}
	/* Return 0 to indeciate that ther is no loop*/
	return (0);
}
