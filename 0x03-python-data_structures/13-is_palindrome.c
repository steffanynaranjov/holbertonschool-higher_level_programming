#include "lists.h"
/**
* is_palindrome - checks if the list of integers is palindrome
* @head: pointer to a pointer
*
* Return: 0 or 1
*/
int is_palindrome(listint_t **head)
{
	int buffer[12];
	listint_t *tmp_node = *head;
	int x, y, z;

	if (tmp_node == NULL)
		return (1);
	x = 0;
	while (tmp_node)
	{
		buffer[x] = tmp_node->n;
		tmp_node = tmp_node->next;
		x++;
	}
	z = (x + 1) / 2;
	x = x - 1;

	for (y = 0; y < z; y++, x--)
	{
		if (buffer[y] != buffer[x])
			return (0);
	}
	return (1);
}
