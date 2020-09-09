#include "lists.h"
/**
* return_node - return last node of the list
* @head: head of the linked list
*
* Return: last node
*/
listint_t *return_node(listint_t *head)
{
	listint_t *tmp_node = head;
	void *prev = NULL;

	while (tmp_node)
	{
		tmp_node->prev = prev;
		prev = tmp_node;

		tmp_node = tmp_node->next;
	}

	tmp_node = head;

	while (tmp_node->next)
		tmp_node = tmp_node->next;

	return (tmp_node);
}

/**
* is_palindrome - checks if the linked list is a palindrome
* @head: head of the linked list
*
* Return: 0 or 1
*/
int is_palindrome(listint_t **head)
{
	listint_t *last = return_node(*head);
	listint_t *tmp_node = *head;

	while (tmp_node && last)
	{

		if (last->n != tmp_node->n)
			return (0);

		last = last->prev;
		tmp_node = tmp_node->next;
	}

	return (1);
}
