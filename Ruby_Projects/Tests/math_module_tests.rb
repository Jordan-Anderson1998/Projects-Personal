def fact_func_tests(num=7, expected_result=5040)

  user_func_result = factorial(num)

  assert_equal user_func_result.class, Integer
  assert_equal user_func_result, expected_result

  return 'Pass'
end
