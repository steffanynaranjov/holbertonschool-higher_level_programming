#include <Python.h>
#include <stdio.h>
/**
* print_python_bytes - prints info about python lists
* @p: object
*
* Description: Prints python list
* Return: void
*/
void print_python_bytes(PyObject *p)
{
	size_t x, size, n;
	char *strng;

	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
        strng = ((PyBytesObject *)p)->ob_sval;
	n = size + 1 > 10 ? 10 : size + 1;

	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", strng);
	printf("  first %lu bytes: ", n);

	for (x = 0; x < n; x++)
		printf("%02hhx%s", strng[x], x + 1 < n ? " " : "");
	printf("\n");
}

/**
* print_python_list - prints info about python bytes type
* @p: object
*
* Description: Python bytes.
* Return: void
*/
void print_python_list(PyObject *p)
{
	int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < ((PyVarObject *)p)->ob_size; i++)
	{
		printf("Element %d: %s\n", i,
		       ((PyListObject *)p)->ob_item[i]->ob_type->tp_name);

		if (!strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[i]);

	}
}
