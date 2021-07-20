def tester_in_place(f, tests):
    # modify in place
    for x, y in tests:
        f(x)
        assert x == y, 'failled for x = {}, expected {}'.format(x, y)


def tester(f, tests):
    for x, y in tests:
        assert f(x) == y, 'failled for x = {}, expected {} but got {}'.format(x, y, f(x))



tests = [(1,1),
         (5,120),
        (4,24),
        (9,362880),
         (14, 87178291200)         
        ]

 
 
tester(factorial, tests)
print('Passed')
