# Arrays

An array can hold several values under one name. Array naming is the same as variables naming. An array is initialized by assign space-delimited values enclosed in ()

`my_array=(apple banana "Fruit Basket" orange)`
`new_array[2]=apricot`
`echo ${my_array[@]} # This will print the list itself (apple banana "Fruit Basket" orange)`

Array members need not be consecutive or contiguous. Some members of the array can be left uninitialized.

**The total number of elements in the array is referenced by `${#arrayname[@]}`**
**The elements in the array are printed by `${arrayname[@]}`**

`my_array=(apple banana "Fruit Basket" orange)`
`echo  ${#my_array[@]}                   # 4`

The array elements can be accessed with their numeric index. The index of the first element is 0.

`my_array=(apple banana "Fruit Basket" orange)`
`echo ${my_array[3]}                     # orange - note that curly brackets are needed`
`# adding another array element`
`my_array[4]="carrot"                    # value assignment without a $ and curly brackets`
`echo ${#my_array[@]}                    # 5`
`echo ${my_array[${#my_array[@]}-1]}     # carrot`

# Arrays - Comparison of Arrays

An array is a variable containing multiple values. Any variable may be used as an array. There is no maximum limit to the size of an array, nor any requirement that member variables be indexed or assigned contiguously. Arrays are zero-based: the first element is indexed with the number 0.

`# basic construct`
`# array=(value1 value2 ... valueN)`
`array=(23 45 34 1 2 3)`
`# To refer to a particular value (e.g. : to refer 3rd value)`
`echo ${array[2]}`

`# To refer to all the array values`
`echo ${array[@]}`

`# To evaluate the number of elements in an array`
`echo ${#array[@]}`