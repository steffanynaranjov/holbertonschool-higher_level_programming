#include "lists.h"
/**
* insert_node - insert a node
* @head: pointer to pointer of first node of listint_t list
* @number: integer to be included in new node
* Return: the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *tmp_node = *head;

	if (!new_node)
		return (NULL);
	new_node->n = number;

	if (!tmp_node || tmp_node->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}
	while (tmp_node && tmp_node->next && tmp_node->next->n < number)
		tmp_node = tmp_node->next;
	new_node->next = tmp_node->next;
	tmp_node->next = new_node;
	if (!tmp_node->next)
		new_node->next = NULL;
	if (new_node == NULL)
	{
		free(new_node);
		return (NULL);
	}
	return (new_node);
}
