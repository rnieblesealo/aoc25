2025 advent of code

things that will help skill issues:

- READ THE GODDAMN PROBLEM
- python string/slicing tricks are ur homies
- writing a naive solution is fine
- flow control math (???)
- python list comprehension is useful
  e.g. 
    nums = [int(n) for n in str(line)] converts a number str. into its individual digits
- enumerate() is useful
  it creates an iterable of pairs out of a list, where the pair also contains each entry's index
  e.g.
    nums = [1, 2, 3] 
    enum = enumerate(nums) // returns [(0, 1), (1, 2), (2, 3)]
- don't analyze performance unless the solution works first
