def tester_in_place(f, tests):
    # modify in place
    for x, y in tests:
        f(x)
        assert x == y, 'failled for x = {}, expected {}'.format(x, y)


def tester(f, tests):
    for x, y in tests:
        assert f(x) == y, 'failled for x = {}, expected {} but got {}'.format(x, y, f(x))



tests = [([1,2,3,1,2,1],1),
         ([-3,2,4,5,3],-3),
        ([4,2,1,9,0], 0),
        ([-4],-4)
        ]

 

minimum = min
tester(minimum, tests)
print('Passed')
