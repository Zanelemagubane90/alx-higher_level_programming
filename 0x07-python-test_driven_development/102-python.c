#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p_object: A PyObject string object.
 */
void print_python_string(PyObject *p_object)
{
	long int a_len;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p_object->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	a_len = ((PyASCIIObject *)(p_object))->a_len;

	if (PyUnicode_IS_COMPACT_ASCII(p_object))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  a_len: %ld\n", a_len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p_object, &a_len));
}
