import lambda_lab as ll

def test_function_builder():
	'''
	Test that items in function list
	are returning correct values
	'''
	the_list = ll.function_builder(4)
	assert the_list[0](2) == 2
	assert the_list[1](2) == 3