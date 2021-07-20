def tester_in_place(f, tests):
    # modify in place
    for x, y in tests:
        f(x)
        assert x == y, 'failled for x = {}, expected {}'.format(x, y)

# not needed here
def tester(f, tests):
    for x, y in tests:
        assert f(x) == y, 'failled for x = {}, expected {} but got {}'.format(x, y, f(x))


tests=[([1,2,3],[3,2,1]),([3],[3])]
tester_in_place(reverse_list, tests)
print('Passed')
