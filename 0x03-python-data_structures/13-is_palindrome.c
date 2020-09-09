#include "lists.h"
/**
* return_node - return last node of the list
* @head: head of the list
*
* Return: last node
*/
listint_t *return_node(listint_t *head)
{
	listint_t *tmp = head;
	void *prev = NULL;

	while (tmp)
	{
		tmp->prev = prev;
		prev = tmp;

		tmp = tmp->next;
	}

	tmp = head;

	while (tmp->next)
		tmp = tmp->next;

	return (tmp);
}

/**
* is_palindrome - checks if the linked list is a palindrome
* @head: head of the list
*
* Return: 0 or 1
*/
int is_palindrome(listint_t **head)
{
	listint_t *last = return_node(*head);
	listint_t *tmp = *head;

	while (tmp && last)
	{
		if (last->n != tmp->n)
			return (0);

		last = last->prev;
		tmp = tmp->next;
	}

	return (1);
}
