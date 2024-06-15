"""
syntax for importing and using a package and module


import package_name.module_name

variable_name = package_name.module_name.call()

"""

"""
import Functions.operations as op
print(op.add(10, 20)

"""

import Functions.operations

add = Functions.operations.add(40, 50)
print(add)
sub = Functions.operations.sub(20, 10)
print(sub)
multi = Functions.operations.mult(70, 2)
print(multi)
div = Functions.operations.div(20, 4)
print(div)

from Functions.operations import *

print(add(10, 66))
