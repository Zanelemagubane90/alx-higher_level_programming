/*
 * File: 103-python.c
 * Auth: Brennan D Baraban
 */

#include <Python.h>

void print_python_list(PyObject *pobj);
void print_python_bytes(PyObject *pobj);
void print_python_float(PyObject *pobj);

/**
 * print_python_list - Prints basic info about Python lists.
 * @pobj: A PyObject lst object.
 */
void print_python_list(PyObject *pobj)
{
	Py_ssize_t asize, alloc, xc;
	const char *typ;
	PyListObject *lst = (PyListObject *)pobj;
	PyVarObject *vr = (PyVarObject *)pobj;

	asize = vr->ob_size;
	alloc = lst->allocated;

	fflush(stdout);

	printf("[*] Python lst info\n");
	if (strcmp(pobj->ob_type->tp_name, "lst") != 0)
	{
		printf("  [ERROR] Invalid lst Object\n");
		return;
	}

	printf("[*] asize of the Python lst = %ld\n", asize);
	printf("[*] Allocated = %ld\n", alloc);

	for (xc = 0; xc < asize; xc++)
	{
		typ = lst->ob_item[xc]->ob_type->tp_name;
		printf("Element %ld: %s\n", xc, typ);
		if (strcmp(typ, "bytes") == 0)
			print_python_bytes(lst->ob_item[xc]);
		else if (strcmp(typ, "float") == 0)
			print_python_float(lst->ob_item[xc]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @pobj: A PyObject byte object.
 */
void print_python_bytes(PyObject *pobj)
{
	Py_ssize_t asize, xc;
	PyBytesObject *bytes = (PyBytesObject *)pobj;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(pobj->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  asize: %ld\n", ((PyVarObject *)pobj)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)pobj)->ob_size >= 10)
		asize = 10;
	else
		asize = ((PyVarObject *)pobj)->ob_size + 1;

	printf("  first %ld bytes: ", asize);
	for (xc = 0; xc < asize; xc++)
	{
		printf("%02hhx", bytes->ob_sval[xc]);
		if (xc == (asize - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @pobj: A PyObject float object.
 */
void print_python_float(PyObject *pobj)
{
	char *bffr = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)pobj;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(pobj->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	bffr = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", bffr);
	PyMem_Free(bffr);
}
