줄리아 도움말 문서
======================
생성일: 2024-11-29T03:16:27.543




복근:
==================================================

```
복근(x)
```

'x'의 절대값입니다.

부호가 있는 정수에 'abs'를 적용하면 오버플로가 발생하여 음수 값이 반환될 수 있습니다. 이 오버플로는 부호가 있는 정수의 최소 표현 가능한 값에 'abs'를 적용할 때만 발생합니다. 즉, 예상대로 '-x'가 아닌 'x == typemin((x의 종류)', 'abs(x) == x < 0'일 때입니다.

또한 참조하십시오: ['abs2'](@ref), ['unsign'](@ref), ['sign'(@ref).

# 예

"'Jldoctest'
줄리아> 복근 (-3)
3

줄리아> 복근(1 + Im)
1.4142135623730951

줄리아> 복근.(Int8[-128-127 -126 0 126 127] # typemin에서 오버플로 (Int8)
1×6 매트릭스{Int8]:
 -128  127  126  0  126  127

줄리아> 최대값(abs, [1, -2, 3, -4])
4
```



복근2:
==================================================

```
abs2(x)
```

절대값 'x'의 제곱.

이는 'abs(x)^2'보다 빠를 수 있으며, 특히 'abs(x)'가 ['hypot'](@ref)를 통해 제곱근이 필요한 복소수의 경우 더욱 그렇습니다.

['abs'](@ref), ['conj'(@ref), ['real'](@ref)도 참조하세요.

# 예

"'Jldoctest'
줄리아> 복근2 (-3)
9

julia> abs2(3.0 + 4.0im)
25.0

julia> sum(abs2, [1+2im, 3+4im])  # 선형대수.norm(x)^2
30
```



abspath:
==================================================

```
abspath(path::AbstractString) -> String
```

Convert a path to an absolute path by adding the current directory if necessary. Also normalizes the path as in [`normpath`](@ref).

# Examples

If you are in a directory called `JuliaExample` and the data you are using is two levels up relative to the `JuliaExample` directory, you could write:

```
abspath("../../data")
```

Which gives a path like `"/home/JuliaUser/data/"`.

See also [`joinpath`](@ref), [`pwd`](@ref), [`expanduser`](@ref).

```
abspath(path::AbstractString, paths::AbstractString...) -> String
```

Convert a set of paths to an absolute path by joining them together and adding the current directory if necessary. Equivalent to `abspath(joinpath(path, paths...))`.



accumulate:
==================================================

```
accumulate(op, A; dims::Integer, [init])
```

Cumulative operation `op` along the dimension `dims` of `A` (providing `dims` is optional for vectors). An initial value `init` may optionally be provided by a keyword argument. See also [`accumulate!`](@ref) to use a preallocated output array, both for performance and to control the precision of the output (e.g. to avoid overflow).

For common operations there are specialized variants of `accumulate`, see [`cumsum`](@ref), [`cumprod`](@ref). For a lazy version, see [`Iterators.accumulate`](@ref).

!!! compat "Julia 1.5"
    `accumulate` on a non-array iterator requires at least Julia 1.5.


# Examples

```jldoctest
julia> accumulate(+, [1,2,3])
3-element Vector{Int64}:
 1
 3
 6

julia> accumulate(min, (1, -2, 3, -4, 5), init=0)
(0, -2, -2, -4, -4)

julia> accumulate(/, (2, 4, Inf), init=100)
(50.0, 12.5, 0.0)

julia> accumulate(=>, i^2 for i in 1:3)
3-element Vector{Any}:
          1
        1 => 4
 (1 => 4) => 9

julia> accumulate(+, fill(1, 3, 4))
3×4 Matrix{Int64}:
 1  4  7  10
 2  5  8  11
 3  6  9  12

julia> accumulate(+, fill(1, 2, 5), dims=2, init=100.0)
2×5 Matrix{Float64}:
 101.0  102.0  103.0  104.0  105.0
 101.0  102.0  103.0  104.0  105.0
```



accumulate!:
==================================================

```
accumulate!(op, B, A; [dims], [init])
```

Cumulative operation `op` on `A` along the dimension `dims`, storing the result in `B`. Providing `dims` is optional for vectors.  If the keyword argument `init` is given, its value is used to instantiate the accumulation.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


See also [`accumulate`](@ref), [`cumsum!`](@ref), [`cumprod!`](@ref).

# Examples

```jldoctest
julia> x = [1, 0, 2, 0, 3];

julia> y = rand(5);

julia> accumulate!(+, y, x);

julia> y
5-element Vector{Float64}:
 1.0
 1.0
 3.0
 3.0
 6.0

julia> A = [1 2 3; 4 5 6];

julia> B = similar(A);

julia> accumulate!(-, B, A, dims=1)
2×3 Matrix{Int64}:
  1   2   3
 -3  -3  -3

julia> accumulate!(*, B, A, dims=2, init=10)
2×3 Matrix{Int64}:
 10   20    60
 40  200  1200
```



acos:
==================================================

```
acos(x)
```

Compute the inverse cosine of `x`, where the output is in radians

```
acos(A::AbstractMatrix)
```

Compute the inverse matrix cosine of a square matrix `A`.

If `A` is symmetric or Hermitian, its eigendecomposition ([`eigen`](@ref)) is used to compute the inverse cosine. Otherwise, the inverse cosine is determined by using [`log`](@ref) and [`sqrt`](@ref).  For the theory and logarithmic formulas used to compute this function, see [^AH16_1].

[^AH16_1]: Mary Aprahamian and Nicholas J. Higham, "Matrix Inverse Trigonometric and Inverse Hyperbolic Functions: Theory and Algorithms", MIMS EPrint: 2016.4. [https://doi.org/10.1137/16M1057577](https://doi.org/10.1137/16M1057577)

# Examples

```julia-repl
julia> acos(cos([0.5 0.1; -0.2 0.3]))
2×2 Matrix{ComplexF64}:
  0.5-8.32667e-17im  0.1+0.0im
 -0.2+2.63678e-16im  0.3-3.46945e-16im
```



acosd:
==================================================

```
acosd(x)
```

Compute the inverse cosine of `x`, where the output is in degrees. If `x` is a matrix, `x` needs to be a square matrix.

!!! compat "Julia 1.7"
    Matrix arguments require Julia 1.7 or later.




acosh:
==================================================

```
acosh(x)
```

Compute the inverse hyperbolic cosine of `x`.

```
acosh(A::AbstractMatrix)
```

Compute the inverse hyperbolic matrix cosine of a square matrix `A`.  For the theory and logarithmic formulas used to compute this function, see [^AH16_4].

[^AH16_4]: Mary Aprahamian and Nicholas J. Higham, "Matrix Inverse Trigonometric and Inverse Hyperbolic Functions: Theory and Algorithms", MIMS EPrint: 2016.4. [https://doi.org/10.1137/16M1057577](https://doi.org/10.1137/16M1057577)



acot:
==================================================

```
acot(x)
```

Compute the inverse cotangent of `x`, where the output is in radians. 

```
acot(A::AbstractMatrix)
```

Compute the inverse matrix cotangent of `A`. 



acotd:
==================================================

```
acotd(x)
```

Compute the inverse cotangent of `x`, where the output is in degrees. If `x` is a matrix, `x` needs to be a square matrix.

!!! compat "Julia 1.7"
    Matrix arguments require Julia 1.7 or later.




acoth:
==================================================

```
acoth(x)
```

Compute the inverse hyperbolic cotangent of `x`. 

```
acoth(A::AbstractMatrix)
```

Compute the inverse matrix hyperbolic cotangent of `A`. 



acsc:
==================================================

```
acsc(x)
```

Compute the inverse cosecant of `x`, where the output is in radians. 

```
acsc(A::AbstractMatrix)
```

Compute the inverse matrix cosecant of `A`. 



acscd:
==================================================

```
acscd(x)
```

Compute the inverse cosecant of `x`, where the output is in degrees. If `x` is a matrix, `x` needs to be a square matrix.

!!! compat "Julia 1.7"
    Matrix arguments require Julia 1.7 or later.




acsch:
==================================================

```
acsch(x)
```

Compute the inverse hyperbolic cosecant of `x`. 

```
acsch(A::AbstractMatrix)
```

Compute the inverse matrix hyperbolic cosecant of `A`. 



addenv:
==================================================

```
addenv(command::Cmd, env...; inherit::Bool = true)
```

Merge new environment mappings into the given [`Cmd`](@ref) object, returning a new `Cmd` object. Duplicate keys are replaced.  If `command` does not contain any environment values set already, it inherits the current environment at time of `addenv()` call if `inherit` is `true`. Keys with value `nothing` are deleted from the env.

See also [`Cmd`](@ref), [`setenv`](@ref), [`ENV`](@ref).

!!! compat "Julia 1.6"
    This function requires Julia 1.6 or later.




adjoint:
==================================================

```
A'
adjoint(A)
```

Lazy adjoint (conjugate transposition). Note that `adjoint` is applied recursively to elements.

For number types, `adjoint` returns the complex conjugate, and therefore it is equivalent to the identity function for real numbers.

This operation is intended for linear algebra usage - for general data manipulation see [`permutedims`](@ref Base.permutedims).

# Examples

```jldoctest
julia> A = [3+2im 9+2im; 0  0]
2×2 Matrix{Complex{Int64}}:
 3+2im  9+2im
 0+0im  0+0im

julia> B = A' # equivalently adjoint(A)
2×2 adjoint(::Matrix{Complex{Int64}}) with eltype Complex{Int64}:
 3-2im  0+0im
 9-2im  0+0im

julia> B isa Adjoint
true

julia> adjoint(B) === A # the adjoint of an adjoint unwraps the parent
true

julia> Adjoint(B) # however, the constructor always wraps its argument
2×2 adjoint(adjoint(::Matrix{Complex{Int64}})) with eltype Complex{Int64}:
 3+2im  9+2im
 0+0im  0+0im

julia> B[1,2] = 4 + 5im; # modifying B will modify A automatically

julia> A
2×2 Matrix{Complex{Int64}}:
 3+2im  9+2im
 4-5im  0+0im
```

For real matrices, the `adjoint` operation is equivalent to a `transpose`.

```jldoctest
julia> A = reshape([x for x in 1:4], 2, 2)
2×2 Matrix{Int64}:
 1  3
 2  4

julia> A'
2×2 adjoint(::Matrix{Int64}) with eltype Int64:
 1  2
 3  4

julia> adjoint(A) == transpose(A)
true
```

The adjoint of an `AbstractVector` is a row-vector:

```jldoctest
julia> x = [3, 4im]
2-element Vector{Complex{Int64}}:
 3 + 0im
 0 + 4im

julia> x'
1×2 adjoint(::Vector{Complex{Int64}}) with eltype Complex{Int64}:
 3+0im  0-4im

julia> x'x # compute the dot product, equivalently x' * x
25 + 0im
```

For a matrix of matrices, the individual blocks are recursively operated on:

```jldoctest
julia> A = reshape([x + im*x for x in 1:4], 2, 2)
2×2 Matrix{Complex{Int64}}:
 1+1im  3+3im
 2+2im  4+4im

julia> C = reshape([A, 2A, 3A, 4A], 2, 2)
2×2 Matrix{Matrix{Complex{Int64}}}:
 [1+1im 3+3im; 2+2im 4+4im]  [3+3im 9+9im; 6+6im 12+12im]
 [2+2im 6+6im; 4+4im 8+8im]  [4+4im 12+12im; 8+8im 16+16im]

julia> C'
2×2 adjoint(::Matrix{Matrix{Complex{Int64}}}) with eltype Adjoint{Complex{Int64}, Matrix{Complex{Int64}}}:
 [1-1im 2-2im; 3-3im 4-4im]    [2-2im 4-4im; 6-6im 8-8im]
 [3-3im 6-6im; 9-9im 12-12im]  [4-4im 8-8im; 12-12im 16-16im]
```

```
adjoint(F::Factorization)
```

Lazy adjoint of the factorization `F`. By default, returns an [`AdjointFactorization`](@ref) wrapper.



all:
==================================================

```
all(itr) -> Bool
```

Test whether all elements of a boolean collection are `true`, returning `false` as soon as the first `false` value in `itr` is encountered (short-circuiting). To short-circuit on `true`, use [`any`](@ref).

If the input contains [`missing`](@ref) values, return `missing` if all non-missing values are `true` (or equivalently, if the input contains no `false` value), following [three-valued logic](https://en.wikipedia.org/wiki/Three-valued_logic).

See also: [`all!`](@ref), [`any`](@ref), [`count`](@ref), [`&`](@ref), , [`&&`](@ref), [`allunique`](@ref).

# Examples

```jldoctest
julia> a = [true,false,false,true]
4-element Vector{Bool}:
 1
 0
 0
 1

julia> all(a)
false

julia> all((println(i); v) for (i, v) in enumerate(a))
1
2
false

julia> all([missing, false])
false

julia> all([true, missing])
missing
```

```
all(p, itr) -> Bool
```

Determine whether predicate `p` returns `true` for all elements of `itr`, returning `false` as soon as the first item in `itr` for which `p` returns `false` is encountered (short-circuiting). To short-circuit on `true`, use [`any`](@ref).

If the input contains [`missing`](@ref) values, return `missing` if all non-missing values are `true` (or equivalently, if the input contains no `false` value), following [three-valued logic](https://en.wikipedia.org/wiki/Three-valued_logic).

# Examples

```jldoctest
julia> all(i->(4<=i<=6), [4,5,6])
true

julia> all(i -> (println(i); i < 3), 1:10)
1
2
3
false

julia> all(i -> i > 0, [1, missing])
missing

julia> all(i -> i > 0, [-1, missing])
false

julia> all(i -> i > 0, [1, 2])
true
```

```
all(A; dims)
```

Test whether all values along the given dimensions of an array are `true`.

# Examples

```jldoctest
julia> A = [true false; true true]
2×2 Matrix{Bool}:
 1  0
 1  1

julia> all(A, dims=1)
1×2 Matrix{Bool}:
 1  0

julia> all(A, dims=2)
2×1 Matrix{Bool}:
 0
 1
```

```
all(p, A; dims)
```

Determine whether predicate `p` returns `true` for all elements along the given dimensions of an array.

# Examples

```jldoctest
julia> A = [1 -1; 2 2]
2×2 Matrix{Int64}:
 1  -1
 2   2

julia> all(i -> i > 0, A, dims=1)
1×2 Matrix{Bool}:
 1  0

julia> all(i -> i > 0, A, dims=2)
2×1 Matrix{Bool}:
 0
 1
```



all!:
==================================================

```
all!(r, A)
```

Test whether all values in `A` along the singleton dimensions of `r` are `true`, and write results to `r`.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


# Examples

```jldoctest
julia> A = [true false; true false]
2×2 Matrix{Bool}:
 1  0
 1  0

julia> all!([1; 1], A)
2-element Vector{Int64}:
 0
 0

julia> all!([1 1], A)
1×2 Matrix{Int64}:
 1  0
```



allequal:
==================================================

```
allequal(itr) -> Bool
allequal(f, itr) -> Bool
```

Return `true` if all values from `itr` are equal when compared with [`isequal`](@ref). Or if all of `[f(x) for x in itr]` are equal, for the second method.

Note that `allequal(f, itr)` may call `f` fewer than `length(itr)` times. The precise number of calls is regarded as an implementation detail.

See also: [`unique`](@ref), [`allunique`](@ref).

!!! compat "Julia 1.8"
    The `allequal` function requires at least Julia 1.8.


!!! compat "Julia 1.11"
    The method `allequal(f, itr)` requires at least Julia 1.11.


# Examples

```jldoctest
julia> allequal([])
true

julia> allequal([1])
true

julia> allequal([1, 1])
true

julia> allequal([1, 2])
false

julia> allequal(Dict(:a => 1, :b => 1))
false

julia> allequal(abs2, [1, -1])
true
```



allunique:
==================================================

```
allunique(itr) -> Bool
allunique(f, itr) -> Bool
```

Return `true` if all values from `itr` are distinct when compared with [`isequal`](@ref). Or if all of `[f(x) for x in itr]` are distinct, for the second method.

Note that `allunique(f, itr)` may call `f` fewer than `length(itr)` times. The precise number of calls is regarded as an implementation detail.

`allunique` may use a specialized implementation when the input is sorted.

See also: [`unique`](@ref), [`issorted`](@ref), [`allequal`](@ref).

!!! compat "Julia 1.11"
    The method `allunique(f, itr)` requires at least Julia 1.11.


# Examples

```jldoctest
julia> allunique([1, 2, 3])
true

julia> allunique([1, 2, 1, 2])
false

julia> allunique(Real[1, 1.0, 2])
false

julia> allunique([NaN, 2.0, NaN, 4.0])
false

julia> allunique(abs, [1, -1, 2])
false
```



angle:
==================================================

```
angle(z)
```

Compute the phase angle in radians of a complex number `z`.

Returns a number `-pi ≤ angle(z) ≤ pi`, and is thus discontinuous along the negative real axis.

See also: [`atan`](@ref), [`cis`](@ref), [`rad2deg`](@ref).

# Examples

```jldoctest
julia> rad2deg(angle(1 + im))
45.0

julia> rad2deg(angle(1 - im))
-45.0

julia> rad2deg(angle(-1 + 1e-20im))
180.0

julia> rad2deg(angle(-1 - 1e-20im))
-180.0
```



ans:
==================================================

```
Nothing
```

A type with no fields that is the type of [`nothing`](@ref).

See also: [`isnothing`](@ref), [`Some`](@ref), [`Missing`](@ref).



any:
==================================================

```
any(itr) -> Bool
```

Test whether any elements of a boolean collection are `true`, returning `true` as soon as the first `true` value in `itr` is encountered (short-circuiting). To short-circuit on `false`, use [`all`](@ref).

If the input contains [`missing`](@ref) values, return `missing` if all non-missing values are `false` (or equivalently, if the input contains no `true` value), following [three-valued logic](https://en.wikipedia.org/wiki/Three-valued_logic).

See also: [`all`](@ref), [`count`](@ref), [`sum`](@ref), [`|`](@ref), , [`||`](@ref).

# Examples

```jldoctest
julia> a = [true,false,false,true]
4-element Vector{Bool}:
 1
 0
 0
 1

julia> any(a)
true

julia> any((println(i); v) for (i, v) in enumerate(a))
1
true

julia> any([missing, true])
true

julia> any([false, missing])
missing
```

```
any(p, itr) -> Bool
```

Determine whether predicate `p` returns `true` for any elements of `itr`, returning `true` as soon as the first item in `itr` for which `p` returns `true` is encountered (short-circuiting). To short-circuit on `false`, use [`all`](@ref).

If the input contains [`missing`](@ref) values, return `missing` if all non-missing values are `false` (or equivalently, if the input contains no `true` value), following [three-valued logic](https://en.wikipedia.org/wiki/Three-valued_logic).

# Examples

```jldoctest
julia> any(i->(4<=i<=6), [3,5,7])
true

julia> any(i -> (println(i); i > 3), 1:10)
1
2
3
4
true

julia> any(i -> i > 0, [1, missing])
true

julia> any(i -> i > 0, [-1, missing])
missing

julia> any(i -> i > 0, [-1, 0])
false
```

```
any(A; dims)
```

Test whether any values along the given dimensions of an array are `true`.

# Examples

```jldoctest
julia> A = [true false; true false]
2×2 Matrix{Bool}:
 1  0
 1  0

julia> any(A, dims=1)
1×2 Matrix{Bool}:
 1  0

julia> any(A, dims=2)
2×1 Matrix{Bool}:
 1
 1
```

```
any(p, A; dims)
```

Determine whether predicate `p` returns `true` for any elements along the given dimensions of an array.

# Examples

```jldoctest
julia> A = [1 -1; 2 -2]
2×2 Matrix{Int64}:
 1  -1
 2  -2

julia> any(i -> i > 0, A, dims=1)
1×2 Matrix{Bool}:
 1  0

julia> any(i -> i > 0, A, dims=2)
2×1 Matrix{Bool}:
 1
 1
```



any!:
==================================================

```
any!(r, A)
```

Test whether any values in `A` along the singleton dimensions of `r` are `true`, and write results to `r`.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


# Examples

```jldoctest
julia> A = [true false; true false]
2×2 Matrix{Bool}:
 1  0
 1  0

julia> any!([1; 1], A)
2-element Vector{Int64}:
 1
 1

julia> any!([1 1], A)
1×2 Matrix{Int64}:
 1  0
```



append!:
==================================================

```
append!(collection, collections...) -> collection.
```

For an ordered container `collection`, add the elements of each `collections` to the end of it.

!!! compat "Julia 1.6"
    Specifying multiple collections to be appended requires at least Julia 1.6.


# Examples

```jldoctest
julia> append!([1], [2, 3])
3-element Vector{Int64}:
 1
 2
 3

julia> append!([1, 2, 3], [4, 5], [6])
6-element Vector{Int64}:
 1
 2
 3
 4
 5
 6
```

Use [`push!`](@ref) to add individual items to `collection` which are not already themselves in another collection. The result of the preceding example is equivalent to `push!([1, 2, 3], 4, 5, 6)`.

See [`sizehint!`](@ref) for notes about the performance model.

See also [`vcat`](@ref) for vectors, [`union!`](@ref) for sets, and [`prepend!`](@ref) and [`pushfirst!`](@ref) for the opposite order.



applicable:
==================================================

```
applicable(f, args...) -> Bool
```

Determine whether the given generic function has a method applicable to the given arguments.

See also [`hasmethod`](@ref).

# Examples

```jldoctest
julia> function f(x, y)
           x + y
       end;

julia> applicable(f, 1)
false

julia> applicable(f, 1, 2)
true
```



apropos:
==================================================

```
apropos([io::IO=stdout], pattern::Union{AbstractString,Regex})
```

Search available docstrings for entries containing `pattern`.

When `pattern` is a string, case is ignored. Results are printed to `io`.

`apropos` can be called from the help mode in the REPL by wrapping the query in double quotes:

```
help?> "pattern"
```



argmax:
==================================================

```
argmax(r::AbstractRange)
```

Ranges can have multiple maximal elements. In that case `argmax` will return a maximal index, but not necessarily the first one.

```
argmax(f, domain)
```

Return a value `x` from `domain` for which `f(x)` is maximised. If there are multiple maximal values for `f(x)` then the first one will be found.

`domain` must be a non-empty iterable.

Values are compared with `isless`.

!!! compat "Julia 1.7"
    This method requires Julia 1.7 or later.


See also [`argmin`](@ref), [`findmax`](@ref).

# Examples

```jldoctest
julia> argmax(abs, -10:5)
-10

julia> argmax(cos, 0:π/2:2π)
0.0
```

```
argmax(itr)
```

Return the index or key of the maximal element in a collection. If there are multiple maximal elements, then the first one will be returned.

The collection must not be empty.

Indices are of the same type as those returned by [`keys(itr)`](@ref) and [`pairs(itr)`](@ref).

Values are compared with `isless`.

See also: [`argmin`](@ref), [`findmax`](@ref).

# Examples

```jldoctest
julia> argmax([8, 0.1, -9, pi])
1

julia> argmax([1, 7, 7, 6])
2

julia> argmax([1, 7, 7, NaN])
4
```

```
argmax(A; dims) -> indices
```

For an array input, return the indices of the maximum elements over the given dimensions. `NaN` is treated as greater than all other values except `missing`.

# Examples

```jldoctest
julia> A = [1.0 2; 3 4]
2×2 Matrix{Float64}:
 1.0  2.0
 3.0  4.0

julia> argmax(A, dims=1)
1×2 Matrix{CartesianIndex{2}}:
 CartesianIndex(2, 1)  CartesianIndex(2, 2)

julia> argmax(A, dims=2)
2×1 Matrix{CartesianIndex{2}}:
 CartesianIndex(1, 2)
 CartesianIndex(2, 2)
```



argmin:
==================================================

```
argmin(r::AbstractRange)
```

Ranges can have multiple minimal elements. In that case `argmin` will return a minimal index, but not necessarily the first one.

```
argmin(f, domain)
```

Return a value `x` from `domain` for which `f(x)` is minimised. If there are multiple minimal values for `f(x)` then the first one will be found.

`domain` must be a non-empty iterable.

`NaN` is treated as less than all other values except `missing`.

!!! compat "Julia 1.7"
    This method requires Julia 1.7 or later.


See also [`argmax`](@ref), [`findmin`](@ref).

# Examples

```jldoctest
julia> argmin(sign, -10:5)
-10

julia> argmin(x -> -x^3 + x^2 - 10, -5:5)
5

julia> argmin(acos, 0:0.1:1)
1.0
```

```
argmin(itr)
```

Return the index or key of the minimal element in a collection. If there are multiple minimal elements, then the first one will be returned.

The collection must not be empty.

Indices are of the same type as those returned by [`keys(itr)`](@ref) and [`pairs(itr)`](@ref).

`NaN` is treated as less than all other values except `missing`.

See also: [`argmax`](@ref), [`findmin`](@ref).

# Examples

```jldoctest
julia> argmin([8, 0.1, -9, pi])
3

julia> argmin([7, 1, 1, 6])
2

julia> argmin([7, 1, 1, NaN])
4
```

```
argmin(A; dims) -> indices
```

For an array input, return the indices of the minimum elements over the given dimensions. `NaN` is treated as less than all other values except `missing`.

# Examples

```jldoctest
julia> A = [1.0 2; 3 4]
2×2 Matrix{Float64}:
 1.0  2.0
 3.0  4.0

julia> argmin(A, dims=1)
1×2 Matrix{CartesianIndex{2}}:
 CartesianIndex(1, 1)  CartesianIndex(1, 2)

julia> argmin(A, dims=2)
2×1 Matrix{CartesianIndex{2}}:
 CartesianIndex(1, 1)
 CartesianIndex(2, 1)
```



arrayref:
==================================================

No documentation found for public symbol.

`Core.arrayref` is a `Function`.

```
# 1 method for generic function "arrayref" from Core:
 [1] arrayref(inbounds::Bool, A::Array, i::Int64...)
     @ boot.jl:968
```



arrayset:
==================================================

No documentation found for public symbol.

`Core.arrayset` is a `Function`.

```
# 1 method for generic function "arrayset" from Core:
 [1] arrayset(inbounds::Bool, A::Array{T}, x, i::Int64...) where T
     @ boot.jl:970
```



arraysize:
==================================================

No documentation found for public symbol.

`Core.arraysize` is a `Function`.

```
# 2 methods for generic function "arraysize" from Core:
 [1] arraysize(a::Array, i::Int64)
     @ boot.jl:972
 [2] arraysize(a::Array)
     @ boot.jl:971
```



ascii:
==================================================

```
ascii(s::AbstractString)
```

Convert a string to `String` type and check that it contains only ASCII data, otherwise throwing an `ArgumentError` indicating the position of the first non-ASCII byte.

See also the [`isascii`](@ref) predicate to filter or replace non-ASCII characters.

# Examples

```jldoctest
julia> ascii("abcdeγfgh")
ERROR: ArgumentError: invalid ASCII at index 6 in "abcdeγfgh"
Stacktrace:
[...]

julia> ascii("abcdefgh")
"abcdefgh"
```



asec:
==================================================

```
asec(x)
```

Compute the inverse secant of `x`, where the output is in radians. 

```
asec(A::AbstractMatrix)
```

Compute the inverse matrix secant of `A`. 



asecd:
==================================================

```
asecd(x)
```

Compute the inverse secant of `x`, where the output is in degrees. If `x` is a matrix, `x` needs to be a square matrix.

!!! compat "Julia 1.7"
    Matrix arguments require Julia 1.7 or later.




asech:
==================================================

```
asech(x)
```

Compute the inverse hyperbolic secant of `x`. 

```
asech(A::AbstractMatrix)
```

Compute the inverse matrix hyperbolic secant of `A`. 



asin:
==================================================

```
asin(x)
```

Compute the inverse sine of `x`, where the output is in radians.

See also [`asind`](@ref) for output in degrees.

# Examples

```jldoctest
julia> asin.((0, 1/2, 1))
(0.0, 0.5235987755982989, 1.5707963267948966)

julia> asind.((0, 1/2, 1))
(0.0, 30.000000000000004, 90.0)
```

```
asin(A::AbstractMatrix)
```

Compute the inverse matrix sine of a square matrix `A`.

If `A` is symmetric or Hermitian, its eigendecomposition ([`eigen`](@ref)) is used to compute the inverse sine. Otherwise, the inverse sine is determined by using [`log`](@ref) and [`sqrt`](@ref).  For the theory and logarithmic formulas used to compute this function, see [^AH16_2].

[^AH16_2]: Mary Aprahamian and Nicholas J. Higham, "Matrix Inverse Trigonometric and Inverse Hyperbolic Functions: Theory and Algorithms", MIMS EPrint: 2016.4. [https://doi.org/10.1137/16M1057577](https://doi.org/10.1137/16M1057577)

# Examples

```julia-repl
julia> asin(sin([0.5 0.1; -0.2 0.3]))
2×2 Matrix{ComplexF64}:
  0.5-4.16334e-17im  0.1-5.55112e-17im
 -0.2+9.71445e-17im  0.3-1.249e-16im
```



asind:
==================================================

```
asind(x)
```

Compute the inverse sine of `x`, where the output is in degrees. If `x` is a matrix, `x` needs to be a square matrix.

!!! compat "Julia 1.7"
    Matrix arguments require Julia 1.7 or later.




asinh:
==================================================

```
asinh(x)
```

Compute the inverse hyperbolic sine of `x`.

```
asinh(A::AbstractMatrix)
```

Compute the inverse hyperbolic matrix sine of a square matrix `A`.  For the theory and logarithmic formulas used to compute this function, see [^AH16_5].

[^AH16_5]: Mary Aprahamian and Nicholas J. Higham, "Matrix Inverse Trigonometric and Inverse Hyperbolic Functions: Theory and Algorithms", MIMS EPrint: 2016.4. [https://doi.org/10.1137/16M1057577](https://doi.org/10.1137/16M1057577)



asyncmap:
==================================================

```
asyncmap(f, c...; ntasks=0, batch_size=nothing)
```

Uses multiple concurrent tasks to map `f` over a collection (or multiple equal length collections). For multiple collection arguments, `f` is applied elementwise.

`ntasks` specifies the number of tasks to run concurrently. Depending on the length of the collections, if `ntasks` is unspecified, up to 100 tasks will be used for concurrent mapping.

`ntasks` can also be specified as a zero-arg function. In this case, the number of tasks to run in parallel is checked before processing every element and a new task started if the value of `ntasks_func` is greater than the current number of tasks.

If `batch_size` is specified, the collection is processed in batch mode. `f` must then be a function that must accept a `Vector` of argument tuples and must return a vector of results. The input vector will have a length of `batch_size` or less.

The following examples highlight execution in different tasks by returning the `objectid` of the tasks in which the mapping function is executed.

First, with `ntasks` undefined, each element is processed in a different task.

```
julia> tskoid() = objectid(current_task());

julia> asyncmap(x->tskoid(), 1:5)
5-element Array{UInt64,1}:
 0x6e15e66c75c75853
 0x440f8819a1baa682
 0x9fb3eeadd0c83985
 0xebd3e35fe90d4050
 0x29efc93edce2b961

julia> length(unique(asyncmap(x->tskoid(), 1:5)))
5
```

With `ntasks=2` all elements are processed in 2 tasks.

```
julia> asyncmap(x->tskoid(), 1:5; ntasks=2)
5-element Array{UInt64,1}:
 0x027ab1680df7ae94
 0xa23d2f80cd7cf157
 0x027ab1680df7ae94
 0xa23d2f80cd7cf157
 0x027ab1680df7ae94

julia> length(unique(asyncmap(x->tskoid(), 1:5; ntasks=2)))
2
```

With `batch_size` defined, the mapping function needs to be changed to accept an array of argument tuples and return an array of results. `map` is used in the modified mapping function to achieve this.

```
julia> batch_func(input) = map(x->string("args_tuple: ", x, ", element_val: ", x[1], ", task: ", tskoid()), input)
batch_func (generic function with 1 method)

julia> asyncmap(batch_func, 1:5; ntasks=2, batch_size=2)
5-element Array{String,1}:
 "args_tuple: (1,), element_val: 1, task: 9118321258196414413"
 "args_tuple: (2,), element_val: 2, task: 4904288162898683522"
 "args_tuple: (3,), element_val: 3, task: 9118321258196414413"
 "args_tuple: (4,), element_val: 4, task: 4904288162898683522"
 "args_tuple: (5,), element_val: 5, task: 9118321258196414413"
```



asyncmap!:
==================================================

```
asyncmap!(f, results, c...; ntasks=0, batch_size=nothing)
```

Like [`asyncmap`](@ref), but stores output in `results` rather than returning a collection.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.




atan:
==================================================

```
atan(y)
atan(y, x)
```

Compute the inverse tangent of `y` or `y/x`, respectively.

For one real argument, this is the angle in radians between the positive *x*-axis and the point (1, *y*), returning a value in the interval $[-\pi/2, \pi/2]$.

For two arguments, this is the angle in radians between the positive *x*-axis and the point (*x*, *y*), returning a value in the interval $[-\pi, \pi]$. This corresponds to a standard [`atan2`](https://en.wikipedia.org/wiki/Atan2) function. Note that by convention `atan(0.0,x)` is defined as $\pi$ and `atan(-0.0,x)` is defined as $-\pi$ when `x < 0`.

See also [`atand`](@ref) for degrees.

# Examples

```jldoctest
julia> rad2deg(atan(-1/√3))
-30.000000000000004

julia> rad2deg(atan(-1, √3))
-30.000000000000004

julia> rad2deg(atan(1, -√3))
150.0
```

```
atan(A::AbstractMatrix)
```

Compute the inverse matrix tangent of a square matrix `A`.

If `A` is symmetric or Hermitian, its eigendecomposition ([`eigen`](@ref)) is used to compute the inverse tangent. Otherwise, the inverse tangent is determined by using [`log`](@ref).  For the theory and logarithmic formulas used to compute this function, see [^AH16_3].

[^AH16_3]: Mary Aprahamian and Nicholas J. Higham, "Matrix Inverse Trigonometric and Inverse Hyperbolic Functions: Theory and Algorithms", MIMS EPrint: 2016.4. [https://doi.org/10.1137/16M1057577](https://doi.org/10.1137/16M1057577)

# Examples

```julia-repl
julia> atan(tan([0.5 0.1; -0.2 0.3]))
2×2 Matrix{ComplexF64}:
  0.5+1.38778e-17im  0.1-2.77556e-17im
 -0.2+6.93889e-17im  0.3-4.16334e-17im
```



atand:
==================================================

```
atand(y)
atand(y,x)
```

Compute the inverse tangent of `y` or `y/x`, respectively, where the output is in degrees.

!!! compat "Julia 1.7"
    The one-argument method supports square matrix arguments as of Julia 1.7.




atanh:
==================================================

```
atanh(x)
```

Compute the inverse hyperbolic tangent of `x`.

```
atanh(A::AbstractMatrix)
```

Compute the inverse hyperbolic matrix tangent of a square matrix `A`.  For the theory and logarithmic formulas used to compute this function, see [^AH16_6].

[^AH16_6]: Mary Aprahamian and Nicholas J. Higham, "Matrix Inverse Trigonometric and Inverse Hyperbolic Functions: Theory and Algorithms", MIMS EPrint: 2016.4. [https://doi.org/10.1137/16M1057577](https://doi.org/10.1137/16M1057577)



atexit:
==================================================

```
atexit(f)
```

Register a zero- or one-argument function `f()` to be called at process exit. `atexit()` hooks are called in last in first out (LIFO) order and run before object finalizers.

If `f` has a method defined for one integer argument, it will be called as `f(n::Int32)`, where `n` is the current exit code, otherwise it will be called as `f()`.

!!! compat "Julia 1.9"
    The one-argument form requires Julia 1.9


Exit hooks are allowed to call `exit(n)`, in which case Julia will exit with exit code `n` (instead of the original exit code). If more than one exit hook calls `exit(n)`, then Julia will exit with the exit code corresponding to the last called exit hook that calls `exit(n)`. (Because exit hooks are called in LIFO order, "last called" is equivalent to "first registered".)

Note: Once all exit hooks have been called, no more exit hooks can be registered, and any call to `atexit(f)` after all hooks have completed will throw an exception. This situation may occur if you are registering exit hooks from background Tasks that may still be executing concurrently during shutdown.



atreplinit:
==================================================

```
atreplinit(f)
```

Register a one-argument function to be called before the REPL interface is initialized in interactive sessions; this is useful to customize the interface. The argument of `f` is the REPL object. This function should be called from within the `.julia/config/startup.jl` initialization file.



axes:
==================================================

```
axes(A, d)
```

Return the valid range of indices for array `A` along dimension `d`.

See also [`size`](@ref), and the manual chapter on [arrays with custom indices](@ref man-custom-indices).

# Examples

```jldoctest
julia> A = fill(1, (5,6,7));

julia> axes(A, 2)
Base.OneTo(6)

julia> axes(A, 4) == 1:1  # all dimensions d > ndims(A) have size 1
true
```

# Usage note

Each of the indices has to be an `AbstractUnitRange{<:Integer}`, but at the same time can be a type that uses custom indices. So, for example, if you need a subset, use generalized indexing constructs like `begin`/`end` or [`firstindex`](@ref)/[`lastindex`](@ref):

```julia
ix = axes(v, 1)
ix[2:end]          # will work for eg Vector, but may fail in general
ix[(begin+1):end]  # works for generalized indexes
```

```
axes(A)
```

Return the tuple of valid indices for array `A`.

See also: [`size`](@ref), [`keys`](@ref), [`eachindex`](@ref).

# Examples

```jldoctest
julia> A = fill(1, (5,6,7));

julia> axes(A)
(Base.OneTo(5), Base.OneTo(6), Base.OneTo(7))
```



basename:
==================================================

```
basename(path::AbstractString) -> String
```

Get the file name part of a path.

!!! note
    This function differs slightly from the Unix `basename` program, where trailing slashes are ignored, i.e. `$ basename /foo/bar/` returns `bar`, whereas `basename` in Julia returns an empty string `""`.


# Examples

```jldoctest
julia> basename("/home/myuser/example.jl")
"example.jl"

julia> basename("/home/myuser/")
""
```

See also [`dirname`](@ref).



big:
==================================================

```
big(T::Type)
```

Compute the type that represents the numeric type `T` with arbitrary precision. Equivalent to `typeof(big(zero(T)))`.

# Examples

```jldoctest
julia> big(Rational)
Rational{BigInt}

julia> big(Float64)
BigFloat

julia> big(Complex{Int})
Complex{BigInt}
```

```
big(x)
```

Convert a number to a maximum precision representation (typically [`BigInt`](@ref) or `BigFloat`). See [`BigFloat`](@ref BigFloat(::Any, rounding::RoundingMode)) for information about some pitfalls with floating-point numbers.



bind:
==================================================

```
bind(chnl::Channel, task::Task)
```

Associate the lifetime of `chnl` with a task. `Channel` `chnl` is automatically closed when the task terminates. Any uncaught exception in the task is propagated to all waiters on `chnl`.

The `chnl` object can be explicitly closed independent of task termination. Terminating tasks have no effect on already closed `Channel` objects.

When a channel is bound to multiple tasks, the first task to terminate will close the channel. When multiple channels are bound to the same task, termination of the task will close all of the bound channels.

# Examples

```jldoctest
julia> c = Channel(0);

julia> task = @async foreach(i->put!(c, i), 1:4);

julia> bind(c,task);

julia> for i in c
           @show i
       end;
i = 1
i = 2
i = 3
i = 4

julia> isopen(c)
false
```

```jldoctest
julia> c = Channel(0);

julia> task = @async (put!(c, 1); error("foo"));

julia> bind(c, task);

julia> take!(c)
1

julia> put!(c, 1);
ERROR: TaskFailedException
Stacktrace:
[...]
    nested task error: foo
[...]
```

```
bind(socket::Union{TCPServer, UDPSocket, TCPSocket}, host::IPAddr, port::Integer; ipv6only=false, reuseaddr=false, kws...)
```

Bind `socket` to the given `host:port`. Note that `0.0.0.0` will listen on all devices.

  * The `ipv6only` parameter disables dual stack mode. If `ipv6only=true`, only an IPv6 stack is created.
  * If `reuseaddr=true`, multiple threads or processes can bind to the same address without error if they all set `reuseaddr=true`, but only the last to bind will receive any traffic.



binomial:
==================================================

```
binomial(n::Integer, k::Integer)
```

The *binomial coefficient* $\binom{n}{k}$, being the coefficient of the $k$th term in the polynomial expansion of $(1+x)^n$.

If $n$ is non-negative, then it is the number of ways to choose `k` out of `n` items:

$$
\binom{n}{k} = \frac{n!}{k! (n-k)!}
$$

where $n!$ is the [`factorial`](@ref) function.

If $n$ is negative, then it is defined in terms of the identity

$$
\binom{n}{k} = (-1)^k \binom{k-n-1}{k}
$$

See also [`factorial`](@ref).

# Examples

```jldoctest
julia> binomial(5, 3)
10

julia> factorial(5) ÷ (factorial(5-3) * factorial(3))
10

julia> binomial(-5, 3)
-35
```

# External links

  * [Binomial coefficient](https://en.wikipedia.org/wiki/Binomial_coefficient) on Wikipedia.

```
binomial(x::Number, k::Integer)
```

The generalized binomial coefficient, defined for `k ≥ 0` by the polynomial

$$
\frac{1}{k!} \prod_{j=0}^{k-1} (x - j)
$$

When `k < 0` it returns zero.

For the case of integer `x`, this is equivalent to the ordinary integer binomial coefficient

$$
\binom{n}{k} = \frac{n!}{k! (n-k)!}
$$

Further generalizations to non-integer `k` are mathematically possible, but involve the Gamma function and/or the beta function, which are not provided by the Julia standard library but are available in external packages such as [SpecialFunctions.jl](https://github.com/JuliaMath/SpecialFunctions.jl).

# External links

  * [Binomial coefficient](https://en.wikipedia.org/wiki/Binomial_coefficient) on Wikipedia.



bitreverse:
==================================================

```
bitreverse(x)
```

Reverse the order of bits in integer `x`. `x` must have a fixed bit width, e.g. be an `Int16` or `Int32`.

!!! compat "Julia 1.5"
    This function requires Julia 1.5 or later.


# Examples

```jldoctest
julia> bitreverse(0x8080808080808080)
0x0101010101010101

julia> reverse(bitstring(0xa06e)) == bitstring(bitreverse(0xa06e))
true
```



bitrotate:
==================================================

```
bitrotate(x::Base.BitInteger, k::Integer)
```

`bitrotate(x, k)` implements bitwise rotation. It returns the value of `x` with its bits rotated left `k` times. A negative value of `k` will rotate to the right instead.

!!! compat "Julia 1.5"
    This function requires Julia 1.5 or later.


See also: [`<<`](@ref), [`circshift`](@ref), [`BitArray`](@ref).

```jldoctest
julia> bitrotate(UInt8(114), 2)
0xc9

julia> bitstring(bitrotate(0b01110010, 2))
"11001001"

julia> bitstring(bitrotate(0b01110010, -2))
"10011100"

julia> bitstring(bitrotate(0b01110010, 8))
"01110010"
```



bitstring:
==================================================

```
bitstring(n)
```

A string giving the literal bit representation of a primitive type.

See also [`count_ones`](@ref), [`count_zeros`](@ref), [`digits`](@ref).

# Examples

```jldoctest
julia> bitstring(Int32(4))
"00000000000000000000000000000100"

julia> bitstring(2.2)
"0100000000000001100110011001100110011001100110011001100110011010"
```



broadcast:
==================================================

```
broadcast(f, As...)
```

Broadcast the function `f` over the arrays, tuples, collections, [`Ref`](@ref)s and/or scalars `As`.

Broadcasting applies the function `f` over the elements of the container arguments and the scalars themselves in `As`. Singleton and missing dimensions are expanded to match the extents of the other arguments by virtually repeating the value. By default, only a limited number of types are considered scalars, including `Number`s, `String`s, `Symbol`s, `Type`s, `Function`s and some common singletons like [`missing`](@ref) and [`nothing`](@ref). All other arguments are iterated over or indexed into elementwise.

The resulting container type is established by the following rules:

  * If all the arguments are scalars or zero-dimensional arrays, it returns an unwrapped scalar.
  * If at least one argument is a tuple and all others are scalars or zero-dimensional arrays, it returns a tuple.
  * All other combinations of arguments default to returning an `Array`, but custom container types can define their own implementation and promotion-like rules to customize the result when they appear as arguments.

A special syntax exists for broadcasting: `f.(args...)` is equivalent to `broadcast(f, args...)`, and nested `f.(g.(args...))` calls are fused into a single broadcast loop.

# Examples

```jldoctest
julia> A = [1, 2, 3, 4, 5]
5-element Vector{Int64}:
 1
 2
 3
 4
 5

julia> B = [1 2; 3 4; 5 6; 7 8; 9 10]
5×2 Matrix{Int64}:
 1   2
 3   4
 5   6
 7   8
 9  10

julia> broadcast(+, A, B)
5×2 Matrix{Int64}:
  2   3
  5   6
  8   9
 11  12
 14  15

julia> parse.(Int, ["1", "2"])
2-element Vector{Int64}:
 1
 2

julia> abs.((1, -2))
(1, 2)

julia> broadcast(+, 1.0, (0, -2.0))
(1.0, -1.0)

julia> (+).([[0,2], [1,3]], Ref{Vector{Int}}([1,-1]))
2-element Vector{Vector{Int64}}:
 [1, 1]
 [2, 2]

julia> string.(("one","two","three","four"), ": ", 1:4)
4-element Vector{String}:
 "one: 1"
 "two: 2"
 "three: 3"
 "four: 4"

```



broadcast!:
==================================================

```
broadcast!(f, dest, As...)
```

Like [`broadcast`](@ref), but store the result of `broadcast(f, As...)` in the `dest` array. Note that `dest` is only used to store the result, and does not supply arguments to `f` unless it is also listed in the `As`, as in `broadcast!(f, A, A, B)` to perform `A[:] = broadcast(f, A, B)`.

# Examples

```jldoctest
julia> A = [1.0; 0.0]; B = [0.0; 0.0];

julia> broadcast!(+, B, A, (0, -2.0));

julia> B
2-element Vector{Float64}:
  1.0
 -2.0

julia> A
2-element Vector{Float64}:
 1.0
 0.0

julia> broadcast!(+, A, A, (0, -2.0));

julia> A
2-element Vector{Float64}:
  1.0
 -2.0
```



bswap:
==================================================

```
bswap(n)
```

Reverse the byte order of `n`.

(See also [`ntoh`](@ref) and [`hton`](@ref) to convert between the current native byte order and big-endian order.)

# Examples

```jldoctest
julia> a = bswap(0x10203040)
0x40302010

julia> bswap(a)
0x10203040

julia> string(1, base = 2)
"1"

julia> string(bswap(1), base = 2)
"100000000000000000000000000000000000000000000000000000000"
```



bytes2hex:
==================================================

```
bytes2hex(itr) -> String
bytes2hex(io::IO, itr)
```

Convert an iterator `itr` of bytes to its hexadecimal string representation, either returning a `String` via `bytes2hex(itr)` or writing the string to an `io` stream via `bytes2hex(io, itr)`.  The hexadecimal characters are all lowercase.

!!! compat "Julia 1.7"
    Calling `bytes2hex` with arbitrary iterators producing `UInt8` values requires Julia 1.7 or later. In earlier versions, you can `collect` the iterator before calling `bytes2hex`.


# Examples

```jldoctest
julia> a = string(12345, base = 16)
"3039"

julia> b = hex2bytes(a)
2-element Vector{UInt8}:
 0x30
 0x39

julia> bytes2hex(b)
"3039"
```



bytesavailable:
==================================================

```
bytesavailable(io)
```

Return the number of bytes available for reading before a read from this stream or buffer will block.

# Examples

```jldoctest
julia> io = IOBuffer("JuliaLang is a GitHub organization");

julia> bytesavailable(io)
34
```



cat:
==================================================

```
cat(A...; dims)
```

Concatenate the input arrays along the dimensions specified in `dims`.

Along a dimension `d in dims`, the size of the output array is `sum(size(a,d) for a in A)`. Along other dimensions, all input arrays should have the same size, which will also be the size of the output array along those dimensions.

If `dims` is a single number, the different arrays are tightly packed along that dimension. If `dims` is an iterable containing several dimensions, the positions along these dimensions are increased simultaneously for each input array, filling with zero elsewhere. This allows one to construct block-diagonal matrices as `cat(matrices...; dims=(1,2))`, and their higher-dimensional analogues.

The special case `dims=1` is [`vcat`](@ref), and `dims=2` is [`hcat`](@ref). See also [`hvcat`](@ref), [`hvncat`](@ref), [`stack`](@ref), [`repeat`](@ref).

The keyword also accepts `Val(dims)`.

!!! compat "Julia 1.8"
    For multiple dimensions `dims = Val(::Tuple)` was added in Julia 1.8.


# Examples

Concatenate two arrays in different dimensions:

```jldoctest
julia> a = [1 2 3]
1×3 Matrix{Int64}:
 1  2  3

julia> b = [4 5 6]
1×3 Matrix{Int64}:
 4  5  6

julia> cat(a, b; dims=1)
2×3 Matrix{Int64}:
 1  2  3
 4  5  6

julia> cat(a, b; dims=2)
1×6 Matrix{Int64}:
 1  2  3  4  5  6

julia> cat(a, b; dims=(1, 2))
2×6 Matrix{Int64}:
 1  2  3  0  0  0
 0  0  0  4  5  6
```

# Extended Help

Concatenate 3D arrays:

```jldoctest
julia> a = ones(2, 2, 3);

julia> b = ones(2, 2, 4);

julia> c = cat(a, b; dims=3);

julia> size(c) == (2, 2, 7)
true
```

Concatenate arrays of different sizes:

```jldoctest
julia> cat([1 2; 3 4], [pi, pi], fill(10, 2,3,1); dims=2)  # same as hcat
2×6×1 Array{Float64, 3}:
[:, :, 1] =
 1.0  2.0  3.14159  10.0  10.0  10.0
 3.0  4.0  3.14159  10.0  10.0  10.0
```

Construct a block diagonal matrix:

```
julia> cat(true, trues(2,2), trues(4)', dims=(1,2))  # block-diagonal
4×7 Matrix{Bool}:
 1  0  0  0  0  0  0
 0  1  1  0  0  0  0
 0  1  1  0  0  0  0
 0  0  0  1  1  1  1
```

```
julia> cat(1, [2], [3;;]; dims=Val(2))
1×3 Matrix{Int64}:
 1  2  3
```

!!! note
    `cat` does not join two strings, you may want to use `*`.


```jldoctest
julia> a = "aaa";

julia> b = "bbb";

julia> cat(a, b; dims=1)
2-element Vector{String}:
 "aaa"
 "bbb"

julia> cat(a, b; dims=2)
1×2 Matrix{String}:
 "aaa"  "bbb"

julia> a * b
"aaabbb"
```



catch_backtrace:
==================================================

```
catch_backtrace()
```

Get the backtrace of the current exception, for use within `catch` blocks.



cbrt:
==================================================

```
cbrt(x::Real)
```

Return the cube root of `x`, i.e. $x^{1/3}$. Negative values are accepted (returning the negative real root when $x < 0$).

The prefix operator `∛` is equivalent to `cbrt`.

# Examples

```jldoctest
julia> cbrt(big(27))
3.0

julia> cbrt(big(-27))
-3.0
```

```
cbrt(A::AbstractMatrix{<:Real})
```

Computes the real-valued cube root of a real-valued matrix `A`. If `T = cbrt(A)`, then we have `T*T*T ≈ A`, see example given below.

If `A` is symmetric, i.e., of type `HermOrSym{<:Real}`, then ([`eigen`](@ref)) is used to find the cube root. Otherwise, a specialized version of the p-th root algorithm [^S03] is utilized, which exploits the real-valued Schur decomposition ([`schur`](@ref)) to compute the cube root.

[^S03]: Matthew I. Smith, "A Schur Algorithm for Computing Matrix pth Roots", SIAM Journal on Matrix Analysis and Applications, vol. 24, 2003, pp. 971–989. [doi:10.1137/S0895479801392697](https://doi.org/10.1137/s0895479801392697)

# Examples

```jldoctest
julia> A = [0.927524 -0.15857; -1.3677 -1.01172]
2×2 Matrix{Float64}:
  0.927524  -0.15857
 -1.3677    -1.01172

julia> T = cbrt(A)
2×2 Matrix{Float64}:
  0.910077  -0.151019
 -1.30257   -0.936818

julia> T*T*T ≈ A
true
```



cd:
==================================================

```
cd(dir::AbstractString=homedir())
```

Set the current working directory.

See also: [`pwd`](@ref), [`mkdir`](@ref), [`mkpath`](@ref), [`mktempdir`](@ref).

# Examples

```julia-repl
julia> cd("/home/JuliaUser/Projects/julia")

julia> pwd()
"/home/JuliaUser/Projects/julia"

julia> cd()

julia> pwd()
"/home/JuliaUser"
```

```
cd(f::Function, dir::AbstractString=homedir())
```

Temporarily change the current working directory to `dir`, apply function `f` and finally return to the original directory.

# Examples

```julia-repl
julia> pwd()
"/home/JuliaUser"

julia> cd(readdir, "/home/JuliaUser/Projects/julia")
34-element Array{String,1}:
 ".circleci"
 ".freebsdci.sh"
 ".git"
 ".gitattributes"
 ".github"
 ⋮
 "test"
 "ui"
 "usr"
 "usr-staging"

julia> pwd()
"/home/JuliaUser"
```



ceil:
==================================================

```
ceil([T,] x)
ceil(x; digits::Integer= [, base = 10])
ceil(x; sigdigits::Integer= [, base = 10])
```

`ceil(x)` returns the nearest integral value of the same type as `x` that is greater than or equal to `x`.

`ceil(T, x)` converts the result to type `T`, throwing an `InexactError` if the ceiled value is not representable as a `T`.

Keywords `digits`, `sigdigits` and `base` work as for [`round`](@ref).

To support `ceil` for a new type, define `Base.round(x::NewType, ::RoundingMode{:Up})`.

```
ceil(dt::TimeType, p::Period) -> TimeType
```

Return the nearest `Date` or `DateTime` greater than or equal to `dt` at resolution `p`.

For convenience, `p` may be a type instead of a value: `ceil(dt, Dates.Hour)` is a shortcut for `ceil(dt, Dates.Hour(1))`.

```jldoctest
julia> ceil(Date(1985, 8, 16), Month)
1985-09-01

julia> ceil(DateTime(2013, 2, 13, 0, 31, 20), Minute(15))
2013-02-13T00:45:00

julia> ceil(DateTime(2016, 8, 6, 12, 0, 0), Day)
2016-08-07T00:00:00
```

```
ceil(x::Period, precision::T) where T <: Union{TimePeriod, Week, Day} -> T
```

Round `x` up to the nearest multiple of `precision`. If `x` and `precision` are different subtypes of `Period`, the return value will have the same type as `precision`.

For convenience, `precision` may be a type instead of a value: `ceil(x, Dates.Hour)` is a shortcut for `ceil(x, Dates.Hour(1))`.

```jldoctest
julia> ceil(Day(16), Week)
3 weeks

julia> ceil(Minute(44), Minute(15))
45 minutes

julia> ceil(Hour(36), Day)
2 days
```

Rounding to a `precision` of `Month`s or `Year`s is not supported, as these `Period`s are of inconsistent length.



cglobal:
==================================================

```
Core.IntrinsicFunction <: Core.Builtin <: Function
```

The `Core.IntrinsicFunction` function define some basic primitives for what defines the abilities and behaviors of a Julia program



checkbounds:
==================================================

```
checkbounds(Bool, A, I...)
```

Return `true` if the specified indices `I` are in bounds for the given array `A`. Subtypes of `AbstractArray` should specialize this method if they need to provide custom bounds checking behaviors; however, in many cases one can rely on `A`'s indices and [`checkindex`](@ref).

See also [`checkindex`](@ref).

# Examples

```jldoctest
julia> A = rand(3, 3);

julia> checkbounds(Bool, A, 2)
true

julia> checkbounds(Bool, A, 3, 4)
false

julia> checkbounds(Bool, A, 1:3)
true

julia> checkbounds(Bool, A, 1:3, 2:4)
false
```

```
checkbounds(A, I...)
```

Throw an error if the specified indices `I` are not in bounds for the given array `A`.



checkindex:
==================================================

```
checkindex(Bool, inds::AbstractUnitRange, index)
```

Return `true` if the given `index` is within the bounds of `inds`. Custom types that would like to behave as indices for all arrays can extend this method in order to provide a specialized bounds checking implementation.

See also [`checkbounds`](@ref).

# Examples

```jldoctest
julia> checkindex(Bool, 1:20, 8)
true

julia> checkindex(Bool, 1:20, 21)
false
```



chmod:
==================================================

```
chmod(path::AbstractString, mode::Integer; recursive::Bool=false)
```

Change the permissions mode of `path` to `mode`. Only integer `mode`s (e.g. `0o777`) are currently supported. If `recursive=true` and the path is a directory all permissions in that directory will be recursively changed. Return `path`.

!!! note
    Prior to Julia 1.6, this did not correctly manipulate filesystem ACLs  on Windows, therefore it would only set read-only bits on files.  It  now is able to manipulate ACLs.




chomp:
==================================================

```
chomp(s::AbstractString) -> SubString
```

Remove a single trailing newline from a string.

See also [`chop`](@ref).

# Examples

```jldoctest
julia> chomp("Hello\n")
"Hello"
```



chop:
==================================================

```
chop(s::AbstractString; head::Integer = 0, tail::Integer = 1)
```

Remove the first `head` and the last `tail` characters from `s`. The call `chop(s)` removes the last character from `s`. If it is requested to remove more characters than `length(s)` then an empty string is returned.

See also [`chomp`](@ref), [`startswith`](@ref), [`first`](@ref).

# Examples

```jldoctest
julia> a = "March"
"March"

julia> chop(a)
"Marc"

julia> chop(a, head = 1, tail = 2)
"ar"

julia> chop(a, head = 5, tail = 5)
""
```



chopprefix:
==================================================

```
chopprefix(s::AbstractString, prefix::Union{AbstractString,Regex}) -> SubString
```

Remove the prefix `prefix` from `s`. If `s` does not start with `prefix`, a string equal to `s` is returned.

See also [`chopsuffix`](@ref).

!!! compat "Julia 1.8"
    This function is available as of Julia 1.8.


# Examples

```jldoctest
julia> chopprefix("Hamburger", "Ham")
"burger"

julia> chopprefix("Hamburger", "hotdog")
"Hamburger"
```



chopsuffix:
==================================================

```
chopsuffix(s::AbstractString, suffix::Union{AbstractString,Regex}) -> SubString
```

Remove the suffix `suffix` from `s`. If `s` does not end with `suffix`, a string equal to `s` is returned.

See also [`chopprefix`](@ref).

!!! compat "Julia 1.8"
    This function is available as of Julia 1.8.


# Examples

```jldoctest
julia> chopsuffix("Hamburger", "er")
"Hamburg"

julia> chopsuffix("Hamburger", "hotdog")
"Hamburger"
```



chown:
==================================================

```
chown(path::AbstractString, owner::Integer, group::Integer=-1)
```

Change the owner and/or group of `path` to `owner` and/or `group`. If the value entered for `owner` or `group` is `-1` the corresponding ID will not change. Only integer `owner`s and `group`s are currently supported. Return `path`.



circcopy!:
==================================================

```
circcopy!(dest, src)
```

Copy `src` to `dest`, indexing each dimension modulo its length. `src` and `dest` must have the same size, but can be offset in their indices; any offset results in a (circular) wraparound. If the arrays have overlapping indices, then on the domain of the overlap `dest` agrees with `src`.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


See also: [`circshift`](@ref).

# Examples

```julia-repl
julia> src = reshape(Vector(1:16), (4,4))
4×4 Array{Int64,2}:
 1  5   9  13
 2  6  10  14
 3  7  11  15
 4  8  12  16

julia> dest = OffsetArray{Int}(undef, (0:3,2:5))

julia> circcopy!(dest, src)
OffsetArrays.OffsetArray{Int64,2,Array{Int64,2}} with indices 0:3×2:5:
 8  12  16  4
 5   9  13  1
 6  10  14  2
 7  11  15  3

julia> dest[1:3,2:4] == src[1:3,2:4]
true
```



circshift:
==================================================

```
circshift(A, shifts)
```

Circularly shift, i.e. rotate, the data in an array. The second argument is a tuple or vector giving the amount to shift in each dimension, or an integer to shift only in the first dimension.

See also: [`circshift!`](@ref), [`circcopy!`](@ref), [`bitrotate`](@ref), [`<<`](@ref).

# Examples

```jldoctest
julia> b = reshape(Vector(1:16), (4,4))
4×4 Matrix{Int64}:
 1  5   9  13
 2  6  10  14
 3  7  11  15
 4  8  12  16

julia> circshift(b, (0,2))
4×4 Matrix{Int64}:
  9  13  1  5
 10  14  2  6
 11  15  3  7
 12  16  4  8

julia> circshift(b, (-1,0))
4×4 Matrix{Int64}:
 2  6  10  14
 3  7  11  15
 4  8  12  16
 1  5   9  13

julia> a = BitArray([true, true, false, false, true])
5-element BitVector:
 1
 1
 0
 0
 1

julia> circshift(a, 1)
5-element BitVector:
 1
 1
 1
 0
 0

julia> circshift(a, -1)
5-element BitVector:
 1
 0
 0
 1
 1
```



circshift!:
==================================================

```
circshift!(dest, src, shifts)
```

Circularly shift, i.e. rotate, the data in `src`, storing the result in `dest`. `shifts` specifies the amount to shift in each dimension.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


See also [`circshift`](@ref).



cis:
==================================================

```
cis(x)
```

More efficient method for `exp(im*x)` by using Euler's formula: $\cos(x) + i \sin(x) = \exp(i x)$.

See also [`cispi`](@ref), [`sincos`](@ref), [`exp`](@ref), [`angle`](@ref).

# Examples

```jldoctest
julia> cis(π) ≈ -1
true
```

```
cis(A::AbstractMatrix)
```

More efficient method for `exp(im*A)` of square matrix `A` (especially if `A` is `Hermitian` or real-`Symmetric`).

See also [`cispi`](@ref), [`sincos`](@ref), [`exp`](@ref).

!!! compat "Julia 1.7"
    Support for using `cis` with matrices was added in Julia 1.7.


# Examples

```jldoctest
julia> cis([π 0; 0 π]) ≈ -I
true
```



cispi:
==================================================

```
cispi(x)
```

More accurate method for `cis(pi*x)` (especially for large `x`).

See also [`cis`](@ref), [`sincospi`](@ref), [`exp`](@ref), [`angle`](@ref).

# Examples

```jldoctest
julia> cispi(10000)
1.0 + 0.0im

julia> cispi(0.25 + 1im)
0.030556854645954562 + 0.03055685464595456im
```

!!! compat "Julia 1.6"
    This function requires Julia 1.6 or later.




clamp:
==================================================

```
clamp(x, lo, hi)
```

Return `x` if `lo <= x <= hi`. If `x > hi`, return `hi`. If `x < lo`, return `lo`. Arguments are promoted to a common type.

See also [`clamp!`](@ref), [`min`](@ref), [`max`](@ref).

!!! compat "Julia 1.3"
    `missing` as the first argument requires at least Julia 1.3.


# Examples

```jldoctest
julia> clamp.([pi, 1.0, big(10)], 2.0, 9.0)
3-element Vector{BigFloat}:
 3.141592653589793238462643383279502884197169399375105820974944592307816406286198
 2.0
 9.0

julia> clamp.([11, 8, 5], 10, 6)  # an example where lo > hi
3-element Vector{Int64}:
  6
  6
 10
```

```
clamp(x, T)::T
```

Clamp `x` between `typemin(T)` and `typemax(T)` and convert the result to type `T`.

See also [`trunc`](@ref).

# Examples

```jldoctest
julia> clamp(200, Int8)
127

julia> clamp(-200, Int8)
-128

julia> trunc(Int, 4pi^2)
39
```

```
clamp(x::Integer, r::AbstractUnitRange)
```

Clamp `x` to lie within range `r`.

!!! compat "Julia 1.6"
    This method requires at least Julia 1.6.




clamp!:
==================================================

```
clamp!(array::AbstractArray, lo, hi)
```

Restrict values in `array` to the specified range, in-place. See also [`clamp`](@ref).

!!! compat "Julia 1.3"
    `missing` entries in `array` require at least Julia 1.3.


# Examples

```jldoctest
julia> row = collect(-4:4)';

julia> clamp!(row, 0, Inf)
1×9 adjoint(::Vector{Int64}) with eltype Int64:
 0  0  0  0  0  1  2  3  4

julia> clamp.((-4:4)', 0, Inf)
1×9 Matrix{Float64}:
 0.0  0.0  0.0  0.0  0.0  1.0  2.0  3.0  4.0
```



cld:
==================================================

```
cld(x, y)
```

Smallest integer larger than or equal to `x / y`. Equivalent to `div(x, y, RoundUp)`.

See also [`div`](@ref), [`fld`](@ref).

# Examples

```jldoctest
julia> cld(5.5, 2.2)
3.0

julia> cld.(-5:5, 3)'
1×11 adjoint(::Vector{Int64}) with eltype Int64:
 -1  -1  -1  0  0  0  1  1  1  2  2
```



clipboard:
==================================================

```
clipboard(x)
```

Send a printed form of `x` to the operating system clipboard ("copy").

```
clipboard() -> String
```

Return a string with the contents of the operating system clipboard ("paste").



close:
==================================================

```
close(stream)
```

Close an I/O stream. Performs a [`flush`](@ref) first.

```
close(c::Channel[, excp::Exception])
```

Close a channel. An exception (optionally given by `excp`), is thrown by:

  * [`put!`](@ref) on a closed channel.
  * [`take!`](@ref) and [`fetch`](@ref) on an empty, closed channel.

```
close(lock::LockMonitor)
```

Release a pidfile lock.



closewrite:
==================================================

```
closewrite(stream)
```

Shutdown the write half of a full-duplex I/O stream. Performs a [`flush`](@ref) first. Notify the other end that no more data will be written to the underlying file. This is not supported by all IO types.

If implemented, `closewrite` causes subsequent `read` or `eof` calls that would block to instead throw EOF or return true, respectively. If the stream is already closed, this is idempotent.

# Examples

```jldoctest
julia> io = Base.BufferStream(); # this never blocks, so we can read and write on the same Task

julia> write(io, "request");

julia> # calling `read(io)` here would block forever

julia> closewrite(io);

julia> read(io, String)
"request"
```



cmp:
==================================================

```
cmp(x,y)
```

Return -1, 0, or 1 depending on whether `x` is less than, equal to, or greater than `y`, respectively. Uses the total order implemented by `isless`.

# Examples

```jldoctest
julia> cmp(1, 2)
-1

julia> cmp(2, 1)
1

julia> cmp(2+im, 3-im)
ERROR: MethodError: no method matching isless(::Complex{Int64}, ::Complex{Int64})
[...]
```

```
cmp(<, x, y)
```

Return -1, 0, or 1 depending on whether `x` is less than, equal to, or greater than `y`, respectively. The first argument specifies a less-than comparison function to use.

```
cmp(a::AbstractString, b::AbstractString) -> Int
```

Compare two strings. Return `0` if both strings have the same length and the character at each index is the same in both strings. Return `-1` if `a` is a prefix of `b`, or if `a` comes before `b` in alphabetical order. Return `1` if `b` is a prefix of `a`, or if `b` comes before `a` in alphabetical order (technically, lexicographical order by Unicode code points).

# Examples

```jldoctest
julia> cmp("abc", "abc")
0

julia> cmp("ab", "abc")
-1

julia> cmp("abc", "ab")
1

julia> cmp("ab", "ac")
-1

julia> cmp("ac", "ab")
1

julia> cmp("α", "a")
1

julia> cmp("b", "β")
-1
```



coalesce:
==================================================

```
coalesce(x...)
```

Return the first value in the arguments which is not equal to [`missing`](@ref), if any. Otherwise return `missing`.

See also [`skipmissing`](@ref), [`something`](@ref), [`@coalesce`](@ref).

# Examples

```jldoctest
julia> coalesce(missing, 1)
1

julia> coalesce(1, missing)
1

julia> coalesce(nothing, 1)  # returns `nothing`

julia> coalesce(missing, missing)
missing
```



code_llvm:
==================================================

```
code_llvm([io=stdout,], f, types; raw=false, dump_module=false, optimize=true, debuginfo=:default)
```

Prints the LLVM bitcodes generated for running the method matching the given generic function and type signature to `io`.

If the `optimize` keyword is unset, the code will be shown before LLVM optimizations. All metadata and dbg.* calls are removed from the printed bitcode. For the full IR, set the `raw` keyword to true. To dump the entire module that encapsulates the function (with declarations), set the `dump_module` keyword to true. Keyword argument `debuginfo` may be one of source (default) or none, to specify the verbosity of code comments.

See also: [`@code_llvm`](@ref), [`code_warntype`](@ref), [`code_typed`](@ref), [`code_lowered`](@ref), [`code_native`](@ref).



code_lowered:
==================================================

```
code_lowered(f, types; generated=true, debuginfo=:default)
```

Return an array of the lowered forms (IR) for the methods matching the given generic function and type signature.

If `generated` is `false`, the returned `CodeInfo` instances will correspond to fallback implementations. An error is thrown if no fallback implementation exists. If `generated` is `true`, these `CodeInfo` instances will correspond to the method bodies yielded by expanding the generators.

The keyword `debuginfo` controls the amount of code metadata present in the output.

Note that an error will be thrown if `types` are not leaf types when `generated` is `true` and any of the corresponding methods are an `@generated` method.



code_native:
==================================================

```
code_native([io=stdout,], f, types; syntax=:intel, debuginfo=:default, binary=false, dump_module=true)
```

Prints the native assembly instructions generated for running the method matching the given generic function and type signature to `io`.

  * Set assembly syntax by setting `syntax` to `:intel` (default) for intel syntax or `:att` for AT&T syntax.
  * Specify verbosity of code comments by setting `debuginfo` to `:source` (default) or `:none`.
  * If `binary` is `true`, also print the binary machine code for each instruction precedented by an abbreviated address.
  * If `dump_module` is `false`, do not print metadata such as rodata or directives.
  * If `raw` is `false`, uninteresting instructions (like the safepoint function prologue) are elided.

See also: [`@code_native`](@ref), [`code_warntype`](@ref), [`code_typed`](@ref), [`code_lowered`](@ref), [`code_llvm`](@ref).



code_typed:
==================================================

```
code_typed(f, types; kw...)
```

Returns an array of type-inferred lowered form (IR) for the methods matching the given generic function and type signature.

# Keyword Arguments

  * `optimize::Bool = true`: optional, controls whether additional optimizations, such as inlining, are also applied.
  * `debuginfo::Symbol = :default`: optional, controls the amount of code metadata present in the output, possible options are `:source` or `:none`.

# Internal Keyword Arguments

This section should be considered internal, and is only for who understands Julia compiler internals.

  * `world::UInt = Base.get_world_counter()`: optional, controls the world age to use when looking up methods, use current world age if not specified.
  * `interp::Core.Compiler.AbstractInterpreter = Core.Compiler.NativeInterpreter(world)`: optional, controls the abstract interpreter to use, use the native interpreter if not specified.

# Examples

One can put the argument types in a tuple to get the corresponding `code_typed`.

```julia
julia> code_typed(+, (Float64, Float64))
1-element Vector{Any}:
 CodeInfo(
1 ─ %1 = Base.add_float(x, y)::Float64
└──      return %1
) => Float64
```



code_warntype:
==================================================

```
code_warntype([io::IO], f, types; debuginfo=:default)
```

Prints lowered and type-inferred ASTs for the methods matching the given generic function and type signature to `io` which defaults to `stdout`. The ASTs are annotated in such a way as to cause "non-leaf" types which may be problematic for performance to be emphasized (if color is available, displayed in red). This serves as a warning of potential type instability.

Not all non-leaf types are particularly problematic for performance, and the performance characteristics of a particular type is an implementation detail of the compiler. `code_warntype` will err on the side of coloring types red if they might be a performance concern, so some types may be colored red even if they do not impact performance. Small unions of concrete types are usually not a concern, so these are highlighted in yellow.

Keyword argument `debuginfo` may be one of `:source` or `:none` (default), to specify the verbosity of code comments.

See the [`@code_warntype`](@ref man-code-warntype) section in the Performance Tips page of the manual for more information.

See also: [`@code_warntype`](@ref), [`code_typed`](@ref), [`code_lowered`](@ref), [`code_llvm`](@ref), [`code_native`](@ref).



codepoint:
==================================================

```
codepoint(c::AbstractChar) -> Integer
```

Return the Unicode codepoint (an unsigned integer) corresponding to the character `c` (or throw an exception if `c` does not represent a valid character). For `Char`, this is a `UInt32` value, but `AbstractChar` types that represent only a subset of Unicode may return a different-sized integer (e.g. `UInt8`).



codeunit:
==================================================

```
codeunit(s::AbstractString) -> Type{<:Union{UInt8, UInt16, UInt32}}
```

Return the code unit type of the given string object. For ASCII, Latin-1, or UTF-8 encoded strings, this would be `UInt8`; for UCS-2 and UTF-16 it would be `UInt16`; for UTF-32 it would be `UInt32`. The code unit type need not be limited to these three types, but it's hard to think of widely used string encodings that don't use one of these units. `codeunit(s)` is the same as `typeof(codeunit(s,1))` when `s` is a non-empty string.

See also [`ncodeunits`](@ref).

```
codeunit(s::AbstractString, i::Integer) -> Union{UInt8, UInt16, UInt32}
```

Return the code unit value in the string `s` at index `i`. Note that

```
codeunit(s, i) :: codeunit(s)
```

I.e. the value returned by `codeunit(s, i)` is of the type returned by `codeunit(s)`.

# Examples

```jldoctest
julia> a = codeunit("Hello", 2)
0x65

julia> typeof(a)
UInt8
```

See also [`ncodeunits`](@ref), [`checkbounds`](@ref).



codeunits:
==================================================

```
codeunits(s::AbstractString)
```

Obtain a vector-like object containing the code units of a string. Returns a `CodeUnits` wrapper by default, but `codeunits` may optionally be defined for new string types if necessary.

# Examples

```jldoctest
julia> codeunits("Juλia")
6-element Base.CodeUnits{UInt8, String}:
 0x4a
 0x75
 0xce
 0xbb
 0x69
 0x61
```



collect:
==================================================

```
collect(element_type, collection)
```

Return an `Array` with the given element type of all items in a collection or iterable. The result has the same shape and number of dimensions as `collection`.

# Examples

```jldoctest
julia> collect(Float64, 1:2:5)
3-element Vector{Float64}:
 1.0
 3.0
 5.0
```

```
collect(collection)
```

Return an `Array` of all items in a collection or iterator. For dictionaries, returns a `Vector` of `key=>value` [Pair](@ref Pair)s. If the argument is array-like or is an iterator with the [`HasShape`](@ref IteratorSize) trait, the result will have the same shape and number of dimensions as the argument.

Used by [comprehensions](@ref man-comprehensions) to turn a [generator expression](@ref man-generators) into an `Array`. Thus, *on generators*, the square-brackets notation may be used instead of calling `collect`, see second example.

# Examples

Collect items from a `UnitRange{Int64}` collection:

```jldoctest
julia> collect(1:3)
3-element Vector{Int64}:
 1
 2
 3
```

Collect items from a generator (same output as `[x^2 for x in 1:3]`):

```jldoctest
julia> collect(x^2 for x in 1:3)
3-element Vector{Int64}:
 1
 4
 9
```



complex:
==================================================

```
complex(r, [i])
```

Convert real numbers or arrays to complex. `i` defaults to zero.

# Examples

```jldoctest
julia> complex(7)
7 + 0im

julia> complex([1, 2, 3])
3-element Vector{Complex{Int64}}:
 1 + 0im
 2 + 0im
 3 + 0im
```

```
complex(T::Type)
```

Return an appropriate type which can represent a value of type `T` as a complex number. Equivalent to `typeof(complex(zero(T)))` if `T` does not contain `Missing`.

# Examples

```jldoctest
julia> complex(Complex{Int})
Complex{Int64}

julia> complex(Int)
Complex{Int64}

julia> complex(Union{Int, Missing})
Union{Missing, Complex{Int64}}
```



conj:
==================================================

```
conj(z)
```

Compute the complex conjugate of a complex number `z`.

See also: [`angle`](@ref), [`adjoint`](@ref).

# Examples

```jldoctest
julia> conj(1 + 3im)
1 - 3im
```

```
conj(A::AbstractArray)
```

Return an array containing the complex conjugate of each entry in array `A`.

Equivalent to `conj.(A)`, except that when `eltype(A) <: Real` `A` is returned without copying, and that when `A` has zero dimensions, a 0-dimensional array is returned (rather than a scalar).

# Examples

```jldoctest
julia> conj([1, 2im, 3 + 4im])
3-element Vector{Complex{Int64}}:
 1 + 0im
 0 - 2im
 3 - 4im

julia> conj(fill(2 - im))
0-dimensional Array{Complex{Int64}, 0}:
2 + 1im
```



conj!:
==================================================

```
conj!(A)
```

Transform an array to its complex conjugate in-place.

See also [`conj`](@ref).

# Examples

```jldoctest
julia> A = [1+im 2-im; 2+2im 3+im]
2×2 Matrix{Complex{Int64}}:
 1+1im  2-1im
 2+2im  3+1im

julia> conj!(A);

julia> A
2×2 Matrix{Complex{Int64}}:
 1-1im  2+1im
 2-2im  3-1im
```



contains:
==================================================

```
contains(haystack::AbstractString, needle)
```

Return `true` if `haystack` contains `needle`. This is the same as `occursin(needle, haystack)`, but is provided for consistency with `startswith(haystack, needle)` and `endswith(haystack, needle)`.

See also [`occursin`](@ref), [`in`](@ref), [`issubset`](@ref).

# Examples

```jldoctest
julia> contains("JuliaLang is pretty cool!", "Julia")
true

julia> contains("JuliaLang is pretty cool!", 'a')
true

julia> contains("aba", r"a.a")
true

julia> contains("abba", r"a.a")
false
```

!!! compat "Julia 1.5"
    The `contains` function requires at least Julia 1.5.


```
contains(needle)
```

Create a function that checks whether its argument contains `needle`, i.e. a function equivalent to `haystack -> contains(haystack, needle)`.

The returned function is of type `Base.Fix2{typeof(contains)}`, which can be used to implement specialized methods.



contractuser:
==================================================

```
contractuser(path::AbstractString) -> AbstractString
```

On Unix systems, if the path starts with `homedir()`, replace it with a tilde character.

See also: [`expanduser`](@ref).



convert:
==================================================

```
convert(T, x)
```

Convert `x` to a value of type `T`.

If `T` is an [`Integer`](@ref) type, an [`InexactError`](@ref) will be raised if `x` is not representable by `T`, for example if `x` is not integer-valued, or is outside the range supported by `T`.

# Examples

```jldoctest
julia> convert(Int, 3.0)
3

julia> convert(Int, 3.5)
ERROR: InexactError: Int64(3.5)
Stacktrace:
[...]
```

If `T` is a [`AbstractFloat`](@ref) type, then it will return the closest value to `x` representable by `T`. Inf is treated as one ulp greater than `floatmax(T)` for purposes of determining nearest.

```jldoctest
julia> x = 1/3
0.3333333333333333

julia> convert(Float32, x)
0.33333334f0

julia> convert(BigFloat, x)
0.333333333333333314829616256247390992939472198486328125
```

If `T` is a collection type and `x` a collection, the result of `convert(T, x)` may alias all or part of `x`.

```jldoctest
julia> x = Int[1, 2, 3];

julia> y = convert(Vector{Int}, x);

julia> y === x
true
```

See also: [`round`](@ref), [`trunc`](@ref), [`oftype`](@ref), [`reinterpret`](@ref).



copy:
==================================================

```
copy(x)
```

Create a shallow copy of `x`: the outer structure is copied, but not all internal values. For example, copying an array produces a new array with identically-same elements as the original.

See also [`copy!`](@ref Base.copy!), [`copyto!`](@ref), [`deepcopy`](@ref).

```
copy(A::Transpose)
copy(A::Adjoint)
```

Eagerly evaluate the lazy matrix transpose/adjoint. Note that the transposition is applied recursively to elements.

This operation is intended for linear algebra usage - for general data manipulation see [`permutedims`](@ref Base.permutedims), which is non-recursive.

# Examples

```jldoctest
julia> A = [1 2im; -3im 4]
2×2 Matrix{Complex{Int64}}:
 1+0im  0+2im
 0-3im  4+0im

julia> T = transpose(A)
2×2 transpose(::Matrix{Complex{Int64}}) with eltype Complex{Int64}:
 1+0im  0-3im
 0+2im  4+0im

julia> copy(T)
2×2 Matrix{Complex{Int64}}:
 1+0im  0-3im
 0+2im  4+0im
```



copy!:
==================================================

```
copy!(dst, src) -> dst
```

In-place [`copy`](@ref) of `src` into `dst`, discarding any pre-existing elements in `dst`. If `dst` and `src` are of the same type, `dst == src` should hold after the call. If `dst` and `src` are multidimensional arrays, they must have equal [`axes`](@ref).

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


See also [`copyto!`](@ref).

!!! compat "Julia 1.1"
    This method requires at least Julia 1.1. In Julia 1.0 this method is available from the `Future` standard library as `Future.copy!`.




copyline:
==================================================

```
copyline(out::IO, io::IO=stdin; keep::Bool=false)
copyline(out::IO, filename::AbstractString; keep::Bool=false)
```

Copy a single line of text from an I/O `stream` or a file to the `out` stream, returning `out`.

When reading from a file, the text is assumed to be encoded in UTF-8. Lines in the input end with `'\n'` or `"\r\n"` or the end of an input stream. When `keep` is false (as it is by default), these trailing newline characters are removed from the line before it is returned. When `keep` is true, they are returned as part of the line.

Similar to [`readline`](@ref), which returns a `String`; in contrast, `copyline` writes directly to `out`, without allocating a string. (This can be used, for example, to read data into a pre-allocated [`IOBuffer`](@ref).)

See also [`copyuntil`](@ref) for reading until more general delimiters.

# Examples

```jldoctest
julia> write("my_file.txt", "JuliaLang is a GitHub organization.\nIt has many members.\n");

julia> String(take!(copyline(IOBuffer(), "my_file.txt")))
"JuliaLang is a GitHub organization."

julia> String(take!(copyline(IOBuffer(), "my_file.txt", keep=true)))
"JuliaLang is a GitHub organization.\n"

julia> rm("my_file.txt")
```



copysign:
==================================================

```
copysign(x, y) -> z
```

Return `z` which has the magnitude of `x` and the same sign as `y`.

# Examples

```jldoctest
julia> copysign(1, -2)
-1

julia> copysign(-1, 2)
1
```



copyto!:
==================================================

```
copyto!(dest, do, src, so, N)
```

Copy `N` elements from collection `src` starting at the linear index `so`, to array `dest` starting at the index `do`. Return `dest`.

```
copyto!(dest::AbstractArray, src) -> dest
```

Copy all elements from collection `src` to array `dest`, whose length must be greater than or equal to the length `n` of `src`. The first `n` elements of `dest` are overwritten, the other elements are left untouched.

See also [`copy!`](@ref Base.copy!), [`copy`](@ref).

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


# Examples

```jldoctest
julia> x = [1., 0., 3., 0., 5.];

julia> y = zeros(7);

julia> copyto!(y, x);

julia> y
7-element Vector{Float64}:
 1.0
 0.0
 3.0
 0.0
 5.0
 0.0
 0.0
```

```
copyto!(dest, Rdest::CartesianIndices, src, Rsrc::CartesianIndices) -> dest
```

Copy the block of `src` in the range of `Rsrc` to the block of `dest` in the range of `Rdest`. The sizes of the two regions must match.

# Examples

```jldoctest
julia> A = zeros(5, 5);

julia> B = [1 2; 3 4];

julia> Ainds = CartesianIndices((2:3, 2:3));

julia> Binds = CartesianIndices(B);

julia> copyto!(A, Ainds, B, Binds)
5×5 Matrix{Float64}:
 0.0  0.0  0.0  0.0  0.0
 0.0  1.0  2.0  0.0  0.0
 0.0  3.0  4.0  0.0  0.0
 0.0  0.0  0.0  0.0  0.0
 0.0  0.0  0.0  0.0  0.0
```

```
copyto!(B::AbstractMatrix, ir_dest::AbstractUnitRange, jr_dest::AbstractUnitRange,
        tM::AbstractChar,
        M::AbstractVecOrMat, ir_src::AbstractUnitRange, jr_src::AbstractUnitRange) -> B
```

Efficiently copy elements of matrix `M` to `B` conditioned on the character parameter `tM` as follows:

|  `tM` | Destination           | Source                         |
| -----:|:--------------------- |:------------------------------ |
| `'N'` | `B[ir_dest, jr_dest]` | `M[ir_src, jr_src]`            |
| `'T'` | `B[ir_dest, jr_dest]` | `transpose(M)[ir_src, jr_src]` |
| `'C'` | `B[ir_dest, jr_dest]` | `adjoint(M)[ir_src, jr_src]`   |

The elements `B[ir_dest, jr_dest]` are overwritten. Furthermore, the index range parameters must satisfy `length(ir_dest) == length(ir_src)` and `length(jr_dest) == length(jr_src)`.

See also [`copy_transpose!`](@ref) and [`copy_adjoint!`](@ref).

```
copyto!(dest::AbstractMatrix, src::UniformScaling)
```

Copies a [`UniformScaling`](@ref) onto a matrix.

!!! compat "Julia 1.1"
    In Julia 1.0 this method only supported a square destination matrix. Julia 1.1. added support for a rectangular matrix.




copyuntil:
==================================================

```
copyuntil(out::IO, stream::IO, delim; keep::Bool = false)
copyuntil(out::IO, filename::AbstractString, delim; keep::Bool = false)
```

Copy a string from an I/O `stream` or a file, up to the given delimiter, to the `out` stream, returning `out`. The delimiter can be a `UInt8`, `AbstractChar`, string, or vector. Keyword argument `keep` controls whether the delimiter is included in the result. The text is assumed to be encoded in UTF-8.

Similar to [`readuntil`](@ref), which returns a `String`; in contrast, `copyuntil` writes directly to `out`, without allocating a string. (This can be used, for example, to read data into a pre-allocated [`IOBuffer`](@ref).)

# Examples

```jldoctest
julia> write("my_file.txt", "JuliaLang is a GitHub organization.\nIt has many members.\n");

julia> String(take!(copyuntil(IOBuffer(), "my_file.txt", 'L')))
"Julia"

julia> String(take!(copyuntil(IOBuffer(), "my_file.txt", '.', keep = true)))
"JuliaLang is a GitHub organization."

julia> rm("my_file.txt")
```



cos:
==================================================

```
cos(x)
```

Compute cosine of `x`, where `x` is in radians.

See also [`cosd`](@ref), [`cospi`](@ref), [`sincos`](@ref), [`cis`](@ref).

```
cos(A::AbstractMatrix)
```

Compute the matrix cosine of a square matrix `A`.

If `A` is symmetric or Hermitian, its eigendecomposition ([`eigen`](@ref)) is used to compute the cosine. Otherwise, the cosine is determined by calling [`exp`](@ref).

# Examples

```jldoctest
julia> cos(fill(1.0, (2,2)))
2×2 Matrix{Float64}:
  0.291927  -0.708073
 -0.708073   0.291927
```



cosc:
==================================================

```
cosc(x)
```

Compute $\cos(\pi x) / x - \sin(\pi x) / (\pi x^2)$ if $x \neq 0$, and $0$ if $x = 0$. This is the derivative of `sinc(x)`.

See also [`sinc`](@ref).



cosd:
==================================================

```
cosd(x)
```

Compute cosine of `x`, where `x` is in degrees. If `x` is a matrix, `x` needs to be a square matrix.

!!! compat "Julia 1.7"
    Matrix arguments require Julia 1.7 or later.




cosh:
==================================================

```
cosh(x)
```

Compute hyperbolic cosine of `x`.

```
cosh(A::AbstractMatrix)
```

Compute the matrix hyperbolic cosine of a square matrix `A`.



cospi:
==================================================

```
cospi(x)
```

Compute $\cos(\pi x)$ more accurately than `cos(pi*x)`, especially for large `x`.



cot:
==================================================

```
cot(x)
```

Compute the cotangent of `x`, where `x` is in radians.

```
cot(A::AbstractMatrix)
```

Compute the matrix cotangent of a square matrix `A`.



cotd:
==================================================

```
cotd(x)
```

Compute the cotangent of `x`, where `x` is in degrees.



coth:
==================================================

```
coth(x)
```

Compute the hyperbolic cotangent of `x`.

```
coth(A::AbstractMatrix)
```

Compute the matrix hyperbolic cotangent of square matrix `A`.



count:
==================================================

```
count([f=identity,] itr; init=0) -> Integer
```

Count the number of elements in `itr` for which the function `f` returns `true`. If `f` is omitted, count the number of `true` elements in `itr` (which should be a collection of boolean values). `init` optionally specifies the value to start counting from and therefore also determines the output type.

!!! compat "Julia 1.6"
    `init` keyword was added in Julia 1.6.


See also: [`any`](@ref), [`sum`](@ref).

# Examples

```jldoctest
julia> count(i->(4<=i<=6), [2,3,4,5,6])
3

julia> count([true, false, true, true])
3

julia> count(>(3), 1:7, init=0x03)
0x07
```

```
count(
    pattern::Union{AbstractChar,AbstractString,AbstractPattern},
    string::AbstractString;
    overlap::Bool = false,
)
```

Return the number of matches for `pattern` in `string`. This is equivalent to calling `length(findall(pattern, string))` but more efficient.

If `overlap=true`, the matching sequences are allowed to overlap indices in the original string, otherwise they must be from disjoint character ranges.

!!! compat "Julia 1.3"
    This method requires at least Julia 1.3.


!!! compat "Julia 1.7"
    Using a character as the pattern requires at least Julia 1.7.


# Examples

```jldoctest
julia> count('a', "JuliaLang")
2

julia> count(r"a(.)a", "cabacabac", overlap=true)
3

julia> count(r"a(.)a", "cabacabac")
2
```

```
count([f=identity,] A::AbstractArray; dims=:)
```

Count the number of elements in `A` for which `f` returns `true` over the given dimensions.

!!! compat "Julia 1.5"
    `dims` keyword was added in Julia 1.5.


!!! compat "Julia 1.6"
    `init` keyword was added in Julia 1.6.


# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> count(<=(2), A, dims=1)
1×2 Matrix{Int64}:
 1  1

julia> count(<=(2), A, dims=2)
2×1 Matrix{Int64}:
 2
 0
```



count!:
==================================================

```
count!([f=identity,] r, A)
```

Count the number of elements in `A` for which `f` returns `true` over the singleton dimensions of `r`, writing the result into `r` in-place.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


!!! compat "Julia 1.5"
    inplace `count!` was added in Julia 1.5.


# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> count!(<=(2), [1 1], A)
1×2 Matrix{Int64}:
 1  1

julia> count!(<=(2), [1; 1], A)
2-element Vector{Int64}:
 2
 0
```



count_ones:
==================================================

```
count_ones(x::Integer) -> Integer
```

Number of ones in the binary representation of `x`.

# Examples

```jldoctest
julia> count_ones(7)
3

julia> count_ones(Int32(-1))
32
```



count_zeros:
==================================================

```
count_zeros(x::Integer) -> Integer
```

Number of zeros in the binary representation of `x`.

# Examples

```jldoctest
julia> count_zeros(Int32(2 ^ 16 - 1))
16

julia> count_zeros(-1)
0
```



countlines:
==================================================

```
countlines(io::IO; eol::AbstractChar = '\n')
countlines(filename::AbstractString; eol::AbstractChar = '\n')
```

Read `io` until the end of the stream/file and count the number of lines. To specify a file pass the filename as the first argument. EOL markers other than `'\n'` are supported by passing them as the second argument.  The last non-empty line of `io` is counted even if it does not end with the EOL, matching the length returned by [`eachline`](@ref) and [`readlines`](@ref).

To count lines of a `String`, `countlines(IOBuffer(str))` can be used.

# Examples

```jldoctest
julia> io = IOBuffer("JuliaLang is a GitHub organization.\n");

julia> countlines(io)
1

julia> io = IOBuffer("JuliaLang is a GitHub organization.");

julia> countlines(io)
1

julia> eof(io) # counting lines moves the file pointer
true

julia> io = IOBuffer("JuliaLang is a GitHub organization.");

julia> countlines(io, eol = '.')
1
```

```jldoctest
julia> write("my_file.txt", "JuliaLang is a GitHub organization.\n")
36

julia> countlines("my_file.txt")
1

julia> countlines("my_file.txt", eol = 'n')
4

julia> rm("my_file.txt")

```



cp:
==================================================

```
cp(src::AbstractString, dst::AbstractString; force::Bool=false, follow_symlinks::Bool=false)
```

Copy the file, link, or directory from `src` to `dst`. `force=true` will first remove an existing `dst`.

If `follow_symlinks=false`, and `src` is a symbolic link, `dst` will be created as a symbolic link. If `follow_symlinks=true` and `src` is a symbolic link, `dst` will be a copy of the file or directory `src` refers to. Return `dst`.

!!! note
    The `cp` function is different from the `cp` command. The `cp` function always operates on the assumption that `dst` is a file, while the command does different things depending on whether `dst` is a directory or a file. Using `force=true` when `dst` is a directory will result in loss of all the contents present in the `dst` directory, and `dst` will become a file that has the contents of `src` instead.




csc:
==================================================

```
csc(x)
```

Compute the cosecant of `x`, where `x` is in radians.

```
csc(A::AbstractMatrix)
```

Compute the matrix cosecant of a square matrix `A`.



cscd:
==================================================

```
cscd(x)
```

Compute the cosecant of `x`, where `x` is in degrees.



csch:
==================================================

```
csch(x)
```

Compute the hyperbolic cosecant of `x`.

```
csch(A::AbstractMatrix)
```

Compute the matrix hyperbolic cosecant of square matrix `A`.



ctime:
==================================================

```
ctime(file)
```

Equivalent to `stat(file).ctime`.



cumprod:
==================================================

```
cumprod(A; dims::Integer)
```

Cumulative product along the dimension `dim`. See also [`cumprod!`](@ref) to use a preallocated output array, both for performance and to control the precision of the output (e.g. to avoid overflow).

# Examples

```jldoctest
julia> a = Int8[1 2 3; 4 5 6];

julia> cumprod(a, dims=1)
2×3 Matrix{Int64}:
 1   2   3
 4  10  18

julia> cumprod(a, dims=2)
2×3 Matrix{Int64}:
 1   2    6
 4  20  120
```

```
cumprod(itr)
```

Cumulative product of an iterator.

See also [`cumprod!`](@ref), [`accumulate`](@ref), [`cumsum`](@ref).

!!! compat "Julia 1.5"
    `cumprod` on a non-array iterator requires at least Julia 1.5.


# Examples

```jldoctest
julia> cumprod(fill(1//2, 3))
3-element Vector{Rational{Int64}}:
 1//2
 1//4
 1//8

julia> cumprod((1, 2, 1, 3, 1))
(1, 2, 2, 6, 6)

julia> cumprod("julia")
5-element Vector{String}:
 "j"
 "ju"
 "jul"
 "juli"
 "julia"
```



cumprod!:
==================================================

```
cumprod!(B, A; dims::Integer)
```

Cumulative product of `A` along the dimension `dims`, storing the result in `B`. See also [`cumprod`](@ref).

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


```
cumprod!(y::AbstractVector, x::AbstractVector)
```

Cumulative product of a vector `x`, storing the result in `y`. See also [`cumprod`](@ref).

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.




cumsum:
==================================================

```
cumsum(A; dims::Integer)
```

Cumulative sum along the dimension `dims`. See also [`cumsum!`](@ref) to use a preallocated output array, both for performance and to control the precision of the output (e.g. to avoid overflow).

# Examples

```jldoctest
julia> a = [1 2 3; 4 5 6]
2×3 Matrix{Int64}:
 1  2  3
 4  5  6

julia> cumsum(a, dims=1)
2×3 Matrix{Int64}:
 1  2  3
 5  7  9

julia> cumsum(a, dims=2)
2×3 Matrix{Int64}:
 1  3   6
 4  9  15
```

!!! note
    The return array's `eltype` is `Int` for signed integers of less than system word size  and `UInt` for unsigned integers of less than system word size. To preserve `eltype` of arrays with small signed or unsigned integer `accumulate(+, A)` should be used.

    ```jldoctest
    julia> cumsum(Int8[100, 28])
    2-element Vector{Int64}:
     100
     128

    julia> accumulate(+,Int8[100, 28])
    2-element Vector{Int8}:
      100
     -128
    ```

    In the former case, the integers are widened to system word size and therefore the result is `Int64[100, 128]`. In the latter case, no such widening happens and integer overflow results in `Int8[100, -128]`.


```
cumsum(itr)
```

Cumulative sum of an iterator.

See also [`accumulate`](@ref) to apply functions other than `+`.

!!! compat "Julia 1.5"
    `cumsum` on a non-array iterator requires at least Julia 1.5.


# Examples

```jldoctest
julia> cumsum(1:3)
3-element Vector{Int64}:
 1
 3
 6

julia> cumsum((true, false, true, false, true))
(1, 1, 2, 2, 3)

julia> cumsum(fill(1, 2) for i in 1:3)
3-element Vector{Vector{Int64}}:
 [1, 1]
 [2, 2]
 [3, 3]
```



cumsum!:
==================================================

```
cumsum!(B, A; dims::Integer)
```

Cumulative sum of `A` along the dimension `dims`, storing the result in `B`. See also [`cumsum`](@ref).

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.




current_exceptions:
==================================================

```
current_exceptions(task::Task=current_task(); [backtrace::Bool=true])
```

Get the stack of exceptions currently being handled. For nested catch blocks there may be more than one current exception in which case the most recently thrown exception is last in the stack. The stack is returned as an `ExceptionStack` which is an AbstractVector of named tuples `(exception,backtrace)`. If `backtrace` is false, the backtrace in each pair will be set to `nothing`.

Explicitly passing `task` will return the current exception stack on an arbitrary task. This is useful for inspecting tasks which have failed due to uncaught exceptions.

!!! compat "Julia 1.7"
    This function went by the experimental name `catch_stack()` in Julia 1.1–1.6, and had a plain Vector-of-tuples as a return type.




current_task:
==================================================

```
current_task()
```

Get the currently running [`Task`](@ref).



deepcopy:
==================================================

```
deepcopy(x)
```

Create a deep copy of `x`: everything is copied recursively, resulting in a fully independent object. For example, deep-copying an array creates deep copies of all the objects it contains and produces a new array with the consistent relationship structure (e.g., if the first two elements are the same object in the original array, the first two elements of the new array will also be the same `deepcopy`ed object). Calling `deepcopy` on an object should generally have the same effect as serializing and then deserializing it.

While it isn't normally necessary, user-defined types can override the default `deepcopy` behavior by defining a specialized version of the function `deepcopy_internal(x::T, dict::IdDict)` (which shouldn't otherwise be used), where `T` is the type to be specialized for, and `dict` keeps track of objects copied so far within the recursion. Within the definition, `deepcopy_internal` should be used in place of `deepcopy`, and the `dict` variable should be updated as appropriate before returning.



deg2rad:
==================================================

```
deg2rad(x)
```

Convert `x` from degrees to radians.

See also [`rad2deg`](@ref), [`sind`](@ref), [`pi`](@ref).

# Examples

```jldoctest
julia> deg2rad(90)
1.5707963267948966
```



delete!:
==================================================

```
delete!(collection, key)
```

Delete the mapping for the given key in a collection, if any, and return the collection.

# Examples

```jldoctest
julia> d = Dict("a"=>1, "b"=>2)
Dict{String, Int64} with 2 entries:
  "b" => 2
  "a" => 1

julia> delete!(d, "b")
Dict{String, Int64} with 1 entry:
  "a" => 1

julia> delete!(d, "b") # d is left unchanged
Dict{String, Int64} with 1 entry:
  "a" => 1
```



deleteat!:
==================================================

```
deleteat!(a::Vector, i::Integer)
```

Remove the item at the given `i` and return the modified `a`. Subsequent items are shifted to fill the resulting gap.

See also: [`keepat!`](@ref), [`delete!`](@ref), [`popat!`](@ref), [`splice!`](@ref).

# Examples

```jldoctest
julia> deleteat!([6, 5, 4, 3, 2, 1], 2)
5-element Vector{Int64}:
 6
 4
 3
 2
 1
```

```
deleteat!(a::Vector, inds)
```

Remove the items at the indices given by `inds`, and return the modified `a`. Subsequent items are shifted to fill the resulting gap.

`inds` can be either an iterator or a collection of sorted and unique integer indices, or a boolean vector of the same length as `a` with `true` indicating entries to delete.

# Examples

```jldoctest
julia> deleteat!([6, 5, 4, 3, 2, 1], 1:2:5)
3-element Vector{Int64}:
 5
 3
 1

julia> deleteat!([6, 5, 4, 3, 2, 1], [true, false, true, false, true, false])
3-element Vector{Int64}:
 5
 3
 1

julia> deleteat!([6, 5, 4, 3, 2, 1], (2, 2))
ERROR: ArgumentError: indices must be unique and sorted
Stacktrace:
[...]
```



denominator:
==================================================

```
denominator(x)
```

Denominator of the rational representation of `x`.

# Examples

```jldoctest
julia> denominator(2//3)
3

julia> denominator(4)
1
```



detach:
==================================================

```
detach(command)
```

Mark a command object so that it will be run in a new process group, allowing it to outlive the julia process, and not have Ctrl-C interrupts passed to it.



devnull:
==================================================

No documentation found for private symbol.

# Summary

```
struct Base.DevNull
```

# Supertype Hierarchy

```
Base.DevNull <: IO <: Any
```



diff:
==================================================

```
diff(A::AbstractVector)
diff(A::AbstractArray; dims::Integer)
```

Finite difference operator on a vector or a multidimensional array `A`. In the latter case the dimension to operate on needs to be specified with the `dims` keyword argument.

!!! compat "Julia 1.1"
    `diff` for arrays with dimension higher than 2 requires at least Julia 1.1.


# Examples

```jldoctest
julia> a = [2 4; 6 16]
2×2 Matrix{Int64}:
 2   4
 6  16

julia> diff(a, dims=2)
2×1 Matrix{Int64}:
  2
 10

julia> diff(vec(a))
3-element Vector{Int64}:
  4
 -2
 12
```



digits:
==================================================

```
digits([T<:Integer], n::Integer; base::T = 10, pad::Integer = 1)
```

Return an array with element type `T` (default `Int`) of the digits of `n` in the given base, optionally padded with zeros to a specified size. More significant digits are at higher indices, such that `n == sum(digits[k]*base^(k-1) for k=1:length(digits))`.

See also [`ndigits`](@ref), [`digits!`](@ref), and for base 2 also [`bitstring`](@ref), [`count_ones`](@ref).

# Examples

```jldoctest
julia> digits(10)
2-element Vector{Int64}:
 0
 1

julia> digits(10, base = 2)
4-element Vector{Int64}:
 0
 1
 0
 1

julia> digits(-256, base = 10, pad = 5)
5-element Vector{Int64}:
 -6
 -5
 -2
  0
  0

julia> n = rand(-999:999);

julia> n == evalpoly(13, digits(n, base = 13))
true
```



digits!:
==================================================

```
digits!(array, n::Integer; base::Integer = 10)
```

Fills an array of the digits of `n` in the given base. More significant digits are at higher indices. If the array length is insufficient, the least significant digits are filled up to the array length. If the array length is excessive, the excess portion is filled with zeros.

# Examples

```jldoctest
julia> digits!([2, 2, 2, 2], 10, base = 2)
4-element Vector{Int64}:
 0
 1
 0
 1

julia> digits!([2, 2, 2, 2, 2, 2], 10, base = 2)
6-element Vector{Int64}:
 0
 1
 0
 1
 0
 0
```



dirname:
==================================================

```
dirname(path::AbstractString) -> String
```

Get the directory part of a path. Trailing characters ('/' or '\') in the path are counted as part of the path.

# Examples

```jldoctest
julia> dirname("/home/myuser")
"/home"

julia> dirname("/home/myuser/")
"/home/myuser"
```

See also [`basename`](@ref).



disable_sigint:
==================================================

```
disable_sigint(f::Function)
```

Disable Ctrl-C handler during execution of a function on the current task, for calling external code that may call julia code that is not interrupt safe. Intended to be called using `do` block syntax as follows:

```
disable_sigint() do
    # interrupt-unsafe code
    ...
end
```

This is not needed on worker threads (`Threads.threadid() != 1`) since the `InterruptException` will only be delivered to the master thread. External functions that do not call julia code or julia runtime automatically disable sigint during their execution.



diskstat:
==================================================

```
diskstat(path=pwd())
```

Returns statistics in bytes about the disk that contains the file or directory pointed at by `path`. If no argument is passed, statistics about the disk that contains the current working directory are returned.

!!! compat "Julia 1.8"
    This method was added in Julia 1.8.




display:
==================================================

```
display(x)
display(d::AbstractDisplay, x)
display(mime, x)
display(d::AbstractDisplay, mime, x)
```

Display `x` using the topmost applicable display in the display stack, typically using the richest supported multimedia output for `x`, with plain-text [`stdout`](@ref) output as a fallback. The `display(d, x)` variant attempts to display `x` on the given display `d` only, throwing a [`MethodError`](@ref) if `d` cannot display objects of this type.

In general, you cannot assume that `display` output goes to `stdout` (unlike [`print(x)`](@ref) or [`show(x)`](@ref)).  For example, `display(x)` may open up a separate window with an image. `display(x)` means "show `x` in the best way you can for the current output device(s)." If you want REPL-like text output that is guaranteed to go to `stdout`, use [`show(stdout, "text/plain", x)`](@ref) instead.

There are also two variants with a `mime` argument (a MIME type string, such as `"image/png"`), which attempt to display `x` using the requested MIME type *only*, throwing a `MethodError` if this type is not supported by either the display(s) or by `x`. With these variants, one can also supply the "raw" data in the requested MIME type by passing `x::AbstractString` (for MIME types with text-based storage, such as text/html or application/postscript) or `x::Vector{UInt8}` (for binary MIME types).

To customize how instances of a type are displayed, overload [`show`](@ref) rather than `display`, as explained in the manual section on [custom pretty-printing](@ref man-custom-pretty-printing).



displayable:
==================================================

```
displayable(mime) -> Bool
displayable(d::AbstractDisplay, mime) -> Bool
```

Return a boolean value indicating whether the given `mime` type (string) is displayable by any of the displays in the current display stack, or specifically by the display `d` in the second variant.



displaysize:
==================================================

```
displaysize([io::IO]) -> (lines, columns)
```

Return the nominal size of the screen that may be used for rendering output to this `IO` object. If no input is provided, the environment variables `LINES` and `COLUMNS` are read. If those are not set, a default size of `(24, 80)` is returned.

# Examples

```jldoctest
julia> withenv("LINES" => 30, "COLUMNS" => 100) do
           displaysize()
       end
(30, 100)
```

To get your TTY size,

```julia-repl
julia> displaysize(stdout)
(34, 147)
```



div:
==================================================

```
div(x, y)
÷(x, y)
```

The quotient from Euclidean (integer) division. Generally equivalent to a mathematical operation x/y without a fractional part.

See also: [`cld`](@ref), [`fld`](@ref), [`rem`](@ref), [`divrem`](@ref).

# Examples

```jldoctest
julia> 9 ÷ 4
2

julia> -5 ÷ 3
-1

julia> 5.0 ÷ 2
2.0

julia> div.(-5:5, 3)'
1×11 adjoint(::Vector{Int64}) with eltype Int64:
 -1  -1  -1  0  0  0  0  0  1  1  1
```

```
div(x, y, r::RoundingMode=RoundToZero)
```

The quotient from Euclidean (integer) division. Computes `x / y`, rounded to an integer according to the rounding mode `r`. In other words, the quantity

```
round(x / y, r)
```

without any intermediate rounding.

!!! compat "Julia 1.4"
    The three-argument method taking a `RoundingMode` requires Julia 1.4 or later.


See also [`fld`](@ref) and [`cld`](@ref), which are special cases of this function.

!!! compat "Julia 1.9"
    `RoundFromZero` requires at least Julia 1.9.


# Examples:

```jldoctest
julia> div(4, 3, RoundToZero) # Matches div(4, 3)
1
julia> div(4, 3, RoundDown) # Matches fld(4, 3)
1
julia> div(4, 3, RoundUp) # Matches cld(4, 3)
2
julia> div(5, 2, RoundNearest)
2
julia> div(5, 2, RoundNearestTiesAway)
3
julia> div(-5, 2, RoundNearest)
-2
julia> div(-5, 2, RoundNearestTiesAway)
-3
julia> div(-5, 2, RoundNearestTiesUp)
-2
julia> div(4, 3, RoundFromZero)
2
julia> div(-4, 3, RoundFromZero)
-2
```



divrem:
==================================================

```
divrem(x, y, r::RoundingMode=RoundToZero)
```

The quotient and remainder from Euclidean division. Equivalent to `(div(x, y, r), rem(x, y, r))`. Equivalently, with the default value of `r`, this call is equivalent to `(x ÷ y, x % y)`.

See also: [`fldmod`](@ref), [`cld`](@ref).

# Examples

```jldoctest
julia> divrem(3, 7)
(0, 3)

julia> divrem(7, 3)
(2, 1)
```



download:
==================================================

```
download(url::AbstractString, [path::AbstractString = tempname()]) -> path
```

Download a file from the given url, saving it to the location `path`, or if not specified, a temporary path. Returns the path of the downloaded file.

!!! note
    Since Julia 1.6, this function is deprecated and is just a thin wrapper around `Downloads.download`. In new code, you should use that function directly instead of calling this.




dropdims:
==================================================

```
dropdims(A; dims)
```

Return an array with the same data as `A`, but with the dimensions specified by `dims` removed. `size(A,d)` must equal 1 for every `d` in `dims`, and repeated dimensions or numbers outside `1:ndims(A)` are forbidden.

The result shares the same underlying data as `A`, such that the result is mutable if and only if `A` is mutable, and setting elements of one alters the values of the other.

See also: [`reshape`](@ref), [`vec`](@ref).

# Examples

```jldoctest
julia> a = reshape(Vector(1:4),(2,2,1,1))
2×2×1×1 Array{Int64, 4}:
[:, :, 1, 1] =
 1  3
 2  4

julia> b = dropdims(a; dims=3)
2×2×1 Array{Int64, 3}:
[:, :, 1] =
 1  3
 2  4

julia> b[1,1,1] = 5; a
2×2×1×1 Array{Int64, 4}:
[:, :, 1, 1] =
 5  3
 2  4
```



dump:
==================================================

```
dump(x; maxdepth=8)
```

Show every part of the representation of a value. The depth of the output is truncated at `maxdepth`.

# Examples

```jldoctest
julia> struct MyStruct
           x
           y
       end

julia> x = MyStruct(1, (2,3));

julia> dump(x)
MyStruct
  x: Int64 1
  y: Tuple{Int64, Int64}
    1: Int64 2
    2: Int64 3

julia> dump(x; maxdepth = 1)
MyStruct
  x: Int64 1
  y: Tuple{Int64, Int64}
```



eachcol:
==================================================

```
eachcol(A::AbstractVecOrMat) <: AbstractVector
```

Create a [`ColumnSlices`](@ref) object that is a vector of columns of matrix or vector `A`. Column slices are returned as `AbstractVector` views of `A`.

For the inverse, see [`stack`](@ref)`(cols)` or `reduce(`[`hcat`](@ref)`, cols)`.

See also [`eachrow`](@ref), [`eachslice`](@ref) and [`mapslices`](@ref).

!!! compat "Julia 1.1"
    This function requires at least Julia 1.1.


!!! compat "Julia 1.9"
    Prior to Julia 1.9, this returned an iterator.


# Examples

```jldoctest
julia> a = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> s = eachcol(a)
2-element ColumnSlices{Matrix{Int64}, Tuple{Base.OneTo{Int64}}, SubArray{Int64, 1, Matrix{Int64}, Tuple{Base.Slice{Base.OneTo{Int64}}, Int64}, true}}:
 [1, 3]
 [2, 4]

julia> s[1]
2-element view(::Matrix{Int64}, :, 1) with eltype Int64:
 1
 3
```



eachindex:
==================================================

```
eachindex(A...)
eachindex(::IndexStyle, A::AbstractArray...)
```

Create an iterable object for visiting each index of an `AbstractArray` `A` in an efficient manner. For array types that have opted into fast linear indexing (like `Array`), this is simply the range `1:length(A)` if they use 1-based indexing. For array types that have not opted into fast linear indexing, a specialized Cartesian range is typically returned to efficiently index into the array with indices specified for every dimension.

In general `eachindex` accepts arbitrary iterables, including strings and dictionaries, and returns an iterator object supporting arbitrary index types (e.g. unevenly spaced or non-integer indices).

If `A` is `AbstractArray` it is possible to explicitly specify the style of the indices that should be returned by `eachindex` by passing a value having `IndexStyle` type as its first argument (typically `IndexLinear()` if linear indices are required or `IndexCartesian()` if Cartesian range is wanted).

If you supply more than one `AbstractArray` argument, `eachindex` will create an iterable object that is fast for all arguments (typically a [`UnitRange`](@ref) if all inputs have fast linear indexing, a [`CartesianIndices`](@ref) otherwise). If the arrays have different sizes and/or dimensionalities, a `DimensionMismatch` exception will be thrown.

See also [`pairs`](@ref)`(A)` to iterate over indices and values together, and [`axes`](@ref)`(A, 2)` for valid indices along one dimension.

# Examples

```jldoctest
julia> A = [10 20; 30 40];

julia> for i in eachindex(A) # linear indexing
           println("A[", i, "] == ", A[i])
       end
A[1] == 10
A[2] == 30
A[3] == 20
A[4] == 40

julia> for i in eachindex(view(A, 1:2, 1:1)) # Cartesian indexing
           println(i)
       end
CartesianIndex(1, 1)
CartesianIndex(2, 1)
```



eachline:
==================================================

```
eachline(io::IO=stdin; keep::Bool=false)
eachline(filename::AbstractString; keep::Bool=false)
```

Create an iterable `EachLine` object that will yield each line from an I/O stream or a file. Iteration calls [`readline`](@ref) on the stream argument repeatedly with `keep` passed through, determining whether trailing end-of-line characters are retained. When called with a file name, the file is opened once at the beginning of iteration and closed at the end. If iteration is interrupted, the file will be closed when the `EachLine` object is garbage collected.

To iterate over each line of a `String`, `eachline(IOBuffer(str))` can be used.

[`Iterators.reverse`](@ref) can be used on an `EachLine` object to read the lines in reverse order (for files, buffers, and other I/O streams supporting [`seek`](@ref)), and [`first`](@ref) or [`last`](@ref) can be used to extract the initial or final lines, respectively.

# Examples

```jldoctest
julia> write("my_file.txt", "JuliaLang is a GitHub organization.\n It has many members.\n");

julia> for line in eachline("my_file.txt")
           print(line)
       end
JuliaLang is a GitHub organization. It has many members.

julia> rm("my_file.txt");
```

!!! compat "Julia 1.8"
    Julia 1.8 is required to use `Iterators.reverse` or `last` with `eachline` iterators.




eachmatch:
==================================================

```
eachmatch(r::Regex, s::AbstractString; overlap::Bool=false)
```

Search for all matches of the regular expression `r` in `s` and return an iterator over the matches. If `overlap` is `true`, the matching sequences are allowed to overlap indices in the original string, otherwise they must be from distinct character ranges.

# Examples

```jldoctest
julia> rx = r"a.a"
r"a.a"

julia> m = eachmatch(rx, "a1a2a3a")
Base.RegexMatchIterator{String}(r"a.a", "a1a2a3a", false)

julia> collect(m)
2-element Vector{RegexMatch}:
 RegexMatch("a1a")
 RegexMatch("a3a")

julia> collect(eachmatch(rx, "a1a2a3a", overlap = true))
3-element Vector{RegexMatch}:
 RegexMatch("a1a")
 RegexMatch("a2a")
 RegexMatch("a3a")
```



eachrow:
==================================================

```
eachrow(A::AbstractVecOrMat) <: AbstractVector
```

Create a [`RowSlices`](@ref) object that is a vector of rows of matrix or vector `A`. Row slices are returned as `AbstractVector` views of `A`.

For the inverse, see [`stack`](@ref)`(rows; dims=1)`.

See also [`eachcol`](@ref), [`eachslice`](@ref) and [`mapslices`](@ref).

!!! compat "Julia 1.1"
    This function requires at least Julia 1.1.


!!! compat "Julia 1.9"
    Prior to Julia 1.9, this returned an iterator.


# Examples

```jldoctest
julia> a = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> s = eachrow(a)
2-element RowSlices{Matrix{Int64}, Tuple{Base.OneTo{Int64}}, SubArray{Int64, 1, Matrix{Int64}, Tuple{Int64, Base.Slice{Base.OneTo{Int64}}}, true}}:
 [1, 2]
 [3, 4]

julia> s[1]
2-element view(::Matrix{Int64}, 1, :) with eltype Int64:
 1
 2
```



eachrsplit:
==================================================

```
eachrsplit(str::AbstractString, dlm; limit::Integer=0, keepempty::Bool=true)
eachrsplit(str::AbstractString; limit::Integer=0, keepempty::Bool=false)
```

Return an iterator over `SubString`s of `str`, produced when splitting on the delimiter(s) `dlm`, and yielded in reverse order (from right to left). `dlm` can be any of the formats allowed by [`findprev`](@ref)'s first argument (i.e. a string, a single character or a function), or a collection of characters.

If `dlm` is omitted, it defaults to [`isspace`](@ref), and `keepempty` default to `false`.

The optional keyword arguments are:

  * If `limit > 0`, the iterator will split at most `limit - 1` times before returning the rest of the string unsplit. `limit < 1` implies no cap to splits (default).
  * `keepempty`: whether empty fields should be returned when iterating Default is `false` without a `dlm` argument, `true` with a `dlm` argument.

Note that unlike [`split`](@ref), [`rsplit`](@ref) and [`eachsplit`](@ref), this function iterates the substrings right to left as they occur in the input.

See also [`eachsplit`](@ref), [`rsplit`](@ref).

!!! compat "Julia 1.11"
    This function requires Julia 1.11 or later.


# Examples

```jldoctest
julia> a = "Ma.r.ch";

julia> collect(eachrsplit(a, ".")) == ["ch", "r", "Ma"]
true

julia> collect(eachrsplit(a, "."; limit=2)) == ["ch", "Ma.r"]
true
```



eachslice:
==================================================

```
eachslice(A::AbstractArray; dims, drop=true)
```

Create a [`Slices`](@ref) object that is an array of slices over dimensions `dims` of `A`, returning views that select all the data from the other dimensions in `A`. `dims` can either be an integer or a tuple of integers.

If `drop = true` (the default), the outer `Slices` will drop the inner dimensions, and the ordering of the dimensions will match those in `dims`. If `drop = false`, then the `Slices` will have the same dimensionality as the underlying array, with inner dimensions having size 1.

See [`stack`](@ref)`(slices; dims)` for the inverse of `eachslice(A; dims::Integer)`.

See also [`eachrow`](@ref), [`eachcol`](@ref), [`mapslices`](@ref) and [`selectdim`](@ref).

!!! compat "Julia 1.1"
    This function requires at least Julia 1.1.


!!! compat "Julia 1.9"
    Prior to Julia 1.9, this returned an iterator, and only a single dimension `dims` was supported.


# Examples

```jldoctest
julia> m = [1 2 3; 4 5 6; 7 8 9]
3×3 Matrix{Int64}:
 1  2  3
 4  5  6
 7  8  9

julia> s = eachslice(m, dims=1)
3-element RowSlices{Matrix{Int64}, Tuple{Base.OneTo{Int64}}, SubArray{Int64, 1, Matrix{Int64}, Tuple{Int64, Base.Slice{Base.OneTo{Int64}}}, true}}:
 [1, 2, 3]
 [4, 5, 6]
 [7, 8, 9]

julia> s[1]
3-element view(::Matrix{Int64}, 1, :) with eltype Int64:
 1
 2
 3

julia> eachslice(m, dims=1, drop=false)
3×1 Slices{Matrix{Int64}, Tuple{Int64, Colon}, Tuple{Base.OneTo{Int64}, Base.OneTo{Int64}}, SubArray{Int64, 1, Matrix{Int64}, Tuple{Int64, Base.Slice{Base.OneTo{Int64}}}, true}, 2}:
 [1, 2, 3]
 [4, 5, 6]
 [7, 8, 9]
```



eachsplit:
==================================================

```
eachsplit(str::AbstractString, dlm; limit::Integer=0, keepempty::Bool=true)
eachsplit(str::AbstractString; limit::Integer=0, keepempty::Bool=false)
```

Split `str` on occurrences of the delimiter(s) `dlm` and return an iterator over the substrings.  `dlm` can be any of the formats allowed by [`findnext`](@ref)'s first argument (i.e. as a string, regular expression or a function), or as a single character or collection of characters.

If `dlm` is omitted, it defaults to [`isspace`](@ref).

The optional keyword arguments are:

  * `limit`: the maximum size of the result. `limit=0` implies no maximum (default)
  * `keepempty`: whether empty fields should be kept in the result. Default is `false` without a `dlm` argument, `true` with a `dlm` argument.

See also [`split`](@ref).

!!! compat "Julia 1.8"
    The `eachsplit` function requires at least Julia 1.8.


# Examples

```jldoctest
julia> a = "Ma.rch"
"Ma.rch"

julia> b = eachsplit(a, ".")
Base.SplitIterator{String, String}("Ma.rch", ".", 0, true)

julia> collect(b)
2-element Vector{SubString{String}}:
 "Ma"
 "rch"
```



edit:
==================================================

```
edit(path::AbstractString, line::Integer=0, column::Integer=0)
```

Edit a file or directory optionally providing a line number to edit the file at. Return to the `julia` prompt when you quit the editor. The editor can be changed by setting `JULIA_EDITOR`, `VISUAL` or `EDITOR` as an environment variable.

!!! compat "Julia 1.9"
    The `column` argument requires at least Julia 1.9.


See also [`InteractiveUtils.define_editor`](@ref).

```
edit(function, [types])
edit(module)
```

Edit the definition of a function, optionally specifying a tuple of types to indicate which method to edit. For modules, open the main source file. The module needs to be loaded with `using` or `import` first.

!!! compat "Julia 1.1"
    `edit` on modules requires at least Julia 1.1.


To ensure that the file can be opened at the given line, you may need to call `InteractiveUtils.define_editor` first.



eltype:
==================================================

```
eltype(type)
```

Determine the type of the elements generated by iterating a collection of the given `type`. For dictionary types, this will be a `Pair{KeyType,ValType}`. The definition `eltype(x) = eltype(typeof(x))` is provided for convenience so that instances can be passed instead of types. However the form that accepts a type argument should be defined for new types.

See also: [`keytype`](@ref), [`typeof`](@ref).

# Examples

```jldoctest
julia> eltype(fill(1f0, (2,2)))
Float32

julia> eltype(fill(0x1, (2,2)))
UInt8
```



empty:
==================================================

```
empty(x::Tuple)
```

Return an empty tuple, `()`.

```
empty(v::AbstractVector, [eltype])
```

Create an empty vector similar to `v`, optionally changing the `eltype`.

See also: [`empty!`](@ref), [`isempty`](@ref), [`isassigned`](@ref).

# Examples

```jldoctest
julia> empty([1.0, 2.0, 3.0])
Float64[]

julia> empty([1.0, 2.0, 3.0], String)
String[]
```

```
empty(a::AbstractDict, [index_type=keytype(a)], [value_type=valtype(a)])
```

Create an empty `AbstractDict` container which can accept indices of type `index_type` and values of type `value_type`. The second and third arguments are optional and default to the input's `keytype` and `valtype`, respectively. (If only one of the two types is specified, it is assumed to be the `value_type`, and the `index_type` we default to `keytype(a)`).

Custom `AbstractDict` subtypes may choose which specific dictionary type is best suited to return for the given index and value types, by specializing on the three-argument signature. The default is to return an empty `Dict`.



empty!:
==================================================

```
empty!(collection) -> collection
```

Remove all elements from a `collection`.

# Examples

```jldoctest
julia> A = Dict("a" => 1, "b" => 2)
Dict{String, Int64} with 2 entries:
  "b" => 2
  "a" => 1

julia> empty!(A);

julia> A
Dict{String, Int64}()
```

```
empty!(c::Channel)
```

Empty a Channel `c` by calling `empty!` on the internal buffer. Return the empty channel.



endswith:
==================================================

```
endswith(s::AbstractString, suffix::Union{AbstractString,Base.Chars})
```

Return `true` if `s` ends with `suffix`, which can be a string, a character, or a tuple/vector/set of characters. If `suffix` is a tuple/vector/set of characters, test whether the last character of `s` belongs to that set.

See also [`startswith`](@ref), [`contains`](@ref).

# Examples

```jldoctest
julia> endswith("Sunday", "day")
true
```

```
endswith(suffix)
```

Create a function that checks whether its argument ends with `suffix`, i.e. a function equivalent to `y -> endswith(y, suffix)`.

The returned function is of type `Base.Fix2{typeof(endswith)}`, which can be used to implement specialized methods.

!!! compat "Julia 1.5"
    The single argument `endswith(suffix)` requires at least Julia 1.5.


# Examples

```jldoctest
julia> endswith("Julia")("Ends with Julia")
true

julia> endswith("Julia")("JuliaLang")
false
```

```
endswith(s::AbstractString, suffix::Regex)
```

Return `true` if `s` ends with the regex pattern, `suffix`.

!!! note
    `endswith` does not compile the anchoring into the regular expression, but instead passes the anchoring as `match_option` to PCRE. If compile time is amortized, `occursin(r"...$", s)` is faster than `endswith(s, r"...")`.


See also [`occursin`](@ref) and [`startswith`](@ref).

!!! compat "Julia 1.2"
    This method requires at least Julia 1.2.


# Examples

```jldoctest
julia> endswith("JuliaLang", r"Lang|Roberts")
true
```



enumerate:
==================================================

```
enumerate(iter)
```

An iterator that yields `(i, x)` where `i` is a counter starting at 1, and `x` is the `i`th value from the given iterator. It's useful when you need not only the values `x` over which you are iterating, but also the number of iterations so far.

Note that `i` may not be valid for indexing `iter`, or may index a different element. This will happen if `iter` has indices that do not start at 1, and may happen for strings, dictionaries, etc. See the `pairs(IndexLinear(), iter)` method if you want to ensure that `i` is an index.

# Examples

```jldoctest
julia> a = ["a", "b", "c"];

julia> for (index, value) in enumerate(a)
           println("$index $value")
       end
1 a
2 b
3 c

julia> str = "naïve";

julia> for (i, val) in enumerate(str)
           print("i = ", i, ", val = ", val, ", ")
           try @show(str[i]) catch e println(e) end
       end
i = 1, val = n, str[i] = 'n'
i = 2, val = a, str[i] = 'a'
i = 3, val = ï, str[i] = 'ï'
i = 4, val = v, StringIndexError("naïve", 4)
i = 5, val = e, str[i] = 'v'
```



eof:
==================================================

```
eof(stream) -> Bool
```

Test whether an I/O stream is at end-of-file. If the stream is not yet exhausted, this function will block to wait for more data if necessary, and then return `false`. Therefore it is always safe to read one byte after seeing `eof` return `false`. `eof` will return `false` as long as buffered data is still available, even if the remote end of a connection is closed.

# Examples

```jldoctest
julia> b = IOBuffer("my buffer");

julia> eof(b)
false

julia> seekend(b);

julia> eof(b)
true
```

```
eof(l::Lexer)
```

Determine whether the end of the lexer's underlying buffer has been reached.



eps:
==================================================

```
eps(::Type{T}) where T<:AbstractFloat
eps()
```

Return the *machine epsilon* of the floating point type `T` (`T = Float64` by default). This is defined as the gap between 1 and the next largest value representable by `typeof(one(T))`, and is equivalent to `eps(one(T))`.  (Since `eps(T)` is a bound on the *relative error* of `T`, it is a "dimensionless" quantity like [`one`](@ref).)

# Examples

```jldoctest
julia> eps()
2.220446049250313e-16

julia> eps(Float32)
1.1920929f-7

julia> 1.0 + eps()
1.0000000000000002

julia> 1.0 + eps()/2
1.0
```

```
eps(x::AbstractFloat)
```

Return the *unit in last place* (ulp) of `x`. This is the distance between consecutive representable floating point values at `x`. In most cases, if the distance on either side of `x` is different, then the larger of the two is taken, that is

```
eps(x) == max(x-prevfloat(x), nextfloat(x)-x)
```

The exceptions to this rule are the smallest and largest finite values (e.g. `nextfloat(-Inf)` and `prevfloat(Inf)` for [`Float64`](@ref)), which round to the smaller of the values.

The rationale for this behavior is that `eps` bounds the floating point rounding error. Under the default `RoundNearest` rounding mode, if $y$ is a real number and $x$ is the nearest floating point number to $y$, then

$$
|y-x| \leq \operatorname{eps}(x)/2.
$$

See also: [`nextfloat`](@ref), [`issubnormal`](@ref), [`floatmax`](@ref).

# Examples

```jldoctest
julia> eps(1.0)
2.220446049250313e-16

julia> eps(prevfloat(2.0))
2.220446049250313e-16

julia> eps(2.0)
4.440892098500626e-16

julia> x = prevfloat(Inf)      # largest finite Float64
1.7976931348623157e308

julia> x + eps(x)/2            # rounds up
Inf

julia> x + prevfloat(eps(x)/2) # rounds down
1.7976931348623157e308
```

```
eps(::Type{DateTime}) -> Millisecond
eps(::Type{Date}) -> Day
eps(::Type{Time}) -> Nanosecond
eps(::TimeType) -> Period
```

Return the smallest unit value supported by the `TimeType`.

# Examples

```jldoctest
julia> eps(DateTime)
1 millisecond

julia> eps(Date)
1 day

julia> eps(Time)
1 nanosecond
```



err:
==================================================

No documentation found for private symbol.

# Summary

```
struct Base.ExceptionStack
```

# Fields

```
stack :: Vector{Any}
```

# Supertype Hierarchy

```
Base.ExceptionStack <: AbstractVector{Any} <: Any
```



error:
==================================================

```
error(message::AbstractString)
```

Raise an `ErrorException` with the given message.

```
error(msg...)
```

Raise an `ErrorException` with a message constructed by `string(msg...)`.



errormonitor:
==================================================

```
errormonitor(t::Task)
```

Print an error log to `stderr` if task `t` fails.

# Examples

```julia-repl
julia> Base._wait(errormonitor(Threads.@spawn error("task failed")))
Unhandled Task ERROR: task failed
Stacktrace:
[...]
```



esc:
==================================================

```
esc(e)
```

Only valid in the context of an [`Expr`](@ref) returned from a macro. Prevents the macro hygiene pass from turning embedded variables into gensym variables. See the [Macros](@ref man-macros) section of the Metaprogramming chapter of the manual for more details and examples.



escape_string:
==================================================

```
escape_string(str::AbstractString[, esc]; keep = ())::AbstractString
escape_string(io, str::AbstractString[, esc]; keep = ())::Nothing
```

General escaping of traditional C and Unicode escape sequences. The first form returns the escaped string, the second prints the result to `io`.

Backslashes (`\`) are escaped with a double-backslash (`"\\"`). Non-printable characters are escaped either with their standard C escape codes, `"\0"` for NUL (if unambiguous), unicode code point (`"\u"` prefix) or hex (`"\x"` prefix).

The optional `esc` argument specifies any additional characters that should also be escaped by a prepending backslash (`"` is also escaped by default in the first form).

The argument `keep` specifies a collection of characters which are to be kept as they are. Notice that `esc` has precedence here.

See also [`unescape_string`](@ref) for the reverse operation.

!!! compat "Julia 1.7"
    The `keep` argument is available as of Julia 1.7.


# Examples

```jldoctest
julia> escape_string("aaa\nbbb")
"aaa\\nbbb"

julia> escape_string("aaa\nbbb"; keep = '\n')
"aaa\nbbb"

julia> escape_string("\xfe\xff") # invalid utf-8
"\\xfe\\xff"

julia> escape_string(string('\u2135','\0')) # unambiguous
"ℵ\\0"

julia> escape_string(string('\u2135','\0','0')) # \0 would be ambiguous
"ℵ\\x000"
```



eval:
==================================================

```
eval(expr)
```

Evaluate an expression in the global scope of the containing module. Every `Module` (except those defined with `baremodule`) has its own 1-argument definition of `eval`, which evaluates expressions in that module.



evalfile:
==================================================

```
evalfile(path::AbstractString, args::Vector{String}=String[])
```

Load the file into an anonymous module using [`include`](@ref), evaluate all expressions, and return the value of the last expression. The optional `args` argument can be used to set the input arguments of the script (i.e. the global `ARGS` variable). Note that definitions (e.g. methods, globals) are evaluated in the anonymous module and do not affect the current module.

# Examples

```jldoctest
julia> write("testfile.jl", """
           @show ARGS
           1 + 1
       """);

julia> x = evalfile("testfile.jl", ["ARG1", "ARG2"]);
ARGS = ["ARG1", "ARG2"]

julia> x
2

julia> rm("testfile.jl")
```



evalpoly:
==================================================

```
evalpoly(x, p)
```

Evaluate the polynomial $\sum_k x^{k-1} p[k]$ for the coefficients `p[1]`, `p[2]`, ...; that is, the coefficients are given in ascending order by power of `x`. Loops are unrolled at compile time if the number of coefficients is statically known, i.e. when `p` is a `Tuple`. This function generates efficient code using Horner's method if `x` is real, or using a Goertzel-like [^DK62] algorithm if `x` is complex.

[^DK62]: Donald Knuth, Art of Computer Programming, Volume 2: Seminumerical Algorithms, Sec. 4.6.4.

!!! compat "Julia 1.4"
    This function requires Julia 1.4 or later.


# Examples

```jldoctest
julia> evalpoly(2, (1, 2, 3))
17
```



exit:
==================================================

```
exit(code=0)
```

Stop the program with an exit code. The default exit code is zero, indicating that the program completed successfully. In an interactive session, `exit()` can be called with the keyboard shortcut `^D`.



exp:
==================================================

```
exp(x)
```

Compute the natural base exponential of `x`, in other words $ℯ^x$.

See also [`exp2`](@ref), [`exp10`](@ref) and [`cis`](@ref).

# Examples

```jldoctest
julia> exp(1.0)
2.718281828459045

julia> exp(im * pi) ≈ cis(pi)
true
```

```
exp(A::AbstractMatrix)
```

Compute the matrix exponential of `A`, defined by

$$
e^A = \sum_{n=0}^{\infty} \frac{A^n}{n!}.
$$

For symmetric or Hermitian `A`, an eigendecomposition ([`eigen`](@ref)) is used, otherwise the scaling and squaring algorithm (see [^H05]) is chosen.

[^H05]: Nicholas J. Higham, "The squaring and scaling method for the matrix exponential revisited", SIAM Journal on Matrix Analysis and Applications, 26(4), 2005, 1179-1193. [doi:10.1137/090768539](https://doi.org/10.1137/090768539)

# Examples

```jldoctest
julia> A = Matrix(1.0I, 2, 2)
2×2 Matrix{Float64}:
 1.0  0.0
 0.0  1.0

julia> exp(A)
2×2 Matrix{Float64}:
 2.71828  0.0
 0.0      2.71828
```



exp10:
==================================================

```
exp10(x)
```

Compute the base 10 exponential of `x`, in other words $10^x$.

# Examples

```jldoctest
julia> exp10(2)
100.0

julia> 10^2
100
```



exp2:
==================================================

```
exp2(x)
```

Compute the base 2 exponential of `x`, in other words $2^x$.

See also [`ldexp`](@ref), [`<<`](@ref).

# Examples

```jldoctest
julia> exp2(5)
32.0

julia> 2^5
32

julia> exp2(63) > typemax(Int)
true
```



expanduser:
==================================================

```
expanduser(path::AbstractString) -> AbstractString
```

On Unix systems, replace a tilde character at the start of a path with the current user's home directory.

See also: [`contractuser`](@ref).



expm1:
==================================================

```
expm1(x)
```

Accurately compute $e^x-1$. It avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small values of x.

# Examples

```jldoctest
julia> expm1(1e-16)
1.0e-16

julia> exp(1e-16) - 1
0.0
```



exponent:
==================================================

```
exponent(x::Real) -> Int
```

Returns the largest integer `y` such that `2^y ≤ abs(x)`.

Throws a `DomainError` when `x` is zero, infinite, or [`NaN`](@ref). For any other non-subnormal floating-point number `x`, this corresponds to the exponent bits of `x`.

See also [`signbit`](@ref), [`significand`](@ref), [`frexp`](@ref), [`issubnormal`](@ref), [`log2`](@ref), [`ldexp`](@ref).

# Examples

```jldoctest
julia> exponent(8)
3

julia> exponent(6.5)
2

julia> exponent(-1//4)
-2

julia> exponent(3.142e-4)
-12

julia> exponent(floatmin(Float32)), exponent(nextfloat(0.0f0))
(-126, -149)

julia> exponent(0.0)
ERROR: DomainError with 0.0:
Cannot be ±0.0.
[...]
```



extrema:
==================================================

```
extrema(itr; [init]) -> (mn, mx)
```

Compute both the minimum `mn` and maximum `mx` element in a single pass, and return them as a 2-tuple.

The value returned for empty `itr` can be specified by `init`. It must be a 2-tuple whose first and second elements are neutral elements for `min` and `max` respectively (i.e. which are greater/less than or equal to any other element). As a consequence, when `itr` is empty the returned `(mn, mx)` tuple will satisfy `mn ≥ mx`. When `init` is specified it may be used even for non-empty `itr`.

!!! compat "Julia 1.8"
    Keyword argument `init` requires Julia 1.8 or later.


# Examples

```jldoctest
julia> extrema(2:10)
(2, 10)

julia> extrema([9,pi,4.5])
(3.141592653589793, 9.0)

julia> extrema([]; init = (Inf, -Inf))
(Inf, -Inf)
```

```
extrema(f, itr; [init]) -> (mn, mx)
```

Compute both the minimum `mn` and maximum `mx` of `f` applied to each element in `itr` and return them as a 2-tuple. Only one pass is made over `itr`.

The value returned for empty `itr` can be specified by `init`. It must be a 2-tuple whose first and second elements are neutral elements for `min` and `max` respectively (i.e. which are greater/less than or equal to any other element). It is used for non-empty collections. Note: it implies that, for empty `itr`, the returned value `(mn, mx)` satisfies `mn ≥ mx` even though for non-empty `itr` it  satisfies `mn ≤ mx`.  This is a "paradoxical" but yet expected result.

!!! compat "Julia 1.2"
    This method requires Julia 1.2 or later.


!!! compat "Julia 1.8"
    Keyword argument `init` requires Julia 1.8 or later.


# Examples

```jldoctest
julia> extrema(sin, 0:π)
(0.0, 0.9092974268256817)

julia> extrema(sin, Real[]; init = (1.0, -1.0))  # good, since -1 ≤ sin(::Real) ≤ 1
(1.0, -1.0)
```

```
extrema(A::AbstractArray; dims) -> Array{Tuple}
```

Compute the minimum and maximum elements of an array over the given dimensions.

See also: [`minimum`](@ref), [`maximum`](@ref), [`extrema!`](@ref).

# Examples

```jldoctest
julia> A = reshape(Vector(1:2:16), (2,2,2))
2×2×2 Array{Int64, 3}:
[:, :, 1] =
 1  5
 3  7

[:, :, 2] =
  9  13
 11  15

julia> extrema(A, dims = (1,2))
1×1×2 Array{Tuple{Int64, Int64}, 3}:
[:, :, 1] =
 (1, 7)

[:, :, 2] =
 (9, 15)
```

```
extrema(f, A::AbstractArray; dims) -> Array{Tuple}
```

Compute the minimum and maximum of `f` applied to each element in the given dimensions of `A`.

!!! compat "Julia 1.2"
    This method requires Julia 1.2 or later.




extrema!:
==================================================

```
extrema!(r, A)
```

Compute the minimum and maximum value of `A` over the singleton dimensions of `r`, and write results to `r`.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


!!! compat "Julia 1.8"
    This method requires Julia 1.8 or later.


# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> extrema!([(1, 1); (1, 1)], A)
2-element Vector{Tuple{Int64, Int64}}:
 (1, 2)
 (3, 4)

julia> extrema!([(1, 1);; (1, 1)], A)
1×2 Matrix{Tuple{Int64, Int64}}:
 (1, 3)  (2, 4)
```



factorial:
==================================================

```
factorial(n::Integer)
```

Factorial of `n`. If `n` is an [`Integer`](@ref), the factorial is computed as an integer (promoted to at least 64 bits). Note that this may overflow if `n` is not small, but you can use `factorial(big(n))` to compute the result exactly in arbitrary precision.

See also [`binomial`](@ref).

# Examples

```jldoctest
julia> factorial(6)
720

julia> factorial(21)
ERROR: OverflowError: 21 is too large to look up in the table; consider using `factorial(big(21))` instead
Stacktrace:
[...]

julia> factorial(big(21))
51090942171709440000
```

# External links

  * [Factorial](https://en.wikipedia.org/wiki/Factorial) on Wikipedia.



falses:
==================================================

```
falses(dims)
```

Create a `BitArray` with all values set to `false`.

# Examples

```jldoctest
julia> falses(2,3)
2×3 BitMatrix:
 0  0  0
 0  0  0
```



fd:
==================================================

```
fd(stream)
```

Return the file descriptor backing the stream or file. Note that this function only applies to synchronous `File`'s and `IOStream`'s not to any of the asynchronous streams.



fdio:
==================================================

```
fdio([name::AbstractString, ]fd::Integer[, own::Bool=false]) -> IOStream
```

Create an [`IOStream`](@ref) object from an integer file descriptor. If `own` is `true`, closing this object will close the underlying descriptor. By default, an `IOStream` is closed when it is garbage collected. `name` allows you to associate the descriptor with a named file.



fetch:
==================================================

```
fetch(c::Channel)
```

Waits for and returns (without removing) the first available item from the `Channel`. Note: `fetch` is unsupported on an unbuffered (0-size) `Channel`.

# Examples

Buffered channel:

```jldoctest
julia> c = Channel(3) do ch
           foreach(i -> put!(ch, i), 1:3)
       end;

julia> fetch(c)
1

julia> collect(c)  # item is not removed
3-element Vector{Any}:
 1
 2
 3
```

```
fetch(x::Any)
```

Return `x`.

```
fetch(t::Task)
```

Wait for a [`Task`](@ref) to finish, then return its result value. If the task fails with an exception, a [`TaskFailedException`](@ref) (which wraps the failed task) is thrown.



fieldcount:
==================================================

```
fieldcount(t::Type)
```

Get the number of fields that an instance of the given type would have. An error is thrown if the type is too abstract to determine this.



fieldname:
==================================================

```
fieldname(x::DataType, i::Integer)
```

Get the name of field `i` of a `DataType`.

# Examples

```jldoctest
julia> fieldname(Rational, 1)
:num

julia> fieldname(Rational, 2)
:den
```



fieldnames:
==================================================

```
fieldnames(x::DataType)
```

Get a tuple with the names of the fields of a `DataType`.

See also [`propertynames`](@ref), [`hasfield`](@ref).

# Examples

```jldoctest
julia> fieldnames(Rational)
(:num, :den)

julia> fieldnames(typeof(1+im))
(:re, :im)
```



fieldoffset:
==================================================

```
fieldoffset(type, i)
```

The byte offset of field `i` of a type relative to the data start. For example, we could use it in the following manner to summarize information about a struct:

```jldoctest
julia> structinfo(T) = [(fieldoffset(T,i), fieldname(T,i), fieldtype(T,i)) for i = 1:fieldcount(T)];

julia> structinfo(Base.Filesystem.StatStruct)
13-element Vector{Tuple{UInt64, Symbol, Type}}:
 (0x0000000000000000, :desc, Union{RawFD, String})
 (0x0000000000000008, :device, UInt64)
 (0x0000000000000010, :inode, UInt64)
 (0x0000000000000018, :mode, UInt64)
 (0x0000000000000020, :nlink, Int64)
 (0x0000000000000028, :uid, UInt64)
 (0x0000000000000030, :gid, UInt64)
 (0x0000000000000038, :rdev, UInt64)
 (0x0000000000000040, :size, Int64)
 (0x0000000000000048, :blksize, Int64)
 (0x0000000000000050, :blocks, Int64)
 (0x0000000000000058, :mtime, Float64)
 (0x0000000000000060, :ctime, Float64)
```



fieldtype:
==================================================

```
fieldtype(T, name::Symbol | index::Int)
```

Determine the declared type of a field (specified by name or index) in a composite DataType `T`.

# Examples

```jldoctest
julia> struct Foo
           x::Int64
           y::String
       end

julia> fieldtype(Foo, :x)
Int64

julia> fieldtype(Foo, 2)
String
```



fieldtypes:
==================================================

```
fieldtypes(T::Type)
```

The declared types of all fields in a composite DataType `T` as a tuple.

!!! compat "Julia 1.1"
    This function requires at least Julia 1.1.


# Examples

```jldoctest
julia> struct Foo
           x::Int64
           y::String
       end

julia> fieldtypes(Foo)
(Int64, String)
```



filemode:
==================================================

```
filemode(file)
```

Equivalent to `stat(file).mode`.



filesize:
==================================================

```
filesize(path...)
```

Equivalent to `stat(file).size`.



fill:
==================================================

```
fill(value, dims::Tuple)
fill(value, dims...)
```

Create an array of size `dims` with every location set to `value`.

For example, `fill(1.0, (5,5))` returns a 5×5 array of floats, with `1.0` in every location of the array.

The dimension lengths `dims` may be specified as either a tuple or a sequence of arguments. An `N`-length tuple or `N` arguments following the `value` specify an `N`-dimensional array. Thus, a common idiom for creating a zero-dimensional array with its only location set to `x` is `fill(x)`.

Every location of the returned array is set to (and is thus [`===`](@ref) to) the `value` that was passed; this means that if the `value` is itself modified, all elements of the `fill`ed array will reflect that modification because they're *still* that very `value`. This is of no concern with `fill(1.0, (5,5))` as the `value` `1.0` is immutable and cannot itself be modified, but can be unexpected with mutable values like — most commonly — arrays.  For example, `fill([], 3)` places *the very same* empty array in all three locations of the returned vector:

```jldoctest
julia> v = fill([], 3)
3-element Vector{Vector{Any}}:
 []
 []
 []

julia> v[1] === v[2] === v[3]
true

julia> value = v[1]
Any[]

julia> push!(value, 867_5309)
1-element Vector{Any}:
 8675309

julia> v
3-element Vector{Vector{Any}}:
 [8675309]
 [8675309]
 [8675309]
```

To create an array of many independent inner arrays, use a [comprehension](@ref man-comprehensions) instead. This creates a new and distinct array on each iteration of the loop:

```jldoctest
julia> v2 = [[] for _ in 1:3]
3-element Vector{Vector{Any}}:
 []
 []
 []

julia> v2[1] === v2[2] === v2[3]
false

julia> push!(v2[1], 8675309)
1-element Vector{Any}:
 8675309

julia> v2
3-element Vector{Vector{Any}}:
 [8675309]
 []
 []
```

See also: [`fill!`](@ref), [`zeros`](@ref), [`ones`](@ref), [`similar`](@ref).

# Examples

```jldoctest
julia> fill(1.0, (2,3))
2×3 Matrix{Float64}:
 1.0  1.0  1.0
 1.0  1.0  1.0

julia> fill(42)
0-dimensional Array{Int64, 0}:
42

julia> A = fill(zeros(2), 2) # sets both elements to the same [0.0, 0.0] vector
2-element Vector{Vector{Float64}}:
 [0.0, 0.0]
 [0.0, 0.0]

julia> A[1][1] = 42; # modifies the filled value to be [42.0, 0.0]

julia> A # both A[1] and A[2] are the very same vector
2-element Vector{Vector{Float64}}:
 [42.0, 0.0]
 [42.0, 0.0]
```



fill!:
==================================================

```
fill!(A, x)
```

Fill array `A` with the value `x`. If `x` is an object reference, all elements will refer to the same object. `fill!(A, Foo())` will return `A` filled with the result of evaluating `Foo()` once.

# Examples

```jldoctest
julia> A = zeros(2,3)
2×3 Matrix{Float64}:
 0.0  0.0  0.0
 0.0  0.0  0.0

julia> fill!(A, 2.)
2×3 Matrix{Float64}:
 2.0  2.0  2.0
 2.0  2.0  2.0

julia> a = [1, 1, 1]; A = fill!(Vector{Vector{Int}}(undef, 3), a); a[1] = 2; A
3-element Vector{Vector{Int64}}:
 [2, 1, 1]
 [2, 1, 1]
 [2, 1, 1]

julia> x = 0; f() = (global x += 1; x); fill!(Vector{Int}(undef, 3), f())
3-element Vector{Int64}:
 1
 1
 1
```



filter:
==================================================

```
filter(f, a)
```

Return a copy of collection `a`, removing elements for which `f` is `false`. The function `f` is passed one argument.

!!! compat "Julia 1.4"
    Support for `a` as a tuple requires at least Julia 1.4.


See also: [`filter!`](@ref), [`Iterators.filter`](@ref).

# Examples

```jldoctest
julia> a = 1:10
1:10

julia> filter(isodd, a)
5-element Vector{Int64}:
 1
 3
 5
 7
 9
```

```
filter(f)
```

Create a function that filters its arguments with function `f` using [`filter`](@ref), i.e. a function equivalent to `x -> filter(f, x)`.

The returned function is of type `Base.Fix1{typeof(filter)}`, which can be used to implement specialized methods.

# Examples

```jldoctest
julia> (1, 2, Inf, 4, NaN, 6) |> filter(isfinite)
(1, 2, 4, 6)

julia> map(filter(iseven), [1:3, 2:4, 3:5])
3-element Vector{Vector{Int64}}:
 [2]
 [2, 4]
 [4]
```

!!! compat "Julia 1.9"
    This method requires at least Julia 1.9.


```
filter(f, d::AbstractDict)
```

Return a copy of `d`, removing elements for which `f` is `false`. The function `f` is passed `key=>value` pairs.

# Examples

```jldoctest
julia> d = Dict(1=>"a", 2=>"b")
Dict{Int64, String} with 2 entries:
  2 => "b"
  1 => "a"

julia> filter(p->isodd(p.first), d)
Dict{Int64, String} with 1 entry:
  1 => "a"
```

```
filter(f, itr::SkipMissing{<:AbstractArray})
```

Return a vector similar to the array wrapped by the given `SkipMissing` iterator but with all missing elements and those for which `f` returns `false` removed.

!!! compat "Julia 1.2"
    This method requires Julia 1.2 or later.


# Examples

```jldoctest
julia> x = [1 2; missing 4]
2×2 Matrix{Union{Missing, Int64}}:
 1         2
  missing  4

julia> filter(isodd, skipmissing(x))
1-element Vector{Int64}:
 1
```



filter!:
==================================================

```
filter!(f, a)
```

Update collection `a`, removing elements for which `f` is `false`. The function `f` is passed one argument.

# Examples

```jldoctest
julia> filter!(isodd, Vector(1:10))
5-element Vector{Int64}:
 1
 3
 5
 7
 9
```

```
filter!(f, d::AbstractDict)
```

Update `d`, removing elements for which `f` is `false`. The function `f` is passed `key=>value` pairs.

# Examples

```jldoctest
julia> d = Dict(1=>"a", 2=>"b", 3=>"c")
Dict{Int64, String} with 3 entries:
  2 => "b"
  3 => "c"
  1 => "a"

julia> filter!(p->isodd(p.first), d)
Dict{Int64, String} with 2 entries:
  3 => "c"
  1 => "a"
```



finalize:
==================================================

```
finalize(x)
```

Immediately run finalizers registered for object `x`.



finalizer:
==================================================

```
finalizer(f, x)
```

Register a function `f(x)` to be called when there are no program-accessible references to `x`, and return `x`. The type of `x` must be a `mutable struct`, otherwise the function will throw.

`f` must not cause a task switch, which excludes most I/O operations such as `println`. Using the `@async` macro (to defer context switching to outside of the finalizer) or `ccall` to directly invoke IO functions in C may be helpful for debugging purposes.

Note that there is no guaranteed world age for the execution of `f`. It may be called in the world age in which the finalizer was registered or any later world age.

# Examples

```julia
finalizer(my_mutable_struct) do x
    @async println("Finalizing $x.")
end

finalizer(my_mutable_struct) do x
    ccall(:jl_safe_printf, Cvoid, (Cstring, Cstring), "Finalizing %s.", repr(x))
end
```

A finalizer may be registered at object construction. In the following example note that we implicitly rely on the finalizer returning the newly created mutable struct `x`.

```julia
mutable struct MyMutableStruct
    bar
    function MyMutableStruct(bar)
        x = new(bar)
        f(t) = @async println("Finalizing $t.")
        finalizer(f, x)
    end
end
```



findall:
==================================================

```
findall(f::Function, A)
```

Return a vector `I` of the indices or keys of `A` where `f(A[I])` returns `true`. If there are no such elements of `A`, return an empty array.

Indices or keys are of the same type as those returned by [`keys(A)`](@ref) and [`pairs(A)`](@ref).

# Examples

```jldoctest
julia> x = [1, 3, 4]
3-element Vector{Int64}:
 1
 3
 4

julia> findall(isodd, x)
2-element Vector{Int64}:
 1
 2

julia> A = [1 2 0; 3 4 0]
2×3 Matrix{Int64}:
 1  2  0
 3  4  0
julia> findall(isodd, A)
2-element Vector{CartesianIndex{2}}:
 CartesianIndex(1, 1)
 CartesianIndex(2, 1)

julia> findall(!iszero, A)
4-element Vector{CartesianIndex{2}}:
 CartesianIndex(1, 1)
 CartesianIndex(2, 1)
 CartesianIndex(1, 2)
 CartesianIndex(2, 2)

julia> d = Dict(:A => 10, :B => -1, :C => 0)
Dict{Symbol, Int64} with 3 entries:
  :A => 10
  :B => -1
  :C => 0

julia> findall(x -> x >= 0, d)
2-element Vector{Symbol}:
 :A
 :C

```

```
findall(A)
```

Return a vector `I` of the `true` indices or keys of `A`. If there are no such elements of `A`, return an empty array. To search for other kinds of values, pass a predicate as the first argument.

Indices or keys are of the same type as those returned by [`keys(A)`](@ref) and [`pairs(A)`](@ref).

See also: [`findfirst`](@ref), [`searchsorted`](@ref).

# Examples

```jldoctest
julia> A = [true, false, false, true]
4-element Vector{Bool}:
 1
 0
 0
 1

julia> findall(A)
2-element Vector{Int64}:
 1
 4

julia> A = [true false; false true]
2×2 Matrix{Bool}:
 1  0
 0  1

julia> findall(A)
2-element Vector{CartesianIndex{2}}:
 CartesianIndex(1, 1)
 CartesianIndex(2, 2)

julia> findall(falses(3))
Int64[]
```

```
findall(c::AbstractChar, s::AbstractString)
```

Return a vector `I` of the indices of `s` where `s[i] == c`. If there are no such elements in `s`, return an empty array.

# Examples

```jldoctest
julia> findall('a', "batman")
2-element Vector{Int64}:
 2
 5
```

!!! compat "Julia 1.7"
    This method requires at least Julia 1.7.




findfirst:
==================================================

```
findfirst(A)
```

Return the index or key of the first `true` value in `A`. Return `nothing` if no such value is found. To search for other kinds of values, pass a predicate as the first argument.

Indices or keys are of the same type as those returned by [`keys(A)`](@ref) and [`pairs(A)`](@ref).

See also: [`findall`](@ref), [`findnext`](@ref), [`findlast`](@ref), [`searchsortedfirst`](@ref).

# Examples

```jldoctest
julia> A = [false, false, true, false]
4-element Vector{Bool}:
 0
 0
 1
 0

julia> findfirst(A)
3

julia> findfirst(falses(3)) # returns nothing, but not printed in the REPL

julia> A = [false false; true false]
2×2 Matrix{Bool}:
 0  0
 1  0

julia> findfirst(A)
CartesianIndex(2, 1)
```

```
findfirst(predicate::Function, A)
```

Return the index or key of the first element of `A` for which `predicate` returns `true`. Return `nothing` if there is no such element.

Indices or keys are of the same type as those returned by [`keys(A)`](@ref) and [`pairs(A)`](@ref).

# Examples

```jldoctest
julia> A = [1, 4, 2, 2]
4-element Vector{Int64}:
 1
 4
 2
 2

julia> findfirst(iseven, A)
2

julia> findfirst(x -> x>10, A) # returns nothing, but not printed in the REPL

julia> findfirst(isequal(4), A)
2

julia> A = [1 4; 2 2]
2×2 Matrix{Int64}:
 1  4
 2  2

julia> findfirst(iseven, A)
CartesianIndex(2, 1)
```

```
findfirst(pattern::AbstractString, string::AbstractString)
findfirst(pattern::AbstractPattern, string::String)
```

Find the first occurrence of `pattern` in `string`. Equivalent to [`findnext(pattern, string, firstindex(s))`](@ref).

# Examples

```jldoctest
julia> findfirst("z", "Hello to the world") # returns nothing, but not printed in the REPL

julia> findfirst("Julia", "JuliaLang")
1:5
```

```
findfirst(ch::AbstractChar, string::AbstractString)
```

Find the first occurrence of character `ch` in `string`.

!!! compat "Julia 1.3"
    This method requires at least Julia 1.3.


# Examples

```jldoctest
julia> findfirst('a', "happy")
2

julia> findfirst('z', "happy") === nothing
true
```

```
findfirst(pattern::AbstractVector{<:Union{Int8,UInt8}},
          A::AbstractVector{<:Union{Int8,UInt8}})
```

Find the first occurrence of sequence `pattern` in vector `A`.

!!! compat "Julia 1.6"
    This method requires at least Julia 1.6.


# Examples

```jldoctest
julia> findfirst([0x52, 0x62], [0x40, 0x52, 0x62, 0x63])
2:3
```



findlast:
==================================================

```
findlast(A)
```

Return the index or key of the last `true` value in `A`. Return `nothing` if there is no `true` value in `A`.

Indices or keys are of the same type as those returned by [`keys(A)`](@ref) and [`pairs(A)`](@ref).

See also: [`findfirst`](@ref), [`findprev`](@ref), [`findall`](@ref).

# Examples

```jldoctest
julia> A = [true, false, true, false]
4-element Vector{Bool}:
 1
 0
 1
 0

julia> findlast(A)
3

julia> A = falses(2,2);

julia> findlast(A) # returns nothing, but not printed in the REPL

julia> A = [true false; true false]
2×2 Matrix{Bool}:
 1  0
 1  0

julia> findlast(A)
CartesianIndex(2, 1)
```

```
findlast(predicate::Function, A)
```

Return the index or key of the last element of `A` for which `predicate` returns `true`. Return `nothing` if there is no such element.

Indices or keys are of the same type as those returned by [`keys(A)`](@ref) and [`pairs(A)`](@ref).

# Examples

```jldoctest
julia> A = [1, 2, 3, 4]
4-element Vector{Int64}:
 1
 2
 3
 4

julia> findlast(isodd, A)
3

julia> findlast(x -> x > 5, A) # returns nothing, but not printed in the REPL

julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> findlast(isodd, A)
CartesianIndex(2, 1)
```

```
findlast(pattern::AbstractString, string::AbstractString)
```

Find the last occurrence of `pattern` in `string`. Equivalent to [`findprev(pattern, string, lastindex(string))`](@ref).

# Examples

```jldoctest
julia> findlast("o", "Hello to the world")
15:15

julia> findfirst("Julia", "JuliaLang")
1:5
```

```
findlast(pattern::AbstractVector{<:Union{Int8,UInt8}},
         A::AbstractVector{<:Union{Int8,UInt8}})
```

Find the last occurrence of `pattern` in array `A`. Equivalent to [`findprev(pattern, A, lastindex(A))`](@ref).

# Examples

```jldoctest
julia> findlast([0x52, 0x62], [0x52, 0x62, 0x52, 0x62])
3:4
```

```
findlast(ch::AbstractChar, string::AbstractString)
```

Find the last occurrence of character `ch` in `string`.

!!! compat "Julia 1.3"
    This method requires at least Julia 1.3.


# Examples

```jldoctest
julia> findlast('p', "happy")
4

julia> findlast('z', "happy") === nothing
true
```



findmax:
==================================================

```
findmax(f, domain) -> (f(x), index)
```

Return a pair of a value in the codomain (outputs of `f`) and the index or key of the corresponding value in the `domain` (inputs to `f`) such that `f(x)` is maximised. If there are multiple maximal points, then the first one will be returned.

`domain` must be a non-empty iterable supporting [`keys`](@ref). Indices are of the same type as those returned by [`keys(domain)`](@ref).

Values are compared with `isless`.

!!! compat "Julia 1.7"
    This method requires Julia 1.7 or later.


# Examples

```jldoctest
julia> findmax(identity, 5:9)
(9, 5)

julia> findmax(-, 1:10)
(-1, 1)

julia> findmax(first, [(1, :a), (3, :b), (3, :c)])
(3, 2)

julia> findmax(cos, 0:π/2:2π)
(1.0, 1)
```

```
findmax(itr) -> (x, index)
```

Return the maximal element of the collection `itr` and its index or key. If there are multiple maximal elements, then the first one will be returned. Values are compared with `isless`.

Indices are of the same type as those returned by [`keys(itr)`](@ref) and [`pairs(itr)`](@ref).

See also: [`findmin`](@ref), [`argmax`](@ref), [`maximum`](@ref).

# Examples

```jldoctest
julia> findmax([8, 0.1, -9, pi])
(8.0, 1)

julia> findmax([1, 7, 7, 6])
(7, 2)

julia> findmax([1, 7, 7, NaN])
(NaN, 4)
```

```
findmax(A; dims) -> (maxval, index)
```

For an array input, returns the value and index of the maximum over the given dimensions. `NaN` is treated as greater than all other values except `missing`.

# Examples

```jldoctest
julia> A = [1.0 2; 3 4]
2×2 Matrix{Float64}:
 1.0  2.0
 3.0  4.0

julia> findmax(A, dims=1)
([3.0 4.0], CartesianIndex{2}[CartesianIndex(2, 1) CartesianIndex(2, 2)])

julia> findmax(A, dims=2)
([2.0; 4.0;;], CartesianIndex{2}[CartesianIndex(1, 2); CartesianIndex(2, 2);;])
```

```
findmax(f, A; dims) -> (f(x), index)
```

For an array input, returns the value in the codomain and index of the corresponding value which maximize `f` over the given dimensions.

# Examples

```jldoctest
julia> A = [-1.0 1; -0.5 2]
2×2 Matrix{Float64}:
 -1.0  1.0
 -0.5  2.0

julia> findmax(abs2, A, dims=1)
([1.0 4.0], CartesianIndex{2}[CartesianIndex(1, 1) CartesianIndex(2, 2)])

julia> findmax(abs2, A, dims=2)
([1.0; 4.0;;], CartesianIndex{2}[CartesianIndex(1, 1); CartesianIndex(2, 2);;])
```



findmax!:
==================================================

```
findmax!(rval, rind, A) -> (maxval, index)
```

Find the maximum of `A` and the corresponding linear index along singleton dimensions of `rval` and `rind`, and store the results in `rval` and `rind`. `NaN` is treated as greater than all other values except `missing`.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.




findmin:
==================================================

```
findmin(f, domain) -> (f(x), index)
```

Return a pair of a value in the codomain (outputs of `f`) and the index or key of the corresponding value in the `domain` (inputs to `f`) such that `f(x)` is minimised. If there are multiple minimal points, then the first one will be returned.

`domain` must be a non-empty iterable.

Indices are of the same type as those returned by [`keys(domain)`](@ref) and [`pairs(domain)`](@ref).

`NaN` is treated as less than all other values except `missing`.

!!! compat "Julia 1.7"
    This method requires Julia 1.7 or later.


# Examples

```jldoctest
julia> findmin(identity, 5:9)
(5, 1)

julia> findmin(-, 1:10)
(-10, 10)

julia> findmin(first, [(2, :a), (2, :b), (3, :c)])
(2, 1)

julia> findmin(cos, 0:π/2:2π)
(-1.0, 3)
```

```
findmin(itr) -> (x, index)
```

Return the minimal element of the collection `itr` and its index or key. If there are multiple minimal elements, then the first one will be returned. `NaN` is treated as less than all other values except `missing`.

Indices are of the same type as those returned by [`keys(itr)`](@ref) and [`pairs(itr)`](@ref).

See also: [`findmax`](@ref), [`argmin`](@ref), [`minimum`](@ref).

# Examples

```jldoctest
julia> findmin([8, 0.1, -9, pi])
(-9.0, 3)

julia> findmin([1, 7, 7, 6])
(1, 1)

julia> findmin([1, 7, 7, NaN])
(NaN, 4)
```

```
findmin(A; dims) -> (minval, index)
```

For an array input, returns the value and index of the minimum over the given dimensions. `NaN` is treated as less than all other values except `missing`.

# Examples

```jldoctest
julia> A = [1.0 2; 3 4]
2×2 Matrix{Float64}:
 1.0  2.0
 3.0  4.0

julia> findmin(A, dims=1)
([1.0 2.0], CartesianIndex{2}[CartesianIndex(1, 1) CartesianIndex(1, 2)])

julia> findmin(A, dims=2)
([1.0; 3.0;;], CartesianIndex{2}[CartesianIndex(1, 1); CartesianIndex(2, 1);;])
```

```
findmin(f, A; dims) -> (f(x), index)
```

For an array input, returns the value in the codomain and index of the corresponding value which minimize `f` over the given dimensions.

# Examples

```jldoctest
julia> A = [-1.0 1; -0.5 2]
2×2 Matrix{Float64}:
 -1.0  1.0
 -0.5  2.0

julia> findmin(abs2, A, dims=1)
([0.25 1.0], CartesianIndex{2}[CartesianIndex(2, 1) CartesianIndex(1, 2)])

julia> findmin(abs2, A, dims=2)
([1.0; 0.25;;], CartesianIndex{2}[CartesianIndex(1, 1); CartesianIndex(2, 1);;])
```



findmin!:
==================================================

```
findmin!(rval, rind, A) -> (minval, index)
```

Find the minimum of `A` and the corresponding linear index along singleton dimensions of `rval` and `rind`, and store the results in `rval` and `rind`. `NaN` is treated as less than all other values except `missing`.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.




findnext:
==================================================

```
findnext(A, i)
```

Find the next index after or including `i` of a `true` element of `A`, or `nothing` if not found.

Indices are of the same type as those returned by [`keys(A)`](@ref) and [`pairs(A)`](@ref).

# Examples

```jldoctest
julia> A = [false, false, true, false]
4-element Vector{Bool}:
 0
 0
 1
 0

julia> findnext(A, 1)
3

julia> findnext(A, 4) # returns nothing, but not printed in the REPL

julia> A = [false false; true false]
2×2 Matrix{Bool}:
 0  0
 1  0

julia> findnext(A, CartesianIndex(1, 1))
CartesianIndex(2, 1)
```

```
findnext(predicate::Function, A, i)
```

Find the next index after or including `i` of an element of `A` for which `predicate` returns `true`, or `nothing` if not found. This works for Arrays, Strings, and most other collections that support [`getindex`](@ref), [`keys(A)`](@ref), and [`nextind`](@ref).

Indices are of the same type as those returned by [`keys(A)`](@ref) and [`pairs(A)`](@ref).

# Examples

```jldoctest
julia> A = [1, 4, 2, 2];

julia> findnext(isodd, A, 1)
1

julia> findnext(isodd, A, 2) # returns nothing, but not printed in the REPL

julia> A = [1 4; 2 2];

julia> findnext(isodd, A, CartesianIndex(1, 1))
CartesianIndex(1, 1)

julia> findnext(isspace, "a b c", 3)
4
```

```
findnext(pattern::AbstractString, string::AbstractString, start::Integer)
findnext(pattern::AbstractPattern, string::String, start::Integer)
```

Find the next occurrence of `pattern` in `string` starting at position `start`. `pattern` can be either a string, or a regular expression, in which case `string` must be of type `String`.

The return value is a range of indices where the matching sequence is found, such that `s[findnext(x, s, i)] == x`:

`findnext("substring", string, i)` == `start:stop` such that `string[start:stop] == "substring"` and `i <= start`, or `nothing` if unmatched.

# Examples

```jldoctest
julia> findnext("z", "Hello to the world", 1) === nothing
true

julia> findnext("o", "Hello to the world", 6)
8:8

julia> findnext("Lang", "JuliaLang", 2)
6:9
```

```
findnext(ch::AbstractChar, string::AbstractString, start::Integer)
```

Find the next occurrence of character `ch` in `string` starting at position `start`.

!!! compat "Julia 1.3"
    This method requires at least Julia 1.3.


# Examples

```jldoctest
julia> findnext('z', "Hello to the world", 1) === nothing
true

julia> findnext('o', "Hello to the world", 6)
8
```

```
findnext(pattern::AbstractVector{<:Union{Int8,UInt8}},
         A::AbstractVector{<:Union{Int8,UInt8}},
         start::Integer)
```

Find the next occurrence of the sequence `pattern` in vector `A` starting at position `start`.

!!! compat "Julia 1.6"
    This method requires at least Julia 1.6.


# Examples

```jldoctest
julia> findnext([0x52, 0x62], [0x52, 0x62, 0x72], 3) === nothing
true

julia> findnext([0x52, 0x62], [0x40, 0x52, 0x62, 0x52, 0x62], 3)
4:5
```



findprev:
==================================================

```
findprev(A, i)
```

Find the previous index before or including `i` of a `true` element of `A`, or `nothing` if not found.

Indices are of the same type as those returned by [`keys(A)`](@ref) and [`pairs(A)`](@ref).

See also: [`findnext`](@ref), [`findfirst`](@ref), [`findall`](@ref).

# Examples

```jldoctest
julia> A = [false, false, true, true]
4-element Vector{Bool}:
 0
 0
 1
 1

julia> findprev(A, 3)
3

julia> findprev(A, 1) # returns nothing, but not printed in the REPL

julia> A = [false false; true true]
2×2 Matrix{Bool}:
 0  0
 1  1

julia> findprev(A, CartesianIndex(2, 1))
CartesianIndex(2, 1)
```

```
findprev(predicate::Function, A, i)
```

Find the previous index before or including `i` of an element of `A` for which `predicate` returns `true`, or `nothing` if not found. This works for Arrays, Strings, and most other collections that support [`getindex`](@ref), [`keys(A)`](@ref), and [`nextind`](@ref).

Indices are of the same type as those returned by [`keys(A)`](@ref) and [`pairs(A)`](@ref).

# Examples

```jldoctest
julia> A = [4, 6, 1, 2]
4-element Vector{Int64}:
 4
 6
 1
 2

julia> findprev(isodd, A, 1) # returns nothing, but not printed in the REPL

julia> findprev(isodd, A, 3)
3

julia> A = [4 6; 1 2]
2×2 Matrix{Int64}:
 4  6
 1  2

julia> findprev(isodd, A, CartesianIndex(1, 2))
CartesianIndex(2, 1)

julia> findprev(isspace, "a b c", 3)
2
```

```
findprev(pattern::AbstractString, string::AbstractString, start::Integer)
```

Find the previous occurrence of `pattern` in `string` starting at position `start`.

The return value is a range of indices where the matching sequence is found, such that `s[findprev(x, s, i)] == x`:

`findprev("substring", string, i)` == `start:stop` such that `string[start:stop] == "substring"` and `stop <= i`, or `nothing` if unmatched.

# Examples

```jldoctest
julia> findprev("z", "Hello to the world", 18) === nothing
true

julia> findprev("o", "Hello to the world", 18)
15:15

julia> findprev("Julia", "JuliaLang", 6)
1:5
```

```
findprev(ch::AbstractChar, string::AbstractString, start::Integer)
```

Find the previous occurrence of character `ch` in `string` starting at position `start`.

!!! compat "Julia 1.3"
    This method requires at least Julia 1.3.


# Examples

```jldoctest
julia> findprev('z', "Hello to the world", 18) === nothing
true

julia> findprev('o', "Hello to the world", 18)
15
```

```
findprev(pattern::AbstractVector{<:Union{Int8,UInt8}},
         A::AbstractVector{<:Union{Int8,UInt8}},
         start::Integer)
```

Find the previous occurrence of the sequence `pattern` in vector `A` starting at position `start`.

!!! compat "Julia 1.6"
    This method requires at least Julia 1.6.


# Examples

```jldoctest
julia> findprev([0x52, 0x62], [0x40, 0x52, 0x62, 0x52, 0x62], 3)
2:3
```



first:
==================================================

```
first(coll)
```

Get the first element of an iterable collection. Return the start point of an [`AbstractRange`](@ref) even if it is empty.

See also: [`only`](@ref), [`firstindex`](@ref), [`last`](@ref).

# Examples

```jldoctest
julia> first(2:2:10)
2

julia> first([1; 2; 3; 4])
1
```

```
first(itr, n::Integer)
```

Get the first `n` elements of the iterable collection `itr`, or fewer elements if `itr` is not long enough.

See also: [`startswith`](@ref), [`Iterators.take`](@ref).

!!! compat "Julia 1.6"
    This method requires at least Julia 1.6.


# Examples

```jldoctest
julia> first(["foo", "bar", "qux"], 2)
2-element Vector{String}:
 "foo"
 "bar"

julia> first(1:6, 10)
1:6

julia> first(Bool[], 1)
Bool[]
```

```
first(s::AbstractString, n::Integer)
```

Get a string consisting of the first `n` characters of `s`.

# Examples

```jldoctest
julia> first("∀ϵ≠0: ϵ²>0", 0)
""

julia> first("∀ϵ≠0: ϵ²>0", 1)
"∀"

julia> first("∀ϵ≠0: ϵ²>0", 3)
"∀ϵ≠"
```



firstindex:
==================================================

```
firstindex(collection) -> Integer
firstindex(collection, d) -> Integer
```

Return the first index of `collection`. If `d` is given, return the first index of `collection` along dimension `d`.

The syntaxes `A[begin]` and `A[1, begin]` lower to `A[firstindex(A)]` and `A[1, firstindex(A, 2)]`, respectively.

See also: [`first`](@ref), [`axes`](@ref), [`lastindex`](@ref), [`nextind`](@ref).

# Examples

```jldoctest
julia> firstindex([1,2,4])
1

julia> firstindex(rand(3,4,5), 2)
1
```



fld:
==================================================

```
fld(x, y)
```

Largest integer less than or equal to `x / y`. Equivalent to `div(x, y, RoundDown)`.

See also [`div`](@ref), [`cld`](@ref), [`fld1`](@ref).

# Examples

```jldoctest
julia> fld(7.3, 5.5)
1.0

julia> fld.(-5:5, 3)'
1×11 adjoint(::Vector{Int64}) with eltype Int64:
 -2  -2  -1  -1  -1  0  0  0  1  1  1
```

Because `fld(x, y)` implements strictly correct floored rounding based on the true value of floating-point numbers, unintuitive situations can arise. For example:

```jldoctest
julia> fld(6.0, 0.1)
59.0
julia> 6.0 / 0.1
60.0
julia> 6.0 / big(0.1)
59.99999999999999666933092612453056361837965690217069245739573412231113406246995
```

What is happening here is that the true value of the floating-point number written as `0.1` is slightly larger than the numerical value 1/10 while `6.0` represents the number 6 precisely. Therefore the true value of `6.0 / 0.1` is slightly less than 60. When doing division, this is rounded to precisely `60.0`, but `fld(6.0, 0.1)` always takes the floor of the true value, so the result is `59.0`.



fld1:
==================================================

```
fld1(x, y)
```

Flooring division, returning a value consistent with `mod1(x,y)`

See also [`mod1`](@ref), [`fldmod1`](@ref).

# Examples

```jldoctest
julia> x = 15; y = 4;

julia> fld1(x, y)
4

julia> x == fld(x, y) * y + mod(x, y)
true

julia> x == (fld1(x, y) - 1) * y + mod1(x, y)
true
```



fldmod:
==================================================

```
fldmod(x, y)
```

The floored quotient and modulus after division. A convenience wrapper for `divrem(x, y, RoundDown)`. Equivalent to `(fld(x, y), mod(x, y))`.

See also: [`fld`](@ref), [`cld`](@ref), [`fldmod1`](@ref).



fldmod1:
==================================================

```
fldmod1(x, y)
```

Return `(fld1(x,y), mod1(x,y))`.

See also [`fld1`](@ref), [`mod1`](@ref).



flipsign:
==================================================

```
flipsign(x, y)
```

Return `x` with its sign flipped if `y` is negative. For example `abs(x) = flipsign(x,x)`.

# Examples

```jldoctest
julia> flipsign(5, 3)
5

julia> flipsign(5, -3)
-5
```



float:
==================================================

```
float(x)
```

Convert a number or array to a floating point data type.

See also: [`complex`](@ref), [`oftype`](@ref), [`convert`](@ref).

# Examples

```jldoctest
julia> float(1:1000)
1.0:1.0:1000.0

julia> float(typemax(Int32))
2.147483647e9
```

```
float(T::Type)
```

Return an appropriate type to represent a value of type `T` as a floating point value. Equivalent to `typeof(float(zero(T)))`.

# Examples

```jldoctest
julia> float(Complex{Int})
ComplexF64 (alias for Complex{Float64})

julia> float(Int)
Float64
```



floatmax:
==================================================

```
floatmax(T = Float64)
```

Return the largest finite number representable by the floating-point type `T`.

See also: [`typemax`](@ref), [`floatmin`](@ref), [`eps`](@ref).

# Examples

```jldoctest
julia> floatmax(Float16)
Float16(6.55e4)

julia> floatmax(Float32)
3.4028235f38

julia> floatmax()
1.7976931348623157e308

julia> typemax(Float64)
Inf
```



floatmin:
==================================================

```
floatmin(T = Float64)
```

Return the smallest positive normal number representable by the floating-point type `T`.

# Examples

```jldoctest
julia> floatmin(Float16)
Float16(6.104e-5)

julia> floatmin(Float32)
1.1754944f-38

julia> floatmin()
2.2250738585072014e-308
```



floor:
==================================================

```
floor([T,] x)
floor(x; digits::Integer= [, base = 10])
floor(x; sigdigits::Integer= [, base = 10])
```

`floor(x)` returns the nearest integral value of the same type as `x` that is less than or equal to `x`.

`floor(T, x)` converts the result to type `T`, throwing an `InexactError` if the floored value is not representable a `T`.

Keywords `digits`, `sigdigits` and `base` work as for [`round`](@ref).

To support `floor` for a new type, define `Base.round(x::NewType, ::RoundingMode{:Down})`.

```
floor(x::Period, precision::T) where T <: Union{TimePeriod, Week, Day} -> T
```

Round `x` down to the nearest multiple of `precision`. If `x` and `precision` are different subtypes of `Period`, the return value will have the same type as `precision`.

For convenience, `precision` may be a type instead of a value: `floor(x, Dates.Hour)` is a shortcut for `floor(x, Dates.Hour(1))`.

```jldoctest
julia> floor(Day(16), Week)
2 weeks

julia> floor(Minute(44), Minute(15))
30 minutes

julia> floor(Hour(36), Day)
1 day
```

Rounding to a `precision` of `Month`s or `Year`s is not supported, as these `Period`s are of inconsistent length.

```
floor(dt::TimeType, p::Period) -> TimeType
```

Return the nearest `Date` or `DateTime` less than or equal to `dt` at resolution `p`.

For convenience, `p` may be a type instead of a value: `floor(dt, Dates.Hour)` is a shortcut for `floor(dt, Dates.Hour(1))`.

```jldoctest
julia> floor(Date(1985, 8, 16), Month)
1985-08-01

julia> floor(DateTime(2013, 2, 13, 0, 31, 20), Minute(15))
2013-02-13T00:30:00

julia> floor(DateTime(2016, 8, 6, 12, 0, 0), Day)
2016-08-06T00:00:00
```



flush:
==================================================

```
flush(stream)
```

Commit all currently buffered writes to the given stream.



fma:
==================================================

```
fma(x, y, z)
```

Computes `x*y+z` without rounding the intermediate result `x*y`. On some systems this is significantly more expensive than `x*y+z`. `fma` is used to improve accuracy in certain algorithms. See [`muladd`](@ref).



foldl:
==================================================

```
foldl(op, itr; [init])
```

Like [`reduce`](@ref), but with guaranteed left associativity. If provided, the keyword argument `init` will be used exactly once. In general, it will be necessary to provide `init` to work with empty collections.

See also [`mapfoldl`](@ref), [`foldr`](@ref), [`accumulate`](@ref).

# Examples

```jldoctest
julia> foldl(=>, 1:4)
((1 => 2) => 3) => 4

julia> foldl(=>, 1:4; init=0)
(((0 => 1) => 2) => 3) => 4

julia> accumulate(=>, (1,2,3,4))
(1, 1 => 2, (1 => 2) => 3, ((1 => 2) => 3) => 4)
```



foldr:
==================================================

```
foldr(op, itr; [init])
```

Like [`reduce`](@ref), but with guaranteed right associativity. If provided, the keyword argument `init` will be used exactly once. In general, it will be necessary to provide `init` to work with empty collections.

# Examples

```jldoctest
julia> foldr(=>, 1:4)
1 => (2 => (3 => 4))

julia> foldr(=>, 1:4; init=0)
1 => (2 => (3 => (4 => 0)))
```



foreach:
==================================================

```
foreach(f, c...) -> Nothing
```

Call function `f` on each element of iterable `c`. For multiple iterable arguments, `f` is called elementwise, and iteration stops when any iterator is finished.

`foreach` should be used instead of [`map`](@ref) when the results of `f` are not needed, for example in `foreach(println, array)`.

# Examples

```jldoctest
julia> tri = 1:3:7; res = Int[];

julia> foreach(x -> push!(res, x^2), tri)

julia> res
3-element Vector{Int64}:
  1
 16
 49

julia> foreach((x, y) -> println(x, " with ", y), tri, 'a':'z')
1 with a
4 with b
7 with c
```



fourthroot:
==================================================

```
fourthroot(x)
```

Return the fourth root of `x` by applying `sqrt` twice successively.



frexp:
==================================================

```
frexp(val)
```

Return `(x,exp)` such that `x` has a magnitude in the interval $[1/2, 1)$ or 0, and `val` is equal to $x \times 2^{exp}$.

See also [`significand`](@ref), [`exponent`](@ref), [`ldexp`](@ref).

# Examples

```jldoctest
julia> frexp(6.0)
(0.75, 3)

julia> significand(6.0), exponent(6.0)  # interval [1, 2) instead
(1.5, 2)

julia> frexp(0.0), frexp(NaN), frexp(-Inf)  # exponent would give an error
((0.0, 0), (NaN, 0), (-Inf, 0))
```



fullname:
==================================================

```
fullname(m::Module)
```

Get the fully-qualified name of a module as a tuple of symbols. For example,

# Examples

```jldoctest
julia> fullname(Base.Iterators)
(:Base, :Iterators)

julia> fullname(Main)
(:Main,)
```



functionloc:
==================================================

```
functionloc(m::Method)
```

Return a tuple `(filename,line)` giving the location of a `Method` definition.

```
functionloc(f::Function, types)
```

Return a tuple `(filename,line)` giving the location of a generic `Function` definition.



gcd:
==================================================

```
gcd(x, y...)
```

Greatest common (positive) divisor (or zero if all arguments are zero). The arguments may be integer and rational numbers.

!!! compat "Julia 1.4"
    Rational arguments require Julia 1.4 or later.


# Examples

```jldoctest
julia> gcd(6, 9)
3

julia> gcd(6, -9)
3

julia> gcd(6, 0)
6

julia> gcd(0, 0)
0

julia> gcd(1//3, 2//3)
1//3

julia> gcd(1//3, -2//3)
1//3

julia> gcd(1//3, 2)
1//3

julia> gcd(0, 0, 10, 15)
5
```



gcdx:
==================================================

```
gcdx(a, b)
```

Computes the greatest common (positive) divisor of `a` and `b` and their Bézout coefficients, i.e. the integer coefficients `u` and `v` that satisfy $ua+vb = d = gcd(a, b)$. $gcdx(a, b)$ returns $(d, u, v)$.

The arguments may be integer and rational numbers.

!!! compat "Julia 1.4"
    Rational arguments require Julia 1.4 or later.


# Examples

```jldoctest
julia> gcdx(12, 42)
(6, -3, 1)

julia> gcdx(240, 46)
(2, -9, 47)
```

!!! note
    Bézout coefficients are *not* uniquely defined. `gcdx` returns the minimal Bézout coefficients that are computed by the extended Euclidean algorithm. (Ref: D. Knuth, TAoCP, 2/e, p. 325, Algorithm X.) For signed integers, these coefficients `u` and `v` are minimal in the sense that $|u| < |b/d|$ and $|v| < |a/d|$. Furthermore, the signs of `u` and `v` are chosen so that `d` is positive. For unsigned integers, the coefficients `u` and `v` might be near their `typemax`, and the identity then holds only via the unsigned integers' modulo arithmetic.




gensym:
==================================================

```
gensym([tag])
```

Generates a symbol which will not conflict with other variable names (in the same module).



get:
==================================================

```
get(collection, key, default)
```

Return the value stored for the given key, or the given default value if no mapping for the key is present.

!!! compat "Julia 1.7"
    For tuples and numbers, this function requires at least Julia 1.7.


# Examples

```jldoctest
julia> d = Dict("a"=>1, "b"=>2);

julia> get(d, "a", 3)
1

julia> get(d, "c", 3)
3
```

```
get(f::Union{Function, Type}, collection, key)
```

Return the value stored for the given key, or if no mapping for the key is present, return `f()`.  Use [`get!`](@ref) to also store the default value in the dictionary.

This is intended to be called using `do` block syntax

```julia
get(dict, key) do
    # default value calculated here
    time()
end
```



get!:
==================================================

```
get!(collection, key, default)
```

Return the value stored for the given key, or if no mapping for the key is present, store `key => default`, and return `default`.

# Examples

```jldoctest
julia> d = Dict("a"=>1, "b"=>2, "c"=>3);

julia> get!(d, "a", 5)
1

julia> get!(d, "d", 4)
4

julia> d
Dict{String, Int64} with 4 entries:
  "c" => 3
  "b" => 2
  "a" => 1
  "d" => 4
```

```
get!(f::Union{Function, Type}, collection, key)
```

Return the value stored for the given key, or if no mapping for the key is present, store `key => f()`, and return `f()`.

This is intended to be called using `do` block syntax.

# Examples

```jldoctest
julia> squares = Dict{Int, Int}();

julia> function get_square!(d, i)
           get!(d, i) do
               i^2
           end
       end
get_square! (generic function with 1 method)

julia> get_square!(squares, 2)
4

julia> squares
Dict{Int64, Int64} with 1 entry:
  2 => 4
```



get_zero_subnormals:
==================================================

```
get_zero_subnormals() -> Bool
```

Return `false` if operations on subnormal floating-point values ("denormals") obey rules for IEEE arithmetic, and `true` if they might be converted to zeros.

!!! warning
    This function only affects the current thread.




getfield:
==================================================

```
getfield(value, name::Symbol, [order::Symbol])
getfield(value, i::Int, [order::Symbol])
```

Extract a field from a composite `value` by name or position. Optionally, an ordering can be defined for the operation. If the field was declared `@atomic`, the specification is strongly recommended to be compatible with the stores to that location. Otherwise, if not declared as `@atomic`, this parameter must be `:not_atomic` if specified. See also [`getproperty`](@ref Base.getproperty) and [`fieldnames`](@ref).

# Examples

```jldoctest
julia> a = 1//2
1//2

julia> getfield(a, :num)
1

julia> a.num
1

julia> getfield(a, 1)
1
```



getglobal:
==================================================

```
getglobal(module::Module, name::Symbol, [order::Symbol=:monotonic])
```

Retrieve the value of the binding `name` from the module `module`. Optionally, an atomic ordering can be defined for the operation, otherwise it defaults to monotonic.

While accessing module bindings using [`getfield`](@ref) is still supported to maintain compatibility, using `getglobal` should always be preferred since `getglobal` allows for control over atomic ordering (`getfield` is always monotonic) and better signifies the code's intent both to the user as well as the compiler.

Most users should not have to call this function directly – The [`getproperty`](@ref Base.getproperty) function or corresponding syntax (i.e. `module.name`) should be preferred in all but few very specific use cases.

!!! compat "Julia 1.9"
    This function requires Julia 1.9 or later.


See also [`getproperty`](@ref Base.getproperty) and [`setglobal!`](@ref).

# Examples

```jldoctest
julia> a = 1
1

julia> module M
       a = 2
       end;

julia> getglobal(@__MODULE__, :a)
1

julia> getglobal(M, :a)
2
```



gethostname:
==================================================

```
gethostname() -> String
```

Get the local machine's host name.



getindex:
==================================================

```
getindex(type[, elements...])
```

Construct a 1-d array of the specified type. This is usually called with the syntax `Type[]`. Element values can be specified using `Type[a,b,c,...]`.

# Examples

```jldoctest
julia> Int8[1, 2, 3]
3-element Vector{Int8}:
 1
 2
 3

julia> getindex(Int8, 1, 2, 3)
3-element Vector{Int8}:
 1
 2
 3
```

```
getindex(collection, key...)
```

Retrieve the value(s) stored at the given key or index within a collection. The syntax `a[i,j,...]` is converted by the compiler to `getindex(a, i, j, ...)`.

See also [`get`](@ref), [`keys`](@ref), [`eachindex`](@ref).

# Examples

```jldoctest
julia> A = Dict("a" => 1, "b" => 2)
Dict{String, Int64} with 2 entries:
  "b" => 2
  "a" => 1

julia> getindex(A, "a")
1
```

```
getindex(A, inds...)
```

Return a subset of array `A` as selected by the indices `inds`.

Each index may be any [supported index type](@ref man-supported-index-types), such as an [`Integer`](@ref), [`CartesianIndex`](@ref), [range](@ref Base.AbstractRange), or [array](@ref man-multi-dim-arrays) of supported indices. A [:](@ref Base.Colon) may be used to select all elements along a specific dimension, and a boolean array (e.g. an `Array{Bool}` or a [`BitArray`](@ref)) may be used to filter for elements where the corresponding index is `true`.

When `inds` selects multiple elements, this function returns a newly allocated array. To index multiple elements without making a copy, use [`view`](@ref) instead.

See the manual section on [array indexing](@ref man-array-indexing) for details.

# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> getindex(A, 1)
1

julia> getindex(A, [2, 1])
2-element Vector{Int64}:
 3
 1

julia> getindex(A, 2:4)
3-element Vector{Int64}:
 3
 2
 4

julia> getindex(A, 2, 1)
3

julia> getindex(A, CartesianIndex(2, 1))
3

julia> getindex(A, :, 2)
2-element Vector{Int64}:
 2
 4

julia> getindex(A, 2, :)
2-element Vector{Int64}:
 3
 4

julia> getindex(A, A .> 2)
2-element Vector{Int64}:
 3
 4
```

```
getindex(tree::GitTree, target::AbstractString) -> GitObject
```

Look up `target` path in the `tree`, returning a [`GitObject`](@ref) (a [`GitBlob`](@ref) in the case of a file, or another [`GitTree`](@ref) if looking up a directory).

# Examples

```julia
tree = LibGit2.GitTree(repo, "HEAD^{tree}")
readme = tree["README.md"]
subtree = tree["test"]
runtests = subtree["runtests.jl"]
```



getkey:
==================================================

```
getkey(collection, key, default)
```

Return the key matching argument `key` if one exists in `collection`, otherwise return `default`.

# Examples

```jldoctest
julia> D = Dict('a'=>2, 'b'=>3)
Dict{Char, Int64} with 2 entries:
  'a' => 2
  'b' => 3

julia> getkey(D, 'a', 1)
'a': ASCII/Unicode U+0061 (category Ll: Letter, lowercase)

julia> getkey(D, 'd', 'a')
'a': ASCII/Unicode U+0061 (category Ll: Letter, lowercase)
```



getpid:
==================================================

```
getpid(process) -> Int32
```

Get the child process ID, if it still exists.

!!! compat "Julia 1.1"
    This function requires at least Julia 1.1.


```
getpid() -> Int32
```

Get Julia's process ID.



getproperty:
==================================================

```
getproperty(value, name::Symbol)
getproperty(value, name::Symbol, order::Symbol)
```

The syntax `a.b` calls `getproperty(a, :b)`. The syntax `@atomic order a.b` calls `getproperty(a, :b, :order)` and the syntax `@atomic a.b` calls `getproperty(a, :b, :sequentially_consistent)`.

# Examples

```jldoctest
julia> struct MyType{T <: Number}
           x::T
       end

julia> function Base.getproperty(obj::MyType, sym::Symbol)
           if sym === :special
               return obj.x + 1
           else # fallback to getfield
               return getfield(obj, sym)
           end
       end

julia> obj = MyType(1);

julia> obj.special
2

julia> obj.x
1
```

One should overload `getproperty` only when necessary, as it can be confusing if the behavior of the syntax `obj.f` is unusual. Also note that using methods is often preferable. See also this style guide documentation for more information: [Prefer exported methods over direct field access](@ref).

See also [`getfield`](@ref Core.getfield), [`propertynames`](@ref Base.propertynames) and [`setproperty!`](@ref Base.setproperty!).



gperm:
==================================================

```
gperm(file)
```

Like [`uperm`](@ref) but gets the permissions of the group owning the file.



hardlink:
==================================================

```
hardlink(src::AbstractString, dst::AbstractString)
```

Creates a hard link to an existing source file `src` with the name `dst`. The destination, `dst`, must not exist.

See also: [`symlink`](@ref).

!!! compat "Julia 1.8"
    This method was added in Julia 1.8.




hasfield:
==================================================

```
hasfield(T::Type, name::Symbol)
```

Return a boolean indicating whether `T` has `name` as one of its own fields.

See also [`fieldnames`](@ref), [`fieldcount`](@ref), [`hasproperty`](@ref).

!!! compat "Julia 1.2"
    This function requires at least Julia 1.2.


# Examples

```jldoctest
julia> struct Foo
            bar::Int
       end

julia> hasfield(Foo, :bar)
true

julia> hasfield(Foo, :x)
false
```



hash:
==================================================

```
hash(x[, h::UInt]) -> UInt
```

Compute an integer hash code such that `isequal(x,y)` implies `hash(x)==hash(y)`. The optional second argument `h` is another hash code to be mixed with the result.

New types should implement the 2-argument form, typically by calling the 2-argument `hash` method recursively in order to mix hashes of the contents with each other (and with `h`). Typically, any type that implements `hash` should also implement its own [`==`](@ref) (hence [`isequal`](@ref)) to guarantee the property mentioned above. Types supporting subtraction (operator `-`) should also implement [`widen`](@ref), which is required to hash values inside heterogeneous arrays.

The hash value may change when a new Julia process is started.

```jldoctest
julia> a = hash(10)
0x95ea2955abd45275

julia> hash(10, a) # only use the output of another hash function as the second argument
0xd42bad54a8575b16
```

See also: [`objectid`](@ref), [`Dict`](@ref), [`Set`](@ref).



haskey:
==================================================

```
haskey(collection, key) -> Bool
```

Determine whether a collection has a mapping for a given `key`.

# Examples

```jldoctest
julia> D = Dict('a'=>2, 'b'=>3)
Dict{Char, Int64} with 2 entries:
  'a' => 2
  'b' => 3

julia> haskey(D, 'a')
true

julia> haskey(D, 'c')
false
```



hasmethod:
==================================================

```
hasmethod(f, t::Type{<:Tuple}[, kwnames]; world=get_world_counter()) -> Bool
```

Determine whether the given generic function has a method matching the given `Tuple` of argument types with the upper bound of world age given by `world`.

If a tuple of keyword argument names `kwnames` is provided, this also checks whether the method of `f` matching `t` has the given keyword argument names. If the matching method accepts a variable number of keyword arguments, e.g. with `kwargs...`, any names given in `kwnames` are considered valid. Otherwise the provided names must be a subset of the method's keyword arguments.

See also [`applicable`](@ref).

!!! compat "Julia 1.2"
    Providing keyword argument names requires Julia 1.2 or later.


# Examples

```jldoctest
julia> hasmethod(length, Tuple{Array})
true

julia> f(; oranges=0) = oranges;

julia> hasmethod(f, Tuple{}, (:oranges,))
true

julia> hasmethod(f, Tuple{}, (:apples, :bananas))
false

julia> g(; xs...) = 4;

julia> hasmethod(g, Tuple{}, (:a, :b, :c, :d))  # g accepts arbitrary kwargs
true
```



hasproperty:
==================================================

```
hasproperty(x, s::Symbol)
```

Return a boolean indicating whether the object `x` has `s` as one of its own properties.

!!! compat "Julia 1.2"
    This function requires at least Julia 1.2.


See also: [`propertynames`](@ref), [`hasfield`](@ref).



hcat:
==================================================

```
hcat(A...)
```

Concatenate arrays or numbers horizontally. Equivalent to [`cat`](@ref)`(A...; dims=2)`, and to the syntax `[a b c]` or `[a;; b;; c]`.

For a large vector of arrays, `reduce(hcat, A)` calls an efficient method when `A isa AbstractVector{<:AbstractVecOrMat}`. For a vector of vectors, this can also be written [`stack`](@ref)`(A)`.

See also [`vcat`](@ref), [`hvcat`](@ref).

# Examples

```jldoctest
julia> hcat([1,2], [3,4], [5,6])
2×3 Matrix{Int64}:
 1  3  5
 2  4  6

julia> hcat(1, 2, [30 40], [5, 6, 7]')  # accepts numbers
1×7 Matrix{Int64}:
 1  2  30  40  5  6  7

julia> ans == [1 2 [30 40] [5, 6, 7]']  # syntax for the same operation
true

julia> Float32[1 2 [30 40] [5, 6, 7]']  # syntax for supplying the eltype
1×7 Matrix{Float32}:
 1.0  2.0  30.0  40.0  5.0  6.0  7.0

julia> ms = [zeros(2,2), [1 2; 3 4], [50 60; 70 80]];

julia> reduce(hcat, ms)  # more efficient than hcat(ms...)
2×6 Matrix{Float64}:
 0.0  0.0  1.0  2.0  50.0  60.0
 0.0  0.0  3.0  4.0  70.0  80.0

julia> stack(ms) |> summary  # disagrees on a vector of matrices
"2×2×3 Array{Float64, 3}"

julia> hcat(Int[], Int[], Int[])  # empty vectors, each of size (0,)
0×3 Matrix{Int64}

julia> hcat([1.1, 9.9], Matrix(undef, 2, 0))  # hcat with empty 2×0 Matrix
2×1 Matrix{Any}:
 1.1
 9.9
```



hex2bytes:
==================================================

```
hex2bytes(itr)
```

Given an iterable `itr` of ASCII codes for a sequence of hexadecimal digits, returns a `Vector{UInt8}` of bytes  corresponding to the binary representation: each successive pair of hexadecimal digits in `itr` gives the value of one byte in the return vector.

The length of `itr` must be even, and the returned array has half of the length of `itr`. See also [`hex2bytes!`](@ref) for an in-place version, and [`bytes2hex`](@ref) for the inverse.

!!! compat "Julia 1.7"
    Calling `hex2bytes` with iterators producing `UInt8` values requires Julia 1.7 or later. In earlier versions, you can `collect` the iterator before calling `hex2bytes`.


# Examples

```jldoctest
julia> s = string(12345, base = 16)
"3039"

julia> hex2bytes(s)
2-element Vector{UInt8}:
 0x30
 0x39

julia> a = b"01abEF"
6-element Base.CodeUnits{UInt8, String}:
 0x30
 0x31
 0x61
 0x62
 0x45
 0x46

julia> hex2bytes(a)
3-element Vector{UInt8}:
 0x01
 0xab
 0xef
```



hex2bytes!:
==================================================

```
hex2bytes!(dest::AbstractVector{UInt8}, itr)
```

Convert an iterable `itr` of bytes representing a hexadecimal string to its binary representation, similar to [`hex2bytes`](@ref) except that the output is written in-place to `dest`. The length of `dest` must be half the length of `itr`.

!!! compat "Julia 1.7"
    Calling hex2bytes! with iterators producing UInt8 requires version 1.7. In earlier versions, you can collect the iterable before calling instead.




homedir:
==================================================

```
homedir() -> String
```

Return the current user's home directory.

!!! note
    `homedir` determines the home directory via `libuv`'s `uv_os_homedir`. For details (for example on how to specify the home directory via environment variables), see the [`uv_os_homedir` documentation](http://docs.libuv.org/en/v1.x/misc.html#c.uv_os_homedir).


See also [`Sys.username`](@ref).



htol:
==================================================

```
htol(x)
```

Convert the endianness of a value from that used by the Host to Little-endian.



hton:
==================================================

```
hton(x)
```

Convert the endianness of a value from that used by the Host to Network byte order (big-endian).



hvcat:
==================================================

```
hvcat(blocks_per_row::Union{Tuple{Vararg{Int}}, Int}, values...)
```

Horizontal and vertical concatenation in one call. This function is called for block matrix syntax. The first argument specifies the number of arguments to concatenate in each block row. If the first argument is a single integer `n`, then all block rows are assumed to have `n` block columns.

# Examples

```jldoctest
julia> a, b, c, d, e, f = 1, 2, 3, 4, 5, 6
(1, 2, 3, 4, 5, 6)

julia> [a b c; d e f]
2×3 Matrix{Int64}:
 1  2  3
 4  5  6

julia> hvcat((3,3), a,b,c,d,e,f)
2×3 Matrix{Int64}:
 1  2  3
 4  5  6

julia> [a b; c d; e f]
3×2 Matrix{Int64}:
 1  2
 3  4
 5  6

julia> hvcat((2,2,2), a,b,c,d,e,f)
3×2 Matrix{Int64}:
 1  2
 3  4
 5  6
julia> hvcat((2,2,2), a,b,c,d,e,f) == hvcat(2, a,b,c,d,e,f)
true
```



hvncat:
==================================================

```
hvncat(dim::Int, row_first, values...)
hvncat(dims::Tuple{Vararg{Int}}, row_first, values...)
hvncat(shape::Tuple{Vararg{Tuple}}, row_first, values...)
```

Horizontal, vertical, and n-dimensional concatenation of many `values` in one call.

This function is called for block matrix syntax. The first argument either specifies the shape of the concatenation, similar to `hvcat`, as a tuple of tuples, or the dimensions that specify the key number of elements along each axis, and is used to determine the output dimensions. The `dims` form is more performant, and is used by default when the concatenation operation has the same number of elements along each axis (e.g., [a b; c d;;; e f ; g h]). The `shape` form is used when the number of elements along each axis is unbalanced (e.g., [a b ; c]). Unbalanced syntax needs additional validation overhead. The `dim` form is an optimization for concatenation along just one dimension. `row_first` indicates how `values` are ordered. The meaning of the first and second elements of `shape` are also swapped based on `row_first`.

# Examples

```jldoctest
julia> a, b, c, d, e, f = 1, 2, 3, 4, 5, 6
(1, 2, 3, 4, 5, 6)

julia> [a b c;;; d e f]
1×3×2 Array{Int64, 3}:
[:, :, 1] =
 1  2  3

[:, :, 2] =
 4  5  6

julia> hvncat((2,1,3), false, a,b,c,d,e,f)
2×1×3 Array{Int64, 3}:
[:, :, 1] =
 1
 2

[:, :, 2] =
 3
 4

[:, :, 3] =
 5
 6

julia> [a b;;; c d;;; e f]
1×2×3 Array{Int64, 3}:
[:, :, 1] =
 1  2

[:, :, 2] =
 3  4

[:, :, 3] =
 5  6

julia> hvncat(((3, 3), (3, 3), (6,)), true, a, b, c, d, e, f)
1×3×2 Array{Int64, 3}:
[:, :, 1] =
 1  2  3

[:, :, 2] =
 4  5  6
```

# Examples for construction of the arguments

```
[a b c ; d e f ;;;
 g h i ; j k l ;;;
 m n o ; p q r ;;;
 s t u ; v w x]
⇒ dims = (2, 3, 4)

[a b ; c ;;; d ;;;;]
 ___   _     _
 2     1     1 = elements in each row (2, 1, 1)
 _______     _
 3           1 = elements in each column (3, 1)
 _____________
 4             = elements in each 3d slice (4,)
 _____________
 4             = elements in each 4d slice (4,)
⇒ shape = ((2, 1, 1), (3, 1), (4,), (4,)) with `row_first` = true
```



hypot:
==================================================

```
hypot(x, y)
```

Compute the hypotenuse $\sqrt{|x|^2+|y|^2}$ avoiding overflow and underflow.

This code is an implementation of the algorithm described in: An Improved Algorithm for `hypot(a,b)` by Carlos F. Borges The article is available online at arXiv at the link   https://arxiv.org/abs/1904.09481

```
hypot(x...)
```

Compute the hypotenuse $\sqrt{\sum |x_i|^2}$ avoiding overflow and underflow.

See also `norm` in the [`LinearAlgebra`](@ref man-linalg) standard library.

# Examples

```jldoctest; filter = r"Stacktrace:(\n \[[0-9]+\].*)*"
julia> a = Int64(10)^10;

julia> hypot(a, a)
1.4142135623730951e10

julia> √(a^2 + a^2) # a^2 overflows
ERROR: DomainError with -2.914184810805068e18:
sqrt was called with a negative real argument but will only return a complex result if called with a complex argument. Try sqrt(Complex(x)).
Stacktrace:
[...]

julia> hypot(3, 4im)
5.0

julia> hypot(-5.7)
5.7

julia> hypot(3, 4im, 12.0)
13.0

julia> using LinearAlgebra

julia> norm([a, a, a, a]) == hypot(a, a, a, a)
true
```



identity:
==================================================

```
identity(x)
```

The identity function. Returns its argument.

See also: [`one`](@ref), [`oneunit`](@ref), and [`LinearAlgebra`](@ref man-linalg)'s `I`.

# Examples

```jldoctest
julia> identity("Well, what did you expect?")
"Well, what did you expect?"
```



ifelse:
==================================================

```
ifelse(condition::Bool, x, y)
```

Return `x` if `condition` is `true`, otherwise return `y`. This differs from `?` or `if` in that it is an ordinary function, so all the arguments are evaluated first. In some cases, using `ifelse` instead of an `if` statement can eliminate the branch in generated code and provide higher performance in tight loops.

# Examples

```jldoctest
julia> ifelse(1 > 2, 1, 2)
2
```



ignorestatus:
==================================================

```
ignorestatus(command)
```

Mark a command object so that running it will not throw an error if the result code is non-zero.



im:
==================================================

```
Complex{T<:Real} <: Number
```

Complex number type with real and imaginary part of type `T`.

`ComplexF16`, `ComplexF32` and `ComplexF64` are aliases for `Complex{Float16}`, `Complex{Float32}` and `Complex{Float64}` respectively.

See also: [`Real`](@ref), [`complex`](@ref), [`real`](@ref).



imag:
==================================================

```
imag(z)
```

Return the imaginary part of the complex number `z`.

See also: [`conj`](@ref), [`reim`](@ref), [`adjoint`](@ref), [`angle`](@ref).

# Examples

```jldoctest
julia> imag(1 + 3im)
3
```

```
imag(A::AbstractArray)
```

Return an array containing the imaginary part of each entry in array `A`.

Equivalent to `imag.(A)`, except that when `A` has zero dimensions, a 0-dimensional array is returned (rather than a scalar).

# Examples

```jldoctest
julia> imag([1, 2im, 3 + 4im])
3-element Vector{Int64}:
 0
 2
 4

julia> imag(fill(2 - im))
0-dimensional Array{Int64, 0}:
-1
```



in:
==================================================

```
in(collection)
∈(collection)
```

Create a function that checks whether its argument is [`in`](@ref) `collection`, i.e. a function equivalent to `y -> y in collection`. See also [`insorted`](@ref) for use with sorted collections.

The returned function is of type `Base.Fix2{typeof(in)}`, which can be used to implement specialized methods.

```
in(item, collection) -> Bool
∈(item, collection) -> Bool
```

Determine whether an item is in the given collection, in the sense that it is [`==`](@ref) to one of the values generated by iterating over the collection. Return a `Bool` value, except if `item` is [`missing`](@ref) or `collection` contains `missing` but not `item`, in which case `missing` is returned ([three-valued logic](https://en.wikipedia.org/wiki/Three-valued_logic), matching the behavior of [`any`](@ref) and [`==`](@ref)).

Some collections follow a slightly different definition. For example, [`Set`](@ref)s check whether the item [`isequal`](@ref) to one of the elements; [`Dict`](@ref)s look for `key=>value` pairs, and the `key` is compared using [`isequal`](@ref).

To test for the presence of a key in a dictionary, use [`haskey`](@ref) or `k in keys(dict)`. For the collections mentioned above, the result is always a `Bool`.

When broadcasting with `in.(items, collection)` or `items .∈ collection`, both `item` and `collection` are broadcasted over, which is often not what is intended. For example, if both arguments are vectors (and the dimensions match), the result is a vector indicating whether each value in collection `items` is `in` the value at the corresponding position in `collection`. To get a vector indicating whether each value in `items` is in `collection`, wrap `collection` in a tuple or a `Ref` like this: `in.(items, Ref(collection))` or `items .∈ Ref(collection)`.

See also: [`∉`](@ref), [`insorted`](@ref), [`contains`](@ref), [`occursin`](@ref), [`issubset`](@ref).

# Examples

```jldoctest
julia> a = 1:3:20
1:3:19

julia> 4 in a
true

julia> 5 in a
false

julia> missing in [1, 2]
missing

julia> 1 in [2, missing]
missing

julia> 1 in [1, missing]
true

julia> missing in Set([1, 2])
false

julia> (1=>missing) in Dict(1=>10, 2=>20)
missing

julia> [1, 2] .∈ [2, 3]
2-element BitVector:
 0
 0

julia> [1, 2] .∈ ([2, 3],)
2-element BitVector:
 0
 1
```



in!:
==================================================

```
in!(x, s::AbstractSet) -> Bool
```

If `x` is in `s`, return `true`. If not, push `x` into `s` and return `false`. This is equivalent to `in(x, s) ? true : (push!(s, x); false)`, but may have a more efficient implementation.

See also: [`in`](@ref), [`push!`](@ref), [`Set`](@ref)

!!! compat "Julia 1.11"
    This function requires at least 1.11.


# Examples

```jldoctest; filter = r"^  [1234]$"
julia> s = Set{Any}([1, 2, 3]); in!(4, s)
false

julia> length(s)
4

julia> in!(0x04, s)
true

julia> s
Set{Any} with 4 elements:
  4
  2
  3
  1
```



include:
==================================================

```
include([mapexpr::Function,] path::AbstractString)
```

Evaluate the contents of the input source file in the global scope of the containing module. Every module (except those defined with `baremodule`) has its own definition of `include`, which evaluates the file in that module. Returns the result of the last evaluated expression of the input file. During including, a task-local include path is set to the directory containing the file. Nested calls to `include` will search relative to that path. This function is typically used to load source interactively, or to combine files in packages that are broken into multiple source files. The argument `path` is normalized using [`normpath`](@ref) which will resolve relative path tokens such as `..` and convert `/` to the appropriate path separator.

The optional first argument `mapexpr` can be used to transform the included code before it is evaluated: for each parsed expression `expr` in `path`, the `include` function actually evaluates `mapexpr(expr)`.  If it is omitted, `mapexpr` defaults to [`identity`](@ref).

Use [`Base.include`](@ref) to evaluate a file into another module.

!!! compat "Julia 1.5"
    Julia 1.5 is required for passing the `mapexpr` argument.




include_dependency:
==================================================

```
include_dependency(path::AbstractString; track_content::Bool=true)
```

In a module, declare that the file, directory, or symbolic link specified by `path` (relative or absolute) is a dependency for precompilation; that is, if `track_content=true` the module will need to be recompiled if the content of `path` changes (if `path` is a directory the content equals `join(readdir(path))`). If `track_content=false` recompilation is triggered when the modification time `mtime` of `path` changes.

This is only needed if your module depends on a path that is not used via [`include`](@ref). It has no effect outside of compilation.

!!! compat "Julia 1.11"
    Keyword argument `track_content` requires at least Julia 1.11. An error is now thrown if `path` is not readable.




include_string:
==================================================

```
include_string([mapexpr::Function,] m::Module, code::AbstractString, filename::AbstractString="string")
```

Like [`include`](@ref), except reads code from the given string rather than from a file.

The optional first argument `mapexpr` can be used to transform the included code before it is evaluated: for each parsed expression `expr` in `code`, the `include_string` function actually evaluates `mapexpr(expr)`.  If it is omitted, `mapexpr` defaults to [`identity`](@ref).

!!! compat "Julia 1.5"
    Julia 1.5 is required for passing the `mapexpr` argument.




indexin:
==================================================

```
indexin(a, b)
```

Return an array containing the first index in `b` for each value in `a` that is a member of `b`. The output array contains `nothing` wherever `a` is not a member of `b`.

See also: [`sortperm`](@ref), [`findfirst`](@ref).

# Examples

```jldoctest
julia> a = ['a', 'b', 'c', 'b', 'd', 'a'];

julia> b = ['a', 'b', 'c'];

julia> indexin(a, b)
6-element Vector{Union{Nothing, Int64}}:
 1
 2
 3
 2
  nothing
 1

julia> indexin(b, a)
3-element Vector{Union{Nothing, Int64}}:
 1
 2
 3
```



insert!:
==================================================

```
insert!(a::Vector, index::Integer, item)
```

Insert an `item` into `a` at the given `index`. `index` is the index of `item` in the resulting `a`.

See also: [`push!`](@ref), [`replace`](@ref), [`popat!`](@ref), [`splice!`](@ref).

# Examples

```jldoctest
julia> insert!(Any[1:6;], 3, "here")
7-element Vector{Any}:
 1
 2
  "here"
 3
 4
 5
 6
```



insorted:
==================================================

```
insorted(x, v; by=identity, lt=isless, rev=false) -> Bool
```

Determine whether a vector `v` contains any value equivalent to `x`. The vector `v` must be sorted according to the order defined by the keywords. Refer to [`sort!`](@ref) for the meaning of the keywords and the definition of equivalence. Note that the `by` function is applied to the searched value `x` as well as the values in `v`.

The check is generally done using binary search, but there are optimized implementations for some inputs.

See also [`in`](@ref).

# Examples

```jldoctest
julia> insorted(4, [1, 2, 4, 5, 5, 7]) # single match
true

julia> insorted(5, [1, 2, 4, 5, 5, 7]) # multiple matches
true

julia> insorted(3, [1, 2, 4, 5, 5, 7]) # no match
false

julia> insorted(9, [1, 2, 4, 5, 5, 7]) # no match
false

julia> insorted(0, [1, 2, 4, 5, 5, 7]) # no match
false

julia> insorted(2=>"TWO", [1=>"one", 2=>"two", 4=>"four"], by=first) # compare the keys of the pairs
true
```

!!! compat "Julia 1.6"
    `insorted` was added in Julia 1.6.




instances:
==================================================

```
instances(T::Type)
```

Return a collection of all instances of the given type, if applicable. Mostly used for enumerated types (see `@enum`).

# Examples

```jldoctest
julia> @enum Color red blue green

julia> instances(Color)
(red, blue, green)
```



intersect:
==================================================

```
intersect(s, itrs...)
∩(s, itrs...)
```

Construct the set containing those elements which appear in all of the arguments.

The first argument controls what kind of container is returned. If this is an array, it maintains the order in which elements first appear.

Unicode `∩` can be typed by writing `\cap` then pressing tab in the Julia REPL, and in many editors. This is an infix operator, allowing `s ∩ itr`.

See also [`setdiff`](@ref), [`isdisjoint`](@ref), [`issubset`](@ref Base.issubset), [`issetequal`](@ref).

!!! compat "Julia 1.8"
    As of Julia 1.8 intersect returns a result with the eltype of the type-promoted eltypes of the two inputs


# Examples

```jldoctest
julia> intersect([1, 2, 3], [3, 4, 5])
1-element Vector{Int64}:
 3

julia> intersect([1, 4, 4, 5, 6], [6, 4, 6, 7, 8])
2-element Vector{Int64}:
 4
 6

julia> intersect(1:16, 7:99)
7:16

julia> (0, 0.0) ∩ (-0.0, 0)
1-element Vector{Real}:
 0

julia> intersect(Set([1, 2]), BitSet([2, 3]), 1.0:10.0)
Set{Float64} with 1 element:
  2.0
```



intersect!:
==================================================

```
intersect!(s::Union{AbstractSet,AbstractVector}, itrs...)
```

Intersect all passed in sets and overwrite `s` with the result. Maintain order with arrays.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.




inv:
==================================================

```
inv(x)
```

Return the multiplicative inverse of `x`, such that `x*inv(x)` or `inv(x)*x` yields [`one(x)`](@ref) (the multiplicative identity) up to roundoff errors.

If `x` is a number, this is essentially the same as `one(x)/x`, but for some types `inv(x)` may be slightly more efficient.

# Examples

```jldoctest
julia> inv(2)
0.5

julia> inv(1 + 2im)
0.2 - 0.4im

julia> inv(1 + 2im) * (1 + 2im)
1.0 + 0.0im

julia> inv(2//3)
3//2
```

!!! compat "Julia 1.2"
    `inv(::Missing)` requires at least Julia 1.2.


```
inv(M)
```

Matrix inverse. Computes matrix `N` such that `M * N = I`, where `I` is the identity matrix. Computed by solving the left-division `N = M \ I`.

# Examples

```jldoctest
julia> M = [2 5; 1 3]
2×2 Matrix{Int64}:
 2  5
 1  3

julia> N = inv(M)
2×2 Matrix{Float64}:
  3.0  -5.0
 -1.0   2.0

julia> M*N == N*M == Matrix(I, 2, 2)
true
```



invmod:
==================================================

```
invmod(n::Integer, m::Integer)
```

Take the inverse of `n` modulo `m`: `y` such that $n y = 1 \pmod m$, and $div(y,m) = 0$. This will throw an error if $m = 0$, or if $gcd(n,m) \neq 1$.

# Examples

```jldoctest
julia> invmod(2, 5)
3

julia> invmod(2, 3)
2

julia> invmod(5, 6)
5
```

```
invmod(n::Integer, T) where {T <: Base.BitInteger}
invmod(n::T) where {T <: Base.BitInteger}
```

Compute the modular inverse of `n` in the integer ring of type `T`, i.e. modulo `2^N` where `N = 8*sizeof(T)` (e.g. `N = 32` for `Int32`). In other words these methods satisfy the following identities:

```
n * invmod(n) == 1
(n * invmod(n, T)) % T == 1
(n % T) * invmod(n, T) == 1
```

Note that `*` here is modular multiplication in the integer ring, `T`.

Specifying the modulus implied by an integer type as an explicit value is often inconvenient since the modulus is by definition too big to be represented by the type.

The modular inverse is computed much more efficiently than the general case using the algorithm described in https://arxiv.org/pdf/2204.04342.pdf.

!!! compat "Julia 1.11"
    The `invmod(n)` and `invmod(n, T)` methods require Julia 1.11 or later.




invoke:
==================================================

```
invoke(f, argtypes::Type, args...; kwargs...)
```

Invoke a method for the given generic function `f` matching the specified types `argtypes` on the specified arguments `args` and passing the keyword arguments `kwargs`. The arguments `args` must conform with the specified types in `argtypes`, i.e. conversion is not automatically performed. This method allows invoking a method other than the most specific matching method, which is useful when the behavior of a more general definition is explicitly needed (often as part of the implementation of a more specific method of the same function).

Be careful when using `invoke` for functions that you don't write.  What definition is used for given `argtypes` is an implementation detail unless the function is explicitly states that calling with certain `argtypes` is a part of public API.  For example, the change between `f1` and `f2` in the example below is usually considered compatible because the change is invisible by the caller with a normal (non-`invoke`) call.  However, the change is visible if you use `invoke`.

# Examples

```jldoctest
julia> f(x::Real) = x^2;

julia> f(x::Integer) = 1 + invoke(f, Tuple{Real}, x);

julia> f(2)
5

julia> f1(::Integer) = Integer
       f1(::Real) = Real;

julia> f2(x::Real) = _f2(x)
       _f2(::Integer) = Integer
       _f2(_) = Real;

julia> f1(1)
Integer

julia> f2(1)
Integer

julia> invoke(f1, Tuple{Real}, 1)
Real

julia> invoke(f2, Tuple{Real}, 1)
Integer
```



invokelatest:
==================================================

```
invokelatest(f, args...; kwargs...)
```

Calls `f(args...; kwargs...)`, but guarantees that the most recent method of `f` will be executed.   This is useful in specialized circumstances, e.g. long-running event loops or callback functions that may call obsolete versions of a function `f`. (The drawback is that `invokelatest` is somewhat slower than calling `f` directly, and the type of the result cannot be inferred by the compiler.)

!!! compat "Julia 1.9"
    Prior to Julia 1.9, this function was not exported, and was called as `Base.invokelatest`.




invperm:
==================================================

```
invperm(v)
```

Return the inverse permutation of `v`. If `B = A[v]`, then `A == B[invperm(v)]`.

See also [`sortperm`](@ref), [`invpermute!`](@ref), [`isperm`](@ref), [`permutedims`](@ref).

# Examples

```jldoctest
julia> p = (2, 3, 1);

julia> invperm(p)
(3, 1, 2)

julia> v = [2; 4; 3; 1];

julia> invperm(v)
4-element Vector{Int64}:
 4
 1
 3
 2

julia> A = ['a','b','c','d'];

julia> B = A[v]
4-element Vector{Char}:
 'b': ASCII/Unicode U+0062 (category Ll: Letter, lowercase)
 'd': ASCII/Unicode U+0064 (category Ll: Letter, lowercase)
 'c': ASCII/Unicode U+0063 (category Ll: Letter, lowercase)
 'a': ASCII/Unicode U+0061 (category Ll: Letter, lowercase)

julia> B[invperm(v)]
4-element Vector{Char}:
 'a': ASCII/Unicode U+0061 (category Ll: Letter, lowercase)
 'b': ASCII/Unicode U+0062 (category Ll: Letter, lowercase)
 'c': ASCII/Unicode U+0063 (category Ll: Letter, lowercase)
 'd': ASCII/Unicode U+0064 (category Ll: Letter, lowercase)
```



invpermute!:
==================================================

```
invpermute!(v, p)
```

Like [`permute!`](@ref), but the inverse of the given permutation is applied.

Note that if you have a pre-allocated output array (e.g. `u = similar(v)`), it is quicker to instead employ `u[p] = v`.  (`invpermute!` internally allocates a copy of the data.)

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


# Examples

```jldoctest
julia> A = [1, 1, 3, 4];

julia> perm = [2, 4, 3, 1];

julia> invpermute!(A, perm);

julia> A
4-element Vector{Int64}:
 4
 1
 3
 1
```



isa:
==================================================

```
isa(x, type) -> Bool
```

Determine whether `x` is of the given `type`. Can also be used as an infix operator, e.g. `x isa type`.

# Examples

```jldoctest
julia> isa(1, Int)
true

julia> isa(1, Matrix)
false

julia> isa(1, Char)
false

julia> isa(1, Number)
true

julia> 1 isa Number
true
```



isabspath:
==================================================

```
isabspath(path::AbstractString) -> Bool
```

Determine whether a path is absolute (begins at the root directory).

# Examples

```jldoctest
julia> isabspath("/home")
true

julia> isabspath("home")
false
```



isabstracttype:
==================================================

```
isabstracttype(T)
```

Determine whether type `T` was declared as an abstract type (i.e. using the `abstract type` syntax). Note that this is not the negation of `isconcretetype(T)`. If `T` is not a type, then return `false`.

# Examples

```jldoctest
julia> isabstracttype(AbstractArray)
true

julia> isabstracttype(Vector)
false
```



isapprox:
==================================================

```
isapprox(x, y; atol::Real=0, rtol::Real=atol>0 ? 0 : √eps, nans::Bool=false[, norm::Function])
```

Inexact equality comparison. Two numbers compare equal if their relative distance *or* their absolute distance is within tolerance bounds: `isapprox` returns `true` if `norm(x-y) <= max(atol, rtol*max(norm(x), norm(y)))`. The default `atol` (absolute tolerance) is zero and the default `rtol` (relative tolerance) depends on the types of `x` and `y`. The keyword argument `nans` determines whether or not NaN values are considered equal (defaults to false).

For real or complex floating-point values, if an `atol > 0` is not specified, `rtol` defaults to the square root of [`eps`](@ref) of the type of `x` or `y`, whichever is bigger (least precise). This corresponds to requiring equality of about half of the significant digits. Otherwise, e.g. for integer arguments or if an `atol > 0` is supplied, `rtol` defaults to zero.

The `norm` keyword defaults to `abs` for numeric `(x,y)` and to `LinearAlgebra.norm` for arrays (where an alternative `norm` choice is sometimes useful). When `x` and `y` are arrays, if `norm(x-y)` is not finite (i.e. `±Inf` or `NaN`), the comparison falls back to checking whether all elements of `x` and `y` are approximately equal component-wise.

The binary operator `≈` is equivalent to `isapprox` with the default arguments, and `x ≉ y` is equivalent to `!isapprox(x,y)`.

Note that `x ≈ 0` (i.e., comparing to zero with the default tolerances) is equivalent to `x == 0` since the default `atol` is `0`.  In such cases, you should either supply an appropriate `atol` (or use `norm(x) ≤ atol`) or rearrange your code (e.g. use `x ≈ y` rather than `x - y ≈ 0`).   It is not possible to pick a nonzero `atol` automatically because it depends on the overall scaling (the "units") of your problem: for example, in `x - y ≈ 0`, `atol=1e-9` is an absurdly small tolerance if `x` is the [radius of the Earth](https://en.wikipedia.org/wiki/Earth_radius) in meters, but an absurdly large tolerance if `x` is the [radius of a Hydrogen atom](https://en.wikipedia.org/wiki/Bohr_radius) in meters.

!!! compat "Julia 1.6"
    Passing the `norm` keyword argument when comparing numeric (non-array) arguments requires Julia 1.6 or later.


# Examples

```jldoctest
julia> isapprox(0.1, 0.15; atol=0.05)
true

julia> isapprox(0.1, 0.15; rtol=0.34)
true

julia> isapprox(0.1, 0.15; rtol=0.33)
false

julia> 0.1 + 1e-10 ≈ 0.1
true

julia> 1e-10 ≈ 0
false

julia> isapprox(1e-10, 0, atol=1e-8)
true

julia> isapprox([10.0^9, 1.0], [10.0^9, 2.0]) # using `norm`
true
```

```
isapprox(x; kwargs...) / ≈(x; kwargs...)
```

Create a function that compares its argument to `x` using `≈`, i.e. a function equivalent to `y -> y ≈ x`.

The keyword arguments supported here are the same as those in the 2-argument `isapprox`.

!!! compat "Julia 1.5"
    This method requires Julia 1.5 or later.




isascii:
==================================================

```
isascii(c::Union{AbstractChar,AbstractString}) -> Bool
```

Test whether a character belongs to the ASCII character set, or whether this is true for all elements of a string.

# Examples

```jldoctest
julia> isascii('a')
true

julia> isascii('α')
false

julia> isascii("abc")
true

julia> isascii("αβγ")
false
```

For example, `isascii` can be used as a predicate function for [`filter`](@ref) or [`replace`](@ref) to remove or replace non-ASCII characters, respectively:

```jldoctest
julia> filter(isascii, "abcdeγfgh") # discard non-ASCII chars
"abcdefgh"

julia> replace("abcdeγfgh", !isascii=>' ') # replace non-ASCII chars with spaces
"abcde fgh"
```

```
isascii(cu::AbstractVector{CU}) where {CU <: Integer} -> Bool
```

Test whether all values in the vector belong to the ASCII character set (0x00 to 0x7f). This function is intended to be used by other string implementations that need a fast ASCII check.



isassigned:
==================================================

```
isassigned(array, i) -> Bool
```

Test whether the given array has a value associated with index `i`. Return `false` if the index is out of bounds, or has an undefined reference.

# Examples

```jldoctest
julia> isassigned(rand(3, 3), 5)
true

julia> isassigned(rand(3, 3), 3 * 3 + 1)
false

julia> mutable struct Foo end

julia> v = similar(rand(3), Foo)
3-element Vector{Foo}:
 #undef
 #undef
 #undef

julia> isassigned(v, 1)
false
```

```
isassigned(ref::RefValue) -> Bool
```

Test whether the given [`Ref`](@ref) is associated with a value. This is always true for a [`Ref`](@ref) of a bitstype object. Return `false` if the reference is undefined.

# Examples

```jldoctest
julia> ref = Ref{Function}()
Base.RefValue{Function}(#undef)

julia> isassigned(ref)
false

julia> ref[] = (foobar(x) = x)
foobar (generic function with 1 method)

julia> isassigned(ref)
true

julia> isassigned(Ref{Int}())
true
```

```
isassigned(val::ScopedValue)
```

Test whether a `ScopedValue` has an assigned value.

See also: [`ScopedValues.with`](@ref), [`ScopedValues.@with`](@ref), [`ScopedValues.get`](@ref).

# Examples

```jldoctest
julia> using Base.ScopedValues

julia> a = ScopedValue(1); b = ScopedValue{Int}();

julia> isassigned(a)
true

julia> isassigned(b)
false
```



isbits:
==================================================

```
isbits(x)
```

Return `true` if `x` is an instance of an [`isbitstype`](@ref) type.



isbitstype:
==================================================

```
isbitstype(T)
```

Return `true` if type `T` is a "plain data" type, meaning it is immutable and contains no references to other values, only `primitive` types and other `isbitstype` types. Typical examples are numeric types such as [`UInt8`](@ref), [`Float64`](@ref), and [`Complex{Float64}`](@ref). This category of types is significant since they are valid as type parameters, may not track [`isdefined`](@ref) / [`isassigned`](@ref) status, and have a defined layout that is compatible with C. If `T` is not a type, then return `false`.

See also [`isbits`](@ref), [`isprimitivetype`](@ref), [`ismutable`](@ref).

# Examples

```jldoctest
julia> isbitstype(Complex{Float64})
true

julia> isbitstype(Complex)
false
```



isblockdev:
==================================================

```
isblockdev(path) -> Bool
```

Return `true` if `path` is a block device, `false` otherwise.



ischardev:
==================================================

```
ischardev(path) -> Bool
```

Return `true` if `path` is a character device, `false` otherwise.



iscntrl:
==================================================

```
iscntrl(c::AbstractChar) -> Bool
```

Tests whether a character is a control character. Control characters are the non-printing characters of the Latin-1 subset of Unicode.

# Examples

```jldoctest
julia> iscntrl('\x01')
true

julia> iscntrl('a')
false
```



isconcretetype:
==================================================

```
isconcretetype(T)
```

Determine whether type `T` is a concrete type, meaning it could have direct instances (values `x` such that `typeof(x) === T`). Note that this is not the negation of `isabstracttype(T)`. If `T` is not a type, then return `false`.

See also: [`isbits`](@ref), [`isabstracttype`](@ref), [`issingletontype`](@ref).

# Examples

```jldoctest
julia> isconcretetype(Complex)
false

julia> isconcretetype(Complex{Float32})
true

julia> isconcretetype(Vector{Complex})
true

julia> isconcretetype(Vector{Complex{Float32}})
true

julia> isconcretetype(Union{})
false

julia> isconcretetype(Union{Int,String})
false
```



isconst:
==================================================

```
isconst(m::Module, s::Symbol) -> Bool
```

Determine whether a global is declared `const` in a given module `m`.

```
isconst(t::DataType, s::Union{Int,Symbol}) -> Bool
```

Determine whether a field `s` is declared `const` in a given type `t`.



isdefined:
==================================================

```
isdefined(m::Module, s::Symbol, [order::Symbol])
isdefined(object, s::Symbol, [order::Symbol])
isdefined(object, index::Int, [order::Symbol])
```

Tests whether a global variable or object field is defined. The arguments can be a module and a symbol or a composite object and field name (as a symbol) or index. Optionally, an ordering can be defined for the operation. If the field was declared `@atomic`, the specification is strongly recommended to be compatible with the stores to that location. Otherwise, if not declared as `@atomic`, this parameter must be `:not_atomic` if specified.

To test whether an array element is defined, use [`isassigned`](@ref) instead.

See also [`@isdefined`](@ref).

# Examples

```jldoctest
julia> isdefined(Base, :sum)
true

julia> isdefined(Base, :NonExistentMethod)
false

julia> a = 1//2;

julia> isdefined(a, 2)
true

julia> isdefined(a, 3)
false

julia> isdefined(a, :num)
true

julia> isdefined(a, :numerator)
false
```



isdigit:
==================================================

```
isdigit(c::AbstractChar) -> Bool
```

Tests whether a character is a decimal digit (0-9).

See also: [`isletter`](@ref).

# Examples

```jldoctest
julia> isdigit('❤')
false

julia> isdigit('9')
true

julia> isdigit('α')
false
```



isdir:
==================================================

```
isdir(path) -> Bool
```

Return `true` if `path` is a directory, `false` otherwise.

# Examples

```jldoctest
julia> isdir(homedir())
true

julia> isdir("not/a/directory")
false
```

See also [`isfile`](@ref) and [`ispath`](@ref).



isdirpath:
==================================================

```
isdirpath(path::AbstractString) -> Bool
```

Determine whether a path refers to a directory (for example, ends with a path separator).

# Examples

```jldoctest
julia> isdirpath("/home")
false

julia> isdirpath("/home/")
true
```



isdisjoint:
==================================================

```
isdisjoint(a, b) -> Bool
```

Determine whether the collections `a` and `b` are disjoint. Equivalent to `isempty(a ∩ b)` but more efficient when possible.

See also: [`intersect`](@ref), [`isempty`](@ref), [`issetequal`](@ref).

!!! compat "Julia 1.5"
    This function requires at least Julia 1.5.


# Examples

```jldoctest
julia> isdisjoint([1, 2], [2, 3, 4])
false

julia> isdisjoint([3, 1], [2, 4])
true
```

```
isdisjoint(x)
```

Create a function that compares its argument to `x` using [`isdisjoint`](@ref), i.e. a function equivalent to `y -> isdisjoint(y, x)`. The returned function is of type `Base.Fix2{typeof(isdisjoint)}`, which can be used to implement specialized methods.

!!! compat "Julia 1.11"
    This functionality requires at least Julia 1.11.




isdispatchtuple:
==================================================

```
isdispatchtuple(T)
```

Determine whether type `T` is a tuple "leaf type", meaning it could appear as a type signature in dispatch and has no subtypes (or supertypes) which could appear in a call. If `T` is not a type, then return `false`.



isempty:
==================================================

```
isempty(collection) -> Bool
```

Determine whether a collection is empty (has no elements).

!!! warning
    `isempty(itr)` may consume the next element of a stateful iterator `itr` unless an appropriate [`Base.isdone(itr)`](@ref) method is defined. Stateful iterators *should* implement `isdone`, but you may want to avoid using `isempty` when writing generic code which should support any iterator type.


# Examples

```jldoctest
julia> isempty([])
true

julia> isempty([1 2 3])
false
```

```
isempty(condition)
```

Return `true` if no tasks are waiting on the condition, `false` otherwise.



isequal:
==================================================

```
isequal(x, y) -> Bool
```

Similar to [`==`](@ref), except for the treatment of floating point numbers and of missing values. `isequal` treats all floating-point `NaN` values as equal to each other, treats `-0.0` as unequal to `0.0`, and [`missing`](@ref) as equal to `missing`. Always returns a `Bool` value.

`isequal` is an equivalence relation - it is reflexive (`===` implies `isequal`), symmetric (`isequal(a, b)` implies `isequal(b, a)`) and transitive (`isequal(a, b)` and `isequal(b, c)` implies `isequal(a, c)`).

# Implementation

The default implementation of `isequal` calls `==`, so a type that does not involve floating-point values generally only needs to define `==`.

`isequal` is the comparison function used by hash tables (`Dict`). `isequal(x,y)` must imply that `hash(x) == hash(y)`.

This typically means that types for which a custom `==` or `isequal` method exists must implement a corresponding [`hash`](@ref) method (and vice versa). Collections typically implement `isequal` by calling `isequal` recursively on all contents.

Furthermore, `isequal` is linked with [`isless`](@ref), and they work together to define a fixed total ordering, where exactly one of `isequal(x, y)`, `isless(x, y)`, or `isless(y, x)` must be `true` (and the other two `false`).

Scalar types generally do not need to implement `isequal` separate from `==`, unless they represent floating-point numbers amenable to a more efficient implementation than that provided as a generic fallback (based on `isnan`, `signbit`, and `==`).

# Examples

```jldoctest
julia> isequal([1., NaN], [1., NaN])
true

julia> [1., NaN] == [1., NaN]
false

julia> 0.0 == -0.0
true

julia> isequal(0.0, -0.0)
false

julia> missing == missing
missing

julia> isequal(missing, missing)
true
```

```
isequal(x)
```

Create a function that compares its argument to `x` using [`isequal`](@ref), i.e. a function equivalent to `y -> isequal(y, x)`.

The returned function is of type `Base.Fix2{typeof(isequal)}`, which can be used to implement specialized methods.



iseven:
==================================================

```
iseven(x::Number) -> Bool
```

Return `true` if `x` is an even integer (that is, an integer divisible by 2), and `false` otherwise.

!!! compat "Julia 1.7"
    Non-`Integer` arguments require Julia 1.7 or later.


# Examples

```jldoctest
julia> iseven(9)
false

julia> iseven(10)
true
```



isexecutable:
==================================================

```
isexecutable(path::String)
```

Return `true` if the given `path` has executable permissions.

!!! note
    This permission may change before the user executes `path`, so it is recommended to execute the file and handle the error if that fails, rather than calling `isexecutable` first.


!!! note
    Prior to Julia 1.6, this did not correctly interrogate filesystem ACLs on Windows, therefore it would return `true` for any file.  From Julia 1.6 on, it correctly determines whether the file is marked as executable or not.


See also [`ispath`](@ref), [`isreadable`](@ref), [`iswritable`](@ref).



isfifo:
==================================================

```
isfifo(path) -> Bool
```

Return `true` if `path` is a FIFO, `false` otherwise.



isfile:
==================================================

```
isfile(path) -> Bool
```

Return `true` if `path` is a regular file, `false` otherwise.

# Examples

```jldoctest
julia> isfile(homedir())
false

julia> filename = "test_file.txt";

julia> write(filename, "Hello world!");

julia> isfile(filename)
true

julia> rm(filename);

julia> isfile(filename)
false
```

See also [`isdir`](@ref) and [`ispath`](@ref).



isfinite:
==================================================

```
isfinite(f) -> Bool
```

Test whether a number is finite.

# Examples

```jldoctest
julia> isfinite(5)
true

julia> isfinite(NaN32)
false
```



isimmutable:
==================================================

```
isimmutable(v) -> Bool
```

!!! warning
    Consider using `!ismutable(v)` instead, as `isimmutable(v)` will be replaced by `!ismutable(v)` in a future release. (Since Julia 1.5)


Return `true` iff value `v` is immutable.  See [Mutable Composite Types](@ref) for a discussion of immutability. Note that this function works on values, so if you give it a type, it will tell you that a value of `DataType` is mutable.

# Examples

```jldoctest
julia> isimmutable(1)
true

julia> isimmutable([1,2])
false
```



isinf:
==================================================

```
isinf(f) -> Bool
```

Test whether a number is infinite.

See also: [`Inf`](@ref), [`iszero`](@ref), [`isfinite`](@ref), [`isnan`](@ref).



isinteger:
==================================================

```
isinteger(x) -> Bool
```

Test whether `x` is numerically equal to some integer.

# Examples

```jldoctest
julia> isinteger(4.0)
true
```



isinteractive:
==================================================

```
isinteractive() -> Bool
```

Determine whether Julia is running an interactive session.



isless:
==================================================

```
isless(t1::Tuple, t2::Tuple)
```

Return `true` when `t1` is less than `t2` in lexicographic order.

```
isless(x, y)
```

Test whether `x` is less than `y`, according to a fixed total order (defined together with [`isequal`](@ref)). `isless` is not defined for pairs `(x, y)` of all types. However, if it is defined, it is expected to satisfy the following:

  * If `isless(x, y)` is defined, then so is `isless(y, x)` and `isequal(x, y)`, and exactly one of those three yields `true`.
  * The relation defined by `isless` is transitive, i.e., `isless(x, y) && isless(y, z)` implies `isless(x, z)`.

Values that are normally unordered, such as `NaN`, are ordered after regular values. [`missing`](@ref) values are ordered last.

This is the default comparison used by [`sort!`](@ref).

# Implementation

Non-numeric types with a total order should implement this function. Numeric types only need to implement it if they have special values such as `NaN`. Types with a partial order should implement [`<`](@ref). See the documentation on [Alternate Orderings](@ref) for how to define alternate ordering methods that can be used in sorting and related functions.

# Examples

```jldoctest
julia> isless(1, 3)
true

julia> isless("Red", "Blue")
false
```

```
isless(A::AbstractVector, B::AbstractVector)
```

Return `true` when `A` is less than `B` in lexicographic order.

```
isless(a::AbstractString, b::AbstractString) -> Bool
```

Test whether string `a` comes before string `b` in alphabetical order (technically, in lexicographical order by Unicode code points).

# Examples

```jldoctest
julia> isless("a", "b")
true

julia> isless("β", "α")
false

julia> isless("a", "a")
false
```



isletter:
==================================================

```
isletter(c::AbstractChar) -> Bool
```

Test whether a character is a letter. A character is classified as a letter if it belongs to the Unicode general category Letter, i.e. a character whose category code begins with 'L'.

See also: [`isdigit`](@ref).

# Examples

```jldoctest
julia> isletter('❤')
false

julia> isletter('α')
true

julia> isletter('9')
false
```



islink:
==================================================

```
islink(path) -> Bool
```

Return `true` if `path` is a symbolic link, `false` otherwise.



islocked:
==================================================

```
islocked(lock) -> Status (Boolean)
```

Check whether the `lock` is held by any task/thread. This function alone should not be used for synchronization. However, `islocked` combined with [`trylock`](@ref) can be used for writing the test-and-test-and-set or exponential backoff algorithms *if it is supported by the `typeof(lock)`* (read its documentation).

# Extended help

For example, an exponential backoff can be implemented as follows if the `lock` implementation satisfied the properties documented below.

```julia
nspins = 0
while true
    while islocked(lock)
        GC.safepoint()
        nspins += 1
        nspins > LIMIT && error("timeout")
    end
    trylock(lock) && break
    backoff()
end
```

## Implementation

A lock implementation is advised to define `islocked` with the following properties and note it in its docstring.

  * `islocked(lock)` is data-race-free.
  * If `islocked(lock)` returns `false`, an immediate invocation of `trylock(lock)` must succeed (returns `true`) if there is no interference from other tasks.



islowercase:
==================================================

```
islowercase(c::AbstractChar) -> Bool
```

Tests whether a character is a lowercase letter (according to the Unicode standard's `Lowercase` derived property).

See also [`isuppercase`](@ref).

# Examples

```jldoctest
julia> islowercase('α')
true

julia> islowercase('Γ')
false

julia> islowercase('❤')
false
```



ismarked:
==================================================

```
ismarked(s::IO)
```

Return `true` if stream `s` is marked.

See also [`mark`](@ref), [`unmark`](@ref), [`reset`](@ref).



ismissing:
==================================================

```
ismissing(x)
```

Indicate whether `x` is [`missing`](@ref).

See also: [`skipmissing`](@ref), [`isnothing`](@ref), [`isnan`](@ref).



ismount:
==================================================

```
ismount(path) -> Bool
```

Return `true` if `path` is a mount point, `false` otherwise.



ismutable:
==================================================

```
ismutable(v) -> Bool
```

Return `true` if and only if value `v` is mutable.  See [Mutable Composite Types](@ref) for a discussion of immutability. Note that this function works on values, so if you give it a `DataType`, it will tell you that a value of the type is mutable.

!!! note
    For technical reasons, `ismutable` returns `true` for values of certain special types (for example `String` and `Symbol`) even though they cannot be mutated in a permissible way.


See also [`isbits`](@ref), [`isstructtype`](@ref).

# Examples

```jldoctest
julia> ismutable(1)
false

julia> ismutable([1,2])
true
```

!!! compat "Julia 1.5"
    This function requires at least Julia 1.5.




ismutabletype:
==================================================

```
ismutabletype(T) -> Bool
```

Determine whether type `T` was declared as a mutable type (i.e. using `mutable struct` keyword). If `T` is not a type, then return `false`.

!!! compat "Julia 1.7"
    This function requires at least Julia 1.7.




isnan:
==================================================

```
isnan(f) -> Bool
```

Test whether a number value is a NaN, an indeterminate value which is neither an infinity nor a finite number ("not a number").

See also: [`iszero`](@ref), [`isone`](@ref), [`isinf`](@ref), [`ismissing`](@ref).



isnothing:
==================================================

```
isnothing(x)
```

Return `true` if `x === nothing`, and return `false` if not.

!!! compat "Julia 1.1"
    This function requires at least Julia 1.1.


See also [`something`](@ref), [`Base.notnothing`](@ref), [`ismissing`](@ref).



isnumeric:
==================================================

```
isnumeric(c::AbstractChar) -> Bool
```

Tests whether a character is numeric. A character is classified as numeric if it belongs to the Unicode general category Number, i.e. a character whose category code begins with 'N'.

Note that this broad category includes characters such as ¾ and ௰. Use [`isdigit`](@ref) to check whether a character is a decimal digit between 0 and 9.

# Examples

```jldoctest
julia> isnumeric('௰')
true

julia> isnumeric('9')
true

julia> isnumeric('α')
false

julia> isnumeric('❤')
false
```



isodd:
==================================================

```
isodd(x::Number) -> Bool
```

Return `true` if `x` is an odd integer (that is, an integer not divisible by 2), and `false` otherwise.

!!! compat "Julia 1.7"
    Non-`Integer` arguments require Julia 1.7 or later.


# Examples

```jldoctest
julia> isodd(9)
true

julia> isodd(10)
false
```



isone:
==================================================

```
isone(x)
```

Return `true` if `x == one(x)`; if `x` is an array, this checks whether `x` is an identity matrix.

# Examples

```jldoctest
julia> isone(1.0)
true

julia> isone([1 0; 0 2])
false

julia> isone([1 0; 0 true])
true
```



isopen:
==================================================

```
isopen(object) -> Bool
```

Determine whether an object - such as a stream or timer – is not yet closed. Once an object is closed, it will never produce a new event. However, since a closed stream may still have data to read in its buffer, use [`eof`](@ref) to check for the ability to read data. Use the `FileWatching` package to be notified when a stream might be writable or readable.

# Examples

```jldoctest
julia> io = open("my_file.txt", "w+");

julia> isopen(io)
true

julia> close(io)

julia> isopen(io)
false
```



ispath:
==================================================

```
ispath(path) -> Bool
```

Return `true` if a valid filesystem entity exists at `path`, otherwise returns `false`. This is the generalization of [`isfile`](@ref), [`isdir`](@ref) etc.



isperm:
==================================================

```
isperm(v) -> Bool
```

Return `true` if `v` is a valid permutation.

# Examples

```jldoctest
julia> isperm([1; 2])
true

julia> isperm([1; 3])
false
```



ispow2:
==================================================

```
ispow2(n::Number) -> Bool
```

Test whether `n` is an integer power of two.

See also [`count_ones`](@ref), [`prevpow`](@ref), [`nextpow`](@ref).

# Examples

```jldoctest
julia> ispow2(4)
true

julia> ispow2(5)
false

julia> ispow2(4.5)
false

julia> ispow2(0.25)
true

julia> ispow2(1//8)
true
```

!!! compat "Julia 1.6"
    Support for non-`Integer` arguments was added in Julia 1.6.




isprimitivetype:
==================================================

```
isprimitivetype(T) -> Bool
```

Determine whether type `T` was declared as a primitive type (i.e. using the `primitive type` syntax). If `T` is not a type, then return `false`.



isprint:
==================================================

```
isprint(c::AbstractChar) -> Bool
```

Tests whether a character is printable, including spaces, but not a control character.

# Examples

```jldoctest
julia> isprint('\x01')
false

julia> isprint('A')
true
```



ispunct:
==================================================

```
ispunct(c::AbstractChar) -> Bool
```

Tests whether a character belongs to the Unicode general category Punctuation, i.e. a character whose category code begins with 'P'.

# Examples

```jldoctest
julia> ispunct('α')
false

julia> ispunct('/')
true

julia> ispunct(';')
true
```



isqrt:
==================================================

```
isqrt(n::Integer)
```

Integer square root: the largest integer `m` such that `m*m <= n`.

```jldoctest
julia> isqrt(5)
2
```



isreadable:
==================================================

```
isreadable(io) -> Bool
```

Return `false` if the specified IO object is not readable.

# Examples

```jldoctest
julia> open("myfile.txt", "w") do io
           print(io, "Hello world!");
           isreadable(io)
       end
false

julia> open("myfile.txt", "r") do io
           isreadable(io)
       end
true

julia> rm("myfile.txt")
```

```
isreadable(path::String)
```

Return `true` if the access permissions for the given `path` permitted reading by the current user.

!!! note
    This permission may change before the user calls `open`, so it is recommended to just call `open` alone and handle the error if that fails, rather than calling `isreadable` first.


!!! note
    Currently this function does not correctly interrogate filesystem ACLs on Windows, therefore it can return wrong results.


!!! compat "Julia 1.11"
    This function requires at least Julia 1.11.


See also [`ispath`](@ref), [`isexecutable`](@ref), [`iswritable`](@ref).



isreadonly:
==================================================

```
isreadonly(io) -> Bool
```

Determine whether a stream is read-only.

# Examples

```jldoctest
julia> io = IOBuffer("JuliaLang is a GitHub organization");

julia> isreadonly(io)
true

julia> io = IOBuffer();

julia> isreadonly(io)
false
```



isready:
==================================================

```
isready(c::Channel)
```

Determines whether a [`Channel`](@ref) has a value stored in it. Returns immediately, does not block.

For unbuffered channels returns `true` if there are tasks waiting on a [`put!`](@ref).

# Examples

Buffered channel:

```jldoctest
julia> c = Channel(1);

julia> isready(c)
false

julia> put!(c, 1);

julia> isready(c)
true
```

Unbuffered channel:

```jldoctest
julia> c = Channel();

julia> isready(c)  # no tasks waiting to put!
false

julia> task = Task(() -> put!(c, 1));

julia> schedule(task);  # schedule a put! task

julia> isready(c)
true
```



isreal:
==================================================

```
isreal(x) -> Bool
```

Test whether `x` or all its elements are numerically equal to some real number including infinities and NaNs. `isreal(x)` is true if `isequal(x, real(x))` is true.

# Examples

```jldoctest
julia> isreal(5.)
true

julia> isreal(1 - 3im)
false

julia> isreal(Inf + 0im)
true

julia> isreal([4.; complex(0,1)])
false
```



issetequal:
==================================================

```
issetequal(a, b) -> Bool
```

Determine whether `a` and `b` have the same elements. Equivalent to `a ⊆ b && b ⊆ a` but more efficient when possible.

See also: [`isdisjoint`](@ref), [`union`](@ref).

# Examples

```jldoctest
julia> issetequal([1, 2], [1, 2, 3])
false

julia> issetequal([1, 2], [2, 1])
true
```

```
issetequal(x)
```

Create a function that compares its argument to `x` using [`issetequal`](@ref), i.e. a function equivalent to `y -> issetequal(y, x)`. The returned function is of type `Base.Fix2{typeof(issetequal)}`, which can be used to implement specialized methods.

!!! compat "Julia 1.11"
    This functionality requires at least Julia 1.11.




issetgid:
==================================================

```
issetgid(path) -> Bool
```

Return `true` if `path` has the setgid flag set, `false` otherwise.



issetuid:
==================================================

```
issetuid(path) -> Bool
```

Return `true` if `path` has the setuid flag set, `false` otherwise.



issocket:
==================================================

```
issocket(path) -> Bool
```

Return `true` if `path` is a socket, `false` otherwise.



issorted:
==================================================

```
issorted(v, lt=isless, by=identity, rev::Bool=false, order::Ordering=Forward)
```

Test whether a collection is in sorted order. The keywords modify what order is considered sorted, as described in the [`sort!`](@ref) documentation.

# Examples

```jldoctest
julia> issorted([1, 2, 3])
true

julia> issorted([(1, "b"), (2, "a")], by = x -> x[1])
true

julia> issorted([(1, "b"), (2, "a")], by = x -> x[2])
false

julia> issorted([(1, "b"), (2, "a")], by = x -> x[2], rev=true)
true

julia> issorted([1, 2, -2, 3], by=abs)
true
```



isspace:
==================================================

```
isspace(c::AbstractChar) -> Bool
```

Tests whether a character is any whitespace character. Includes ASCII characters '\t', '\n', '\v', '\f', '\r', and ' ', Latin-1 character U+0085, and characters in Unicode category Zs.

# Examples

```jldoctest
julia> isspace('\n')
true

julia> isspace('\r')
true

julia> isspace(' ')
true

julia> isspace('\x20')
true
```



issticky:
==================================================

```
issticky(path) -> Bool
```

Return `true` if `path` has the sticky bit set, `false` otherwise.



isstructtype:
==================================================

```
isstructtype(T) -> Bool
```

Determine whether type `T` was declared as a struct type (i.e. using the `struct` or `mutable struct` keyword). If `T` is not a type, then return `false`.



issubnormal:
==================================================

```
issubnormal(f) -> Bool
```

Test whether a floating point number is subnormal.

An IEEE floating point number is [subnormal](https://en.wikipedia.org/wiki/Subnormal_number) when its exponent bits are zero and its significand is not zero.

# Examples

```jldoctest
julia> floatmin(Float32)
1.1754944f-38

julia> issubnormal(1.0f-37)
false

julia> issubnormal(1.0f-38)
true
```



issubset:
==================================================

```
issubset(a, b) -> Bool
⊆(a, b) -> Bool
⊇(b, a) -> Bool
```

Determine whether every element of `a` is also in `b`, using [`in`](@ref).

See also [`⊊`](@ref), [`⊈`](@ref), [`∩`](@ref intersect), [`∪`](@ref union), [`contains`](@ref).

# Examples

```jldoctest
julia> issubset([1, 2], [1, 2, 3])
true

julia> [1, 2, 3] ⊆ [1, 2]
false

julia> [1, 2, 3] ⊇ [1, 2]
true
```

```
issubset(x)
```

Create a function that compares its argument to `x` using [`issubset`](@ref), i.e. a function equivalent to `y -> issubset(y, x)`. The returned function is of type `Base.Fix2{typeof(issubset)}`, which can be used to implement specialized methods.

!!! compat "Julia 1.11"
    This functionality requires at least Julia 1.11.




istaskdone:
==================================================

```
istaskdone(t::Task) -> Bool
```

Determine whether a task has exited.

# Examples

```jldoctest
julia> a2() = sum(i for i in 1:1000);

julia> b = Task(a2);

julia> istaskdone(b)
false

julia> schedule(b);

julia> yield();

julia> istaskdone(b)
true
```



istaskfailed:
==================================================

```
istaskfailed(t::Task) -> Bool
```

Determine whether a task has exited because an exception was thrown.

# Examples

```jldoctest
julia> a4() = error("task failed");

julia> b = Task(a4);

julia> istaskfailed(b)
false

julia> schedule(b);

julia> yield();

julia> istaskfailed(b)
true
```

!!! compat "Julia 1.3"
    This function requires at least Julia 1.3.




istaskstarted:
==================================================

```
istaskstarted(t::Task) -> Bool
```

Determine whether a task has started executing.

# Examples

```jldoctest
julia> a3() = sum(i for i in 1:1000);

julia> b = Task(a3);

julia> istaskstarted(b)
false
```



istextmime:
==================================================

```
istextmime(m::MIME)
```

Determine whether a MIME type is text data. MIME types are assumed to be binary data except for a set of types known to be text data (possibly Unicode).

# Examples

```jldoctest
julia> istextmime(MIME("text/plain"))
true

julia> istextmime(MIME("image/png"))
false
```



isunordered:
==================================================

```
isunordered(x)
```

Return `true` if `x` is a value that is not orderable according to [`<`](@ref), such as `NaN` or `missing`.

The values that evaluate to `true` with this predicate may be orderable with respect to other orderings such as [`isless`](@ref).

!!! compat "Julia 1.7"
    This function requires Julia 1.7 or later.




isuppercase:
==================================================

```
isuppercase(c::AbstractChar) -> Bool
```

Tests whether a character is an uppercase letter (according to the Unicode standard's `Uppercase` derived property).

See also [`islowercase`](@ref).

# Examples

```jldoctest
julia> isuppercase('γ')
false

julia> isuppercase('Γ')
true

julia> isuppercase('❤')
false
```



isvalid:
==================================================

```
isvalid(s::AbstractString, i::Integer) -> Bool
```

Predicate indicating whether the given index is the start of the encoding of a character in `s` or not. If `isvalid(s, i)` is true then `s[i]` will return the character whose encoding starts at that index, if it's false, then `s[i]` will raise an invalid index error or a bounds error depending on if `i` is in bounds. In order for `isvalid(s, i)` to be an O(1) function, the encoding of `s` must be [self-synchronizing](https://en.wikipedia.org/wiki/Self-synchronizing_code). This is a basic assumption of Julia's generic string support.

See also [`getindex`](@ref), [`iterate`](@ref), [`thisind`](@ref), [`nextind`](@ref), [`prevind`](@ref), [`length`](@ref).

# Examples

```jldoctest
julia> str = "αβγdef";

julia> isvalid(str, 1)
true

julia> str[1]
'α': Unicode U+03B1 (category Ll: Letter, lowercase)

julia> isvalid(str, 2)
false

julia> str[2]
ERROR: StringIndexError: invalid index [2], valid nearby indices [1]=>'α', [3]=>'β'
Stacktrace:
[...]
```

```
isvalid(value) -> Bool
```

Return `true` if the given value is valid for its type, which currently can be either `AbstractChar` or `String` or `SubString{String}`.

# Examples

```jldoctest
julia> isvalid(Char(0xd800))
false

julia> isvalid(SubString(String(UInt8[0xfe,0x80,0x80,0x80,0x80,0x80]),1,2))
false

julia> isvalid(Char(0xd799))
true
```

```
isvalid(T, value) -> Bool
```

Return `true` if the given value is valid for that type. Types currently can be either `AbstractChar` or `String`. Values for `AbstractChar` can be of type `AbstractChar` or [`UInt32`](@ref). Values for `String` can be of that type, `SubString{String}`, `Vector{UInt8}`, or a contiguous subarray thereof.

# Examples

```jldoctest
julia> isvalid(Char, 0xd800)
false

julia> isvalid(String, SubString("thisisvalid",1,5))
true

julia> isvalid(Char, 0xd799)
true
```

!!! compat "Julia 1.6"
    Support for subarray values was added in Julia 1.6.




iswritable:
==================================================

```
iswritable(io) -> Bool
```

Return `false` if the specified IO object is not writable.

# Examples

```jldoctest
julia> open("myfile.txt", "w") do io
           print(io, "Hello world!");
           iswritable(io)
       end
true

julia> open("myfile.txt", "r") do io
           iswritable(io)
       end
false

julia> rm("myfile.txt")
```

```
iswritable(path::String)
```

Return `true` if the access permissions for the given `path` permitted writing by the current user.

!!! note
    This permission may change before the user calls `open`, so it is recommended to just call `open` alone and handle the error if that fails, rather than calling `iswritable` first.


!!! note
    Currently this function does not correctly interrogate filesystem ACLs on Windows, therefore it can return wrong results.


!!! compat "Julia 1.11"
    This function requires at least Julia 1.11.


See also [`ispath`](@ref), [`isexecutable`](@ref), [`isreadable`](@ref).



isxdigit:
==================================================

```
isxdigit(c::AbstractChar) -> Bool
```

Test whether a character is a valid hexadecimal digit. Note that this does not include `x` (as in the standard `0x` prefix).

# Examples

```jldoctest
julia> isxdigit('a')
true

julia> isxdigit('x')
false
```



iszero:
==================================================

```
iszero(x)
```

Return `true` if `x == zero(x)`; if `x` is an array, this checks whether all of the elements of `x` are zero.

See also: [`isone`](@ref), [`isinteger`](@ref), [`isfinite`](@ref), [`isnan`](@ref).

# Examples

```jldoctest
julia> iszero(0.0)
true

julia> iszero([1, 9, 0])
false

julia> iszero([false, 0, 0])
true
```



iterate:
==================================================

```
iterate(iter [, state]) -> Union{Nothing, Tuple{Any, Any}}
```

Advance the iterator to obtain the next element. If no elements remain, `nothing` should be returned. Otherwise, a 2-tuple of the next element and the new iteration state should be returned.

```
iterate(s::AbstractString, i::Integer) -> Union{Tuple{<:AbstractChar, Int}, Nothing}
```

Return a tuple of the character in `s` at index `i` with the index of the start of the following character in `s`. This is the key method that allows strings to be iterated, yielding a sequences of characters. If `i` is out of bounds in `s` then a bounds error is raised. The `iterate` function, as part of the iteration protocol may assume that `i` is the start of a character in `s`.

See also [`getindex`](@ref), [`checkbounds`](@ref).



join:
==================================================

```
join([io::IO,] iterator [, delim [, last]])
```

Join any `iterator` into a single string, inserting the given delimiter (if any) between adjacent items.  If `last` is given, it will be used instead of `delim` between the last two items.  Each item of `iterator` is converted to a string via `print(io::IOBuffer, x)`. If `io` is given, the result is written to `io` rather than returned as a `String`.

# Examples

```jldoctest
julia> join(["apples", "bananas", "pineapples"], ", ", " and ")
"apples, bananas and pineapples"

julia> join([1,2,3,4,5])
"12345"
```



keepat!:
==================================================

```
keepat!(a::Vector, inds)
keepat!(a::BitVector, inds)
```

Remove the items at all the indices which are not given by `inds`, and return the modified `a`. Items which are kept are shifted to fill the resulting gaps.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


`inds` must be an iterator of sorted and unique integer indices. See also [`deleteat!`](@ref).

!!! compat "Julia 1.7"
    This function is available as of Julia 1.7.


# Examples

```jldoctest
julia> keepat!([6, 5, 4, 3, 2, 1], 1:2:5)
3-element Vector{Int64}:
 6
 4
 2
```

```
keepat!(a::Vector, m::AbstractVector{Bool})
keepat!(a::BitVector, m::AbstractVector{Bool})
```

The in-place version of logical indexing `a = a[m]`. That is, `keepat!(a, m)` on vectors of equal length `a` and `m` will remove all elements from `a` for which `m` at the corresponding index is `false`.

# Examples

```jldoctest
julia> a = [:a, :b, :c];

julia> keepat!(a, [true, false, true])
2-element Vector{Symbol}:
 :a
 :c

julia> a
2-element Vector{Symbol}:
 :a
 :c
```



keys:
==================================================

```
keys(a::AbstractArray)
```

Return an efficient array describing all valid indices for `a` arranged in the shape of `a` itself.

The keys of 1-dimensional arrays (vectors) are integers, whereas all other N-dimensional arrays use [`CartesianIndex`](@ref) to describe their locations.  Often the special array types [`LinearIndices`](@ref) and [`CartesianIndices`](@ref) are used to efficiently represent these arrays of integers and `CartesianIndex`es, respectively.

Note that the `keys` of an array might not be the most efficient index type; for maximum performance use  [`eachindex`](@ref) instead.

# Examples

```jldoctest
julia> keys([4, 5, 6])
3-element LinearIndices{1, Tuple{Base.OneTo{Int64}}}:
 1
 2
 3

julia> keys([4 5; 6 7])
CartesianIndices((2, 2))
```

```
keys(iterator)
```

For an iterator or collection that has keys and values (e.g. arrays and dictionaries), return an iterator over the keys.

```
keys(a::AbstractDict)
```

Return an iterator over all keys in a dictionary. `collect(keys(a))` returns an array of keys. When the keys are stored internally in a hash table, as is the case for `Dict`, the order in which they are returned may vary. But `keys(a)` and `values(a)` both iterate `a` and return the elements in the same order.

# Examples

```jldoctest
julia> D = Dict('a'=>2, 'b'=>3)
Dict{Char, Int64} with 2 entries:
  'a' => 2
  'b' => 3

julia> collect(keys(D))
2-element Vector{Char}:
 'a': ASCII/Unicode U+0061 (category Ll: Letter, lowercase)
 'b': ASCII/Unicode U+0062 (category Ll: Letter, lowercase)
```

```
keys(m::RegexMatch) -> Vector
```

Return a vector of keys for all capture groups of the underlying regex. A key is included even if the capture group fails to match. That is, `idx` will be in the return value even if `m[idx] == nothing`.

Unnamed capture groups will have integer keys corresponding to their index. Named capture groups will have string keys.

!!! compat "Julia 1.7"
    This method was added in Julia 1.7


# Examples

```jldoctest
julia> keys(match(r"(?<hour>\d+):(?<minute>\d+)(am|pm)?", "11:30"))
3-element Vector{Any}:
  "hour"
  "minute"
 3
```



keytype:
==================================================

```
keytype(T::Type{<:AbstractArray})
keytype(A::AbstractArray)
```

Return the key type of an array. This is equal to the [`eltype`](@ref) of the result of `keys(...)`, and is provided mainly for compatibility with the dictionary interface.

# Examples

```jldoctest
julia> keytype([1, 2, 3]) == Int
true

julia> keytype([1 2; 3 4])
CartesianIndex{2}
```

!!! compat "Julia 1.2"
    For arrays, this function requires at least Julia 1.2.


```
keytype(type)
```

Get the key type of a dictionary type. Behaves similarly to [`eltype`](@ref).

# Examples

```jldoctest
julia> keytype(Dict(Int32(1) => "foo"))
Int32
```



kill:
==================================================

```
kill(p::Process, signum=Base.SIGTERM)
```

Send a signal to a process. The default is to terminate the process. Returns successfully if the process has already exited, but throws an error if killing the process failed for other reasons (e.g. insufficient permissions).



kron:
==================================================

```
kron(A, B)
```

Computes the Kronecker product of two vectors, matrices or numbers.

For real vectors `v` and `w`, the Kronecker product is related to the outer product by `kron(v,w) == vec(w * transpose(v))` or `w * transpose(v) == reshape(kron(v,w), (length(w), length(v)))`. Note how the ordering of `v` and `w` differs on the left and right of these expressions (due to column-major storage). For complex vectors, the outer product `w * v'` also differs by conjugation of `v`.

# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> B = [im 1; 1 -im]
2×2 Matrix{Complex{Int64}}:
 0+1im  1+0im
 1+0im  0-1im

julia> kron(A, B)
4×4 Matrix{Complex{Int64}}:
 0+1im  1+0im  0+2im  2+0im
 1+0im  0-1im  2+0im  0-2im
 0+3im  3+0im  0+4im  4+0im
 3+0im  0-3im  4+0im  0-4im

julia> v = [1, 2]; w = [3, 4, 5];

julia> w*transpose(v)
3×2 Matrix{Int64}:
 3   6
 4   8
 5  10

julia> reshape(kron(v,w), (length(w), length(v)))
3×2 Matrix{Int64}:
 3   6
 4   8
 5  10
```



kron!:
==================================================

```
kron!(C, A, B)
```

Computes the Kronecker product of `A` and `B` and stores the result in `C`, overwriting the existing content of `C`. This is the in-place version of [`kron`](@ref).

!!! compat "Julia 1.6"
    This function requires Julia 1.6 or later.




last:
==================================================

```
last(coll)
```

Get the last element of an ordered collection, if it can be computed in O(1) time. This is accomplished by calling [`lastindex`](@ref) to get the last index. Return the end point of an [`AbstractRange`](@ref) even if it is empty.

See also [`first`](@ref), [`endswith`](@ref).

# Examples

```jldoctest
julia> last(1:2:10)
9

julia> last([1; 2; 3; 4])
4
```

```
last(itr, n::Integer)
```

Get the last `n` elements of the iterable collection `itr`, or fewer elements if `itr` is not long enough.

!!! compat "Julia 1.6"
    This method requires at least Julia 1.6.


# Examples

```jldoctest
julia> last(["foo", "bar", "qux"], 2)
2-element Vector{String}:
 "bar"
 "qux"

julia> last(1:6, 10)
1:6

julia> last(Float64[], 1)
Float64[]
```

```
last(s::AbstractString, n::Integer)
```

Get a string consisting of the last `n` characters of `s`.

# Examples

```jldoctest
julia> last("∀ϵ≠0: ϵ²>0", 0)
""

julia> last("∀ϵ≠0: ϵ²>0", 1)
"0"

julia> last("∀ϵ≠0: ϵ²>0", 3)
"²>0"
```



lastindex:
==================================================

```
lastindex(collection) -> Integer
lastindex(collection, d) -> Integer
```

Return the last index of `collection`. If `d` is given, return the last index of `collection` along dimension `d`.

The syntaxes `A[end]` and `A[end, end]` lower to `A[lastindex(A)]` and `A[lastindex(A, 1), lastindex(A, 2)]`, respectively.

See also: [`axes`](@ref), [`firstindex`](@ref), [`eachindex`](@ref), [`prevind`](@ref).

# Examples

```jldoctest
julia> lastindex([1,2,4])
3

julia> lastindex(rand(3,4,5), 2)
4
```



lcm:
==================================================

```
lcm(x, y...)
```

Least common (positive) multiple (or zero if any argument is zero). The arguments may be integer and rational numbers.

!!! compat "Julia 1.4"
    Rational arguments require Julia 1.4 or later.


# Examples

```jldoctest
julia> lcm(2, 3)
6

julia> lcm(-2, 3)
6

julia> lcm(0, 3)
0

julia> lcm(0, 0)
0

julia> lcm(1//3, 2//3)
2//3

julia> lcm(1//3, -2//3)
2//3

julia> lcm(1//3, 2)
2//1

julia> lcm(1, 3, 5, 7)
105
```



ldexp:
==================================================

```
ldexp(x, n)
```

Compute $x \times 2^n$.

See also [`frexp`](@ref), [`exponent`](@ref).

# Examples

```jldoctest
julia> ldexp(5.0, 2)
20.0
```



leading_ones:
==================================================

```
leading_ones(x::Integer) -> Integer
```

Number of ones leading the binary representation of `x`.

# Examples

```jldoctest
julia> leading_ones(UInt32(2 ^ 32 - 2))
31
```



leading_zeros:
==================================================

```
leading_zeros(x::Integer) -> Integer
```

Number of zeros leading the binary representation of `x`.

# Examples

```jldoctest
julia> leading_zeros(Int32(1))
31
```



length:
==================================================

```
length(collection) -> Integer
```

Return the number of elements in the collection.

Use [`lastindex`](@ref) to get the last valid index of an indexable collection.

See also: [`size`](@ref), [`ndims`](@ref), [`eachindex`](@ref).

# Examples

```jldoctest
julia> length(1:5)
5

julia> length([1, 2, 3, 4])
4

julia> length([1 2; 3 4])
4
```

```
length(A::AbstractArray)
```

Return the number of elements in the array, defaults to `prod(size(A))`.

# Examples

```jldoctest
julia> length([1, 2, 3, 4])
4

julia> length([1 2; 3 4])
4
```

```
length(s::AbstractString) -> Int
length(s::AbstractString, i::Integer, j::Integer) -> Int
```

Return the number of characters in string `s` from indices `i` through `j`.

This is computed as the number of code unit indices from `i` to `j` which are valid character indices. With only a single string argument, this computes the number of characters in the entire string. With `i` and `j` arguments it computes the number of indices between `i` and `j` inclusive that are valid indices in the string `s`. In addition to in-bounds values, `i` may take the out-of-bounds value `ncodeunits(s) + 1` and `j` may take the out-of-bounds value `0`.

!!! note
    The time complexity of this operation is linear in general. That is, it will take the time proportional to the number of bytes or characters in the string because it counts the value on the fly. This is in contrast to the method for arrays, which is a constant-time operation.


See also [`isvalid`](@ref), [`ncodeunits`](@ref), [`lastindex`](@ref), [`thisind`](@ref), [`nextind`](@ref), [`prevind`](@ref).

# Examples

```jldoctest
julia> length("jμΛIα")
5
```



less:
==================================================

```
less(file::AbstractString, [line::Integer])
```

Show a file using the default pager, optionally providing a starting line number. Returns to the `julia` prompt when you quit the pager.

```
less(function, [types])
```

Show the definition of a function using the default pager, optionally specifying a tuple of types to indicate which method to see.



lock:
==================================================

```
lock(lock)
```

Acquire the `lock` when it becomes available. If the lock is already locked by a different task/thread, wait for it to become available.

Each `lock` must be matched by an [`unlock`](@ref).

```
lock(f::Function, lock)
```

Acquire the `lock`, execute `f` with the `lock` held, and release the `lock` when `f` returns. If the lock is already locked by a different task/thread, wait for it to become available.

When this function returns, the `lock` has been released, so the caller should not attempt to `unlock` it.

See also: [`@lock`](@ref).

!!! compat "Julia 1.7"
    Using a [`Channel`](@ref) as the second argument requires Julia 1.7 or later.


lock(f::Function, l::Lockable)

Acquire the lock associated with `l`, execute `f` with the lock held, and release the lock when `f` returns. `f` will receive one positional argument: the value wrapped by `l`. If the lock is already locked by a different task/thread, wait for it to become available. When this function returns, the `lock` has been released, so the caller should not attempt to `unlock` it.

!!! compat "Julia 1.11"
    Requires at least Julia 1.11.




log:
==================================================

```
log(b,x)
```

Compute the base `b` logarithm of `x`. Throws [`DomainError`](@ref) for negative [`Real`](@ref) arguments.

# Examples

```jldoctest; filter = r"Stacktrace:(\n \[[0-9]+\].*)*"
julia> log(4,8)
1.5

julia> log(4,2)
0.5

julia> log(-2, 3)
ERROR: DomainError with -2.0:
log was called with a negative real argument but will only return a complex result if called with a complex argument. Try log(Complex(x)).
Stacktrace:
 [1] throw_complex_domainerror(::Symbol, ::Float64) at ./math.jl:31
[...]

julia> log(2, -3)
ERROR: DomainError with -3.0:
log was called with a negative real argument but will only return a complex result if called with a complex argument. Try log(Complex(x)).
Stacktrace:
 [1] throw_complex_domainerror(::Symbol, ::Float64) at ./math.jl:31
[...]
```

!!! note
    If `b` is a power of 2 or 10, [`log2`](@ref) or [`log10`](@ref) should be used, as these will typically be faster and more accurate. For example,

    ```jldoctest
    julia> log(100,1000000)
    2.9999999999999996

    julia> log10(1000000)/2
    3.0
    ```


```
log(x)
```

Compute the natural logarithm of `x`.

Throws [`DomainError`](@ref) for negative [`Real`](@ref) arguments. Use complex arguments to obtain complex results. Has a branch cut along the negative real axis, for which `-0.0im` is taken to be below the axis.

See also [`ℯ`](@ref), [`log1p`](@ref), [`log2`](@ref), [`log10`](@ref).

# Examples

```jldoctest; filter = r"Stacktrace:(\n \[[0-9]+\].*)*"
julia> log(2)
0.6931471805599453

julia> log(-3)
ERROR: DomainError with -3.0:
log was called with a negative real argument but will only return a complex result if called with a complex argument. Try log(Complex(x)).
Stacktrace:
 [1] throw_complex_domainerror(::Symbol, ::Float64) at ./math.jl:31
[...]

julia> log(-3 + 0im)
1.0986122886681098 + 3.141592653589793im

julia> log(-3 - 0.0im)
1.0986122886681098 - 3.141592653589793im

julia> log.(exp.(-1:1))
3-element Vector{Float64}:
 -1.0
  0.0
  1.0
```

```
log(A::AbstractMatrix)
```

If `A` has no negative real eigenvalue, compute the principal matrix logarithm of `A`, i.e. the unique matrix $X$ such that $e^X = A$ and $-\pi < Im(\lambda) < \pi$ for all the eigenvalues $\lambda$ of $X$. If `A` has nonpositive eigenvalues, a nonprincipal matrix function is returned whenever possible.

If `A` is symmetric or Hermitian, its eigendecomposition ([`eigen`](@ref)) is used, if `A` is triangular an improved version of the inverse scaling and squaring method is employed (see [^AH12] and [^AHR13]). If `A` is real with no negative eigenvalues, then the real Schur form is computed. Otherwise, the complex Schur form is computed. Then the upper (quasi-)triangular algorithm in [^AHR13] is used on the upper (quasi-)triangular factor.

[^AH12]: Awad H. Al-Mohy and Nicholas J. Higham, "Improved inverse  scaling and squaring algorithms for the matrix logarithm", SIAM Journal on Scientific Computing, 34(4), 2012, C153-C169. [doi:10.1137/110852553](https://doi.org/10.1137/110852553)

[^AHR13]: Awad H. Al-Mohy, Nicholas J. Higham and Samuel D. Relton, "Computing the Fréchet derivative of the matrix logarithm and estimating the condition number", SIAM Journal on Scientific Computing, 35(4), 2013, C394-C410. [doi:10.1137/120885991](https://doi.org/10.1137/120885991)

# Examples

```jldoctest
julia> A = Matrix(2.7182818*I, 2, 2)
2×2 Matrix{Float64}:
 2.71828  0.0
 0.0      2.71828

julia> log(A)
2×2 Matrix{Float64}:
 1.0  0.0
 0.0  1.0
```



log10:
==================================================

```
log10(x)
```

Compute the logarithm of `x` to base 10. Throws [`DomainError`](@ref) for negative [`Real`](@ref) arguments.

# Examples

```jldoctest; filter = r"Stacktrace:(\n \[[0-9]+\].*)*"
julia> log10(100)
2.0

julia> log10(2)
0.3010299956639812

julia> log10(-2)
ERROR: DomainError with -2.0:
log10 was called with a negative real argument but will only return a complex result if called with a complex argument. Try log10(Complex(x)).
Stacktrace:
 [1] throw_complex_domainerror(f::Symbol, x::Float64) at ./math.jl:31
[...]
```



log1p:
==================================================

```
log1p(x)
```

Accurate natural logarithm of `1+x`. Throws [`DomainError`](@ref) for [`Real`](@ref) arguments less than -1.

# Examples

```jldoctest; filter = r"Stacktrace:(\n \[[0-9]+\].*)*"
julia> log1p(-0.5)
-0.6931471805599453

julia> log1p(0)
0.0

julia> log1p(-2)
ERROR: DomainError with -2.0:
log1p was called with a real argument < -1 but will only return a complex result if called with a complex argument. Try log1p(Complex(x)).
Stacktrace:
 [1] throw_complex_domainerror(::Symbol, ::Float64) at ./math.jl:31
[...]
```



log2:
==================================================

```
log2(x)
```

Compute the logarithm of `x` to base 2. Throws [`DomainError`](@ref) for negative [`Real`](@ref) arguments.

See also: [`exp2`](@ref), [`ldexp`](@ref), [`ispow2`](@ref).

# Examples

```jldoctest; filter = r"Stacktrace:(\n \[[0-9]+\].*)*"
julia> log2(4)
2.0

julia> log2(10)
3.321928094887362

julia> log2(-2)
ERROR: DomainError with -2.0:
log2 was called with a negative real argument but will only return a complex result if called with a complex argument. Try log2(Complex(x)).
Stacktrace:
 [1] throw_complex_domainerror(f::Symbol, x::Float64) at ./math.jl:31
[...]

julia> log2.(2.0 .^ (-1:1))
3-element Vector{Float64}:
 -1.0
  0.0
  1.0
```



logrange:
==================================================

```
logrange(start, stop, length)
logrange(start, stop; length)
```

Construct a specialized array whose elements are spaced logarithmically between the given endpoints. That is, the ratio of successive elements is a constant, calculated from the length.

This is similar to `geomspace` in Python. Unlike `PowerRange` in Mathematica, you specify the number of elements not the ratio. Unlike `logspace` in Python and Matlab, the `start` and `stop` arguments are always the first and last elements of the result, not powers applied to some base.

# Examples

```jldoctest
julia> logrange(10, 4000, length=3)
3-element Base.LogRange{Float64, Base.TwicePrecision{Float64}}:
 10.0, 200.0, 4000.0

julia> ans[2] ≈ sqrt(10 * 4000)  # middle element is the geometric mean
true

julia> range(10, 40, length=3)[2] ≈ (10 + 40)/2  # arithmetic mean
true

julia> logrange(1f0, 32f0, 11)
11-element Base.LogRange{Float32, Float64}:
 1.0, 1.41421, 2.0, 2.82843, 4.0, 5.65685, 8.0, 11.3137, 16.0, 22.6274, 32.0

julia> logrange(1, 1000, length=4) ≈ 10 .^ (0:3)
true
```

See the [`LogRange`](@ref Base.LogRange) type for further details.

See also [`range`](@ref) for linearly spaced points.

!!! compat "Julia 1.11"
    This function requires at least Julia 1.11.




lowercase:
==================================================

```
lowercase(c::AbstractChar)
```

Convert `c` to lowercase.

See also [`uppercase`](@ref), [`titlecase`](@ref).

# Examples

```jldoctest
julia> lowercase('A')
'a': ASCII/Unicode U+0061 (category Ll: Letter, lowercase)

julia> lowercase('Ö')
'ö': Unicode U+00F6 (category Ll: Letter, lowercase)
```

```
lowercase(s::AbstractString)
```

Return `s` with all characters converted to lowercase.

See also [`uppercase`](@ref), [`titlecase`](@ref), [`lowercasefirst`](@ref).

# Examples

```jldoctest
julia> lowercase("STRINGS AND THINGS")
"strings and things"
```



lowercasefirst:
==================================================

```
lowercasefirst(s::AbstractString)
```

Return `s` with the first character converted to lowercase.

See also [`uppercasefirst`](@ref), [`uppercase`](@ref), [`lowercase`](@ref), [`titlecase`](@ref).

# Examples

```jldoctest
julia> lowercasefirst("Julia")
"julia"
```



lpad:
==================================================

```
lpad(s, n::Integer, p::Union{AbstractChar,AbstractString}=' ') -> String
```

Stringify `s` and pad the resulting string on the left with `p` to make it `n` characters (in [`textwidth`](@ref)) long. If `s` is already `n` characters long, an equal string is returned. Pad with spaces by default.

# Examples

```jldoctest
julia> lpad("March", 10)
"     March"
```

!!! compat "Julia 1.7"
    In Julia 1.7, this function was changed to use `textwidth` rather than a raw character (codepoint) count.




lstat:
==================================================

```
lstat(file)
```

Like [`stat`](@ref), but for symbolic links gets the info for the link itself rather than the file it refers to. This function must be called on a file path rather than a file object or a file descriptor.



lstrip:
==================================================

```
lstrip([pred=isspace,] str::AbstractString) -> SubString
lstrip(str::AbstractString, chars) -> SubString
```

Remove leading characters from `str`, either those specified by `chars` or those for which the function `pred` returns `true`.

The default behaviour is to remove leading whitespace and delimiters: see [`isspace`](@ref) for precise details.

The optional `chars` argument specifies which characters to remove: it can be a single character, or a vector or set of characters.

See also [`strip`](@ref) and [`rstrip`](@ref).

# Examples

```jldoctest
julia> a = lpad("March", 20)
"               March"

julia> lstrip(a)
"March"
```



ltoh:
==================================================

```
ltoh(x)
```

Convert the endianness of a value from Little-endian to that used by the Host.



macroexpand:
==================================================

```
macroexpand(m::Module, x; recursive=true)
```

Take the expression `x` and return an equivalent expression with all macros removed (expanded) for executing in module `m`. The `recursive` keyword controls whether deeper levels of nested macros are also expanded. This is demonstrated in the example below:

```julia-repl
julia> module M
           macro m1()
               42
           end
           macro m2()
               :(@m1())
           end
       end
M

julia> macroexpand(M, :(@m2()), recursive=true)
42

julia> macroexpand(M, :(@m2()), recursive=false)
:(#= REPL[16]:6 =# M.@m1)
```



map:
==================================================

```
map(f, c...) -> collection
```

Transform collection `c` by applying `f` to each element. For multiple collection arguments, apply `f` elementwise, and stop when any of them is exhausted.

See also [`map!`](@ref), [`foreach`](@ref), [`mapreduce`](@ref), [`mapslices`](@ref), [`zip`](@ref), [`Iterators.map`](@ref).

# Examples

```jldoctest
julia> map(x -> x * 2, [1, 2, 3])
3-element Vector{Int64}:
 2
 4
 6

julia> map(+, [1, 2, 3], [10, 20, 30, 400, 5000])
3-element Vector{Int64}:
 11
 22
 33
```

```
map(f, A::AbstractArray...) -> N-array
```

When acting on multi-dimensional arrays of the same [`ndims`](@ref), they must all have the same [`axes`](@ref), and the answer will too.

See also [`broadcast`](@ref), which allows mismatched sizes.

# Examples

```
julia> map(//, [1 2; 3 4], [4 3; 2 1])
2×2 Matrix{Rational{Int64}}:
 1//4  2//3
 3//2  4//1

julia> map(+, [1 2; 3 4], zeros(2,1))
ERROR: DimensionMismatch

julia> map(+, [1 2; 3 4], [1,10,100,1000], zeros(3,1))  # iterates until 3rd is exhausted
3-element Vector{Float64}:
   2.0
  13.0
 102.0
```



map!:
==================================================

```
map!(function, destination, collection...)
```

Like [`map`](@ref), but stores the result in `destination` rather than a new collection. `destination` must be at least as large as the smallest collection.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


See also: [`map`](@ref), [`foreach`](@ref), [`zip`](@ref), [`copyto!`](@ref).

# Examples

```jldoctest
julia> a = zeros(3);

julia> map!(x -> x * 2, a, [1, 2, 3]);

julia> a
3-element Vector{Float64}:
 2.0
 4.0
 6.0

julia> map!(+, zeros(Int, 5), 100:999, 1:3)
5-element Vector{Int64}:
 101
 103
 105
   0
   0
```

```
map!(f, values(dict::AbstractDict))
```

Modifies `dict` by transforming each value from `val` to `f(val)`. Note that the type of `dict` cannot be changed: if `f(val)` is not an instance of the value type of `dict` then it will be converted to the value type if possible and otherwise raise an error.

!!! compat "Julia 1.2"
    `map!(f, values(dict::AbstractDict))` requires Julia 1.2 or later.


# Examples

```jldoctest
julia> d = Dict(:a => 1, :b => 2)
Dict{Symbol, Int64} with 2 entries:
  :a => 1
  :b => 2

julia> map!(v -> v-1, values(d))
ValueIterator for a Dict{Symbol, Int64} with 2 entries. Values:
  0
  1
```



mapfoldl:
==================================================

```
mapfoldl(f, op, itr; [init])
```

Like [`mapreduce`](@ref), but with guaranteed left associativity, as in [`foldl`](@ref). If provided, the keyword argument `init` will be used exactly once. In general, it will be necessary to provide `init` to work with empty collections.



mapfoldr:
==================================================

```
mapfoldr(f, op, itr; [init])
```

Like [`mapreduce`](@ref), but with guaranteed right associativity, as in [`foldr`](@ref). If provided, the keyword argument `init` will be used exactly once. In general, it will be necessary to provide `init` to work with empty collections.



mapreduce:
==================================================

```
mapreduce(f, op, itrs...; [init])
```

Apply function `f` to each element(s) in `itrs`, and then reduce the result using the binary function `op`. If provided, `init` must be a neutral element for `op` that will be returned for empty collections. It is unspecified whether `init` is used for non-empty collections. In general, it will be necessary to provide `init` to work with empty collections.

[`mapreduce`](@ref) is functionally equivalent to calling `reduce(op, map(f, itr); init=init)`, but will in general execute faster since no intermediate collection needs to be created. See documentation for [`reduce`](@ref) and [`map`](@ref).

!!! compat "Julia 1.2"
    `mapreduce` with multiple iterators requires Julia 1.2 or later.


# Examples

```jldoctest
julia> mapreduce(x->x^2, +, [1:3;]) # == 1 + 4 + 9
14
```

The associativity of the reduction is implementation-dependent. Additionally, some implementations may reuse the return value of `f` for elements that appear multiple times in `itr`. Use [`mapfoldl`](@ref) or [`mapfoldr`](@ref) instead for guaranteed left or right associativity and invocation of `f` for every value.

```
mapreduce(f, op, A::AbstractArray...; dims=:, [init])
```

Evaluates to the same as `reduce(op, map(f, A...); dims=dims, init=init)`, but is generally faster because the intermediate array is avoided.

!!! compat "Julia 1.2"
    `mapreduce` with multiple iterators requires Julia 1.2 or later.


# Examples

```jldoctest
julia> a = reshape(Vector(1:16), (4,4))
4×4 Matrix{Int64}:
 1  5   9  13
 2  6  10  14
 3  7  11  15
 4  8  12  16

julia> mapreduce(isodd, *, a, dims=1)
1×4 Matrix{Bool}:
 0  0  0  0

julia> mapreduce(isodd, |, a, dims=1)
1×4 Matrix{Bool}:
 1  1  1  1
```



mapslices:
==================================================

```
mapslices(f, A; dims)
```

Transform the given dimensions of array `A` by applying a function `f` on each slice of the form `A[..., :, ..., :, ...]`, with a colon at each `d` in `dims`. The results are concatenated along the remaining dimensions.

For example, if `dims = [1,2]` and `A` is 4-dimensional, then `f` is called on `x = A[:,:,i,j]` for all `i` and `j`, and `f(x)` becomes `R[:,:,i,j]` in the result `R`.

See also [`eachcol`](@ref) or [`eachslice`](@ref), used with [`map`](@ref) or [`stack`](@ref).

# Examples

```jldoctest
julia> A = reshape(1:30,(2,5,3))
2×5×3 reshape(::UnitRange{Int64}, 2, 5, 3) with eltype Int64:
[:, :, 1] =
 1  3  5  7   9
 2  4  6  8  10

[:, :, 2] =
 11  13  15  17  19
 12  14  16  18  20

[:, :, 3] =
 21  23  25  27  29
 22  24  26  28  30

julia> f(x::Matrix) = fill(x[1,1], 1,4);  # returns a 1×4 matrix

julia> B = mapslices(f, A, dims=(1,2))
1×4×3 Array{Int64, 3}:
[:, :, 1] =
 1  1  1  1

[:, :, 2] =
 11  11  11  11

[:, :, 3] =
 21  21  21  21

julia> f2(x::AbstractMatrix) = fill(x[1,1], 1,4);

julia> B == stack(f2, eachslice(A, dims=3))
true

julia> g(x) = x[begin] // x[end-1];  # returns a number

julia> mapslices(g, A, dims=[1,3])
1×5×1 Array{Rational{Int64}, 3}:
[:, :, 1] =
 1//21  3//23  1//5  7//27  9//29

julia> map(g, eachslice(A, dims=2))
5-element Vector{Rational{Int64}}:
 1//21
 3//23
 1//5
 7//27
 9//29

julia> mapslices(sum, A; dims=(1,3)) == sum(A; dims=(1,3))
true
```

Notice that in `eachslice(A; dims=2)`, the specified dimension is the one *without* a colon in the slice. This is `view(A,:,i,:)`, whereas `mapslices(f, A; dims=(1,3))` uses `A[:,i,:]`. The function `f` may mutate values in the slice without affecting `A`.



mark:
==================================================

```
mark(s::IO)
```

Add a mark at the current position of stream `s`. Return the marked position.

See also [`unmark`](@ref), [`reset`](@ref), [`ismarked`](@ref).



match:
==================================================

```
match(r::Regex, s::AbstractString[, idx::Integer[, addopts]])
```

Search for the first match of the regular expression `r` in `s` and return a [`RegexMatch`](@ref) object containing the match, or nothing if the match failed. The matching substring can be retrieved by accessing `m.match` and the captured sequences can be retrieved by accessing `m.captures` The optional `idx` argument specifies an index at which to start the search.

# Examples

```jldoctest
julia> rx = r"a(.)a"
r"a(.)a"

julia> m = match(rx, "cabac")
RegexMatch("aba", 1="b")

julia> m.captures
1-element Vector{Union{Nothing, SubString{String}}}:
 "b"

julia> m.match
"aba"

julia> match(rx, "cabac", 3) === nothing
true
```



max:
==================================================

```
max(x, y, ...)
```

Return the maximum of the arguments, with respect to [`isless`](@ref). If any of the arguments is [`missing`](@ref), return `missing`. See also the [`maximum`](@ref) function to take the maximum element from a collection.

# Examples

```jldoctest
julia> max(2, 5, 1)
5

julia> max(5, missing, 6)
missing
```



maximum:
==================================================

```
maximum(f, itr; [init])
```

Return the largest result of calling function `f` on each element of `itr`.

The value returned for empty `itr` can be specified by `init`. It must be a neutral element for `max` (i.e. which is less than or equal to any other element) as it is unspecified whether `init` is used for non-empty collections.

!!! compat "Julia 1.6"
    Keyword argument `init` requires Julia 1.6 or later.


# Examples

```jldoctest
julia> maximum(length, ["Julion", "Julia", "Jule"])
6

julia> maximum(length, []; init=-1)
-1

julia> maximum(sin, Real[]; init=-1.0)  # good, since output of sin is >= -1
-1.0
```

```
maximum(itr; [init])
```

Return the largest element in a collection.

The value returned for empty `itr` can be specified by `init`. It must be a neutral element for `max` (i.e. which is less than or equal to any other element) as it is unspecified whether `init` is used for non-empty collections.

!!! compat "Julia 1.6"
    Keyword argument `init` requires Julia 1.6 or later.


# Examples

```jldoctest
julia> maximum(-20.5:10)
9.5

julia> maximum([1,2,3])
3

julia> maximum(())
ERROR: ArgumentError: reducing over an empty collection is not allowed; consider supplying `init` to the reducer
Stacktrace:
[...]

julia> maximum((); init=-Inf)
-Inf
```

```
maximum(A::AbstractArray; dims)
```

Compute the maximum value of an array over the given dimensions. See also the [`max(a,b)`](@ref) function to take the maximum of two or more arguments, which can be applied elementwise to arrays via `max.(a,b)`.

See also: [`maximum!`](@ref), [`extrema`](@ref), [`findmax`](@ref), [`argmax`](@ref).

# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> maximum(A, dims=1)
1×2 Matrix{Int64}:
 3  4

julia> maximum(A, dims=2)
2×1 Matrix{Int64}:
 2
 4
```

```
maximum(f, A::AbstractArray; dims)
```

Compute the maximum value by calling the function `f` on each element of an array over the given dimensions.

# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> maximum(abs2, A, dims=1)
1×2 Matrix{Int64}:
 9  16

julia> maximum(abs2, A, dims=2)
2×1 Matrix{Int64}:
  4
 16
```



maximum!:
==================================================

```
maximum!(r, A)
```

Compute the maximum value of `A` over the singleton dimensions of `r`, and write results to `r`.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> maximum!([1; 1], A)
2-element Vector{Int64}:
 2
 4

julia> maximum!([1 1], A)
1×2 Matrix{Int64}:
 3  4
```



maxintfloat:
==================================================

```
maxintfloat(T=Float64)
```

The largest consecutive integer-valued floating-point number that is exactly represented in the given floating-point type `T` (which defaults to `Float64`).

That is, `maxintfloat` returns the smallest positive integer-valued floating-point number `n` such that `n+1` is *not* exactly representable in the type `T`.

When an `Integer`-type value is needed, use `Integer(maxintfloat(T))`.

```
maxintfloat(T, S)
```

The largest consecutive integer representable in the given floating-point type `T` that also does not exceed the maximum integer representable by the integer type `S`.  Equivalently, it is the minimum of `maxintfloat(T)` and [`typemax(S)`](@ref).



memoryref:
==================================================

```
`memoryref(::GenericMemory)`
```

Construct a `GenericMemoryRef` from a memory object. This does not fail, but the resulting memory will point out-of-bounds if and only if the memory is empty.

```
memoryref(::GenericMemory, index::Integer)
memoryref(::GenericMemoryRef, index::Integer)
```

Construct a `GenericMemoryRef` from a memory object and an offset index (1-based) which can also be negative. This always returns an inbounds object, and will throw an error if that is not possible (because the index would result in a shift out-of-bounds of the underlying memory).



merge:
==================================================

```
merge(d::AbstractDict, others::AbstractDict...)
```

Construct a merged collection from the given collections. If necessary, the types of the resulting collection will be promoted to accommodate the types of the merged collections. If the same key is present in another collection, the value for that key will be the value it has in the last collection listed. See also [`mergewith`](@ref) for custom handling of values with the same key.

# Examples

```jldoctest
julia> a = Dict("foo" => 0.0, "bar" => 42.0)
Dict{String, Float64} with 2 entries:
  "bar" => 42.0
  "foo" => 0.0

julia> b = Dict("baz" => 17, "bar" => 4711)
Dict{String, Int64} with 2 entries:
  "bar" => 4711
  "baz" => 17

julia> merge(a, b)
Dict{String, Float64} with 3 entries:
  "bar" => 4711.0
  "baz" => 17.0
  "foo" => 0.0

julia> merge(b, a)
Dict{String, Float64} with 3 entries:
  "bar" => 42.0
  "baz" => 17.0
  "foo" => 0.0
```

```
merge(a::NamedTuple, bs::NamedTuple...)
```

Construct a new named tuple by merging two or more existing ones, in a left-associative manner. Merging proceeds left-to-right, between pairs of named tuples, and so the order of fields present in both the leftmost and rightmost named tuples take the same position as they are found in the leftmost named tuple. However, values are taken from matching fields in the rightmost named tuple that contains that field. Fields present in only the rightmost named tuple of a pair are appended at the end. A fallback is implemented for when only a single named tuple is supplied, with signature `merge(a::NamedTuple)`.

!!! compat "Julia 1.1"
    Merging 3 or more `NamedTuple` requires at least Julia 1.1.


# Examples

```jldoctest
julia> merge((a=1, b=2, c=3), (b=4, d=5))
(a = 1, b = 4, c = 3, d = 5)
```

```jldoctest
julia> merge((a=1, b=2), (b=3, c=(d=1,)), (c=(d=2,),))
(a = 1, b = 3, c = (d = 2,))
```

```
merge(a::NamedTuple, iterable)
```

Interpret an iterable of key-value pairs as a named tuple, and perform a merge.

```jldoctest
julia> merge((a=1, b=2, c=3), [:b=>4, :d=>5])
(a = 1, b = 4, c = 3, d = 5)
```

```
merge(initial::Face, others::Face...)
```

Merge the properties of the `initial` face and `others`, with later faces taking priority.



merge!:
==================================================

```
merge!(d::AbstractDict, others::AbstractDict...)
```

Update collection with pairs from the other collections. See also [`merge`](@ref).

# Examples

```jldoctest
julia> d1 = Dict(1 => 2, 3 => 4);

julia> d2 = Dict(1 => 4, 4 => 5);

julia> merge!(d1, d2);

julia> d1
Dict{Int64, Int64} with 3 entries:
  4 => 5
  3 => 4
  1 => 4
```



mergewith:
==================================================

```
mergewith(combine, d::AbstractDict, others::AbstractDict...)
mergewith(combine)
merge(combine, d::AbstractDict, others::AbstractDict...)
```

Construct a merged collection from the given collections. If necessary, the types of the resulting collection will be promoted to accommodate the types of the merged collections. Values with the same key will be combined using the combiner function.  The curried form `mergewith(combine)` returns the function `(args...) -> mergewith(combine, args...)`.

Method `merge(combine::Union{Function,Type}, args...)` as an alias of `mergewith(combine, args...)` is still available for backward compatibility.

!!! compat "Julia 1.5"
    `mergewith` requires Julia 1.5 or later.


# Examples

```jldoctest
julia> a = Dict("foo" => 0.0, "bar" => 42.0)
Dict{String, Float64} with 2 entries:
  "bar" => 42.0
  "foo" => 0.0

julia> b = Dict("baz" => 17, "bar" => 4711)
Dict{String, Int64} with 2 entries:
  "bar" => 4711
  "baz" => 17

julia> mergewith(+, a, b)
Dict{String, Float64} with 3 entries:
  "bar" => 4753.0
  "baz" => 17.0
  "foo" => 0.0

julia> ans == mergewith(+)(a, b)
true
```



mergewith!:
==================================================

```
mergewith!(combine, d::AbstractDict, others::AbstractDict...) -> d
mergewith!(combine)
merge!(combine, d::AbstractDict, others::AbstractDict...) -> d
```

Update collection with pairs from the other collections. Values with the same key will be combined using the combiner function.  The curried form `mergewith!(combine)` returns the function `(args...) -> mergewith!(combine, args...)`.

Method `merge!(combine::Union{Function,Type}, args...)` as an alias of `mergewith!(combine, args...)` is still available for backward compatibility.

!!! compat "Julia 1.5"
    `mergewith!` requires Julia 1.5 or later.


# Examples

```jldoctest
julia> d1 = Dict(1 => 2, 3 => 4);

julia> d2 = Dict(1 => 4, 4 => 5);

julia> mergewith!(+, d1, d2);

julia> d1
Dict{Int64, Int64} with 3 entries:
  4 => 5
  3 => 4
  1 => 6

julia> mergewith!(-, d1, d1);

julia> d1
Dict{Int64, Int64} with 3 entries:
  4 => 0
  3 => 0
  1 => 0

julia> foldl(mergewith!(+), [d1, d2]; init=Dict{Int64, Int64}())
Dict{Int64, Int64} with 3 entries:
  4 => 5
  3 => 0
  1 => 4
```



methods:
==================================================

```
methods(f, [types], [module])
```

Return the method table for `f`.

If `types` is specified, return an array of methods whose types match. If `module` is specified, return an array of methods defined in that module. A list of modules can also be specified as an array.

!!! compat "Julia 1.4"
    At least Julia 1.4 is required for specifying a module.


See also: [`which`](@ref), [`@which`](@ref Main.InteractiveUtils.@which) and [`methodswith`](@ref Main.InteractiveUtils.methodswith).



methodswith:
==================================================

```
methodswith(typ[, module or function]; supertypes::Bool=false])
```

Return an array of methods with an argument of type `typ`.

The optional second argument restricts the search to a particular module or function (the default is all top-level modules).

If keyword `supertypes` is `true`, also return arguments with a parent type of `typ`, excluding type `Any`.

See also: [`methods`](@ref).



min:
==================================================

```
min(x, y, ...)
```

Return the minimum of the arguments, with respect to [`isless`](@ref). If any of the arguments is [`missing`](@ref), return `missing`. See also the [`minimum`](@ref) function to take the minimum element from a collection.

# Examples

```jldoctest
julia> min(2, 5, 1)
1

julia> min(4, missing, 6)
missing
```



minimum:
==================================================

```
minimum(f, itr; [init])
```

Return the smallest result of calling function `f` on each element of `itr`.

The value returned for empty `itr` can be specified by `init`. It must be a neutral element for `min` (i.e. which is greater than or equal to any other element) as it is unspecified whether `init` is used for non-empty collections.

!!! compat "Julia 1.6"
    Keyword argument `init` requires Julia 1.6 or later.


# Examples

```jldoctest
julia> minimum(length, ["Julion", "Julia", "Jule"])
4

julia> minimum(length, []; init=typemax(Int64))
9223372036854775807

julia> minimum(sin, Real[]; init=1.0)  # good, since output of sin is <= 1
1.0
```

```
minimum(itr; [init])
```

Return the smallest element in a collection.

The value returned for empty `itr` can be specified by `init`. It must be a neutral element for `min` (i.e. which is greater than or equal to any other element) as it is unspecified whether `init` is used for non-empty collections.

!!! compat "Julia 1.6"
    Keyword argument `init` requires Julia 1.6 or later.


# Examples

```jldoctest
julia> minimum(-20.5:10)
-20.5

julia> minimum([1,2,3])
1

julia> minimum([])
ERROR: ArgumentError: reducing over an empty collection is not allowed; consider supplying `init` to the reducer
Stacktrace:
[...]

julia> minimum([]; init=Inf)
Inf
```

```
minimum(A::AbstractArray; dims)
```

Compute the minimum value of an array over the given dimensions. See also the [`min(a,b)`](@ref) function to take the minimum of two or more arguments, which can be applied elementwise to arrays via `min.(a,b)`.

See also: [`minimum!`](@ref), [`extrema`](@ref), [`findmin`](@ref), [`argmin`](@ref).

# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> minimum(A, dims=1)
1×2 Matrix{Int64}:
 1  2

julia> minimum(A, dims=2)
2×1 Matrix{Int64}:
 1
 3
```

```
minimum(f, A::AbstractArray; dims)
```

Compute the minimum value by calling the function `f` on each element of an array over the given dimensions.

# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> minimum(abs2, A, dims=1)
1×2 Matrix{Int64}:
 1  4

julia> minimum(abs2, A, dims=2)
2×1 Matrix{Int64}:
 1
 9
```



minimum!:
==================================================

```
minimum!(r, A)
```

Compute the minimum value of `A` over the singleton dimensions of `r`, and write results to `r`.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> minimum!([1; 1], A)
2-element Vector{Int64}:
 1
 3

julia> minimum!([1 1], A)
1×2 Matrix{Int64}:
 1  2
```



minmax:
==================================================

```
minmax(x, y)
```

Return `(min(x,y), max(x,y))`.

See also [`extrema`](@ref) that returns `(minimum(x), maximum(x))`.

# Examples

```jldoctest
julia> minmax('c','b')
('b', 'c')
```



missing:
==================================================

```
Missing
```

A type with no fields whose singleton instance [`missing`](@ref) is used to represent missing values.

See also: [`skipmissing`](@ref), [`nonmissingtype`](@ref), [`Nothing`](@ref).



mkdir:
==================================================

```
mkdir(path::AbstractString; mode::Unsigned = 0o777)
```

Make a new directory with name `path` and permissions `mode`. `mode` defaults to `0o777`, modified by the current file creation mask. This function never creates more than one directory. If the directory already exists, or some intermediate directories do not exist, this function throws an error. See [`mkpath`](@ref) for a function which creates all required intermediate directories. Return `path`.

# Examples

```julia-repl
julia> mkdir("testingdir")
"testingdir"

julia> cd("testingdir")

julia> pwd()
"/home/JuliaUser/testingdir"
```



mkpath:
==================================================

```
mkpath(path::AbstractString; mode::Unsigned = 0o777)
```

Create all intermediate directories in the `path` as required. Directories are created with the permissions `mode` which defaults to `0o777` and is modified by the current file creation mask. Unlike [`mkdir`](@ref), `mkpath` does not error if `path` (or parts of it) already exists. However, an error will be thrown if `path` (or parts of it) points to an existing file. Return `path`.

If `path` includes a filename you will probably want to use `mkpath(dirname(path))` to avoid creating a directory using the filename.

# Examples

```julia-repl
julia> cd(mktempdir())

julia> mkpath("my/test/dir") # creates three directories
"my/test/dir"

julia> readdir()
1-element Array{String,1}:
 "my"

julia> cd("my")

julia> readdir()
1-element Array{String,1}:
 "test"

julia> readdir("test")
1-element Array{String,1}:
 "dir"

julia> mkpath("intermediate_dir/actually_a_directory.txt") # creates two directories
"intermediate_dir/actually_a_directory.txt"

julia> isdir("intermediate_dir/actually_a_directory.txt")
true

```



mktemp:
==================================================

```
mktemp(parent=tempdir(); cleanup=true) -> (path, io)
```

Return `(path, io)`, where `path` is the path of a new temporary file in `parent` and `io` is an open file object for this path. The `cleanup` option controls whether the temporary file is automatically deleted when the process exits.

!!! compat "Julia 1.3"
    The `cleanup` keyword argument was added in Julia 1.3. Relatedly, starting from 1.3, Julia will remove the temporary paths created by `mktemp` when the Julia process exits, unless `cleanup` is explicitly set to `false`.


```
mktemp(f::Function, parent=tempdir())
```

Apply the function `f` to the result of [`mktemp(parent)`](@ref) and remove the temporary file upon completion.

See also: [`mktempdir`](@ref).



mktempdir:
==================================================

```
mktempdir(parent=tempdir(); prefix="jl_", cleanup=true) -> path
```

Create a temporary directory in the `parent` directory with a name constructed from the given `prefix` and a random suffix, and return its path. Additionally, on some platforms, any trailing `'X'` characters in `prefix` may be replaced with random characters. If `parent` does not exist, throw an error. The `cleanup` option controls whether the temporary directory is automatically deleted when the process exits.

!!! compat "Julia 1.2"
    The `prefix` keyword argument was added in Julia 1.2.


!!! compat "Julia 1.3"
    The `cleanup` keyword argument was added in Julia 1.3. Relatedly, starting from 1.3, Julia will remove the temporary paths created by `mktempdir` when the Julia process exits, unless `cleanup` is explicitly set to `false`.


See also: [`mktemp`](@ref), [`mkdir`](@ref).

```
mktempdir(f::Function, parent=tempdir(); prefix="jl_")
```

Apply the function `f` to the result of [`mktempdir(parent; prefix)`](@ref) and remove the temporary directory all of its contents upon completion.

See also: [`mktemp`](@ref), [`mkdir`](@ref).

!!! compat "Julia 1.2"
    The `prefix` keyword argument was added in Julia 1.2.




mod:
==================================================

```
mod(x::Integer, r::AbstractUnitRange)
```

Find `y` in the range `r` such that $x ≡ y (mod n)$, where `n = length(r)`, i.e. `y = mod(x - first(r), n) + first(r)`.

See also [`mod1`](@ref).

# Examples

```jldoctest
julia> mod(0, Base.OneTo(3))  # mod1(0, 3)
3

julia> mod(3, 0:2)  # mod(3, 3)
0
```

!!! compat "Julia 1.3"
    This method requires at least Julia 1.3.


```
mod(x, y)
rem(x, y, RoundDown)
```

The reduction of `x` modulo `y`, or equivalently, the remainder of `x` after floored division by `y`, i.e. `x - y*fld(x,y)` if computed without intermediate rounding.

The result will have the same sign as `y`, and magnitude less than `abs(y)` (with some exceptions, see note below).

!!! note
    When used with floating point values, the exact result may not be representable by the type, and so rounding error may occur. In particular, if the exact result is very close to `y`, then it may be rounded to `y`.


See also: [`rem`](@ref), [`div`](@ref), [`fld`](@ref), [`mod1`](@ref), [`invmod`](@ref).

```jldoctest
julia> mod(8, 3)
2

julia> mod(9, 3)
0

julia> mod(8.9, 3)
2.9000000000000004

julia> mod(eps(), 3)
2.220446049250313e-16

julia> mod(-eps(), 3)
3.0

julia> mod.(-5:5, 3)'
1×11 adjoint(::Vector{Int64}) with eltype Int64:
 1  2  0  1  2  0  1  2  0  1  2
```

```
rem(x::Integer, T::Type{<:Integer}) -> T
mod(x::Integer, T::Type{<:Integer}) -> T
%(x::Integer, T::Type{<:Integer}) -> T
```

Find `y::T` such that `x` ≡ `y` (mod n), where n is the number of integers representable in `T`, and `y` is an integer in `[typemin(T),typemax(T)]`. If `T` can represent any integer (e.g. `T == BigInt`), then this operation corresponds to a conversion to `T`.

# Examples

```jldoctest
julia> x = 129 % Int8
-127

julia> typeof(x)
Int8

julia> x = 129 % BigInt
129

julia> typeof(x)
BigInt
```



mod1:
==================================================

```
mod1(x, y)
```

Modulus after flooring division, returning a value `r` such that `mod(r, y) == mod(x, y)` in the range $(0, y]$ for positive `y` and in the range $[y,0)$ for negative `y`.

With integer arguments and positive `y`, this is equal to `mod(x, 1:y)`, and hence natural for 1-based indexing. By comparison, `mod(x, y) == mod(x, 0:y-1)` is natural for computations with offsets or strides.

See also [`mod`](@ref), [`fld1`](@ref), [`fldmod1`](@ref).

# Examples

```jldoctest
julia> mod1(4, 2)
2

julia> mod1.(-5:5, 3)'
1×11 adjoint(::Vector{Int64}) with eltype Int64:
 1  2  3  1  2  3  1  2  3  1  2

julia> mod1.([-0.1, 0, 0.1, 1, 2, 2.9, 3, 3.1]', 3)
1×8 Matrix{Float64}:
 2.9  3.0  0.1  1.0  2.0  2.9  3.0  0.1
```



mod2pi:
==================================================

```
mod2pi(x)
```

Modulus after division by `2π`, returning in the range $[0,2π)$.

This function computes a floating point representation of the modulus after division by numerically exact `2π`, and is therefore not exactly the same as `mod(x,2π)`, which would compute the modulus of `x` relative to division by the floating-point number `2π`.

!!! note
    Depending on the format of the input value, the closest representable value to 2π may be less than 2π. For example, the expression `mod2pi(2π)` will not return `0`, because the intermediate value of `2*π` is a `Float64` and `2*Float64(π) < 2*big(π)`. See [`rem2pi`](@ref) for more refined control of this behavior.


# Examples

```jldoctest
julia> mod2pi(9*pi/4)
0.7853981633974481
```



modf:
==================================================

```
modf(x)
```

Return a tuple `(fpart, ipart)` of the fractional and integral parts of a number. Both parts have the same sign as the argument.

# Examples

```jldoctest
julia> modf(3.5)
(0.5, 3.0)

julia> modf(-3.5)
(-0.5, -3.0)
```



modifyfield!:
==================================================

```
modifyfield!(value, name::Symbol, op, x, [order::Symbol]) -> Pair
modifyfield!(value, i::Int, op, x, [order::Symbol]) -> Pair
```

Atomically perform the operations to get and set a field after applying the function `op`.

```
y = getfield(value, name)
z = op(y, x)
setfield!(value, name, z)
return y => z
```

If supported by the hardware (for example, atomic increment), this may be optimized to the appropriate hardware instruction, otherwise it'll use a loop.

!!! compat "Julia 1.7"
    This function requires Julia 1.7 or later.




modifyglobal!:
==================================================

```
modifyglobal!(module::Module, name::Symbol, op, x, [order::Symbol=:monotonic]) -> Pair
```

Atomically perform the operations to get and set a global after applying the function `op`.

!!! compat "Julia 1.11"
    This function requires Julia 1.11 or later.


See also [`modifyproperty!`](@ref Base.modifyproperty!) and [`setglobal!`](@ref).



modifyproperty!:
==================================================

```
modifyproperty!(x, f::Symbol, op, v, order::Symbol=:not_atomic)
```

The syntax `@atomic op(x.f, v)` (and its equivalent `@atomic x.f op v`) returns `modifyproperty!(x, :f, op, v, :sequentially_consistent)`, where the first argument must be a `getproperty` expression and is modified atomically.

Invocation of `op(getproperty(x, f), v)` must return a value that can be stored in the field `f` of the object `x` by default.  In particular, unlike the default behavior of [`setproperty!`](@ref Base.setproperty!), the `convert` function is not called automatically.

See also [`modifyfield!`](@ref Core.modifyfield!) and [`setproperty!`](@ref Base.setproperty!).



mtime:
==================================================

```
mtime(file)
```

Equivalent to `stat(file).mtime`.



muladd:
==================================================

```
muladd(x, y, z)
```

Combined multiply-add: computes `x*y+z`, but allowing the add and multiply to be merged with each other or with surrounding operations for performance. For example, this may be implemented as an [`fma`](@ref) if the hardware supports it efficiently. The result can be different on different machines and can also be different on the same machine due to constant propagation or other optimizations. See [`fma`](@ref).

# Examples

```jldoctest
julia> muladd(3, 2, 1)
7

julia> 3 * 2 + 1
7
```

```
muladd(A, y, z)
```

Combined multiply-add, `A*y .+ z`, for matrix-matrix or matrix-vector multiplication. The result is always the same size as `A*y`, but `z` may be smaller, or a scalar.

!!! compat "Julia 1.6"
    These methods require Julia 1.6 or later.


# Examples

```jldoctest
julia> A=[1.0 2.0; 3.0 4.0]; B=[1.0 1.0; 1.0 1.0]; z=[0, 100];

julia> muladd(A, B, z)
2×2 Matrix{Float64}:
   3.0    3.0
 107.0  107.0
```



mv:
==================================================

```
mv(src::AbstractString, dst::AbstractString; force::Bool=false)
```

Move the file, link, or directory from `src` to `dst`. `force=true` will first remove an existing `dst`. Return `dst`.

# Examples

```jldoctest; filter = r"Stacktrace:(\n \[[0-9]+\].*)*"
julia> write("hello.txt", "world");

julia> mv("hello.txt", "goodbye.txt")
"goodbye.txt"

julia> "hello.txt" in readdir()
false

julia> readline("goodbye.txt")
"world"

julia> write("hello.txt", "world2");

julia> mv("hello.txt", "goodbye.txt")
ERROR: ArgumentError: 'goodbye.txt' exists. `force=true` is required to remove 'goodbye.txt' before moving.
Stacktrace:
 [1] #checkfor_mv_cp_cptree#10(::Bool, ::Function, ::String, ::String, ::String) at ./file.jl:293
[...]

julia> mv("hello.txt", "goodbye.txt", force=true)
"goodbye.txt"

julia> rm("goodbye.txt");

```



nameof:
==================================================

```
nameof(m::Module) -> Symbol
```

Get the name of a `Module` as a [`Symbol`](@ref).

# Examples

```jldoctest
julia> nameof(Base.Broadcast)
:Broadcast
```

```
nameof(t::DataType) -> Symbol
```

Get the name of a (potentially `UnionAll`-wrapped) `DataType` (without its parent module) as a symbol.

# Examples

```jldoctest
julia> module Foo
           struct S{T}
           end
       end
Foo

julia> nameof(Foo.S{T} where T)
:S
```

```
nameof(f::Function) -> Symbol
```

Get the name of a generic `Function` as a symbol. For anonymous functions, this is a compiler-generated name. For explicitly-declared subtypes of `Function`, it is the name of the function's type.



names:
==================================================

```
names(x::Module; all::Bool = false, imported::Bool = false)
```

Get a vector of the public names of a `Module`, excluding deprecated names. If `all` is true, then the list also includes non-public names defined in the module, deprecated names, and compiler-generated names. If `imported` is true, then names explicitly imported from other modules are also included. Names are returned in sorted order.

As a special case, all names defined in `Main` are considered "public", since it is not idiomatic to explicitly mark names from `Main` as public.

!!! note
    `sym ∈ names(SomeModule)` does *not* imply `isdefined(SomeModule, sym)`. `names` will return symbols marked with `public` or `export`, even if they are not defined in the module.


See also: [`Base.isexported`](@ref), [`Base.ispublic`](@ref), [`Base.@locals`](@ref), [`@__MODULE__`](@ref).



nand:
==================================================

```
nand(x, y)
⊼(x, y)
```

Bitwise nand (not and) of `x` and `y`. Implements [three-valued logic](https://en.wikipedia.org/wiki/Three-valued_logic), returning [`missing`](@ref) if one of the arguments is `missing`.

The infix operation `a ⊼ b` is a synonym for `nand(a,b)`, and `⊼` can be typed by tab-completing `\nand` or `\barwedge` in the Julia REPL.

# Examples

```jldoctest
julia> nand(true, false)
true

julia> nand(true, true)
false

julia> nand(true, missing)
missing

julia> false ⊼ false
true

julia> [true; true; false] .⊼ [true; false; false]
3-element BitVector:
 0
 1
 1
```



ncodeunits:
==================================================

```
ncodeunits(c::Char) -> Int
```

Return the number of code units required to encode a character as UTF-8. This is the number of bytes which will be printed if the character is written to an output stream, or `ncodeunits(string(c))` but computed efficiently.

!!! compat "Julia 1.1"
    This method requires at least Julia 1.1. In Julia 1.0 consider using `ncodeunits(string(c))`.


```
ncodeunits(s::AbstractString) -> Int
```

Return the number of code units in a string. Indices that are in bounds to access this string must satisfy `1 ≤ i ≤ ncodeunits(s)`. Not all such indices are valid – they may not be the start of a character, but they will return a code unit value when calling `codeunit(s,i)`.

# Examples

```jldoctest
julia> ncodeunits("The Julia Language")
18

julia> ncodeunits("∫eˣ")
6

julia> ncodeunits('∫'), ncodeunits('e'), ncodeunits('ˣ')
(3, 1, 2)
```

See also [`codeunit`](@ref), [`checkbounds`](@ref), [`sizeof`](@ref), [`length`](@ref), [`lastindex`](@ref).



ndigits:
==================================================

```
ndigits(n::Integer; base::Integer=10, pad::Integer=1)
```

Compute the number of digits in integer `n` written in base `base` (`base` must not be in `[-1, 0, 1]`), optionally padded with zeros to a specified size (the result will never be less than `pad`).

See also [`digits`](@ref), [`count_ones`](@ref).

# Examples

```jldoctest
julia> ndigits(0)
1

julia> ndigits(12345)
5

julia> ndigits(1022, base=16)
3

julia> string(1022, base=16)
"3fe"

julia> ndigits(123, pad=5)
5

julia> ndigits(-123)
3
```



ndims:
==================================================

```
ndims(A::AbstractArray) -> Integer
```

Return the number of dimensions of `A`.

See also: [`size`](@ref), [`axes`](@ref).

# Examples

```jldoctest
julia> A = fill(1, (3,4,5));

julia> ndims(A)
3
```



nextfloat:
==================================================

```
nextfloat(x::AbstractFloat, n::Integer)
```

The result of `n` iterative applications of `nextfloat` to `x` if `n >= 0`, or `-n` applications of [`prevfloat`](@ref) if `n < 0`.

```
nextfloat(x::AbstractFloat)
```

Return the smallest floating point number `y` of the same type as `x` such `x < y`. If no such `y` exists (e.g. if `x` is `Inf` or `NaN`), then return `x`.

See also: [`prevfloat`](@ref), [`eps`](@ref), [`issubnormal`](@ref).



nextind:
==================================================

```
nextind(A, i)
```

Return the index after `i` in `A`. The returned index is often equivalent to `i + 1` for an integer `i`. This function can be useful for generic code.

!!! warning
    The returned index might be out of bounds. Consider using [`checkbounds`](@ref).


See also: [`prevind`](@ref).

# Examples

```jldoctest
julia> x = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> nextind(x, 1) # valid result
2

julia> nextind(x, 4) # invalid result
5

julia> nextind(x, CartesianIndex(1, 1)) # valid result
CartesianIndex(2, 1)

julia> nextind(x, CartesianIndex(2, 2)) # invalid result
CartesianIndex(1, 3)
```

```
nextind(str::AbstractString, i::Integer, n::Integer=1) -> Int
```

  * Case `n == 1`

    If `i` is in bounds in `s` return the index of the start of the character whose encoding starts after index `i`. In other words, if `i` is the start of a character, return the start of the next character; if `i` is not the start of a character, move forward until the start of a character and return that index. If `i` is equal to `0` return `1`. If `i` is in bounds but greater or equal to `lastindex(str)` return `ncodeunits(str)+1`. Otherwise throw `BoundsError`.
  * Case `n > 1`

    Behaves like applying `n` times `nextind` for `n==1`. The only difference is that if `n` is so large that applying `nextind` would reach `ncodeunits(str)+1` then each remaining iteration increases the returned value by `1`. This means that in this case `nextind` can return a value greater than `ncodeunits(str)+1`.
  * Case `n == 0`

    Return `i` only if `i` is a valid index in `s` or is equal to `0`. Otherwise `StringIndexError` or `BoundsError` is thrown.

# Examples

```jldoctest
julia> nextind("α", 0)
1

julia> nextind("α", 1)
3

julia> nextind("α", 3)
ERROR: BoundsError: attempt to access 2-codeunit String at index [3]
[...]

julia> nextind("α", 0, 2)
3

julia> nextind("α", 1, 2)
4
```



nextpow:
==================================================

```
nextpow(a, x)
```

The smallest `a^n` not less than `x`, where `n` is a non-negative integer. `a` must be greater than 1, and `x` must be greater than 0.

See also [`prevpow`](@ref).

# Examples

```jldoctest
julia> nextpow(2, 7)
8

julia> nextpow(2, 9)
16

julia> nextpow(5, 20)
25

julia> nextpow(4, 16)
16
```



nextprod:
==================================================

```
nextprod(factors::Union{Tuple,AbstractVector}, n)
```

Next integer greater than or equal to `n` that can be written as $\prod k_i^{p_i}$ for integers $p_1$, $p_2$, etcetera, for factors $k_i$ in `factors`.

# Examples

```jldoctest
julia> nextprod((2, 3), 105)
108

julia> 2^2 * 3^3
108
```

!!! compat "Julia 1.6"
    The method that accepts a tuple requires Julia 1.6 or later.




nfields:
==================================================

```
nfields(x) -> Int
```

Get the number of fields in the given object.

# Examples

```jldoctest
julia> a = 1//2;

julia> nfields(a)
2

julia> b = 1
1

julia> nfields(b)
0

julia> ex = ErrorException("I've done a bad thing");

julia> nfields(ex)
1
```

In these examples, `a` is a [`Rational`](@ref), which has two fields. `b` is an `Int`, which is a primitive bitstype with no fields at all. `ex` is an [`ErrorException`](@ref), which has one field.



nonmissingtype:
==================================================

```
nonmissingtype(T::Type)
```

If `T` is a union of types containing `Missing`, return a new type with `Missing` removed.

# Examples

```jldoctest
julia> nonmissingtype(Union{Int64,Missing})
Int64

julia> nonmissingtype(Any)
Any
```

!!! compat "Julia 1.3"
    This function is exported as of Julia 1.3.




nor:
==================================================

```
nor(x, y)
⊽(x, y)
```

Bitwise nor (not or) of `x` and `y`. Implements [three-valued logic](https://en.wikipedia.org/wiki/Three-valued_logic), returning [`missing`](@ref) if one of the arguments is `missing` and the other is not `true`.

The infix operation `a ⊽ b` is a synonym for `nor(a,b)`, and `⊽` can be typed by tab-completing `\nor` or `\barvee` in the Julia REPL.

# Examples

```jldoctest
julia> nor(true, false)
false

julia> nor(true, true)
false

julia> nor(true, missing)
false

julia> false ⊽ false
true

julia> false ⊽ missing
missing

julia> [true; true; false] .⊽ [true; false; false]
3-element BitVector:
 0
 0
 1
```



normpath:
==================================================

```
normpath(path::AbstractString) -> String
```

Normalize a path, removing "." and ".." entries and changing "/" to the canonical path separator for the system.

# Examples

```jldoctest
julia> normpath("/home/myuser/../example.jl")
"/home/example.jl"

julia> normpath("Documents/Julia") == joinpath("Documents", "Julia")
true
```

```
normpath(path::AbstractString, paths::AbstractString...) -> String
```

Convert a set of paths to a normalized path by joining them together and removing "." and ".." entries. Equivalent to `normpath(joinpath(path, paths...))`.



nothing:
==================================================

```
Nothing
```

A type with no fields that is the type of [`nothing`](@ref).

See also: [`isnothing`](@ref), [`Some`](@ref), [`Missing`](@ref).



notify:
==================================================

```
notify(condition, val=nothing; all=true, error=false)
```

Wake up tasks waiting for a condition, passing them `val`. If `all` is `true` (the default), all waiting tasks are woken, otherwise only one is. If `error` is `true`, the passed value is raised as an exception in the woken tasks.

Return the count of tasks woken up. Return 0 if no tasks are waiting on `condition`.



ntoh:
==================================================

```
ntoh(x)
```

Convert the endianness of a value from Network byte order (big-endian) to that used by the Host.



ntuple:
==================================================

```
ntuple(f, n::Integer)
```

Create a tuple of length `n`, computing each element as `f(i)`, where `i` is the index of the element.

# Examples

```jldoctest
julia> ntuple(i -> 2*i, 4)
(2, 4, 6, 8)
```

```
ntuple(f, ::Val{N})
```

Create a tuple of length `N`, computing each element as `f(i)`, where `i` is the index of the element. By taking a `Val(N)` argument, it is possible that this version of ntuple may generate more efficient code than the version taking the length as an integer. But `ntuple(f, N)` is preferable to `ntuple(f, Val(N))` in cases where `N` cannot be determined at compile time.

# Examples

```jldoctest
julia> ntuple(i -> 2*i, Val(4))
(2, 4, 6, 8)
```



numerator:
==================================================

```
numerator(x)
```

Numerator of the rational representation of `x`.

# Examples

```jldoctest
julia> numerator(2//3)
2

julia> numerator(4)
4
```



objectid:
==================================================

```
objectid(x) -> UInt
```

Get a hash value for `x` based on object identity.

If `x === y` then `objectid(x) == objectid(y)`, and usually when `x !== y`, `objectid(x) != objectid(y)`.

See also [`hash`](@ref), [`IdDict`](@ref).



occursin:
==================================================

```
occursin(needle::Union{AbstractString,AbstractPattern,AbstractChar}, haystack::AbstractString)
```

Determine whether the first argument is a substring of the second. If `needle` is a regular expression, checks whether `haystack` contains a match.

# Examples

```jldoctest
julia> occursin("Julia", "JuliaLang is pretty cool!")
true

julia> occursin('a', "JuliaLang is pretty cool!")
true

julia> occursin(r"a.a", "aba")
true

julia> occursin(r"a.a", "abba")
false
```

See also [`contains`](@ref).

```
occursin(haystack)
```

Create a function that checks whether its argument occurs in `haystack`, i.e. a function equivalent to `needle -> occursin(needle, haystack)`.

The returned function is of type `Base.Fix2{typeof(occursin)}`.

!!! compat "Julia 1.6"
    This method requires Julia 1.6 or later.


# Examples

```jldoctest
julia> search_f = occursin("JuliaLang is a programming language");

julia> search_f("JuliaLang")
true

julia> search_f("Python")
false
```



oftype:
==================================================

```
oftype(x, y)
```

Convert `y` to the type of `x` i.e. `convert(typeof(x), y)`.

# Examples

```jldoctest
julia> x = 4;

julia> y = 3.;

julia> oftype(x, y)
3

julia> oftype(y, x)
4.0
```



one:
==================================================

```
one(x)
one(T::type)
```

Return a multiplicative identity for `x`: a value such that `one(x)*x == x*one(x) == x`.  Alternatively `one(T)` can take a type `T`, in which case `one` returns a multiplicative identity for any `x` of type `T`.

If possible, `one(x)` returns a value of the same type as `x`, and `one(T)` returns a value of type `T`.  However, this may not be the case for types representing dimensionful quantities (e.g. time in days), since the multiplicative identity must be dimensionless.  In that case, `one(x)` should return an identity value of the same precision (and shape, for matrices) as `x`.

If you want a quantity that is of the same type as `x`, or of type `T`, even if `x` is dimensionful, use [`oneunit`](@ref) instead.

See also the [`identity`](@ref) function, and `I` in [`LinearAlgebra`](@ref man-linalg) for the identity matrix.

# Examples

```jldoctest
julia> one(3.7)
1.0

julia> one(Int)
1

julia> import Dates; one(Dates.Day(1))
1
```



ones:
==================================================

```
ones([T=Float64,] dims::Tuple)
ones([T=Float64,] dims...)
```

Create an `Array`, with element type `T`, of all ones with size specified by `dims`. See also [`fill`](@ref), [`zeros`](@ref).

# Examples

```jldoctest
julia> ones(1,2)
1×2 Matrix{Float64}:
 1.0  1.0

julia> ones(ComplexF64, 2, 3)
2×3 Matrix{ComplexF64}:
 1.0+0.0im  1.0+0.0im  1.0+0.0im
 1.0+0.0im  1.0+0.0im  1.0+0.0im
```



oneunit:
==================================================

```
oneunit(x::T)
oneunit(T::Type)
```

Return `T(one(x))`, where `T` is either the type of the argument or (if a type is passed) the argument.  This differs from [`one`](@ref) for dimensionful quantities: `one` is dimensionless (a multiplicative identity) while `oneunit` is dimensionful (of the same type as `x`, or of type `T`).

# Examples

```jldoctest
julia> oneunit(3.7)
1.0

julia> import Dates; oneunit(Dates.Day)
1 day
```



only:
==================================================

```
only(x)
```

Return the one and only element of collection `x`, or throw an [`ArgumentError`](@ref) if the collection has zero or multiple elements.

See also [`first`](@ref), [`last`](@ref).

!!! compat "Julia 1.4"
    This method requires at least Julia 1.4.


# Examples

```jldoctest
julia> only(["a"])
"a"

julia> only("a")
'a': ASCII/Unicode U+0061 (category Ll: Letter, lowercase)

julia> only(())
ERROR: ArgumentError: Tuple contains 0 elements, must contain exactly 1 element
Stacktrace:
[...]

julia> only(('a', 'b'))
ERROR: ArgumentError: Tuple contains 2 elements, must contain exactly 1 element
Stacktrace:
[...]
```



open:
==================================================

```
open(f::Function, args...; kwargs...)
```

Apply the function `f` to the result of `open(args...; kwargs...)` and close the resulting file descriptor upon completion.

# Examples

```jldoctest
julia> write("myfile.txt", "Hello world!");

julia> open(io->read(io, String), "myfile.txt")
"Hello world!"

julia> rm("myfile.txt")
```

```
open(filename::AbstractString; lock = true, keywords...) -> IOStream
```

Open a file in a mode specified by five boolean keyword arguments:

| Keyword    | Description            | Default                               |
|:---------- |:---------------------- |:------------------------------------- |
| `read`     | open for reading       | `!write`                              |
| `write`    | open for writing       | `truncate \| append`                  |
| `create`   | create if non-existent | `!read & write \| truncate \| append` |
| `truncate` | truncate to zero size  | `!read & write`                       |
| `append`   | seek to end            | `false`                               |

The default when no keywords are passed is to open files for reading only. Returns a stream for accessing the opened file.

The `lock` keyword argument controls whether operations will be locked for safe multi-threaded access.

!!! compat "Julia 1.5"
    The `lock` argument is available as of Julia 1.5.


```
open(filename::AbstractString, [mode::AbstractString]; lock = true) -> IOStream
```

Alternate syntax for open, where a string-based mode specifier is used instead of the five booleans. The values of `mode` correspond to those from `fopen(3)` or Perl `open`, and are equivalent to setting the following boolean groups:

| Mode | Description                   | Keywords                       |
|:---- |:----------------------------- |:------------------------------ |
| `r`  | read                          | none                           |
| `w`  | write, create, truncate       | `write = true`                 |
| `a`  | write, create, append         | `append = true`                |
| `r+` | read, write                   | `read = true, write = true`    |
| `w+` | read, write, create, truncate | `truncate = true, read = true` |
| `a+` | read, write, create, append   | `append = true, read = true`   |

The `lock` keyword argument controls whether operations will be locked for safe multi-threaded access.

# Examples

```jldoctest
julia> io = open("myfile.txt", "w");

julia> write(io, "Hello world!");

julia> close(io);

julia> io = open("myfile.txt", "r");

julia> read(io, String)
"Hello world!"

julia> write(io, "This file is read only")
ERROR: ArgumentError: write failed, IOStream is not writeable
[...]

julia> close(io)

julia> io = open("myfile.txt", "a");

julia> write(io, "This stream is not read only")
28

julia> close(io)

julia> rm("myfile.txt")
```

!!! compat "Julia 1.5"
    The `lock` argument is available as of Julia 1.5.


```
open(fd::OS_HANDLE) -> IO
```

Take a raw file descriptor wrap it in a Julia-aware IO type, and take ownership of the fd handle. Call `open(Libc.dup(fd))` to avoid the ownership capture of the original handle.

!!! warning
    Do not call this on a handle that's already owned by some other part of the system.


```
open(command, mode::AbstractString, stdio=devnull)
```

Run `command` asynchronously. Like `open(command, stdio; read, write)` except specifying the read and write flags via a mode string instead of keyword arguments. Possible mode strings are:

| Mode | Description | Keywords                    |
|:---- |:----------- |:--------------------------- |
| `r`  | read        | none                        |
| `w`  | write       | `write = true`              |
| `r+` | read, write | `read = true, write = true` |
| `w+` | read, write | `read = true, write = true` |

```
open(command, stdio=devnull; write::Bool = false, read::Bool = !write)
```

Start running `command` asynchronously, and return a `process::IO` object.  If `read` is true, then reads from the process come from the process's standard output and `stdio` optionally specifies the process's standard input stream.  If `write` is true, then writes go to the process's standard input and `stdio` optionally specifies the process's standard output stream. The process's standard error stream is connected to the current global `stderr`.

```
open(f::Function, command, args...; kwargs...)
```

Similar to `open(command, args...; kwargs...)`, but calls `f(stream)` on the resulting process stream, then closes the input stream and waits for the process to complete. Return the value returned by `f` on success. Throw an error if the process failed, or if the process attempts to print anything to stdout.



operm:
==================================================

```
operm(file)
```

Like [`uperm`](@ref) but gets the permissions for people who neither own the file nor are a member of the group owning the file



pairs:
==================================================

```
pairs(collection)
```

Return an iterator over `key => value` pairs for any collection that maps a set of keys to a set of values. This includes arrays, where the keys are the array indices.

# Examples

```jldoctest
julia> a = Dict(zip(["a", "b", "c"], [1, 2, 3]))
Dict{String, Int64} with 3 entries:
  "c" => 3
  "b" => 2
  "a" => 1

julia> pairs(a)
Dict{String, Int64} with 3 entries:
  "c" => 3
  "b" => 2
  "a" => 1

julia> foreach(println, pairs(["a", "b", "c"]))
1 => "a"
2 => "b"
3 => "c"

julia> (;a=1, b=2, c=3) |> pairs |> collect
3-element Vector{Pair{Symbol, Int64}}:
 :a => 1
 :b => 2
 :c => 3

julia> (;a=1, b=2, c=3) |> collect
3-element Vector{Int64}:
 1
 2
 3
```

```
pairs(IndexLinear(), A)
pairs(IndexCartesian(), A)
pairs(IndexStyle(A), A)
```

An iterator that accesses each element of the array `A`, returning `i => x`, where `i` is the index for the element and `x = A[i]`. Identical to `pairs(A)`, except that the style of index can be selected. Also similar to `enumerate(A)`, except `i` will be a valid index for `A`, while `enumerate` always counts from 1 regardless of the indices of `A`.

Specifying [`IndexLinear()`](@ref) ensures that `i` will be an integer; specifying [`IndexCartesian()`](@ref) ensures that `i` will be a [`Base.CartesianIndex`](@ref); specifying `IndexStyle(A)` chooses whichever has been defined as the native indexing style for array `A`.

Mutation of the bounds of the underlying array will invalidate this iterator.

# Examples

```jldoctest
julia> A = ["a" "d"; "b" "e"; "c" "f"];

julia> for (index, value) in pairs(IndexStyle(A), A)
           println("$index $value")
       end
1 a
2 b
3 c
4 d
5 e
6 f

julia> S = view(A, 1:2, :);

julia> for (index, value) in pairs(IndexStyle(S), S)
           println("$index $value")
       end
CartesianIndex(1, 1) a
CartesianIndex(2, 1) b
CartesianIndex(1, 2) d
CartesianIndex(2, 2) e
```

See also [`IndexStyle`](@ref), [`axes`](@ref).



parent:
==================================================

```
parent(A)
```

Return the underlying parent object of the view. This parent of objects of types `SubArray`, `SubString`, `ReshapedArray` or `LinearAlgebra.Transpose` is what was passed as an argument to `view`, `reshape`, `transpose`, etc. during object creation. If the input is not a wrapped object, return the input itself. If the input is wrapped multiple times, only the outermost wrapper will be removed.

# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> V = view(A, 1:2, :)
2×2 view(::Matrix{Int64}, 1:2, :) with eltype Int64:
 1  2
 3  4

julia> parent(V)
2×2 Matrix{Int64}:
 1  2
 3  4
```



parentindices:
==================================================

```
parentindices(A)
```

Return the indices in the [`parent`](@ref) which correspond to the view `A`.

# Examples

```jldoctest
julia> A = [1 2; 3 4];

julia> V = view(A, 1, :)
2-element view(::Matrix{Int64}, 1, :) with eltype Int64:
 1
 2

julia> parentindices(V)
(1, Base.Slice(Base.OneTo(2)))
```



parentmodule:
==================================================

```
parentmodule(m::Module) -> Module
```

Get a module's enclosing `Module`. `Main` is its own parent.

See also: [`names`](@ref), [`nameof`](@ref), [`fullname`](@ref), [`@__MODULE__`](@ref).

# Examples

```jldoctest
julia> parentmodule(Main)
Main

julia> parentmodule(Base.Broadcast)
Base
```

```
parentmodule(t::DataType) -> Module
```

Determine the module containing the definition of a (potentially `UnionAll`-wrapped) `DataType`.

# Examples

```jldoctest
julia> module Foo
           struct Int end
       end
Foo

julia> parentmodule(Int)
Core

julia> parentmodule(Foo.Int)
Foo
```

```
parentmodule(f::Function) -> Module
```

Determine the module containing the (first) definition of a generic function.

```
parentmodule(f::Function, types) -> Module
```

Determine the module containing the first method of a generic function `f` matching the specified `types`.

```
parentmodule(m::Method) -> Module
```

Return the module in which the given method `m` is defined.

!!! compat "Julia 1.9"
    Passing a `Method` as an argument requires Julia 1.9 or later.




parse:
==================================================

```
parse(type, str; base)
```

Parse a string as a number. For `Integer` types, a base can be specified (the default is 10). For floating-point types, the string is parsed as a decimal floating-point number.  `Complex` types are parsed from decimal strings of the form `"R±Iim"` as a `Complex(R,I)` of the requested type; `"i"` or `"j"` can also be used instead of `"im"`, and `"R"` or `"Iim"` are also permitted. If the string does not contain a valid number, an error is raised.

!!! compat "Julia 1.1"
    `parse(Bool, str)` requires at least Julia 1.1.


# Examples

```jldoctest
julia> parse(Int, "1234")
1234

julia> parse(Int, "1234", base = 5)
194

julia> parse(Int, "afc", base = 16)
2812

julia> parse(Float64, "1.2e-3")
0.0012

julia> parse(Complex{Float64}, "3.2e-1 + 4.5im")
0.32 + 4.5im
```

```
parse(::Type{Platform}, triplet::AbstractString)
```

Parses a string platform triplet back into a `Platform` object.

```
parse(::Type{SimpleColor}, rgb::String)
```

An analogue of `tryparse(SimpleColor, rgb::String)` (which see), that raises an error instead of returning `nothing`.



partialsort:
==================================================

```
partialsort(v, k, by=identity, lt=isless, rev=false)
```

Variant of [`partialsort!`](@ref) that copies `v` before partially sorting it, thereby returning the same thing as `partialsort!` but leaving `v` unmodified.



partialsort!:
==================================================

```
partialsort!(v, k; by=identity, lt=isless, rev=false)
```

Partially sort the vector `v` in place so that the value at index `k` (or range of adjacent values if `k` is a range) occurs at the position where it would appear if the array were fully sorted. If `k` is a single index, that value is returned; if `k` is a range, an array of values at those indices is returned. Note that `partialsort!` may not fully sort the input array.

For the keyword arguments, see the documentation of [`sort!`](@ref).

# Examples

```jldoctest
julia> a = [1, 2, 4, 3, 4]
5-element Vector{Int64}:
 1
 2
 4
 3
 4

julia> partialsort!(a, 4)
4

julia> a
5-element Vector{Int64}:
 1
 2
 3
 4
 4

julia> a = [1, 2, 4, 3, 4]
5-element Vector{Int64}:
 1
 2
 4
 3
 4

julia> partialsort!(a, 4, rev=true)
2

julia> a
5-element Vector{Int64}:
 4
 4
 3
 2
 1
```



partialsortperm:
==================================================

```
partialsortperm(v, k; by=identity, lt=isless, rev=false)
```

Return a partial permutation `I` of the vector `v`, so that `v[I]` returns values of a fully sorted version of `v` at index `k`. If `k` is a range, a vector of indices is returned; if `k` is an integer, a single index is returned. The order is specified using the same keywords as `sort!`. The permutation is stable: the indices of equal elements will appear in ascending order.

This function is equivalent to, but more efficient than, calling `sortperm(...)[k]`.

# Examples

```jldoctest
julia> v = [3, 1, 2, 1];

julia> v[partialsortperm(v, 1)]
1

julia> p = partialsortperm(v, 1:3)
3-element view(::Vector{Int64}, 1:3) with eltype Int64:
 2
 4
 3

julia> v[p]
3-element Vector{Int64}:
 1
 1
 2
```



partialsortperm!:
==================================================

```
partialsortperm!(ix, v, k; by=identity, lt=isless, rev=false)
```

Like [`partialsortperm`](@ref), but accepts a preallocated index vector `ix` the same size as `v`, which is used to store (a permutation of) the indices of `v`.

`ix` is initialized to contain the indices of `v`.

(Typically, the indices of `v` will be `1:length(v)`, although if `v` has an alternative array type with non-one-based indices, such as an `OffsetArray`, `ix` must share those same indices)

Upon return, `ix` is guaranteed to have the indices `k` in their sorted positions, such that

```julia
partialsortperm!(ix, v, k);
v[ix[k]] == partialsort(v, k)
```

The return value is the `k`th element of `ix` if `k` is an integer, or view into `ix` if `k` is a range.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


# Examples

```jldoctest
julia> v = [3, 1, 2, 1];

julia> ix = Vector{Int}(undef, 4);

julia> partialsortperm!(ix, v, 1)
2

julia> ix = [1:4;];

julia> partialsortperm!(ix, v, 2:3)
2-element view(::Vector{Int64}, 2:3) with eltype Int64:
 4
 3
```

```

```



pathof:
==================================================

```
pathof(m::Module)
```

Return the path of the `m.jl` file that was used to `import` module `m`, or `nothing` if `m` was not imported from a package.

Use [`dirname`](@ref) to get the directory part and [`basename`](@ref) to get the file name part of the path.

See also [`pkgdir`](@ref).



peakflops:
==================================================

```
peakflops(n::Integer=4096; eltype::DataType=Float64, ntrials::Integer=3, parallel::Bool=false)
```

`peakflops` computes the peak flop rate of the computer by using double precision [`gemm!`](@ref LinearAlgebra.BLAS.gemm!). For more information see [`LinearAlgebra.peakflops`](@ref).

!!! compat "Julia 1.1"
    This function will be moved from `InteractiveUtils` to `LinearAlgebra` in the future. In Julia 1.1 and later it is available as `LinearAlgebra.peakflops`.




peek:
==================================================

```
peek(stream[, T=UInt8])
```

Read and return a value of type `T` from a stream without advancing the current position in the stream.   See also [`startswith(stream, char_or_string)`](@ref).

# Examples

```jldoctest
julia> b = IOBuffer("julia");

julia> peek(b)
0x6a

julia> position(b)
0

julia> peek(b, Char)
'j': ASCII/Unicode U+006A (category Ll: Letter, lowercase)
```

!!! compat "Julia 1.5"
    The method which accepts a type requires Julia 1.5 or later.


```
peek(stream [, n=1]; skip_newlines=false)
```

Look ahead in the stream `n` tokens, returning the token kind. Comments and non-newline whitespace are skipped automatically. Whitespace containing a single newline is returned as kind `K"NewlineWs"` unless `skip_newlines` is true.



permute!:
==================================================

```
permute!(v, p)
```

Permute vector `v` in-place, according to permutation `p`. No checking is done to verify that `p` is a permutation.

To return a new permutation, use `v[p]`. This is generally faster than `permute!(v, p)`; it is even faster to write into a pre-allocated output array with `u .= @view v[p]`. (Even though `permute!` overwrites `v` in-place, it internally requires some allocation to keep track of which elements have been moved.)

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


See also [`invpermute!`](@ref).

# Examples

```jldoctest
julia> A = [1, 1, 3, 4];

julia> perm = [2, 4, 3, 1];

julia> permute!(A, perm);

julia> A
4-element Vector{Int64}:
 1
 4
 3
 1
```



permutedims:
==================================================

```
permutedims(A::AbstractArray, perm)
permutedims(A::AbstractMatrix)
```

Permute the dimensions (axes) of array `A`. `perm` is a tuple or vector of `ndims(A)` integers specifying the permutation.

If `A` is a 2d array ([`AbstractMatrix`](@ref)), then `perm` defaults to `(2,1)`, swapping the two axes of `A` (the rows and columns of the matrix).   This differs from [`transpose`](@ref) in that the operation is not recursive, which is especially useful for arrays of non-numeric values (where the recursive `transpose` would throw an error) and/or 2d arrays that do not represent linear operators.

For 1d arrays, see [`permutedims(v::AbstractVector)`](@ref), which returns a 1-row “matrix”.

See also [`permutedims!`](@ref), [`PermutedDimsArray`](@ref), [`transpose`](@ref), [`invperm`](@ref).

# Examples

## 2d arrays:

Unlike `transpose`, `permutedims` can be used to swap rows and columns of 2d arrays of arbitrary non-numeric elements, such as strings:

```jldoctest
julia> A = ["a" "b" "c"
            "d" "e" "f"]
2×3 Matrix{String}:
 "a"  "b"  "c"
 "d"  "e"  "f"

julia> permutedims(A)
3×2 Matrix{String}:
 "a"  "d"
 "b"  "e"
 "c"  "f"
```

And `permutedims` produces results that differ from `transpose` for matrices whose elements are themselves numeric matrices:

```jldoctest; setup = :(using LinearAlgebra)
julia> a = [1 2; 3 4];

julia> b = [5 6; 7 8];

julia> c = [9 10; 11 12];

julia> d = [13 14; 15 16];

julia> X = [[a] [b]; [c] [d]]
2×2 Matrix{Matrix{Int64}}:
 [1 2; 3 4]     [5 6; 7 8]
 [9 10; 11 12]  [13 14; 15 16]

julia> permutedims(X)
2×2 Matrix{Matrix{Int64}}:
 [1 2; 3 4]  [9 10; 11 12]
 [5 6; 7 8]  [13 14; 15 16]

julia> transpose(X)
2×2 transpose(::Matrix{Matrix{Int64}}) with eltype Transpose{Int64, Matrix{Int64}}:
 [1 3; 2 4]  [9 11; 10 12]
 [5 7; 6 8]  [13 15; 14 16]
```

## Multi-dimensional arrays

```jldoctest
julia> A = reshape(Vector(1:8), (2,2,2))
2×2×2 Array{Int64, 3}:
[:, :, 1] =
 1  3
 2  4

[:, :, 2] =
 5  7
 6  8

julia> perm = (3, 1, 2); # put the last dimension first

julia> B = permutedims(A, perm)
2×2×2 Array{Int64, 3}:
[:, :, 1] =
 1  2
 5  6

[:, :, 2] =
 3  4
 7  8

julia> A == permutedims(B, invperm(perm)) # the inverse permutation
true
```

For each dimension `i` of `B = permutedims(A, perm)`, its corresponding dimension of `A` will be `perm[i]`. This means the equality `size(B, i) == size(A, perm[i])` holds.

```jldoctest
julia> A = randn(5, 7, 11, 13);

julia> perm = [4, 1, 3, 2];

julia> B = permutedims(A, perm);

julia> size(B)
(13, 5, 11, 7)

julia> size(A)[perm] == ans
true
```

```
permutedims(v::AbstractVector)
```

Reshape vector `v` into a `1 × length(v)` row matrix. Differs from [`transpose`](@ref) in that the operation is not recursive, which is especially useful for arrays of non-numeric values (where the recursive `transpose` might throw an error).

# Examples

Unlike `transpose`, `permutedims` can be used on vectors of arbitrary non-numeric elements, such as strings:

```jldoctest
julia> permutedims(["a", "b", "c"])
1×3 Matrix{String}:
 "a"  "b"  "c"
```

For vectors of numbers, `permutedims(v)` works much like `transpose(v)` except that the return type differs (it uses [`reshape`](@ref) rather than a `LinearAlgebra.Transpose` view, though both share memory with the original array `v`):

```jldoctest; setup = :(using LinearAlgebra)
julia> v = [1, 2, 3, 4]
4-element Vector{Int64}:
 1
 2
 3
 4

julia> p = permutedims(v)
1×4 Matrix{Int64}:
 1  2  3  4

julia> r = transpose(v)
1×4 transpose(::Vector{Int64}) with eltype Int64:
 1  2  3  4

julia> p == r
true

julia> typeof(r)
Transpose{Int64, Vector{Int64}}

julia> p[1] = 5; r[2] = 6; # mutating p or r also changes v

julia> v # shares memory with both p and r
4-element Vector{Int64}:
 5
 6
 3
 4
```

However, `permutedims` produces results that differ from `transpose` for vectors whose elements are themselves numeric matrices:

```jldoctest; setup = :(using LinearAlgebra)
julia> V = [[[1 2; 3 4]]; [[5 6; 7 8]]]
2-element Vector{Matrix{Int64}}:
 [1 2; 3 4]
 [5 6; 7 8]

julia> permutedims(V)
1×2 Matrix{Matrix{Int64}}:
 [1 2; 3 4]  [5 6; 7 8]

julia> transpose(V)
1×2 transpose(::Vector{Matrix{Int64}}) with eltype Transpose{Int64, Matrix{Int64}}:
 [1 3; 2 4]  [5 7; 6 8]
```



permutedims!:
==================================================

```
permutedims!(dest, src, perm)
```

Permute the dimensions of array `src` and store the result in the array `dest`. `perm` is a vector specifying a permutation of length `ndims(src)`. The preallocated array `dest` should have `size(dest) == size(src)[perm]` and is completely overwritten. No in-place permutation is supported and unexpected results will happen if `src` and `dest` have overlapping memory regions.

See also [`permutedims`](@ref).



pi:
==================================================

```
Irrational{sym} <: AbstractIrrational
```

Number type representing an exact irrational value denoted by the symbol `sym`, such as [`π`](@ref pi), [`ℯ`](@ref) and [`γ`](@ref Base.MathConstants.eulergamma).

See also [`AbstractIrrational`](@ref).



pipeline:
==================================================

```
pipeline(command; stdin, stdout, stderr, append=false)
```

Redirect I/O to or from the given `command`. Keyword arguments specify which of the command's streams should be redirected. `append` controls whether file output appends to the file. This is a more general version of the 2-argument `pipeline` function. `pipeline(from, to)` is equivalent to `pipeline(from, stdout=to)` when `from` is a command, and to `pipeline(to, stdin=from)` when `from` is another kind of data source.

**Examples**:

```julia
run(pipeline(`dothings`, stdout="out.txt", stderr="errs.txt"))
run(pipeline(`update`, stdout="log.txt", append=true))
```

```
pipeline(from, to, ...)
```

Create a pipeline from a data source to a destination. The source and destination can be commands, I/O streams, strings, or results of other `pipeline` calls. At least one argument must be a command. Strings refer to filenames. When called with more than two arguments, they are chained together from left to right. For example, `pipeline(a,b,c)` is equivalent to `pipeline(pipeline(a,b),c)`. This provides a more concise way to specify multi-stage pipelines.

**Examples**:

```julia
run(pipeline(`ls`, `grep xyz`))
run(pipeline(`ls`, "out.txt"))
run(pipeline("out.txt", `grep xyz`))
```



pkgdir:
==================================================

```
pkgdir(m::Module[, paths::String...])
```

Return the root directory of the package that declared module `m`, or `nothing` if `m` was not declared in a package. Optionally further path component strings can be provided to construct a path within the package root.

To get the root directory of the package that implements the current module the form `pkgdir(@__MODULE__)` can be used.

If an extension module is given, the root of the parent package is returned.

```julia-repl
julia> pkgdir(Foo)
"/path/to/Foo.jl"

julia> pkgdir(Foo, "src", "file.jl")
"/path/to/Foo.jl/src/file.jl"
```

See also [`pathof`](@ref).

!!! compat "Julia 1.7"
    The optional argument `paths` requires at least Julia 1.7.




pkgversion:
==================================================

```
pkgversion(m::Module)
```

Return the version of the package that imported module `m`, or `nothing` if `m` was not imported from a package, or imported from a package without a version field set.

The version is read from the package's Project.toml during package load.

To get the version of the package that imported the current module the form `pkgversion(@__MODULE__)` can be used.

!!! compat "Julia 1.9"
    This function was introduced in Julia 1.9.




pointer:
==================================================

```
pointer(array [, index])
```

Get the native address of an array or string, optionally at a given location `index`.

This function is "unsafe". Be careful to ensure that a Julia reference to `array` exists as long as this pointer will be used. The [`GC.@preserve`](@ref) macro should be used to protect the `array` argument from garbage collection within a given block of code.

Calling [`Ref(array[, index])`](@ref Ref) is generally preferable to this function as it guarantees validity.



pointer_from_objref:
==================================================

```
pointer_from_objref(x)
```

Get the memory address of a Julia object as a `Ptr`. The existence of the resulting `Ptr` will not protect the object from garbage collection, so you must ensure that the object remains referenced for the whole time that the `Ptr` will be used.

This function may not be called on immutable objects, since they do not have stable memory addresses.

See also [`unsafe_pointer_to_objref`](@ref).



pop!:
==================================================

```
pop!(collection) -> item
```

Remove an item in `collection` and return it. If `collection` is an ordered container, the last item is returned; for unordered containers, an arbitrary element is returned.

See also: [`popfirst!`](@ref), [`popat!`](@ref), [`delete!`](@ref), [`deleteat!`](@ref), [`splice!`](@ref), and [`push!`](@ref).

# Examples

```jldoctest
julia> A=[1, 2, 3]
3-element Vector{Int64}:
 1
 2
 3

julia> pop!(A)
3

julia> A
2-element Vector{Int64}:
 1
 2

julia> S = Set([1, 2])
Set{Int64} with 2 elements:
  2
  1

julia> pop!(S)
2

julia> S
Set{Int64} with 1 element:
  1

julia> pop!(Dict(1=>2))
1 => 2
```

```
pop!(collection, key[, default])
```

Delete and return the mapping for `key` if it exists in `collection`, otherwise return `default`, or throw an error if `default` is not specified.

# Examples

```jldoctest
julia> d = Dict("a"=>1, "b"=>2, "c"=>3);

julia> pop!(d, "a")
1

julia> pop!(d, "d")
ERROR: KeyError: key "d" not found
Stacktrace:
[...]

julia> pop!(d, "e", 4)
4
```



popat!:
==================================================

```
popat!(a::Vector, i::Integer, [default])
```

Remove the item at the given `i` and return it. Subsequent items are shifted to fill the resulting gap. When `i` is not a valid index for `a`, return `default`, or throw an error if `default` is not specified.

See also: [`pop!`](@ref), [`popfirst!`](@ref), [`deleteat!`](@ref), [`splice!`](@ref).

!!! compat "Julia 1.5"
    This function is available as of Julia 1.5.


# Examples

```jldoctest
julia> a = [4, 3, 2, 1]; popat!(a, 2)
3

julia> a
3-element Vector{Int64}:
 4
 2
 1

julia> popat!(a, 4, missing)
missing

julia> popat!(a, 4)
ERROR: BoundsError: attempt to access 3-element Vector{Int64} at index [4]
[...]
```



popdisplay:
==================================================

```
popdisplay()
popdisplay(d::AbstractDisplay)
```

Pop the topmost backend off of the display-backend stack, or the topmost copy of `d` in the second variant.



popfirst!:
==================================================

```
popfirst!(collection) -> item
```

Remove the first `item` from `collection`.

This function is called `shift` in many other programming languages.

See also: [`pop!`](@ref), [`popat!`](@ref), [`delete!`](@ref).

# Examples

```jldoctest
julia> A = [1, 2, 3, 4, 5, 6]
6-element Vector{Int64}:
 1
 2
 3
 4
 5
 6

julia> popfirst!(A)
1

julia> A
5-element Vector{Int64}:
 2
 3
 4
 5
 6
```



position:
==================================================

```
position(s)
```

Get the current position of a stream.

# Examples

```jldoctest
julia> io = IOBuffer("JuliaLang is a GitHub organization.");

julia> seek(io, 5);

julia> position(io)
5

julia> skip(io, 10);

julia> position(io)
15

julia> seekend(io);

julia> position(io)
35
```

```
position(l::Lexer)
```

Returns the current position.



powermod:
==================================================

```
powermod(x::Integer, p::Integer, m)
```

Compute $x^p \pmod m$.

# Examples

```jldoctest
julia> powermod(2, 6, 5)
4

julia> mod(2^6, 5)
4

julia> powermod(5, 2, 20)
5

julia> powermod(5, 2, 19)
6

julia> powermod(5, 3, 19)
11
```



precision:
==================================================

```
precision(num::AbstractFloat; base::Integer=2)
precision(T::Type; base::Integer=2)
```

Get the precision of a floating point number, as defined by the effective number of bits in the significand, or the precision of a floating-point type `T` (its current default, if `T` is a variable-precision type like [`BigFloat`](@ref)).

If `base` is specified, then it returns the maximum corresponding number of significand digits in that base.

!!! compat "Julia 1.8"
    The `base` keyword requires at least Julia 1.8.




precompile:
==================================================

```
precompile(f, argtypes::Tuple{Vararg{Any}})
```

Compile the given function `f` for the argument tuple (of types) `argtypes`, but do not execute it.

```
precompile(f, argtypes::Tuple{Vararg{Any}}, m::Method)
```

Precompile a specific method for the given argument types. This may be used to precompile a different method than the one that would ordinarily be chosen by dispatch, thus mimicking `invoke`.



prepend!:
==================================================

```
prepend!(a::Vector, collections...) -> collection
```

Insert the elements of each `collections` to the beginning of `a`.

When `collections` specifies multiple collections, order is maintained: elements of `collections[1]` will appear leftmost in `a`, and so on.

!!! compat "Julia 1.6"
    Specifying multiple collections to be prepended requires at least Julia 1.6.


# Examples

```jldoctest
julia> prepend!([3], [1, 2])
3-element Vector{Int64}:
 1
 2
 3

julia> prepend!([6], [1, 2], [3, 4, 5])
6-element Vector{Int64}:
 1
 2
 3
 4
 5
 6
```



prevfloat:
==================================================

```
prevfloat(x::AbstractFloat, n::Integer)
```

The result of `n` iterative applications of `prevfloat` to `x` if `n >= 0`, or `-n` applications of [`nextfloat`](@ref) if `n < 0`.

```
prevfloat(x::AbstractFloat)
```

Return the largest floating point number `y` of the same type as `x` such `y < x`. If no such `y` exists (e.g. if `x` is `-Inf` or `NaN`), then return `x`.



prevind:
==================================================

```
prevind(A, i)
```

Return the index before `i` in `A`. The returned index is often equivalent to `i - 1` for an integer `i`. This function can be useful for generic code.

!!! warning
    The returned index might be out of bounds. Consider using [`checkbounds`](@ref).


See also: [`nextind`](@ref).

# Examples

```jldoctest
julia> x = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> prevind(x, 4) # valid result
3

julia> prevind(x, 1) # invalid result
0

julia> prevind(x, CartesianIndex(2, 2)) # valid result
CartesianIndex(1, 2)

julia> prevind(x, CartesianIndex(1, 1)) # invalid result
CartesianIndex(2, 0)
```

```
prevind(str::AbstractString, i::Integer, n::Integer=1) -> Int
```

  * Case `n == 1`

    If `i` is in bounds in `s` return the index of the start of the character whose encoding starts before index `i`. In other words, if `i` is the start of a character, return the start of the previous character; if `i` is not the start of a character, rewind until the start of a character and return that index. If `i` is equal to `1` return `0`. If `i` is equal to `ncodeunits(str)+1` return `lastindex(str)`. Otherwise throw `BoundsError`.
  * Case `n > 1`

    Behaves like applying `n` times `prevind` for `n==1`. The only difference is that if `n` is so large that applying `prevind` would reach `0` then each remaining iteration decreases the returned value by `1`. This means that in this case `prevind` can return a negative value.
  * Case `n == 0`

    Return `i` only if `i` is a valid index in `str` or is equal to `ncodeunits(str)+1`. Otherwise `StringIndexError` or `BoundsError` is thrown.

# Examples

```jldoctest
julia> prevind("α", 3)
1

julia> prevind("α", 1)
0

julia> prevind("α", 0)
ERROR: BoundsError: attempt to access 2-codeunit String at index [0]
[...]

julia> prevind("α", 2, 2)
0

julia> prevind("α", 2, 3)
-1
```



prevpow:
==================================================

```
prevpow(a, x)
```

The largest `a^n` not greater than `x`, where `n` is a non-negative integer. `a` must be greater than 1, and `x` must not be less than 1.

See also [`nextpow`](@ref), [`isqrt`](@ref).

# Examples

```jldoctest
julia> prevpow(2, 7)
4

julia> prevpow(2, 9)
8

julia> prevpow(5, 20)
5

julia> prevpow(4, 16)
16
```



print:
==================================================

```
print([io::IO], xs...)
```

Write to `io` (or to the default output stream [`stdout`](@ref) if `io` is not given) a canonical (un-decorated) text representation. The representation used by `print` includes minimal formatting and tries to avoid Julia-specific details.

`print` falls back to calling `show`, so most types should just define `show`. Define `print` if your type has a separate "plain" representation. For example, `show` displays strings with quotes, and `print` displays strings without quotes.

See also [`println`](@ref), [`string`](@ref), [`printstyled`](@ref).

# Examples

```jldoctest
julia> print("Hello World!")
Hello World!
julia> io = IOBuffer();

julia> print(io, "Hello", ' ', :World!)

julia> String(take!(io))
"Hello World!"
```



println:
==================================================

```
println([io::IO], xs...)
```

Print (using [`print`](@ref)) `xs` to `io` followed by a newline. If `io` is not supplied, prints to the default output stream [`stdout`](@ref).

See also [`printstyled`](@ref) to add colors etc.

# Examples

```jldoctest
julia> println("Hello, world")
Hello, world

julia> io = IOBuffer();

julia> println(io, "Hello", ',', " world.")

julia> String(take!(io))
"Hello, world.\n"
```



printstyled:
==================================================

```
printstyled([io], xs...; bold::Bool=false, italic::Bool=false, underline::Bool=false, blink::Bool=false, reverse::Bool=false, hidden::Bool=false, color::Union{Symbol,Int}=:normal)
```

Print `xs` in a color specified as a symbol or integer, optionally in bold.

Keyword `color` may take any of the values `:normal`, `:italic`, `:default`, `:bold`, `:black`, `:blink`, `:blue`, `:cyan`, `:green`, `:hidden`, `:light_black`, `:light_blue`, `:light_cyan`, `:light_green`, `:light_magenta`, `:light_red`, `:light_white`, `:light_yellow`, `:magenta`, `:nothing`, `:red`, `:reverse`, `:underline`, `:white`, or  `:yellow` or an integer between 0 and 255 inclusive. Note that not all terminals support 256 colors.

Keywords `bold=true`, `italic=true`, `underline=true`, `blink=true` are self-explanatory. Keyword `reverse=true` prints with foreground and background colors exchanged, and `hidden=true` should be invisible in the terminal but can still be copied. These properties can be used in any combination.

See also [`print`](@ref), [`println`](@ref), [`show`](@ref).

!!! note
    Not all terminals support italic output. Some terminals interpret italic as reverse or blink.


!!! compat "Julia 1.7"
    Keywords except `color` and `bold` were added in Julia 1.7.


!!! compat "Julia 1.10"
    Support for italic output was added in Julia 1.10.




process_exited:
==================================================

```
process_exited(p::Process)
```

Determine whether a process has exited.



process_running:
==================================================

```
process_running(p::Process)
```

Determine whether a process is currently running.



prod:
==================================================

```
prod(f, itr; [init])
```

Return the product of `f` applied to each element of `itr`.

The return type is `Int` for signed integers of less than system word size, and `UInt` for unsigned integers of less than system word size.  For all other arguments, a common return type is found to which all arguments are promoted.

The value returned for empty `itr` can be specified by `init`. It must be the multiplicative identity (i.e. one) as it is unspecified whether `init` is used for non-empty collections.

!!! compat "Julia 1.6"
    Keyword argument `init` requires Julia 1.6 or later.


# Examples

```jldoctest
julia> prod(abs2, [2; 3; 4])
576
```

```
prod(itr; [init])
```

Return the product of all elements of a collection.

The return type is `Int` for signed integers of less than system word size, and `UInt` for unsigned integers of less than system word size.  For all other arguments, a common return type is found to which all arguments are promoted.

The value returned for empty `itr` can be specified by `init`. It must be the multiplicative identity (i.e. one) as it is unspecified whether `init` is used for non-empty collections.

!!! compat "Julia 1.6"
    Keyword argument `init` requires Julia 1.6 or later.


See also: [`reduce`](@ref), [`cumprod`](@ref), [`any`](@ref).

# Examples

```jldoctest
julia> prod(1:5)
120

julia> prod(1:5; init = 1.0)
120.0
```

```
prod(A::AbstractArray; dims)
```

Multiply elements of an array over the given dimensions.

# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> prod(A, dims=1)
1×2 Matrix{Int64}:
 3  8

julia> prod(A, dims=2)
2×1 Matrix{Int64}:
  2
 12
```

```
prod(f, A::AbstractArray; dims)
```

Multiply the results of calling the function `f` on each element of an array over the given dimensions.

# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> prod(abs2, A, dims=1)
1×2 Matrix{Int64}:
 9  64

julia> prod(abs2, A, dims=2)
2×1 Matrix{Int64}:
   4
 144
```



prod!:
==================================================

```
prod!(r, A)
```

Multiply elements of `A` over the singleton dimensions of `r`, and write results to `r`.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> prod!([1; 1], A)
2-element Vector{Int64}:
  2
 12

julia> prod!([1 1], A)
1×2 Matrix{Int64}:
 3  8
```



promote:
==================================================

```
promote(xs...)
```

Convert all arguments to a common type, and return them all (as a tuple). If no arguments can be converted, an error is raised.

See also: [`promote_type`](@ref), [`promote_rule`](@ref).

# Examples

```jldoctest
julia> promote(Int8(1), Float16(4.5), Float32(4.1))
(1.0f0, 4.5f0, 4.1f0)

julia> promote_type(Int8, Float16, Float32)
Float32

julia> reduce(Base.promote_typejoin, (Int8, Float16, Float32))
Real

julia> promote(1, "x")
ERROR: promotion of types Int64 and String failed to change any arguments
[...]

julia> promote_type(Int, String)
Any
```



promote_rule:
==================================================

```
promote_rule(type1, type2)
```

Specifies what type should be used by [`promote`](@ref) when given values of types `type1` and `type2`. This function should not be called directly, but should have definitions added to it for new types as appropriate.



promote_shape:
==================================================

```
promote_shape(s1, s2)
```

Check two array shapes for compatibility, allowing trailing singleton dimensions, and return whichever shape has more dimensions.

# Examples

```jldoctest
julia> a = fill(1, (3,4,1,1,1));

julia> b = fill(1, (3,4));

julia> promote_shape(a,b)
(Base.OneTo(3), Base.OneTo(4), Base.OneTo(1), Base.OneTo(1), Base.OneTo(1))

julia> promote_shape((2,3,1,4), (2, 3, 1, 4, 1))
(2, 3, 1, 4, 1)
```



promote_type:
==================================================

```
promote_type(type1, type2, ...)
```

Promotion refers to converting values of mixed types to a single common type. `promote_type` represents the default promotion behavior in Julia when operators (usually mathematical) are given arguments of differing types. `promote_type` generally tries to return a type which can at least approximate most values of either input type without excessively widening.  Some loss is tolerated; for example, `promote_type(Int64, Float64)` returns [`Float64`](@ref) even though strictly, not all [`Int64`](@ref) values can be represented exactly as `Float64` values.

See also: [`promote`](@ref), [`promote_typejoin`](@ref), [`promote_rule`](@ref).

# Examples

```jldoctest
julia> promote_type(Int64, Float64)
Float64

julia> promote_type(Int32, Int64)
Int64

julia> promote_type(Float32, BigInt)
BigFloat

julia> promote_type(Int16, Float16)
Float16

julia> promote_type(Int64, Float16)
Float16

julia> promote_type(Int8, UInt16)
UInt16
```

!!! warning "Don't overload this directly"
    To overload promotion for your own types you should overload [`promote_rule`](@ref). `promote_type` calls `promote_rule` internally to determine the type. Overloading `promote_type` directly can cause ambiguity errors.




propertynames:
==================================================

```
propertynames(x, private=false)
```

Get a tuple or a vector of the properties (`x.property`) of an object `x`. This is typically the same as [`fieldnames(typeof(x))`](@ref), but types that overload [`getproperty`](@ref) should generally overload `propertynames` as well to get the properties of an instance of the type.

`propertynames(x)` may return only "public" property names that are part of the documented interface of `x`.   If you want it to also return "private" property names intended for internal use, pass `true` for the optional second argument. REPL tab completion on `x.` shows only the `private=false` properties.

See also: [`hasproperty`](@ref), [`hasfield`](@ref).



push!:
==================================================

```
push!(collection, items...) -> collection
```

Insert one or more `items` in `collection`. If `collection` is an ordered container, the items are inserted at the end (in the given order).

# Examples

```jldoctest
julia> push!([1, 2, 3], 4, 5, 6)
6-element Vector{Int64}:
 1
 2
 3
 4
 5
 6
```

If `collection` is ordered, use [`append!`](@ref) to add all the elements of another collection to it. The result of the preceding example is equivalent to `append!([1, 2, 3], [4, 5, 6])`. For `AbstractSet` objects, [`union!`](@ref) can be used instead.

See [`sizehint!`](@ref) for notes about the performance model.

See also [`pushfirst!`](@ref).



pushdisplay:
==================================================

```
pushdisplay(d::AbstractDisplay)
```

Pushes a new display `d` on top of the global display-backend stack. Calling `display(x)` or `display(mime, x)` will display `x` on the topmost compatible backend in the stack (i.e., the topmost backend that does not throw a [`MethodError`](@ref)).



pushfirst!:
==================================================

```
pushfirst!(collection, items...) -> collection
```

Insert one or more `items` at the beginning of `collection`.

This function is called `unshift` in many other programming languages.

# Examples

```jldoctest
julia> pushfirst!([1, 2, 3, 4], 5, 6)
6-element Vector{Int64}:
 5
 6
 1
 2
 3
 4
```



put!:
==================================================

```
put!(c::Channel, v)
```

Append an item `v` to the channel `c`. Blocks if the channel is full.

For unbuffered channels, blocks until a [`take!`](@ref) is performed by a different task.

!!! compat "Julia 1.1"
    `v` now gets converted to the channel's type with [`convert`](@ref) as `put!` is called.




pwd:
==================================================

```
pwd() -> String
```

Get the current working directory.

See also: [`cd`](@ref), [`tempdir`](@ref).

# Examples

```julia-repl
julia> pwd()
"/home/JuliaUser"

julia> cd("/home/JuliaUser/Projects/julia")

julia> pwd()
"/home/JuliaUser/Projects/julia"
```



rad2deg:
==================================================

```
rad2deg(x)
```

Convert `x` from radians to degrees.

See also [`deg2rad`](@ref).

# Examples

```jldoctest
julia> rad2deg(pi)
180.0
```



rand:
==================================================

```
rand([rng=default_rng()], [S], [dims...])
```

Pick a random element or array of random elements from the set of values specified by `S`; `S` can be

  * an indexable collection (for example `1:9` or `('x', "y", :z)`)
  * an `AbstractDict` or `AbstractSet` object
  * a string (considered as a collection of characters), or
  * a type from the list below, corresponding to the specified set of values

      * concrete integer types sample from `typemin(S):typemax(S)` (excepting [`BigInt`](@ref) which is not supported)
      * concrete floating point types sample from `[0, 1)`
      * concrete complex types `Complex{T}` if `T` is a sampleable type take their real and imaginary components independently from the set of values corresponding to `T`, but are not supported if `T` is not sampleable.
      * all `<:AbstractChar` types sample from the set of valid Unicode scalars
      * a user-defined type and set of values; for implementation guidance please see [Hooking into the `Random` API](@ref rand-api-hook)
      * a tuple type of known size and where each parameter of `S` is itself a sampleable type; return a value of type `S`. Note that tuple types such as `Tuple{Vararg{T}}` (unknown size) and `Tuple{1:2}` (parameterized with a value) are not supported
      * a `Pair` type, e.g. `Pair{X, Y}` such that `rand` is defined for `X` and `Y`, in which case random pairs are produced.

`S` defaults to [`Float64`](@ref). When only one argument is passed besides the optional `rng` and is a `Tuple`, it is interpreted as a collection of values (`S`) and not as `dims`.

See also [`randn`](@ref) for normally distributed numbers, and [`rand!`](@ref) and [`randn!`](@ref) for the in-place equivalents.

!!! compat "Julia 1.1"
    Support for `S` as a tuple requires at least Julia 1.1.


!!! compat "Julia 1.11"
    Support for `S` as a `Tuple` type requires at least Julia 1.11.


# Examples

```julia-repl
julia> rand(Int, 2)
2-element Array{Int64,1}:
 1339893410598768192
 1575814717733606317

julia> using Random

julia> rand(Xoshiro(0), Dict(1=>2, 3=>4))
3 => 4

julia> rand((2, 3))
3

julia> rand(Float64, (2, 3))
2×3 Array{Float64,2}:
 0.999717  0.0143835  0.540787
 0.696556  0.783855   0.938235
```

!!! note
    The complexity of `rand(rng, s::Union{AbstractDict,AbstractSet})` is linear in the length of `s`, unless an optimized method with constant complexity is available, which is the case for `Dict`, `Set` and dense `BitSet`s. For more than a few calls, use `rand(rng, collect(s))` instead, or either `rand(rng, Dict(s))` or `rand(rng, Set(s))` as appropriate.




randn:
==================================================

```
randn([rng=default_rng()], [T=Float64], [dims...])
```

Generate a normally-distributed random number of type `T` with mean 0 and standard deviation 1. Given the optional `dims` argument(s), generate an array of size `dims` of such numbers. Julia's standard library supports `randn` for any floating-point type that implements [`rand`](@ref), e.g. the `Base` types [`Float16`](@ref), [`Float32`](@ref), [`Float64`](@ref) (the default), and [`BigFloat`](@ref), along with their [`Complex`](@ref) counterparts.

(When `T` is complex, the values are drawn from the circularly symmetric complex normal distribution of variance 1, corresponding to real and imaginary parts having independent normal distribution with mean zero and variance `1/2`).

See also [`randn!`](@ref) to act in-place.

# Examples

Generating a single random number (with the default `Float64` type):

```julia-repl
julia> randn()
-0.942481877315864
```

Generating a matrix of normal random numbers (with the default `Float64` type):

```julia-repl
julia> randn(2,3)
2×3 Matrix{Float64}:
  1.18786   -0.678616   1.49463
 -0.342792  -0.134299  -1.45005
```

Setting up of the random number generator `rng` with a user-defined seed (for reproducible numbers) and using it to generate a random `Float32` number or a matrix of `ComplexF32` random numbers:

```jldoctest
julia> using Random

julia> rng = Xoshiro(123);

julia> randn(rng, Float32)
-0.6457307f0

julia> randn(rng, ComplexF32, (2, 3))
2×3 Matrix{ComplexF32}:
  -1.03467-1.14806im  0.693657+0.056538im   0.291442+0.419454im
 -0.153912+0.34807im    1.0954-0.948661im  -0.543347-0.0538589im
```



range:
==================================================

```
range(start, stop, length)
range(start, stop; length, step)
range(start; length, stop, step)
range(;start, length, stop, step)
```

Construct a specialized array with evenly spaced elements and optimized storage (an [`AbstractRange`](@ref)) from the arguments. Mathematically a range is uniquely determined by any three of `start`, `step`, `stop` and `length`. Valid invocations of range are:

  * Call `range` with any three of `start`, `step`, `stop`, `length`.
  * Call `range` with two of `start`, `stop`, `length`. In this case `step` will be assumed to be one. If both arguments are Integers, a [`UnitRange`](@ref) will be returned.
  * Call `range` with one of `stop` or `length`. `start` and `step` will be assumed to be one.

See Extended Help for additional details on the returned type. See also [`logrange`](@ref) for logarithmically spaced points.

# Examples

```jldoctest
julia> range(1, length=100)
1:100

julia> range(1, stop=100)
1:100

julia> range(1, step=5, length=100)
1:5:496

julia> range(1, step=5, stop=100)
1:5:96

julia> range(1, 10, length=101)
1.0:0.09:10.0

julia> range(1, 100, step=5)
1:5:96

julia> range(stop=10, length=5)
6:10

julia> range(stop=10, step=1, length=5)
6:1:10

julia> range(start=1, step=1, stop=10)
1:1:10

julia> range(; length = 10)
Base.OneTo(10)

julia> range(; stop = 6)
Base.OneTo(6)

julia> range(; stop = 6.5)
1.0:1.0:6.0
```

If `length` is not specified and `stop - start` is not an integer multiple of `step`, a range that ends before `stop` will be produced.

```jldoctest
julia> range(1, 3.5, step=2)
1.0:2.0:3.0
```

Special care is taken to ensure intermediate values are computed rationally. To avoid this induced overhead, see the [`LinRange`](@ref) constructor.

!!! compat "Julia 1.1"
    `stop` as a positional argument requires at least Julia 1.1.


!!! compat "Julia 1.7"
    The versions without keyword arguments and `start` as a keyword argument require at least Julia 1.7.


!!! compat "Julia 1.8"
    The versions with `stop` as a sole keyword argument, or `length` as a sole keyword argument require at least Julia 1.8.


# Extended Help

`range` will produce a `Base.OneTo` when the arguments are Integers and

  * Only `length` is provided
  * Only `stop` is provided

`range` will produce a `UnitRange` when the arguments are Integers and

  * Only `start`  and `stop` are provided
  * Only `length` and `stop` are provided

A `UnitRange` is not produced if `step` is provided even if specified as one.



rationalize:
==================================================

```
rationalize([T<:Integer=Int,] x; tol::Real=eps(x))
```

Approximate floating point number `x` as a [`Rational`](@ref) number with components of the given integer type. The result will differ from `x` by no more than `tol`.

# Examples

```jldoctest
julia> rationalize(5.6)
28//5

julia> a = rationalize(BigInt, 10.3)
103//10

julia> typeof(numerator(a))
BigInt
```



read:
==================================================

```
read(io::IO, T)
```

Read a single value of type `T` from `io`, in canonical binary representation.

Note that Julia does not convert the endianness for you. Use [`ntoh`](@ref) or [`ltoh`](@ref) for this purpose.

```
read(io::IO, String)
```

Read the entirety of `io`, as a `String` (see also [`readchomp`](@ref)).

# Examples

```jldoctest
julia> io = IOBuffer("JuliaLang is a GitHub organization");

julia> read(io, Char)
'J': ASCII/Unicode U+004A (category Lu: Letter, uppercase)

julia> io = IOBuffer("JuliaLang is a GitHub organization");

julia> read(io, String)
"JuliaLang is a GitHub organization"
```

```
read(filename::AbstractString)
```

Read the entire contents of a file as a `Vector{UInt8}`.

```
read(filename::AbstractString, String)
```

Read the entire contents of a file as a string.

```
read(filename::AbstractString, args...)
```

Open a file and read its contents. `args` is passed to `read`: this is equivalent to `open(io->read(io, args...), filename)`.

```
read(s::IO, nb=typemax(Int))
```

Read at most `nb` bytes from `s`, returning a `Vector{UInt8}` of the bytes read.

```
read(s::IOStream, nb::Integer; all=true)
```

Read at most `nb` bytes from `s`, returning a `Vector{UInt8}` of the bytes read.

If `all` is `true` (the default), this function will block repeatedly trying to read all requested bytes, until an error or end-of-file occurs. If `all` is `false`, at most one `read` call is performed, and the amount of data returned is device-dependent. Note that not all stream types support the `all` option.

```
read(command::Cmd)
```

Run `command` and return the resulting output as an array of bytes.

```
read(command::Cmd, String)
```

Run `command` and return the resulting output as a `String`.



read!:
==================================================

```
read!(stream::IO, array::AbstractArray)
read!(filename::AbstractString, array::AbstractArray)
```

Read binary data from an I/O stream or file, filling in `array`.



readavailable:
==================================================

```
readavailable(stream)
```

Read available buffered data from a stream. Actual I/O is performed only if no data has already been buffered. The result is a `Vector{UInt8}`.

!!! warning
    The amount of data returned is implementation-dependent; for example it can depend on the internal choice of buffer size. Other functions such as [`read`](@ref) should generally be used instead.




readbytes!:
==================================================

```
readbytes!(stream::IO, b::AbstractVector{UInt8}, nb=length(b))
```

Read at most `nb` bytes from `stream` into `b`, returning the number of bytes read. The size of `b` will be increased if needed (i.e. if `nb` is greater than `length(b)` and enough bytes could be read), but it will never be decreased.

```
readbytes!(stream::IOStream, b::AbstractVector{UInt8}, nb=length(b); all::Bool=true)
```

Read at most `nb` bytes from `stream` into `b`, returning the number of bytes read. The size of `b` will be increased if needed (i.e. if `nb` is greater than `length(b)` and enough bytes could be read), but it will never be decreased.

If `all` is `true` (the default), this function will block repeatedly trying to read all requested bytes, until an error or end-of-file occurs. If `all` is `false`, at most one `read` call is performed, and the amount of data returned is device-dependent. Note that not all stream types support the `all` option.



readchomp:
==================================================

```
readchomp(x)
```

Read the entirety of `x` as a string and remove a single trailing newline if there is one. Equivalent to `chomp(read(x, String))`.

# Examples

```jldoctest
julia> write("my_file.txt", "JuliaLang is a GitHub organization.\nIt has many members.\n");

julia> readchomp("my_file.txt")
"JuliaLang is a GitHub organization.\nIt has many members."

julia> rm("my_file.txt");
```



readdir:
==================================================

```
readdir(dir::AbstractString=pwd();
    join::Bool = false,
    sort::Bool = true,
) -> Vector{String}
```

Return the names in the directory `dir` or the current working directory if not given. When `join` is false, `readdir` returns just the names in the directory as is; when `join` is true, it returns `joinpath(dir, name)` for each `name` so that the returned strings are full paths. If you want to get absolute paths back, call `readdir` with an absolute directory path and `join` set to true.

By default, `readdir` sorts the list of names it returns. If you want to skip sorting the names and get them in the order that the file system lists them, you can use `readdir(dir, sort=false)` to opt out of sorting.

See also: [`walkdir`](@ref).

!!! compat "Julia 1.4"
    The `join` and `sort` keyword arguments require at least Julia 1.4.


# Examples

```julia-repl
julia> cd("/home/JuliaUser/dev/julia")

julia> readdir()
30-element Array{String,1}:
 ".appveyor.yml"
 ".git"
 ".gitattributes"
 ⋮
 "ui"
 "usr"
 "usr-staging"

julia> readdir(join=true)
30-element Array{String,1}:
 "/home/JuliaUser/dev/julia/.appveyor.yml"
 "/home/JuliaUser/dev/julia/.git"
 "/home/JuliaUser/dev/julia/.gitattributes"
 ⋮
 "/home/JuliaUser/dev/julia/ui"
 "/home/JuliaUser/dev/julia/usr"
 "/home/JuliaUser/dev/julia/usr-staging"

julia> readdir("base")
145-element Array{String,1}:
 ".gitignore"
 "Base.jl"
 "Enums.jl"
 ⋮
 "version_git.sh"
 "views.jl"
 "weakkeydict.jl"

julia> readdir("base", join=true)
145-element Array{String,1}:
 "base/.gitignore"
 "base/Base.jl"
 "base/Enums.jl"
 ⋮
 "base/version_git.sh"
 "base/views.jl"
 "base/weakkeydict.jl"

julia> readdir(abspath("base"), join=true)
145-element Array{String,1}:
 "/home/JuliaUser/dev/julia/base/.gitignore"
 "/home/JuliaUser/dev/julia/base/Base.jl"
 "/home/JuliaUser/dev/julia/base/Enums.jl"
 ⋮
 "/home/JuliaUser/dev/julia/base/version_git.sh"
 "/home/JuliaUser/dev/julia/base/views.jl"
 "/home/JuliaUser/dev/julia/base/weakkeydict.jl"
```



readeach:
==================================================

```
readeach(io::IO, T)
```

Return an iterable object yielding [`read(io, T)`](@ref).

See also [`skipchars`](@ref), [`eachline`](@ref), [`readuntil`](@ref).

!!! compat "Julia 1.6"
    `readeach` requires Julia 1.6 or later.


# Examples

```jldoctest
julia> io = IOBuffer("JuliaLang is a GitHub organization.\n It has many members.\n");

julia> for c in readeach(io, Char)
           c == '\n' && break
           print(c)
       end
JuliaLang is a GitHub organization.
```



readline:
==================================================

```
readline(io::IO=stdin; keep::Bool=false)
readline(filename::AbstractString; keep::Bool=false)
```

Read a single line of text from the given I/O stream or file (defaults to `stdin`). When reading from a file, the text is assumed to be encoded in UTF-8. Lines in the input end with `'\n'` or `"\r\n"` or the end of an input stream. When `keep` is false (as it is by default), these trailing newline characters are removed from the line before it is returned. When `keep` is true, they are returned as part of the line.

Return a `String`.   See also [`copyline`](@ref) to instead write in-place to another stream (which can be a preallocated [`IOBuffer`](@ref)).

See also [`readuntil`](@ref) for reading until more general delimiters.

# Examples

```jldoctest
julia> write("my_file.txt", "JuliaLang is a GitHub organization.\nIt has many members.\n");

julia> readline("my_file.txt")
"JuliaLang is a GitHub organization."

julia> readline("my_file.txt", keep=true)
"JuliaLang is a GitHub organization.\n"

julia> rm("my_file.txt")
```

```julia-repl
julia> print("Enter your name: ")
Enter your name:

julia> your_name = readline()
Logan
"Logan"
```



readlines:
==================================================

```
readlines(io::IO=stdin; keep::Bool=false)
readlines(filename::AbstractString; keep::Bool=false)
```

Read all lines of an I/O stream or a file as a vector of strings. Behavior is equivalent to saving the result of reading [`readline`](@ref) repeatedly with the same arguments and saving the resulting lines as a vector of strings.  See also [`eachline`](@ref) to iterate over the lines without reading them all at once.

# Examples

```jldoctest
julia> write("my_file.txt", "JuliaLang is a GitHub organization.\nIt has many members.\n");

julia> readlines("my_file.txt")
2-element Vector{String}:
 "JuliaLang is a GitHub organization."
 "It has many members."

julia> readlines("my_file.txt", keep=true)
2-element Vector{String}:
 "JuliaLang is a GitHub organization.\n"
 "It has many members.\n"

julia> rm("my_file.txt")
```



readlink:
==================================================

```
readlink(path::AbstractString) -> String
```

Return the target location a symbolic link `path` points to.



readuntil:
==================================================

```
readuntil(stream::IO, delim; keep::Bool = false)
readuntil(filename::AbstractString, delim; keep::Bool = false)
```

Read a string from an I/O `stream` or a file, up to the given delimiter. The delimiter can be a `UInt8`, `AbstractChar`, string, or vector. Keyword argument `keep` controls whether the delimiter is included in the result. The text is assumed to be encoded in UTF-8.

Return a `String` if `delim` is an `AbstractChar` or a string or otherwise return a `Vector{typeof(delim)}`.   See also [`copyuntil`](@ref) to instead write in-place to another stream (which can be a preallocated [`IOBuffer`](@ref)).

# Examples

```jldoctest
julia> write("my_file.txt", "JuliaLang is a GitHub organization.\nIt has many members.\n");

julia> readuntil("my_file.txt", 'L')
"Julia"

julia> readuntil("my_file.txt", '.', keep = true)
"JuliaLang is a GitHub organization."

julia> rm("my_file.txt")
```



real:
==================================================

```
real(z)
```

Return the real part of the complex number `z`.

See also: [`imag`](@ref), [`reim`](@ref), [`complex`](@ref), [`isreal`](@ref), [`Real`](@ref).

# Examples

```jldoctest
julia> real(1 + 3im)
1
```

```
real(T::Type)
```

Return the type that represents the real part of a value of type `T`. e.g: for `T == Complex{R}`, returns `R`. Equivalent to `typeof(real(zero(T)))`.

# Examples

```jldoctest
julia> real(Complex{Int})
Int64

julia> real(Float64)
Float64
```

```
real(A::AbstractArray)
```

Return an array containing the real part of each entry in array `A`.

Equivalent to `real.(A)`, except that when `eltype(A) <: Real` `A` is returned without copying, and that when `A` has zero dimensions, a 0-dimensional array is returned (rather than a scalar).

# Examples

```jldoctest
julia> real([1, 2im, 3 + 4im])
3-element Vector{Int64}:
 1
 0
 3

julia> real(fill(2 - im))
0-dimensional Array{Int64, 0}:
2
```



realpath:
==================================================

```
realpath(path::AbstractString) -> String
```

Canonicalize a path by expanding symbolic links and removing "." and ".." entries. On case-insensitive case-preserving filesystems (typically Mac and Windows), the filesystem's stored case for the path is returned.

(This function throws an exception if `path` does not exist in the filesystem.)



redirect_stderr:
==================================================

```
Any::DataType
```

`Any` is the union of all types. It has the defining property `isa(x, Any) == true` for any `x`. `Any` therefore describes the entire universe of possible values. For example `Integer` is a subset of `Any` that includes `Int`, `Int8`, and other integer types.



redirect_stdin:
==================================================

```
Any::DataType
```

`Any` is the union of all types. It has the defining property `isa(x, Any) == true` for any `x`. `Any` therefore describes the entire universe of possible values. For example `Integer` is a subset of `Any` that includes `Int`, `Int8`, and other integer types.



redirect_stdio:
==================================================

```
redirect_stdio(;stdin=stdin, stderr=stderr, stdout=stdout)
```

Redirect a subset of the streams `stdin`, `stderr`, `stdout`. Each argument must be an `IOStream`, `TTY`, [`Pipe`](@ref), socket, or `devnull`.

!!! compat "Julia 1.7"
    `redirect_stdio` requires Julia 1.7 or later.


```
redirect_stdio(f; stdin=nothing, stderr=nothing, stdout=nothing)
```

Redirect a subset of the streams `stdin`, `stderr`, `stdout`, call `f()` and restore each stream.

Possible values for each stream are:

  * `nothing` indicating the stream should not be redirected.
  * `path::AbstractString` redirecting the stream to the file at `path`.
  * `io` an `IOStream`, `TTY`, [`Pipe`](@ref), socket, or `devnull`.

# Examples

```julia-repl
julia> redirect_stdio(stdout="stdout.txt", stderr="stderr.txt") do
           print("hello stdout")
           print(stderr, "hello stderr")
       end

julia> read("stdout.txt", String)
"hello stdout"

julia> read("stderr.txt", String)
"hello stderr"
```

# Edge cases

It is possible to pass the same argument to `stdout` and `stderr`:

```julia-repl
julia> redirect_stdio(stdout="log.txt", stderr="log.txt", stdin=devnull) do
    ...
end
```

However it is not supported to pass two distinct descriptors of the same file.

```julia-repl
julia> io1 = open("same/path", "w")

julia> io2 = open("same/path", "w")

julia> redirect_stdio(f, stdout=io1, stderr=io2) # not supported
```

Also the `stdin` argument may not be the same descriptor as `stdout` or `stderr`.

```julia-repl
julia> io = open(...)

julia> redirect_stdio(f, stdout=io, stdin=io) # not supported
```

!!! compat "Julia 1.7"
    `redirect_stdio` requires Julia 1.7 or later.




redirect_stdout:
==================================================

```
Any::DataType
```

`Any` is the union of all types. It has the defining property `isa(x, Any) == true` for any `x`. `Any` therefore describes the entire universe of possible values. For example `Integer` is a subset of `Any` that includes `Int`, `Int8`, and other integer types.



redisplay:
==================================================

```
redisplay(x)
redisplay(d::AbstractDisplay, x)
redisplay(mime, x)
redisplay(d::AbstractDisplay, mime, x)
```

By default, the `redisplay` functions simply call [`display`](@ref). However, some display backends may override `redisplay` to modify an existing display of `x` (if any). Using `redisplay` is also a hint to the backend that `x` may be redisplayed several times, and the backend may choose to defer the display until (for example) the next interactive prompt.



reduce:
==================================================

```
reduce(op, itr; [init])
```

Reduce the given collection `itr` with the given binary operator `op`. If provided, the initial value `init` must be a neutral element for `op` that will be returned for empty collections. It is unspecified whether `init` is used for non-empty collections.

For empty collections, providing `init` will be necessary, except for some special cases (e.g. when `op` is one of `+`, `*`, `max`, `min`, `&`, `|`) when Julia can determine the neutral element of `op`.

Reductions for certain commonly-used operators may have special implementations, and should be used instead: [`maximum`](@ref)`(itr)`, [`minimum`](@ref)`(itr)`, [`sum`](@ref)`(itr)`, [`prod`](@ref)`(itr)`, [`any`](@ref)`(itr)`, [`all`](@ref)`(itr)`. There are efficient methods for concatenating certain arrays of arrays by calling `reduce(`[`vcat`](@ref)`, arr)` or `reduce(`[`hcat`](@ref)`, arr)`.

The associativity of the reduction is implementation dependent. This means that you can't use non-associative operations like `-` because it is undefined whether `reduce(-,[1,2,3])` should be evaluated as `(1-2)-3` or `1-(2-3)`. Use [`foldl`](@ref) or [`foldr`](@ref) instead for guaranteed left or right associativity.

Some operations accumulate error. Parallelism will be easier if the reduction can be executed in groups. Future versions of Julia might change the algorithm. Note that the elements are not reordered if you use an ordered collection.

# Examples

```jldoctest
julia> reduce(*, [2; 3; 4])
24

julia> reduce(*, [2; 3; 4]; init=-1)
-24
```

```
reduce(f, A::AbstractArray; dims=:, [init])
```

Reduce 2-argument function `f` along dimensions of `A`. `dims` is a vector specifying the dimensions to reduce, and the keyword argument `init` is the initial value to use in the reductions. For `+`, `*`, `max` and `min` the `init` argument is optional.

The associativity of the reduction is implementation-dependent; if you need a particular associativity, e.g. left-to-right, you should write your own loop or consider using [`foldl`](@ref) or [`foldr`](@ref). See documentation for [`reduce`](@ref).

# Examples

```jldoctest
julia> a = reshape(Vector(1:16), (4,4))
4×4 Matrix{Int64}:
 1  5   9  13
 2  6  10  14
 3  7  11  15
 4  8  12  16

julia> reduce(max, a, dims=2)
4×1 Matrix{Int64}:
 13
 14
 15
 16

julia> reduce(max, a, dims=1)
1×4 Matrix{Int64}:
 4  8  12  16
```



reenable_sigint:
==================================================

```
reenable_sigint(f::Function)
```

Re-enable Ctrl-C handler during execution of a function. Temporarily reverses the effect of [`disable_sigint`](@ref).



reim:
==================================================

```
reim(z)
```

Return a tuple of the real and imaginary parts of the complex number `z`.

# Examples

```jldoctest
julia> reim(1 + 3im)
(1, 3)
```

```
reim(A::AbstractArray)
```

Return a tuple of two arrays containing respectively the real and the imaginary part of each entry in `A`.

Equivalent to `(real.(A), imag.(A))`, except that when `eltype(A) <: Real` `A` is returned without copying to represent the real part, and that when `A` has zero dimensions, a 0-dimensional array is returned (rather than a scalar).

# Examples

```jldoctest
julia> reim([1, 2im, 3 + 4im])
([1, 0, 3], [0, 2, 4])

julia> reim(fill(2 - im))
(fill(2), fill(-1))
```



reinterpret:
==================================================

```
reinterpret(::Type{Out}, x::In)
```

Change the type-interpretation of the binary data in the isbits value `x` to that of the isbits type `Out`. The size (ignoring padding) of `Out` has to be the same as that of the type of `x`. For example, `reinterpret(Float32, UInt32(7))` interprets the 4 bytes corresponding to `UInt32(7)` as a [`Float32`](@ref). Note that `reinterpret(In, reinterpret(Out, x)) === x`

```jldoctest
julia> reinterpret(Float32, UInt32(7))
1.0f-44

julia> reinterpret(NTuple{2, UInt8}, 0x1234)
(0x34, 0x12)

julia> reinterpret(UInt16, (0x34, 0x12))
0x1234

julia> reinterpret(Tuple{UInt16, UInt8}, (0x01, 0x0203))
(0x0301, 0x02)
```

!!! note
    The treatment of padding differs from reinterpret(::DataType, ::AbstractArray).


!!! warning
    Use caution if some combinations of bits in `Out` are not considered valid and would otherwise be prevented by the type's constructors and methods. Unexpected behavior may result without additional validation.


```
reinterpret(T::DataType, A::AbstractArray)
```

Construct a view of the array with the same binary data as the given array, but with `T` as element type.

This function also works on "lazy" array whose elements are not computed until they are explicitly retrieved. For instance, `reinterpret` on the range `1:6` works similarly as on the dense vector `collect(1:6)`:

```jldoctest
julia> reinterpret(Float32, UInt32[1 2 3 4 5])
1×5 reinterpret(Float32, ::Matrix{UInt32}):
 1.0f-45  3.0f-45  4.0f-45  6.0f-45  7.0f-45

julia> reinterpret(Complex{Int}, 1:6)
3-element reinterpret(Complex{Int64}, ::UnitRange{Int64}):
 1 + 2im
 3 + 4im
 5 + 6im
```

If the location of padding bits does not line up between `T` and `eltype(A)`, the resulting array will be read-only or write-only, to prevent invalid bits from being written to or read from, respectively.

```jldoctest
julia> a = reinterpret(Tuple{UInt8, UInt32}, UInt32[1, 2])
1-element reinterpret(Tuple{UInt8, UInt32}, ::Vector{UInt32}):
 (0x01, 0x00000002)

julia> a[1] = 3
ERROR: Padding of type Tuple{UInt8, UInt32} is not compatible with type UInt32.

julia> b = reinterpret(UInt32, Tuple{UInt8, UInt32}[(0x01, 0x00000002)]); # showing will error

julia> b[1]
ERROR: Padding of type UInt32 is not compatible with type Tuple{UInt8, UInt32}.
```

```
reinterpret(reshape, T, A::AbstractArray{S}) -> B
```

Change the type-interpretation of `A` while consuming or adding a "channel dimension."

If `sizeof(T) = n*sizeof(S)` for `n>1`, `A`'s first dimension must be of size `n` and `B` lacks `A`'s first dimension. Conversely, if `sizeof(S) = n*sizeof(T)` for `n>1`, `B` gets a new first dimension of size `n`. The dimensionality is unchanged if `sizeof(T) == sizeof(S)`.

!!! compat "Julia 1.6"
    This method requires at least Julia 1.6.


# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> reinterpret(reshape, Complex{Int}, A)    # the result is a vector
2-element reinterpret(reshape, Complex{Int64}, ::Matrix{Int64}) with eltype Complex{Int64}:
 1 + 3im
 2 + 4im

julia> a = [(1,2,3), (4,5,6)]
2-element Vector{Tuple{Int64, Int64, Int64}}:
 (1, 2, 3)
 (4, 5, 6)

julia> reinterpret(reshape, Int, a)             # the result is a matrix
3×2 reinterpret(reshape, Int64, ::Vector{Tuple{Int64, Int64, Int64}}) with eltype Int64:
 1  4
 2  5
 3  6
```



relpath:
==================================================

```
relpath(path::AbstractString, startpath::AbstractString = ".") -> String
```

Return a relative filepath to `path` either from the current directory or from an optional start directory. This is a path computation: the filesystem is not accessed to confirm the existence or nature of `path` or `startpath`.

On Windows, case sensitivity is applied to every part of the path except drive letters. If `path` and `startpath` refer to different drives, the absolute path of `path` is returned.



rem:
==================================================

```
rem(x::Integer, T::Type{<:Integer}) -> T
mod(x::Integer, T::Type{<:Integer}) -> T
%(x::Integer, T::Type{<:Integer}) -> T
```

Find `y::T` such that `x` ≡ `y` (mod n), where n is the number of integers representable in `T`, and `y` is an integer in `[typemin(T),typemax(T)]`. If `T` can represent any integer (e.g. `T == BigInt`), then this operation corresponds to a conversion to `T`.

# Examples

```jldoctest
julia> x = 129 % Int8
-127

julia> typeof(x)
Int8

julia> x = 129 % BigInt
129

julia> typeof(x)
BigInt
```

```
rem(x, y)
%(x, y)
```

Remainder from Euclidean division, returning a value of the same sign as `x`, and smaller in magnitude than `y`. This value is always exact.

See also: [`div`](@ref), [`mod`](@ref), [`mod1`](@ref), [`divrem`](@ref).

# Examples

```jldoctest
julia> x = 15; y = 4;

julia> x % y
3

julia> x == div(x, y) * y + rem(x, y)
true

julia> rem.(-5:5, 3)'
1×11 adjoint(::Vector{Int64}) with eltype Int64:
 -2  -1  0  -2  -1  0  1  2  0  1  2
```

```
rem(x, y, r::RoundingMode=RoundToZero)
```

Compute the remainder of `x` after integer division by `y`, with the quotient rounded according to the rounding mode `r`. In other words, the quantity

```
x - y * round(x / y, r)
```

without any intermediate rounding.

  * if `r == RoundNearest`, then the result is exact, and in the interval $[-|y| / 2, |y| / 2]$. See also [`RoundNearest`](@ref).
  * if `r == RoundToZero` (default), then the result is exact, and in the interval $[0, |y|)$ if `x` is positive, or $(-|y|, 0]$ otherwise. See also [`RoundToZero`](@ref).
  * if `r == RoundDown`, then the result is in the interval $[0, y)$ if `y` is positive, or $(y, 0]$ otherwise. The result may not be exact if `x` and `y` have different signs, and `abs(x) < abs(y)`. See also [`RoundDown`](@ref).
  * if `r == RoundUp`, then the result is in the interval $(-y, 0]$ if `y` is positive, or $[0, -y)$ otherwise. The result may not be exact if `x` and `y` have the same sign, and `abs(x) < abs(y)`. See also [`RoundUp`](@ref).
  * if `r == RoundFromZero`, then the result is in the interval $(-y, 0]$ if `y` is positive, or $[0, -y)$ otherwise. The result may not be exact if `x` and `y` have the same sign, and `abs(x) < abs(y)`. See also [`RoundFromZero`](@ref).

!!! compat "Julia 1.9"
    `RoundFromZero` requires at least Julia 1.9.


# Examples:

```jldoctest
julia> x = 9; y = 4;

julia> x % y  # same as rem(x, y)
1

julia> x ÷ y  # same as div(x, y)
2

julia> x == div(x, y) * y + rem(x, y)
true
```



rem2pi:
==================================================

```
rem2pi(x, r::RoundingMode)
```

Compute the remainder of `x` after integer division by `2π`, with the quotient rounded according to the rounding mode `r`. In other words, the quantity

```
x - 2π*round(x/(2π),r)
```

without any intermediate rounding. This internally uses a high precision approximation of 2π, and so will give a more accurate result than `rem(x,2π,r)`

  * if `r == RoundNearest`, then the result is in the interval $[-π, π]$. This will generally be the most accurate result. See also [`RoundNearest`](@ref).
  * if `r == RoundToZero`, then the result is in the interval $[0, 2π]$ if `x` is positive,. or $[-2π, 0]$ otherwise. See also [`RoundToZero`](@ref).
  * if `r == RoundDown`, then the result is in the interval $[0, 2π]$. See also [`RoundDown`](@ref).
  * if `r == RoundUp`, then the result is in the interval $[-2π, 0]$. See also [`RoundUp`](@ref).

# Examples

```jldoctest
julia> rem2pi(7pi/4, RoundNearest)
-0.7853981633974485

julia> rem2pi(7pi/4, RoundDown)
5.497787143782138
```



repeat:
==================================================

```
repeat(A::AbstractArray, counts::Integer...)
```

Construct an array by repeating array `A` a given number of times in each dimension, specified by `counts`.

See also: [`fill`](@ref), [`Iterators.repeated`](@ref), [`Iterators.cycle`](@ref).

# Examples

```jldoctest
julia> repeat([1, 2, 3], 2)
6-element Vector{Int64}:
 1
 2
 3
 1
 2
 3

julia> repeat([1, 2, 3], 2, 3)
6×3 Matrix{Int64}:
 1  1  1
 2  2  2
 3  3  3
 1  1  1
 2  2  2
 3  3  3
```

```
repeat(A::AbstractArray; inner=ntuple(Returns(1), ndims(A)), outer=ntuple(Returns(1), ndims(A)))
```

Construct an array by repeating the entries of `A`. The i-th element of `inner` specifies the number of times that the individual entries of the i-th dimension of `A` should be repeated. The i-th element of `outer` specifies the number of times that a slice along the i-th dimension of `A` should be repeated. If `inner` or `outer` are omitted, no repetition is performed.

# Examples

```jldoctest
julia> repeat(1:2, inner=2)
4-element Vector{Int64}:
 1
 1
 2
 2

julia> repeat(1:2, outer=2)
4-element Vector{Int64}:
 1
 2
 1
 2

julia> repeat([1 2; 3 4], inner=(2, 1), outer=(1, 3))
4×6 Matrix{Int64}:
 1  2  1  2  1  2
 1  2  1  2  1  2
 3  4  3  4  3  4
 3  4  3  4  3  4
```

```
repeat(s::AbstractString, r::Integer)
```

Repeat a string `r` times. This can be written as `s^r`.

See also [`^`](@ref :^(::Union{AbstractString, AbstractChar}, ::Integer)).

# Examples

```jldoctest
julia> repeat("ha", 3)
"hahaha"
```

```
repeat(c::AbstractChar, r::Integer) -> String
```

Repeat a character `r` times. This can equivalently be accomplished by calling [`c^r`](@ref :^(::Union{AbstractString, AbstractChar}, ::Integer)).

# Examples

```jldoctest
julia> repeat('A', 3)
"AAA"
```



replace:
==================================================

```
replace(A, old_new::Pair...; [count::Integer])
```

Return a copy of collection `A` where, for each pair `old=>new` in `old_new`, all occurrences of `old` are replaced by `new`. Equality is determined using [`isequal`](@ref). If `count` is specified, then replace at most `count` occurrences in total.

The element type of the result is chosen using promotion (see [`promote_type`](@ref)) based on the element type of `A` and on the types of the `new` values in pairs. If `count` is omitted and the element type of `A` is a `Union`, the element type of the result will not include singleton types which are replaced with values of a different type: for example, `Union{T,Missing}` will become `T` if `missing` is replaced.

See also [`replace!`](@ref), [`splice!`](@ref), [`delete!`](@ref), [`insert!`](@ref).

!!! compat "Julia 1.7"
    Version 1.7 is required to replace elements of a `Tuple`.


# Examples

```jldoctest
julia> replace([1, 2, 1, 3], 1=>0, 2=>4, count=2)
4-element Vector{Int64}:
 0
 4
 1
 3

julia> replace([1, missing], missing=>0)
2-element Vector{Int64}:
 1
 0
```

```
replace(new::Union{Function, Type}, A; [count::Integer])
```

Return a copy of `A` where each value `x` in `A` is replaced by `new(x)`. If `count` is specified, then replace at most `count` values in total (replacements being defined as `new(x) !== x`).

!!! compat "Julia 1.7"
    Version 1.7 is required to replace elements of a `Tuple`.


# Examples

```jldoctest
julia> replace(x -> isodd(x) ? 2x : x, [1, 2, 3, 4])
4-element Vector{Int64}:
 2
 2
 6
 4

julia> replace(Dict(1=>2, 3=>4)) do kv
           first(kv) < 3 ? first(kv)=>3 : kv
       end
Dict{Int64, Int64} with 2 entries:
  3 => 4
  1 => 3
```

```
replace([io::IO], s::AbstractString, pat=>r, [pat2=>r2, ...]; [count::Integer])
```

Search for the given pattern `pat` in `s`, and replace each occurrence with `r`. If `count` is provided, replace at most `count` occurrences. `pat` may be a single character, a vector or a set of characters, a string, or a regular expression. If `r` is a function, each occurrence is replaced with `r(s)` where `s` is the matched substring (when `pat` is a `AbstractPattern` or `AbstractString`) or character (when `pat` is an `AbstractChar` or a collection of `AbstractChar`). If `pat` is a regular expression and `r` is a [`SubstitutionString`](@ref), then capture group references in `r` are replaced with the corresponding matched text. To remove instances of `pat` from `string`, set `r` to the empty `String` (`""`).

The return value is a new string after the replacements.  If the `io::IO` argument is supplied, the transformed string is instead written to `io` (returning `io`). (For example, this can be used in conjunction with an [`IOBuffer`](@ref) to re-use a pre-allocated buffer array in-place.)

Multiple patterns can be specified, and they will be applied left-to-right simultaneously, so only one pattern will be applied to any character, and the patterns will only be applied to the input text, not the replacements.

!!! compat "Julia 1.7"
    Support for multiple patterns requires version 1.7.


!!! compat "Julia 1.10"
    The `io::IO` argument requires version 1.10.


# Examples

```jldoctest
julia> replace("Python is a programming language.", "Python" => "Julia")
"Julia is a programming language."

julia> replace("The quick foxes run quickly.", "quick" => "slow", count=1)
"The slow foxes run quickly."

julia> replace("The quick foxes run quickly.", "quick" => "", count=1)
"The  foxes run quickly."

julia> replace("The quick foxes run quickly.", r"fox(es)?" => s"bus\1")
"The quick buses run quickly."

julia> replace("abcabc", "a" => "b", "b" => "c", r".+" => "a")
"bca"
```



replace!:
==================================================

```
replace!(A, old_new::Pair...; [count::Integer])
```

For each pair `old=>new` in `old_new`, replace all occurrences of `old` in collection `A` by `new`. Equality is determined using [`isequal`](@ref). If `count` is specified, then replace at most `count` occurrences in total. See also [`replace`](@ref replace(A, old_new::Pair...)).

# Examples

```jldoctest
julia> replace!([1, 2, 1, 3], 1=>0, 2=>4, count=2)
4-element Vector{Int64}:
 0
 4
 1
 3

julia> replace!(Set([1, 2, 3]), 1=>0)
Set{Int64} with 3 elements:
  0
  2
  3
```

```
replace!(new::Union{Function, Type}, A; [count::Integer])
```

Replace each element `x` in collection `A` by `new(x)`. If `count` is specified, then replace at most `count` values in total (replacements being defined as `new(x) !== x`).

# Examples

```jldoctest
julia> replace!(x -> isodd(x) ? 2x : x, [1, 2, 3, 4])
4-element Vector{Int64}:
 2
 2
 6
 4

julia> replace!(Dict(1=>2, 3=>4)) do kv
           first(kv) < 3 ? first(kv)=>3 : kv
       end
Dict{Int64, Int64} with 2 entries:
  3 => 4
  1 => 3

julia> replace!(x->2x, Set([3, 6]))
Set{Int64} with 2 elements:
  6
  12
```



replacefield!:
==================================================

```
replacefield!(value, name::Symbol, expected, desired,
              [success_order::Symbol, [fail_order::Symbol=success_order]) -> (; old, success::Bool)
replacefield!(value, i::Int, expected, desired,
              [success_order::Symbol, [fail_order::Symbol=success_order]) -> (; old, success::Bool)
```

Atomically perform the operations to get and conditionally set a field to a given value.

```
y = getfield(value, name, fail_order)
ok = y === expected
if ok
    setfield!(value, name, desired, success_order)
end
return (; old = y, success = ok)
```

If supported by the hardware, this may be optimized to the appropriate hardware instruction, otherwise it'll use a loop.

!!! compat "Julia 1.7"
    This function requires Julia 1.7 or later.




replaceglobal!:
==================================================

```
replaceglobal!(module::Module, name::Symbol, expected, desired,
              [success_order::Symbol, [fail_order::Symbol=success_order]) -> (; old, success::Bool)
```

Atomically perform the operations to get and conditionally set a global to a given value.

!!! compat "Julia 1.11"
    This function requires Julia 1.11 or later.


See also [`replaceproperty!`](@ref Base.replaceproperty!) and [`setglobal!`](@ref).



replaceproperty!:
==================================================

```
replaceproperty!(x, f::Symbol, expected, desired, success_order::Symbol=:not_atomic, fail_order::Symbol=success_order)
```

Perform a compare-and-swap operation on `x.f` from `expected` to `desired`, per egal. The syntax `@atomicreplace x.f expected => desired` can be used instead of the function call form.

See also [`replacefield!`](@ref Core.replacefield!) [`setproperty!`](@ref Base.setproperty!), [`setpropertyonce!`](@ref Base.setpropertyonce!).



repr:
==================================================

```
repr(x; context=nothing)
```

Create a string from any value using the [`show`](@ref) function. You should not add methods to `repr`; define a `show` method instead.

The optional keyword argument `context` can be set to a `:key=>value` pair, a tuple of `:key=>value` pairs, or an `IO` or [`IOContext`](@ref) object whose attributes are used for the I/O stream passed to `show`.

Note that `repr(x)` is usually similar to how the value of `x` would be entered in Julia.  See also [`repr(MIME("text/plain"), x)`](@ref) to instead return a "pretty-printed" version of `x` designed more for human consumption, equivalent to the REPL display of `x`.

!!! compat "Julia 1.7"
    Passing a tuple to keyword `context` requires Julia 1.7 or later.


# Examples

```jldoctest
julia> repr(1)
"1"

julia> repr(zeros(3))
"[0.0, 0.0, 0.0]"

julia> repr(big(1/3))
"0.333333333333333314829616256247390992939472198486328125"

julia> repr(big(1/3), context=:compact => true)
"0.333333"

```

```
repr(mime, x; context=nothing)
```

Return an `AbstractString` or `Vector{UInt8}` containing the representation of `x` in the requested `mime` type, as written by [`show(io, mime, x)`](@ref) (throwing a [`MethodError`](@ref) if no appropriate `show` is available). An `AbstractString` is returned for MIME types with textual representations (such as `"text/html"` or `"application/postscript"`), whereas binary data is returned as `Vector{UInt8}`. (The function `istextmime(mime)` returns whether or not Julia treats a given `mime` type as text.)

The optional keyword argument `context` can be set to `:key=>value` pair or an `IO` or [`IOContext`](@ref) object whose attributes are used for the I/O stream passed to `show`.

As a special case, if `x` is an `AbstractString` (for textual MIME types) or a `Vector{UInt8}` (for binary MIME types), the `repr` function assumes that `x` is already in the requested `mime` format and simply returns `x`. This special case does not apply to the `"text/plain"` MIME type. This is useful so that raw data can be passed to `display(m::MIME, x)`.

In particular, `repr("text/plain", x)` is typically a "pretty-printed" version of `x` designed for human consumption.  See also [`repr(x)`](@ref) to instead return a string corresponding to [`show(x)`](@ref) that may be closer to how the value of `x` would be entered in Julia.

# Examples

```jldoctest
julia> A = [1 2; 3 4];

julia> repr("text/plain", A)
"2×2 Matrix{Int64}:\n 1  2\n 3  4"
```



reset:
==================================================

```
reset(s::IO)
```

Reset a stream `s` to a previously marked position, and remove the mark. Return the previously marked position. Throw an error if the stream is not marked.

See also [`mark`](@ref), [`unmark`](@ref), [`ismarked`](@ref).

```
reset(::Event)
```

Reset an [`Event`](@ref) back into an un-set state. Then any future calls to `wait` will block until [`notify`](@ref) is called again.



reshape:
==================================================

```
reshape(A, dims...) -> AbstractArray
reshape(A, dims) -> AbstractArray
```

Return an array with the same data as `A`, but with different dimension sizes or number of dimensions. The two arrays share the same underlying data, so that the result is mutable if and only if `A` is mutable, and setting elements of one alters the values of the other.

The new dimensions may be specified either as a list of arguments or as a shape tuple. At most one dimension may be specified with a `:`, in which case its length is computed such that its product with all the specified dimensions is equal to the length of the original array `A`. The total number of elements must not change.

# Examples

```jldoctest
julia> A = Vector(1:16)
16-element Vector{Int64}:
  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16

julia> reshape(A, (4, 4))
4×4 Matrix{Int64}:
 1  5   9  13
 2  6  10  14
 3  7  11  15
 4  8  12  16

julia> reshape(A, 2, :)
2×8 Matrix{Int64}:
 1  3  5  7   9  11  13  15
 2  4  6  8  10  12  14  16

julia> reshape(1:6, 2, 3)
2×3 reshape(::UnitRange{Int64}, 2, 3) with eltype Int64:
 1  3  5
 2  4  6
```



resize!:
==================================================

```
resize!(a::Vector, n::Integer) -> Vector
```

Resize `a` to contain `n` elements. If `n` is smaller than the current collection length, the first `n` elements will be retained. If `n` is larger, the new elements are not guaranteed to be initialized.

# Examples

```jldoctest
julia> resize!([6, 5, 4, 3, 2, 1], 3)
3-element Vector{Int64}:
 6
 5
 4

julia> a = resize!([6, 5, 4, 3, 2, 1], 8);

julia> length(a)
8

julia> a[1:6]
6-element Vector{Int64}:
 6
 5
 4
 3
 2
 1
```



rethrow:
==================================================

```
rethrow()
```

Rethrow the current exception from within a `catch` block. The rethrown exception will continue propagation as if it had not been caught.

!!! note
    The alternative form `rethrow(e)` allows you to associate an alternative exception object `e` with the current backtrace. However this misrepresents the program state at the time of the error so you're encouraged to instead throw a new exception using `throw(e)`. In Julia 1.1 and above, using `throw(e)` will preserve the root cause exception on the stack, as described in [`current_exceptions`](@ref).




retry:
==================================================

```
retry(f;  delays=ExponentialBackOff(), check=nothing) -> Function
```

Return an anonymous function that calls function `f`.  If an exception arises, `f` is repeatedly called again, each time `check` returns `true`, after waiting the number of seconds specified in `delays`.  `check` should input `delays`'s current state and the `Exception`.

!!! compat "Julia 1.2"
    Before Julia 1.2 this signature was restricted to `f::Function`.


# Examples

```julia
retry(f, delays=fill(5.0, 3))
retry(f, delays=rand(5:10, 2))
retry(f, delays=Base.ExponentialBackOff(n=3, first_delay=5, max_delay=1000))
retry(http_get, check=(s,e)->e.status == "503")(url)
retry(read, check=(s,e)->isa(e, IOError))(io, 128; all=false)
```



reverse:
==================================================

```
reverse(v [, start=firstindex(v) [, stop=lastindex(v) ]] )
```

Return a copy of `v` reversed from start to stop.  See also [`Iterators.reverse`](@ref) for reverse-order iteration without making a copy, and in-place [`reverse!`](@ref).

# Examples

```jldoctest
julia> A = Vector(1:5)
5-element Vector{Int64}:
 1
 2
 3
 4
 5

julia> reverse(A)
5-element Vector{Int64}:
 5
 4
 3
 2
 1

julia> reverse(A, 1, 4)
5-element Vector{Int64}:
 4
 3
 2
 1
 5

julia> reverse(A, 3, 5)
5-element Vector{Int64}:
 1
 2
 5
 4
 3
```

```
reverse(A; dims=:)
```

Reverse `A` along dimension `dims`, which can be an integer (a single dimension), a tuple of integers (a tuple of dimensions) or `:` (reverse along all the dimensions, the default).  See also [`reverse!`](@ref) for in-place reversal.

# Examples

```jldoctest
julia> b = Int64[1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> reverse(b, dims=2)
2×2 Matrix{Int64}:
 2  1
 4  3

julia> reverse(b)
2×2 Matrix{Int64}:
 4  3
 2  1
```

!!! compat "Julia 1.6"
    Prior to Julia 1.6, only single-integer `dims` are supported in `reverse`.


```
reverse(s::AbstractString) -> AbstractString
```

Reverses a string. Technically, this function reverses the codepoints in a string and its main utility is for reversed-order string processing, especially for reversed regular-expression searches. See also [`reverseind`](@ref) to convert indices in `s` to indices in `reverse(s)` and vice-versa, and `graphemes` from module `Unicode` to operate on user-visible "characters" (graphemes) rather than codepoints. See also [`Iterators.reverse`](@ref) for reverse-order iteration without making a copy. Custom string types must implement the `reverse` function themselves and should typically return a string with the same type and encoding. If they return a string with a different encoding, they must also override `reverseind` for that string type to satisfy `s[reverseind(s,i)] == reverse(s)[i]`.

# Examples

```jldoctest
julia> reverse("JuliaLang")
"gnaLailuJ"
```

!!! note
    The examples below may be rendered differently on different systems. The comments indicate how they're supposed to be rendered


Combining characters can lead to surprising results:

```jldoctest
julia> reverse("ax̂e") # hat is above x in the input, above e in the output
"êxa"

julia> using Unicode

julia> join(reverse(collect(graphemes("ax̂e")))) # reverses graphemes; hat is above x in both in- and output
"ex̂a"
```

```
reverse(o::Base.Ordering)
```

reverses ordering specified by `o`.



reverse!:
==================================================

```
reverse!(v [, start=firstindex(v) [, stop=lastindex(v) ]]) -> v
```

In-place version of [`reverse`](@ref).

# Examples

```jldoctest
julia> A = Vector(1:5)
5-element Vector{Int64}:
 1
 2
 3
 4
 5

julia> reverse!(A);

julia> A
5-element Vector{Int64}:
 5
 4
 3
 2
 1
```

```
reverse!(A; dims=:)
```

Like [`reverse`](@ref), but operates in-place in `A`.

!!! compat "Julia 1.6"
    Multidimensional `reverse!` requires Julia 1.6.




reverseind:
==================================================

```
reverseind(v, i)
```

Given an index `i` in [`reverse(v)`](@ref), return the corresponding index in `v` so that `v[reverseind(v,i)] == reverse(v)[i]`. (This can be nontrivial in cases where `v` contains non-ASCII characters.)

# Examples

```jldoctest
julia> s = "Julia🚀"
"Julia🚀"

julia> r = reverse(s)
"🚀ailuJ"

julia> for i in eachindex(s)
           print(r[reverseind(r, i)])
       end
Julia🚀
```



rm:
==================================================

```
rm(path::AbstractString; force::Bool=false, recursive::Bool=false)
```

Delete the file, link, or empty directory at the given path. If `force=true` is passed, a non-existing path is not treated as error. If `recursive=true` is passed and the path is a directory, then all contents are removed recursively.

# Examples

```jldoctest
julia> mkpath("my/test/dir");

julia> rm("my", recursive=true)

julia> rm("this_file_does_not_exist", force=true)

julia> rm("this_file_does_not_exist")
ERROR: IOError: unlink("this_file_does_not_exist"): no such file or directory (ENOENT)
Stacktrace:
[...]
```



rot180:
==================================================

```
rot180(A)
```

Rotate matrix `A` 180 degrees.

# Examples

```jldoctest
julia> a = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> rot180(a)
2×2 Matrix{Int64}:
 4  3
 2  1
```

```
rot180(A, k)
```

Rotate matrix `A` 180 degrees an integer `k` number of times. If `k` is even, this is equivalent to a `copy`.

# Examples

```jldoctest
julia> a = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> rot180(a,1)
2×2 Matrix{Int64}:
 4  3
 2  1

julia> rot180(a,2)
2×2 Matrix{Int64}:
 1  2
 3  4
```



rotl90:
==================================================

```
rotl90(A)
```

Rotate matrix `A` left 90 degrees.

# Examples

```jldoctest
julia> a = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> rotl90(a)
2×2 Matrix{Int64}:
 2  4
 1  3
```

```
rotl90(A, k)
```

Left-rotate matrix `A` 90 degrees counterclockwise an integer `k` number of times. If `k` is a multiple of four (including zero), this is equivalent to a `copy`.

# Examples

```jldoctest
julia> a = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> rotl90(a,1)
2×2 Matrix{Int64}:
 2  4
 1  3

julia> rotl90(a,2)
2×2 Matrix{Int64}:
 4  3
 2  1

julia> rotl90(a,3)
2×2 Matrix{Int64}:
 3  1
 4  2

julia> rotl90(a,4)
2×2 Matrix{Int64}:
 1  2
 3  4
```



rotr90:
==================================================

```
rotr90(A)
```

Rotate matrix `A` right 90 degrees.

# Examples

```jldoctest
julia> a = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> rotr90(a)
2×2 Matrix{Int64}:
 3  1
 4  2
```

```
rotr90(A, k)
```

Right-rotate matrix `A` 90 degrees clockwise an integer `k` number of times. If `k` is a multiple of four (including zero), this is equivalent to a `copy`.

# Examples

```jldoctest
julia> a = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> rotr90(a,1)
2×2 Matrix{Int64}:
 3  1
 4  2

julia> rotr90(a,2)
2×2 Matrix{Int64}:
 4  3
 2  1

julia> rotr90(a,3)
2×2 Matrix{Int64}:
 2  4
 1  3

julia> rotr90(a,4)
2×2 Matrix{Int64}:
 1  2
 3  4
```



round:
==================================================

```
round([T,] x, [r::RoundingMode])
round(x, [r::RoundingMode]; digits::Integer=0, base = 10)
round(x, [r::RoundingMode]; sigdigits::Integer, base = 10)
```

Rounds the number `x`.

Without keyword arguments, `x` is rounded to an integer value, returning a value of type `T`, or of the same type of `x` if no `T` is provided. An [`InexactError`](@ref) will be thrown if the value is not representable by `T`, similar to [`convert`](@ref).

If the `digits` keyword argument is provided, it rounds to the specified number of digits after the decimal place (or before if negative), in base `base`.

If the `sigdigits` keyword argument is provided, it rounds to the specified number of significant digits, in base `base`.

The [`RoundingMode`](@ref) `r` controls the direction of the rounding; the default is [`RoundNearest`](@ref), which rounds to the nearest integer, with ties (fractional values of 0.5) being rounded to the nearest even integer. Note that `round` may give incorrect results if the global rounding mode is changed (see [`rounding`](@ref)).

When rounding to a floating point type, will round to integers representable by that type (and Inf) rather than true integers. Inf is treated as one ulp greater than the `floatmax(T)` for purposes of determining "nearest", similar to [`convert`](@ref).

# Examples

```jldoctest
julia> round(1.7)
2.0

julia> round(Int, 1.7)
2

julia> round(1.5)
2.0

julia> round(2.5)
2.0

julia> round(pi; digits=2)
3.14

julia> round(pi; digits=3, base=2)
3.125

julia> round(123.456; sigdigits=2)
120.0

julia> round(357.913; sigdigits=4, base=2)
352.0

julia> round(Float16, typemax(UInt128))
Inf16

julia> floor(Float16, typemax(UInt128))
Float16(6.55e4)
```

!!! note
    Rounding to specified digits in bases other than 2 can be inexact when operating on binary floating point numbers. For example, the [`Float64`](@ref) value represented by `1.15` is actually *less* than 1.15, yet will be rounded to 1.2. For example:

    ```jldoctest
    julia> x = 1.15
    1.15

    julia> big(1.15)
    1.149999999999999911182158029987476766109466552734375

    julia> x < 115//100
    true

    julia> round(x, digits=1)
    1.2
    ```


# Extensions

To extend `round` to new numeric types, it is typically sufficient to define `Base.round(x::NewType, r::RoundingMode)`.

```
round(z::Complex[, RoundingModeReal, [RoundingModeImaginary]])
round(z::Complex[, RoundingModeReal, [RoundingModeImaginary]]; digits=0, base=10)
round(z::Complex[, RoundingModeReal, [RoundingModeImaginary]]; sigdigits, base=10)
```

Return the nearest integral value of the same type as the complex-valued `z` to `z`, breaking ties using the specified [`RoundingMode`](@ref)s. The first [`RoundingMode`](@ref) is used for rounding the real components while the second is used for rounding the imaginary components.

`RoundingModeReal` and `RoundingModeImaginary` default to [`RoundNearest`](@ref), which rounds to the nearest integer, with ties (fractional values of 0.5) being rounded to the nearest even integer.

# Examples

```jldoctest
julia> round(3.14 + 4.5im)
3.0 + 4.0im

julia> round(3.14 + 4.5im, RoundUp, RoundNearestTiesUp)
4.0 + 5.0im

julia> round(3.14159 + 4.512im; digits = 1)
3.1 + 4.5im

julia> round(3.14159 + 4.512im; sigdigits = 3)
3.14 + 4.51im
```

```
round(dt::TimeType, p::Period, [r::RoundingMode]) -> TimeType
```

Return the `Date` or `DateTime` nearest to `dt` at resolution `p`. By default (`RoundNearestTiesUp`), ties (e.g., rounding 9:30 to the nearest hour) will be rounded up.

For convenience, `p` may be a type instead of a value: `round(dt, Dates.Hour)` is a shortcut for `round(dt, Dates.Hour(1))`.

```jldoctest
julia> round(Date(1985, 8, 16), Month)
1985-08-01

julia> round(DateTime(2013, 2, 13, 0, 31, 20), Minute(15))
2013-02-13T00:30:00

julia> round(DateTime(2016, 8, 6, 12, 0, 0), Day)
2016-08-07T00:00:00
```

Valid rounding modes for `round(::TimeType, ::Period, ::RoundingMode)` are `RoundNearestTiesUp` (default), `RoundDown` (`floor`), and `RoundUp` (`ceil`).

```
round(x::Period, precision::T, [r::RoundingMode]) where T <: Union{TimePeriod, Week, Day} -> T
```

Round `x` to the nearest multiple of `precision`. If `x` and `precision` are different subtypes of `Period`, the return value will have the same type as `precision`. By default (`RoundNearestTiesUp`), ties (e.g., rounding 90 minutes to the nearest hour) will be rounded up.

For convenience, `precision` may be a type instead of a value: `round(x, Dates.Hour)` is a shortcut for `round(x, Dates.Hour(1))`.

```jldoctest
julia> round(Day(16), Week)
2 weeks

julia> round(Minute(44), Minute(15))
45 minutes

julia> round(Hour(36), Day)
2 days
```

Valid rounding modes for `round(::Period, ::T, ::RoundingMode)` are `RoundNearestTiesUp` (default), `RoundDown` (`floor`), and `RoundUp` (`ceil`).

Rounding to a `precision` of `Month`s or `Year`s is not supported, as these `Period`s are of inconsistent length.



rounding:
==================================================

```
rounding(T)
```

Get the current floating point rounding mode for type `T`, controlling the rounding of basic arithmetic functions ([`+`](@ref), [`-`](@ref), [`*`](@ref), [`/`](@ref) and [`sqrt`](@ref)) and type conversion.

See [`RoundingMode`](@ref) for available modes.



rpad:
==================================================

```
rpad(s, n::Integer, p::Union{AbstractChar,AbstractString}=' ') -> String
```

Stringify `s` and pad the resulting string on the right with `p` to make it `n` characters (in [`textwidth`](@ref)) long. If `s` is already `n` characters long, an equal string is returned. Pad with spaces by default.

# Examples

```jldoctest
julia> rpad("March", 20)
"March               "
```

!!! compat "Julia 1.7"
    In Julia 1.7, this function was changed to use `textwidth` rather than a raw character (codepoint) count.




rsplit:
==================================================

```
rsplit(s::AbstractString; limit::Integer=0, keepempty::Bool=false)
rsplit(s::AbstractString, chars; limit::Integer=0, keepempty::Bool=true)
```

Similar to [`split`](@ref), but starting from the end of the string.

# Examples

```jldoctest
julia> a = "M.a.r.c.h"
"M.a.r.c.h"

julia> rsplit(a, ".")
5-element Vector{SubString{String}}:
 "M"
 "a"
 "r"
 "c"
 "h"

julia> rsplit(a, "."; limit=1)
1-element Vector{SubString{String}}:
 "M.a.r.c.h"

julia> rsplit(a, "."; limit=2)
2-element Vector{SubString{String}}:
 "M.a.r.c"
 "h"
```



rstrip:
==================================================

```
rstrip([pred=isspace,] str::AbstractString) -> SubString
rstrip(str::AbstractString, chars) -> SubString
```

Remove trailing characters from `str`, either those specified by `chars` or those for which the function `pred` returns `true`.

The default behaviour is to remove trailing whitespace and delimiters: see [`isspace`](@ref) for precise details.

The optional `chars` argument specifies which characters to remove: it can be a single character, or a vector or set of characters.

See also [`strip`](@ref) and [`lstrip`](@ref).

# Examples

```jldoctest
julia> a = rpad("March", 20)
"March               "

julia> rstrip(a)
"March"
```



run:
==================================================

```
run(command, args...; wait::Bool = true)
```

Run a command object, constructed with backticks (see the [Running External Programs](@ref) section in the manual). Throws an error if anything goes wrong, including the process exiting with a non-zero status (when `wait` is true).

The `args...` allow you to pass through file descriptors to the command, and are ordered like regular unix file descriptors (eg `stdin, stdout, stderr, FD(3), FD(4)...`).

If `wait` is false, the process runs asynchronously. You can later wait for it and check its exit status by calling `success` on the returned process object.

When `wait` is false, the process' I/O streams are directed to `devnull`. When `wait` is true, I/O streams are shared with the parent process. Use [`pipeline`](@ref) to control I/O redirection.



samefile:
==================================================

```
samefile(path_a::AbstractString, path_b::AbstractString)
```

Check if the paths `path_a` and `path_b` refer to the same existing file or directory.



schedule:
==================================================

```
schedule(t::Task, [val]; error=false)
```

Add a [`Task`](@ref) to the scheduler's queue. This causes the task to run constantly when the system is otherwise idle, unless the task performs a blocking operation such as [`wait`](@ref).

If a second argument `val` is provided, it will be passed to the task (via the return value of [`yieldto`](@ref)) when it runs again. If `error` is `true`, the value is raised as an exception in the woken task.

!!! warning
    It is incorrect to use `schedule` on an arbitrary `Task` that has already been started. See [the API reference](@ref low-level-schedule-wait) for more information.


!!! warning
    By default tasks will have the sticky bit set to true `t.sticky`. This models the historic default for [`@async`](@ref). Sticky tasks can only be run on the worker thread they are first scheduled on, and when scheduled will make the task that they were scheduled from sticky. To obtain the behavior of [`Threads.@spawn`](@ref) set the sticky bit manually to `false`.


# Examples

```jldoctest
julia> a5() = sum(i for i in 1:1000);

julia> b = Task(a5);

julia> istaskstarted(b)
false

julia> schedule(b);

julia> yield();

julia> istaskstarted(b)
true

julia> istaskdone(b)
true
```



searchsorted:
==================================================

```
searchsorted(v, x; by=identity, lt=isless, rev=false)
```

Return the range of indices in `v` where values are equivalent to `x`, or an empty range located at the insertion point if `v` does not contain values equivalent to `x`. The vector `v` must be sorted according to the order defined by the keywords. Refer to [`sort!`](@ref) for the meaning of the keywords and the definition of equivalence. Note that the `by` function is applied to the searched value `x` as well as the values in `v`.

The range is generally found using binary search, but there are optimized implementations for some inputs.

See also: [`searchsortedfirst`](@ref), [`sort!`](@ref), [`insorted`](@ref), [`findall`](@ref).

# Examples

```jldoctest
julia> searchsorted([1, 2, 4, 5, 5, 7], 4) # single match
3:3

julia> searchsorted([1, 2, 4, 5, 5, 7], 5) # multiple matches
4:5

julia> searchsorted([1, 2, 4, 5, 5, 7], 3) # no match, insert in the middle
3:2

julia> searchsorted([1, 2, 4, 5, 5, 7], 9) # no match, insert at end
7:6

julia> searchsorted([1, 2, 4, 5, 5, 7], 0) # no match, insert at start
1:0

julia> searchsorted([1=>"one", 2=>"two", 2=>"two", 4=>"four"], 2=>"two", by=first) # compare the keys of the pairs
2:3
```



searchsortedfirst:
==================================================

```
searchsortedfirst(v, x; by=identity, lt=isless, rev=false)
```

Return the index of the first value in `v` that is not ordered before `x`. If all values in `v` are ordered before `x`, return `lastindex(v) + 1`.

The vector `v` must be sorted according to the order defined by the keywords. `insert!`ing `x` at the returned index will maintain the sorted order. Refer to [`sort!`](@ref) for the meaning and use of the keywords. Note that the `by` function is applied to the searched value `x` as well as the values in `v`.

The index is generally found using binary search, but there are optimized implementations for some inputs.

See also: [`searchsortedlast`](@ref), [`searchsorted`](@ref), [`findfirst`](@ref).

# Examples

```jldoctest
julia> searchsortedfirst([1, 2, 4, 5, 5, 7], 4) # single match
3

julia> searchsortedfirst([1, 2, 4, 5, 5, 7], 5) # multiple matches
4

julia> searchsortedfirst([1, 2, 4, 5, 5, 7], 3) # no match, insert in the middle
3

julia> searchsortedfirst([1, 2, 4, 5, 5, 7], 9) # no match, insert at end
7

julia> searchsortedfirst([1, 2, 4, 5, 5, 7], 0) # no match, insert at start
1

julia> searchsortedfirst([1=>"one", 2=>"two", 4=>"four"], 3=>"three", by=first) # compare the keys of the pairs
3
```



searchsortedlast:
==================================================

```
searchsortedlast(v, x; by=identity, lt=isless, rev=false)
```

Return the index of the last value in `v` that is not ordered after `x`. If all values in `v` are ordered after `x`, return `firstindex(v) - 1`.

The vector `v` must be sorted according to the order defined by the keywords. `insert!`ing `x` immediately after the returned index will maintain the sorted order. Refer to [`sort!`](@ref) for the meaning and use of the keywords. Note that the `by` function is applied to the searched value `x` as well as the values in `v`.

The index is generally found using binary search, but there are optimized implementations for some inputs

# Examples

```jldoctest
julia> searchsortedlast([1, 2, 4, 5, 5, 7], 4) # single match
3

julia> searchsortedlast([1, 2, 4, 5, 5, 7], 5) # multiple matches
5

julia> searchsortedlast([1, 2, 4, 5, 5, 7], 3) # no match, insert in the middle
2

julia> searchsortedlast([1, 2, 4, 5, 5, 7], 9) # no match, insert at end
6

julia> searchsortedlast([1, 2, 4, 5, 5, 7], 0) # no match, insert at start
0

julia> searchsortedlast([1=>"one", 2=>"two", 4=>"four"], 3=>"three", by=first) # compare the keys of the pairs
2
```



sec:
==================================================

```
sec(x)
```

Compute the secant of `x`, where `x` is in radians.

```
sec(A::AbstractMatrix)
```

Compute the matrix secant of a square matrix `A`.



secd:
==================================================

```
secd(x)
```

Compute the secant of `x`, where `x` is in degrees.



sech:
==================================================

```
sech(x)
```

Compute the hyperbolic secant of `x`.

```
sech(A::AbstractMatrix)
```

Compute the matrix hyperbolic secant of square matrix `A`.



seek:
==================================================

```
seek(s, pos)
```

Seek a stream to the given position.

# Examples

```jldoctest
julia> io = IOBuffer("JuliaLang is a GitHub organization.");

julia> seek(io, 5);

julia> read(io, Char)
'L': ASCII/Unicode U+004C (category Lu: Letter, uppercase)
```



seekend:
==================================================

```
seekend(s)
```

Seek a stream to its end.



seekstart:
==================================================

```
seekstart(s)
```

Seek a stream to its beginning.

# Examples

```jldoctest
julia> io = IOBuffer("JuliaLang is a GitHub organization.");

julia> seek(io, 5);

julia> read(io, Char)
'L': ASCII/Unicode U+004C (category Lu: Letter, uppercase)

julia> seekstart(io);

julia> read(io, Char)
'J': ASCII/Unicode U+004A (category Lu: Letter, uppercase)
```



selectdim:
==================================================

```
selectdim(A, d::Integer, i)
```

Return a view of all the data of `A` where the index for dimension `d` equals `i`.

Equivalent to `view(A,:,:,...,i,:,:,...)` where `i` is in position `d`.

See also: [`eachslice`](@ref).

# Examples

```jldoctest
julia> A = [1 2 3 4; 5 6 7 8]
2×4 Matrix{Int64}:
 1  2  3  4
 5  6  7  8

julia> selectdim(A, 2, 3)
2-element view(::Matrix{Int64}, :, 3) with eltype Int64:
 3
 7

julia> selectdim(A, 2, 3:4)
2×2 view(::Matrix{Int64}, :, 3:4) with eltype Int64:
 3  4
 7  8
```



set_zero_subnormals:
==================================================

```
set_zero_subnormals(yes::Bool) -> Bool
```

If `yes` is `false`, subsequent floating-point operations follow rules for IEEE arithmetic on subnormal values ("denormals"). Otherwise, floating-point operations are permitted (but not required) to convert subnormal inputs or outputs to zero. Returns `true` unless `yes==true` but the hardware does not support zeroing of subnormal numbers.

`set_zero_subnormals(true)` can speed up some computations on some hardware. However, it can break identities such as `(x-y==0) == (x==y)`.

!!! warning
    This function only affects the current thread.




setcpuaffinity:
==================================================

```
setcpuaffinity(original_command::Cmd, cpus) -> command::Cmd
```

Set the CPU affinity of the `command` by a list of CPU IDs (1-based) `cpus`.  Passing `cpus = nothing` means to unset the CPU affinity if the `original_command` has any.

This function is supported only in Linux and Windows.  It is not supported in macOS because libuv does not support affinity setting.

!!! compat "Julia 1.8"
    This function requires at least Julia 1.8.


# Examples

In Linux, the `taskset` command line program can be used to see how `setcpuaffinity` works.

```julia
julia> run(setcpuaffinity(`sh -c 'taskset -p $$'`, [1, 2, 5]));
pid 2273's current affinity mask: 13
```

Note that the mask value `13` reflects that the first, second, and the fifth bits (counting from the least significant position) are turned on:

```julia
julia> 0b010011
0x13
```



setdiff:
==================================================

```
setdiff(s, itrs...)
```

Construct the set of elements in `s` but not in any of the iterables in `itrs`. Maintain order with arrays.

See also [`setdiff!`](@ref), [`union`](@ref) and [`intersect`](@ref).

# Examples

```jldoctest
julia> setdiff([1,2,3], [3,4,5])
2-element Vector{Int64}:
 1
 2
```



setdiff!:
==================================================

```
setdiff!(s, itrs...)
```

Remove from set `s` (in-place) each element of each iterable from `itrs`. Maintain order with arrays.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


# Examples

```jldoctest
julia> a = Set([1, 3, 4, 5]);

julia> setdiff!(a, 1:2:6);

julia> a
Set{Int64} with 1 element:
  4
```



setenv:
==================================================

```
setenv(command::Cmd, env; dir)
```

Set environment variables to use when running the given `command`. `env` is either a dictionary mapping strings to strings, an array of strings of the form `"var=val"`, or zero or more `"var"=>val` pair arguments. In order to modify (rather than replace) the existing environment, create `env` through `copy(ENV)` and then setting `env["var"]=val` as desired, or use [`addenv`](@ref).

The `dir` keyword argument can be used to specify a working directory for the command. `dir` defaults to the currently set `dir` for `command` (which is the current working directory if not specified already).

See also [`Cmd`](@ref), [`addenv`](@ref), [`ENV`](@ref), [`pwd`](@ref).



setfield!:
==================================================

```
setfield!(value, name::Symbol, x, [order::Symbol])
setfield!(value, i::Int, x, [order::Symbol])
```

Assign `x` to a named field in `value` of composite type. The `value` must be mutable and `x` must be a subtype of `fieldtype(typeof(value), name)`. Additionally, an ordering can be specified for this operation. If the field was declared `@atomic`, this specification is mandatory. Otherwise, if not declared as `@atomic`, it must be `:not_atomic` if specified. See also [`setproperty!`](@ref Base.setproperty!).

# Examples

```jldoctest
julia> mutable struct MyMutableStruct
           field::Int
       end

julia> a = MyMutableStruct(1);

julia> setfield!(a, :field, 2);

julia> getfield(a, :field)
2

julia> a = 1//2
1//2

julia> setfield!(a, :num, 3);
ERROR: setfield!: immutable struct of type Rational cannot be changed
```



setfieldonce!:
==================================================

```
setfieldonce!(value, name::Union{Int,Symbol}, desired,
              [success_order::Symbol, [fail_order::Symbol=success_order]) -> success::Bool
```

Atomically perform the operations to set a field to a given value, only if it was previously not set.

```
ok = !isdefined(value, name, fail_order)
if ok
    setfield!(value, name, desired, success_order)
end
return ok
```

!!! compat "Julia 1.11"
    This function requires Julia 1.11 or later.




setglobal!:
==================================================

```
setglobal!(module::Module, name::Symbol, x, [order::Symbol=:monotonic])
```

Set or change the value of the binding `name` in the module `module` to `x`. No type conversion is performed, so if a type has already been declared for the binding, `x` must be of appropriate type or an error is thrown.

Additionally, an atomic ordering can be specified for this operation, otherwise it defaults to monotonic.

Users will typically access this functionality through the [`setproperty!`](@ref Base.setproperty!) function or corresponding syntax (i.e. `module.name = x`) instead, so this is intended only for very specific use cases.

!!! compat "Julia 1.9"
    This function requires Julia 1.9 or later.


See also [`setproperty!`](@ref Base.setproperty!) and [`getglobal`](@ref)

# Examples

```jldoctest; filter = r"Stacktrace:(\n \[[0-9]+\].*)*"
julia> module M; global a; end;

julia> M.a  # same as `getglobal(M, :a)`
ERROR: UndefVarError: `a` not defined in `M`
Suggestion: add an appropriate import or assignment. This global was declared but not assigned.
Stacktrace:
 [1] getproperty(x::Module, f::Symbol)
   @ Base ./Base.jl:42
 [2] top-level scope
   @ none:1

julia> setglobal!(M, :a, 1)
1

julia> M.a
1
```



setglobalonce!:
==================================================

```
setglobalonce!(module::Module, name::Symbol, value,
              [success_order::Symbol, [fail_order::Symbol=success_order]) -> success::Bool
```

Atomically perform the operations to set a global to a given value, only if it was previously not set.

!!! compat "Julia 1.11"
    This function requires Julia 1.11 or later.


See also [`setpropertyonce!`](@ref Base.setpropertyonce!) and [`setglobal!`](@ref).



setindex!:
==================================================

```
setindex!(collection, value, key...)
```

Store the given value at the given key or index within a collection. The syntax `a[i,j,...] = x` is converted by the compiler to `(setindex!(a, x, i, j, ...); x)`.

# Examples

```jldoctest
julia> a = Dict("a"=>1)
Dict{String, Int64} with 1 entry:
  "a" => 1

julia> setindex!(a, 2, "b")
Dict{String, Int64} with 2 entries:
  "b" => 2
  "a" => 1
```

```
setindex!(A, X, inds...)
A[inds...] = X
```

Store values from array `X` within some subset of `A` as specified by `inds`. The syntax `A[inds...] = X` is equivalent to `(setindex!(A, X, inds...); X)`.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


# Examples

```jldoctest
julia> A = zeros(2,2);

julia> setindex!(A, [10, 20], [1, 2]);

julia> A[[3, 4]] = [30, 40];

julia> A
2×2 Matrix{Float64}:
 10.0  30.0
 20.0  40.0
```



setprecision:
==================================================

```
setprecision([T=BigFloat,] precision::Int; base=2)
```

Set the precision (in bits, by default) to be used for `T` arithmetic. If `base` is specified, then the precision is the minimum required to give at least `precision` digits in the given `base`.

!!! warning
    This function is not thread-safe. It will affect code running on all threads, but its behavior is undefined if called concurrently with computations that use the setting.


!!! compat "Julia 1.8"
    The `base` keyword requires at least Julia 1.8.


```
setprecision(f::Function, [T=BigFloat,] precision::Integer; base=2)
```

Change the `T` arithmetic precision (in the given `base`) for the duration of `f`. It is logically equivalent to:

```
old = precision(BigFloat)
setprecision(BigFloat, precision)
f()
setprecision(BigFloat, old)
```

Often used as `setprecision(T, precision) do ... end`

Note: `nextfloat()`, `prevfloat()` do not use the precision mentioned by `setprecision`.

!!! compat "Julia 1.8"
    The `base` keyword requires at least Julia 1.8.




setproperty!:
==================================================

```
setproperty!(value, name::Symbol, x)
setproperty!(value, name::Symbol, x, order::Symbol)
```

The syntax `a.b = c` calls `setproperty!(a, :b, c)`. The syntax `@atomic order a.b = c` calls `setproperty!(a, :b, c, :order)` and the syntax `@atomic a.b = c` calls `setproperty!(a, :b, c, :sequentially_consistent)`.

!!! compat "Julia 1.8"
    `setproperty!` on modules requires at least Julia 1.8.


See also [`setfield!`](@ref Core.setfield!), [`propertynames`](@ref Base.propertynames) and [`getproperty`](@ref Base.getproperty).



setpropertyonce!:
==================================================

```
setpropertyonce!(x, f::Symbol, value, success_order::Symbol=:not_atomic, fail_order::Symbol=success_order)
```

Perform a compare-and-swap operation on `x.f` to set it to `value` if previously unset. The syntax `@atomiconce x.f = value` can be used instead of the function call form.

See also [`setfieldonce!`](@ref Core.replacefield!), [`setproperty!`](@ref Base.setproperty!), [`replaceproperty!`](@ref Base.replaceproperty!).

!!! compat "Julia 1.11"
    This function requires Julia 1.11 or later.




setrounding:
==================================================

```
setrounding(T, mode)
```

Set the rounding mode of floating point type `T`, controlling the rounding of basic arithmetic functions ([`+`](@ref), [`-`](@ref), [`*`](@ref), [`/`](@ref) and [`sqrt`](@ref)) and type conversion. Other numerical functions may give incorrect or invalid values when using rounding modes other than the default [`RoundNearest`](@ref).

Note that this is currently only supported for `T == BigFloat`.

!!! warning
    This function is not thread-safe. It will affect code running on all threads, but its behavior is undefined if called concurrently with computations that use the setting.


```
setrounding(f::Function, T, mode)
```

Change the rounding mode of floating point type `T` for the duration of `f`. It is logically equivalent to:

```
old = rounding(T)
setrounding(T, mode)
f()
setrounding(T, old)
```

See [`RoundingMode`](@ref) for available rounding modes.



show:
==================================================

```
show([io::IO = stdout], x)
```

Write a text representation of a value `x` to the output stream `io`. New types `T` should overload `show(io::IO, x::T)`. The representation used by `show` generally includes Julia-specific formatting and type information, and should be parseable Julia code when possible.

[`repr`](@ref) returns the output of `show` as a string.

For a more verbose human-readable text output for objects of type `T`, define `show(io::IO, ::MIME"text/plain", ::T)` in addition. Checking the `:compact` [`IOContext`](@ref) key (often checked as `get(io, :compact, false)::Bool`) of `io` in such methods is recommended, since some containers show their elements by calling this method with `:compact => true`.

See also [`print`](@ref), which writes un-decorated representations.

# Examples

```jldoctest
julia> show("Hello World!")
"Hello World!"
julia> print("Hello World!")
Hello World!
```

```
show(io::IO, mime, x)
```

The [`display`](@ref) functions ultimately call `show` in order to write an object `x` as a given `mime` type to a given I/O stream `io` (usually a memory buffer), if possible. In order to provide a rich multimedia representation of a user-defined type `T`, it is only necessary to define a new `show` method for `T`, via: `show(io, ::MIME"mime", x::T) = ...`, where `mime` is a MIME-type string and the function body calls [`write`](@ref) (or similar) to write that representation of `x` to `io`. (Note that the `MIME""` notation only supports literal strings; to construct `MIME` types in a more flexible manner use `MIME{Symbol("")}`.)

For example, if you define a `MyImage` type and know how to write it to a PNG file, you could define a function `show(io, ::MIME"image/png", x::MyImage) = ...` to allow your images to be displayed on any PNG-capable `AbstractDisplay` (such as IJulia). As usual, be sure to `import Base.show` in order to add new methods to the built-in Julia function `show`.

Technically, the `MIME"mime"` macro defines a singleton type for the given `mime` string, which allows us to exploit Julia's dispatch mechanisms in determining how to display objects of any given type.

The default MIME type is `MIME"text/plain"`. There is a fallback definition for `text/plain` output that calls `show` with 2 arguments, so it is not always necessary to add a method for that case. If a type benefits from custom human-readable output though, `show(::IO, ::MIME"text/plain", ::T)` should be defined. For example, the `Day` type uses `1 day` as the output for the `text/plain` MIME type, and `Day(1)` as the output of 2-argument `show`.

# Examples

```jldoctest
julia> struct Day
           n::Int
       end

julia> Base.show(io::IO, ::MIME"text/plain", d::Day) = print(io, d.n, " day")

julia> Day(1)
1 day
```

Container types generally implement 3-argument `show` by calling `show(io, MIME"text/plain"(), x)` for elements `x`, with `:compact => true` set in an [`IOContext`](@ref) passed as the first argument.



showable:
==================================================

```
showable(mime, x)
```

Return a boolean value indicating whether or not the object `x` can be written as the given `mime` type.

(By default, this is determined automatically by the existence of the corresponding [`show`](@ref) method for `typeof(x)`.  Some types provide custom `showable` methods; for example, if the available MIME formats depend on the *value* of `x`.)

# Examples

```jldoctest
julia> showable(MIME("text/plain"), rand(5))
true

julia> showable("image/png", rand(5))
false
```



showerror:
==================================================

```
showerror(io, e)
```

Show a descriptive representation of an exception object `e`. This method is used to display the exception after a call to [`throw`](@ref).

# Examples

```jldoctest
julia> struct MyException <: Exception
           msg::String
       end

julia> function Base.showerror(io::IO, err::MyException)
           print(io, "MyException: ")
           print(io, err.msg)
       end

julia> err = MyException("test exception")
MyException("test exception")

julia> sprint(showerror, err)
"MyException: test exception"

julia> throw(MyException("test exception"))
ERROR: MyException: test exception
```



sign:
==================================================

```
sign(x)
```

Return zero if `x==0` and $x/|x|$ otherwise (i.e., ±1 for real `x`).

See also [`signbit`](@ref), [`zero`](@ref), [`copysign`](@ref), [`flipsign`](@ref).

# Examples

```jldoctest
julia> sign(-4.0)
-1.0

julia> sign(99)
1

julia> sign(-0.0)
-0.0

julia> sign(0 + im)
0.0 + 1.0im
```



signbit:
==================================================

```
signbit(x)
```

Return `true` if the value of the sign of `x` is negative, otherwise `false`.

See also [`sign`](@ref) and [`copysign`](@ref).

# Examples

```jldoctest
julia> signbit(-4)
true

julia> signbit(5)
false

julia> signbit(5.5)
false

julia> signbit(-4.1)
true
```



signed:
==================================================

```
signed(T::Integer)
```

Convert an integer bitstype to the signed type of the same size.

# Examples

```jldoctest
julia> signed(UInt16)
Int16
julia> signed(UInt64)
Int64
```

```
signed(x)
```

Convert a number to a signed integer. If the argument is unsigned, it is reinterpreted as signed without checking for overflow.

See also: [`unsigned`](@ref), [`sign`](@ref), [`signbit`](@ref).



significand:
==================================================

```
significand(x)
```

Extract the significand (a.k.a. mantissa) of a floating-point number. If `x` is a non-zero finite number, then the result will be a number of the same type and sign as `x`, and whose absolute value is on the interval $[1,2)$. Otherwise `x` is returned.

See also [`frexp`](@ref), [`exponent`](@ref).

# Examples

```jldoctest
julia> significand(15.2)
1.9

julia> significand(-15.2)
-1.9

julia> significand(-15.2) * 2^3
-15.2

julia> significand(-Inf), significand(Inf), significand(NaN)
(-Inf, Inf, NaN)
```



similar:
==================================================

```
similar(array, [element_type=eltype(array)], [dims=size(array)])
```

Create an uninitialized mutable array with the given element type and size, based upon the given source array. The second and third arguments are both optional, defaulting to the given array's `eltype` and `size`. The dimensions may be specified either as a single tuple argument or as a series of integer arguments.

Custom AbstractArray subtypes may choose which specific array type is best-suited to return for the given element type and dimensionality. If they do not specialize this method, the default is an `Array{element_type}(undef, dims...)`.

For example, `similar(1:10, 1, 4)` returns an uninitialized `Array{Int,2}` since ranges are neither mutable nor support 2 dimensions:

```julia-repl
julia> similar(1:10, 1, 4)
1×4 Matrix{Int64}:
 4419743872  4374413872  4419743888  0
```

Conversely, `similar(trues(10,10), 2)` returns an uninitialized `BitVector` with two elements since `BitArray`s are both mutable and can support 1-dimensional arrays:

```julia-repl
julia> similar(trues(10,10), 2)
2-element BitVector:
 0
 0
```

Since `BitArray`s can only store elements of type [`Bool`](@ref), however, if you request a different element type it will create a regular `Array` instead:

```julia-repl
julia> similar(falses(10), Float64, 2, 4)
2×4 Matrix{Float64}:
 2.18425e-314  2.18425e-314  2.18425e-314  2.18425e-314
 2.18425e-314  2.18425e-314  2.18425e-314  2.18425e-314
```

See also: [`undef`](@ref), [`isassigned`](@ref).

```
similar(storagetype, axes)
```

Create an uninitialized mutable array analogous to that specified by `storagetype`, but with `axes` specified by the last argument.

**Examples**:

```
similar(Array{Int}, axes(A))
```

creates an array that "acts like" an `Array{Int}` (and might indeed be backed by one), but which is indexed identically to `A`. If `A` has conventional indexing, this will be identical to `Array{Int}(undef, size(A))`, but if `A` has unconventional indexing then the indices of the result will match `A`.

```
similar(BitArray, (axes(A, 2),))
```

would create a 1-dimensional logical array whose indices match those of the columns of `A`.



sin:
==================================================

```
sin(x)
```

Compute sine of `x`, where `x` is in radians.

See also [`sind`](@ref), [`sinpi`](@ref), [`sincos`](@ref), [`cis`](@ref), [`asin`](@ref).

# Examples

```jldoctest
julia> round.(sin.(range(0, 2pi, length=9)'), digits=3)
1×9 Matrix{Float64}:
 0.0  0.707  1.0  0.707  0.0  -0.707  -1.0  -0.707  -0.0

julia> sind(45)
0.7071067811865476

julia> sinpi(1/4)
0.7071067811865475

julia> round.(sincos(pi/6), digits=3)
(0.5, 0.866)

julia> round(cis(pi/6), digits=3)
0.866 + 0.5im

julia> round(exp(im*pi/6), digits=3)
0.866 + 0.5im
```

```
sin(A::AbstractMatrix)
```

Compute the matrix sine of a square matrix `A`.

If `A` is symmetric or Hermitian, its eigendecomposition ([`eigen`](@ref)) is used to compute the sine. Otherwise, the sine is determined by calling [`exp`](@ref).

# Examples

```jldoctest
julia> sin(fill(1.0, (2,2)))
2×2 Matrix{Float64}:
 0.454649  0.454649
 0.454649  0.454649
```



sinc:
==================================================

```
sinc(x)
```

Compute normalized sinc function $\operatorname{sinc}(x) = \sin(\pi x) / (\pi x)$ if $x \neq 0$, and $1$ if $x = 0$.

See also [`cosc`](@ref), its derivative.



sincos:
==================================================

```
sincos(x)
```

Simultaneously compute the sine and cosine of `x`, where `x` is in radians, returning a tuple `(sine, cosine)`.

See also [`cis`](@ref), [`sincospi`](@ref), [`sincosd`](@ref).

```
sincos(A::AbstractMatrix)
```

Compute the matrix sine and cosine of a square matrix `A`.

# Examples

```jldoctest
julia> S, C = sincos(fill(1.0, (2,2)));

julia> S
2×2 Matrix{Float64}:
 0.454649  0.454649
 0.454649  0.454649

julia> C
2×2 Matrix{Float64}:
  0.291927  -0.708073
 -0.708073   0.291927
```



sincosd:
==================================================

```
sincosd(x)
```

Simultaneously compute the sine and cosine of `x`, where `x` is in degrees.

!!! compat "Julia 1.3"
    This function requires at least Julia 1.3.




sincospi:
==================================================

```
sincospi(x)
```

Simultaneously compute [`sinpi(x)`](@ref) and [`cospi(x)`](@ref) (the sine and cosine of `π*x`, where `x` is in radians), returning a tuple `(sine, cosine)`.

!!! compat "Julia 1.6"
    This function requires Julia 1.6 or later.


See also: [`cispi`](@ref), [`sincosd`](@ref), [`sinpi`](@ref).



sind:
==================================================

```
sind(x)
```

Compute sine of `x`, where `x` is in degrees. If `x` is a matrix, `x` needs to be a square matrix.

!!! compat "Julia 1.7"
    Matrix arguments require Julia 1.7 or later.




sinh:
==================================================

```
sinh(x)
```

Compute hyperbolic sine of `x`.

```
sinh(A::AbstractMatrix)
```

Compute the matrix hyperbolic sine of a square matrix `A`.



sinpi:
==================================================

```
sinpi(x)
```

Compute $\sin(\pi x)$ more accurately than `sin(pi*x)`, especially for large `x`.

See also [`sind`](@ref), [`cospi`](@ref), [`sincospi`](@ref).



size:
==================================================

```
size(A::AbstractArray, [dim])
```

Return a tuple containing the dimensions of `A`. Optionally you can specify a dimension to just get the length of that dimension.

Note that `size` may not be defined for arrays with non-standard indices, in which case [`axes`](@ref) may be useful. See the manual chapter on [arrays with custom indices](@ref man-custom-indices).

See also: [`length`](@ref), [`ndims`](@ref), [`eachindex`](@ref), [`sizeof`](@ref).

# Examples

```jldoctest
julia> A = fill(1, (2,3,4));

julia> size(A)
(2, 3, 4)

julia> size(A, 2)
3
```



sizehint!:
==================================================

```
sizehint!(s, n; first::Bool=false, shrink::Bool=true) -> s
```

Suggest that collection `s` reserve capacity for at least `n` elements. That is, if you expect that you're going to have to push a lot of values onto `s`, you can avoid the cost of incremental reallocation by doing it once up front; this can improve performance.

If `first` is `true`, then any additional space is reserved before the start of the collection. This way, subsequent calls to `pushfirst!` (instead of `push!`) may become faster. Supplying this keyword may result in an error if the collection is not ordered or if `pushfirst!` is not supported for this collection.

If `shrink=true` (the default), the collection's capacity may be reduced if its current capacity is greater than `n`.

See also [`resize!`](@ref).

# Notes on the performance model

For types that support `sizehint!`,

1. `push!` and `append!` methods generally may (but are not required to) preallocate extra storage. For types implemented in `Base`, they typically do, using a heuristic optimized for a general use case.
2. `sizehint!` may control this preallocation. Again, it typically does this for types in `Base`.
3. `empty!` is nearly costless (and O(1)) for types that support this kind of preallocation.

!!! compat "Julia 1.11"
    The `shrink` and `first` arguments were added in Julia 1.11.




sizeof:
==================================================

```
sizeof(T::DataType)
sizeof(obj)
```

Size, in bytes, of the canonical binary representation of the given `DataType` `T`, if any. Or the size, in bytes, of object `obj` if it is not a `DataType`.

See also [`Base.summarysize`](@ref).

# Examples

```jldoctest
julia> sizeof(Float32)
4

julia> sizeof(ComplexF64)
16

julia> sizeof(1.0)
8

julia> sizeof(collect(1.0:10.0))
80

julia> struct StructWithPadding
           x::Int64
           flag::Bool
       end

julia> sizeof(StructWithPadding) # not the sum of `sizeof` of fields due to padding
16

julia> sizeof(Int64) + sizeof(Bool) # different from above
9
```

If `DataType` `T` does not have a specific size, an error is thrown.

```jldoctest
julia> sizeof(AbstractArray)
ERROR: Abstract type AbstractArray does not have a definite size.
Stacktrace:
[...]
```

```
sizeof(str::AbstractString)
```

Size, in bytes, of the string `str`. Equal to the number of code units in `str` multiplied by the size, in bytes, of one code unit in `str`.

# Examples

```jldoctest
julia> sizeof("")
0

julia> sizeof("∀")
3
```



skip:
==================================================

```
skip(s, offset)
```

Seek a stream relative to the current position.

# Examples

```jldoctest
julia> io = IOBuffer("JuliaLang is a GitHub organization.");

julia> seek(io, 5);

julia> skip(io, 10);

julia> read(io, Char)
'G': ASCII/Unicode U+0047 (category Lu: Letter, uppercase)
```



skipchars:
==================================================

```
skipchars(predicate, io::IO; linecomment=nothing)
```

Advance the stream `io` such that the next-read character will be the first remaining for which `predicate` returns `false`. If the keyword argument `linecomment` is specified, all characters from that character until the start of the next line are ignored.

# Examples

```jldoctest
julia> buf = IOBuffer("    text")
IOBuffer(data=UInt8[...], readable=true, writable=false, seekable=true, append=false, size=8, maxsize=Inf, ptr=1, mark=-1)

julia> skipchars(isspace, buf)
IOBuffer(data=UInt8[...], readable=true, writable=false, seekable=true, append=false, size=8, maxsize=Inf, ptr=5, mark=-1)

julia> String(readavailable(buf))
"text"
```



skipmissing:
==================================================

```
skipmissing(itr)
```

Return an iterator over the elements in `itr` skipping [`missing`](@ref) values. The returned object can be indexed using indices of `itr` if the latter is indexable. Indices corresponding to missing values are not valid: they are skipped by [`keys`](@ref) and [`eachindex`](@ref), and a `MissingException` is thrown when trying to use them.

Use [`collect`](@ref) to obtain an `Array` containing the non-`missing` values in `itr`. Note that even if `itr` is a multidimensional array, the result will always be a `Vector` since it is not possible to remove missings while preserving dimensions of the input.

See also [`coalesce`](@ref), [`ismissing`](@ref), [`something`](@ref).

# Examples

```jldoctest
julia> x = skipmissing([1, missing, 2])
skipmissing(Union{Missing, Int64}[1, missing, 2])

julia> sum(x)
3

julia> x[1]
1

julia> x[2]
ERROR: MissingException: the value at index (2,) is missing
[...]

julia> argmax(x)
3

julia> collect(keys(x))
2-element Vector{Int64}:
 1
 3

julia> collect(skipmissing([1, missing, 2]))
2-element Vector{Int64}:
 1
 2

julia> collect(skipmissing([1 missing; 2 missing]))
2-element Vector{Int64}:
 1
 2
```



sleep:
==================================================

```
sleep(seconds)
```

Block the current task for a specified number of seconds. The minimum sleep time is 1 millisecond or input of `0.001`.



something:
==================================================

```
something(x...)
```

Return the first value in the arguments which is not equal to [`nothing`](@ref), if any. Otherwise throw an error. Arguments of type [`Some`](@ref) are unwrapped.

See also [`coalesce`](@ref), [`skipmissing`](@ref), [`@something`](@ref).

# Examples

```jldoctest
julia> something(nothing, 1)
1

julia> something(Some(1), nothing)
1

julia> something(Some(nothing), 2) === nothing
true

julia> something(missing, nothing)
missing

julia> something(nothing, nothing)
ERROR: ArgumentError: No value arguments present
```



sort:
==================================================

```
sort(v; alg::Algorithm=defalg(v), lt=isless, by=identity, rev::Bool=false, order::Ordering=Forward)
```

Variant of [`sort!`](@ref) that returns a sorted copy of `v` leaving `v` itself unmodified.

# Examples

```jldoctest
julia> v = [3, 1, 2];

julia> sort(v)
3-element Vector{Int64}:
 1
 2
 3

julia> v
3-element Vector{Int64}:
 3
 1
 2
```

```
sort(A; dims::Integer, alg::Algorithm=defalg(A), lt=isless, by=identity, rev::Bool=false, order::Ordering=Forward)
```

Sort a multidimensional array `A` along the given dimension. See [`sort!`](@ref) for a description of possible keyword arguments.

To sort slices of an array, refer to [`sortslices`](@ref).

# Examples

```jldoctest
julia> A = [4 3; 1 2]
2×2 Matrix{Int64}:
 4  3
 1  2

julia> sort(A, dims = 1)
2×2 Matrix{Int64}:
 1  2
 4  3

julia> sort(A, dims = 2)
2×2 Matrix{Int64}:
 3  4
 1  2
```



sort!:
==================================================

```
sort!(v; alg::Algorithm=defalg(v), lt=isless, by=identity, rev::Bool=false, order::Ordering=Forward)
```

Sort the vector `v` in place. A stable algorithm is used by default: the ordering of elements that compare equal is preserved. A specific algorithm can be selected via the `alg` keyword (see [Sorting Algorithms](@ref) for available algorithms).

Elements are first transformed with the function `by` and then compared according to either the function `lt` or the ordering `order`. Finally, the resulting order is reversed if `rev=true` (this preserves forward stability: elements that compare equal are not reversed). The current implementation applies the `by` transformation before each comparison rather than once per element.

Passing an `lt` other than `isless` along with an `order` other than [`Base.Order.Forward`](@ref) or [`Base.Order.Reverse`](@ref) is not permitted, otherwise all options are independent and can be used together in all possible combinations. Note that `order` can also include a "by" transformation, in which case it is applied after that defined with the `by` keyword. For more information on `order` values see the documentation on [Alternate Orderings](@ref).

Relations between two elements are defined as follows (with "less" and "greater" exchanged when `rev=true`):

  * `x` is less than `y` if `lt(by(x), by(y))` (or `Base.Order.lt(order, by(x), by(y))`) yields true.
  * `x` is greater than `y` if `y` is less than `x`.
  * `x` and `y` are equivalent if neither is less than the other ("incomparable" is sometimes used as a synonym for "equivalent").

The result of `sort!` is sorted in the sense that every element is greater than or equivalent to the previous one.

The `lt` function must define a strict weak order, that is, it must be

  * irreflexive: `lt(x, x)` always yields `false`,
  * asymmetric: if `lt(x, y)` yields `true` then `lt(y, x)` yields `false`,
  * transitive: `lt(x, y) && lt(y, z)` implies `lt(x, z)`,
  * transitive in equivalence: `!lt(x, y) && !lt(y, x)` and `!lt(y, z) && !lt(z, y)` together imply `!lt(x, z) && !lt(z, x)`. In words: if `x` and `y` are equivalent and `y` and `z` are equivalent then `x` and `z` must be equivalent.

For example `<` is a valid `lt` function for `Int` values but `≤` is not: it violates irreflexivity. For `Float64` values even `<` is invalid as it violates the fourth condition: `1.0` and `NaN` are equivalent and so are `NaN` and `2.0` but `1.0` and `2.0` are not equivalent.

See also [`sort`](@ref), [`sortperm`](@ref), [`sortslices`](@ref), [`partialsort!`](@ref), [`partialsortperm`](@ref), [`issorted`](@ref), [`searchsorted`](@ref), [`insorted`](@ref), [`Base.Order.ord`](@ref).

# Examples

```jldoctest
julia> v = [3, 1, 2]; sort!(v); v
3-element Vector{Int64}:
 1
 2
 3

julia> v = [3, 1, 2]; sort!(v, rev = true); v
3-element Vector{Int64}:
 3
 2
 1

julia> v = [(1, "c"), (3, "a"), (2, "b")]; sort!(v, by = x -> x[1]); v
3-element Vector{Tuple{Int64, String}}:
 (1, "c")
 (2, "b")
 (3, "a")

julia> v = [(1, "c"), (3, "a"), (2, "b")]; sort!(v, by = x -> x[2]); v
3-element Vector{Tuple{Int64, String}}:
 (3, "a")
 (2, "b")
 (1, "c")

julia> sort(0:3, by=x->x-2, order=Base.Order.By(abs)) # same as sort(0:3, by=abs(x->x-2))
4-element Vector{Int64}:
 2
 1
 3
 0

julia> sort([2, NaN, 1, NaN, 3]) # correct sort with default lt=isless
5-element Vector{Float64}:
   1.0
   2.0
   3.0
 NaN
 NaN

julia> sort([2, NaN, 1, NaN, 3], lt=<) # wrong sort due to invalid lt. This behavior is undefined.
5-element Vector{Float64}:
   2.0
 NaN
   1.0
 NaN
   3.0
```

```
sort!(A; dims::Integer, alg::Algorithm=defalg(A), lt=isless, by=identity, rev::Bool=false, order::Ordering=Forward)
```

Sort the multidimensional array `A` along dimension `dims`. See the one-dimensional version of [`sort!`](@ref) for a description of possible keyword arguments.

To sort slices of an array, refer to [`sortslices`](@ref).

!!! compat "Julia 1.1"
    This function requires at least Julia 1.1.


# Examples

```jldoctest
julia> A = [4 3; 1 2]
2×2 Matrix{Int64}:
 4  3
 1  2

julia> sort!(A, dims = 1); A
2×2 Matrix{Int64}:
 1  2
 4  3

julia> sort!(A, dims = 2); A
2×2 Matrix{Int64}:
 1  2
 3  4
```



sortperm:
==================================================

```
sortperm(A; alg::Algorithm=DEFAULT_UNSTABLE, lt=isless, by=identity, rev::Bool=false, order::Ordering=Forward, [dims::Integer])
```

Return a permutation vector or array `I` that puts `A[I]` in sorted order along the given dimension. If `A` has more than one dimension, then the `dims` keyword argument must be specified. The order is specified using the same keywords as [`sort!`](@ref). The permutation is guaranteed to be stable even if the sorting algorithm is unstable: the indices of equal elements will appear in ascending order.

See also [`sortperm!`](@ref), [`partialsortperm`](@ref), [`invperm`](@ref), [`indexin`](@ref). To sort slices of an array, refer to [`sortslices`](@ref).

!!! compat "Julia 1.9"
    The method accepting `dims` requires at least Julia 1.9.


# Examples

```jldoctest
julia> v = [3, 1, 2];

julia> p = sortperm(v)
3-element Vector{Int64}:
 2
 3
 1

julia> v[p]
3-element Vector{Int64}:
 1
 2
 3

julia> A = [8 7; 5 6]
2×2 Matrix{Int64}:
 8  7
 5  6

julia> sortperm(A, dims = 1)
2×2 Matrix{Int64}:
 2  4
 1  3

julia> sortperm(A, dims = 2)
2×2 Matrix{Int64}:
 3  1
 2  4
```



sortperm!:
==================================================

```
sortperm!(ix, A; alg::Algorithm=DEFAULT_UNSTABLE, lt=isless, by=identity, rev::Bool=false, order::Ordering=Forward, [dims::Integer])
```

Like [`sortperm`](@ref), but accepts a preallocated index vector or array `ix` with the same `axes` as `A`. `ix` is initialized to contain the values `LinearIndices(A)`.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


!!! compat "Julia 1.9"
    The method accepting `dims` requires at least Julia 1.9.


# Examples

```jldoctest
julia> v = [3, 1, 2]; p = zeros(Int, 3);

julia> sortperm!(p, v); p
3-element Vector{Int64}:
 2
 3
 1

julia> v[p]
3-element Vector{Int64}:
 1
 2
 3

julia> A = [8 7; 5 6]; p = zeros(Int,2, 2);

julia> sortperm!(p, A; dims=1); p
2×2 Matrix{Int64}:
 2  4
 1  3

julia> sortperm!(p, A; dims=2); p
2×2 Matrix{Int64}:
 3  1
 2  4
```



sortslices:
==================================================

```
sortslices(A; dims, alg::Algorithm=DEFAULT_UNSTABLE, lt=isless, by=identity, rev::Bool=false, order::Ordering=Forward)
```

Sort slices of an array `A`. The required keyword argument `dims` must be either an integer or a tuple of integers. It specifies the dimension(s) over which the slices are sorted.

E.g., if `A` is a matrix, `dims=1` will sort rows, `dims=2` will sort columns. Note that the default comparison function on one dimensional slices sorts lexicographically.

For the remaining keyword arguments, see the documentation of [`sort!`](@ref).

# Examples

```jldoctest
julia> sortslices([7 3 5; -1 6 4; 9 -2 8], dims=1) # Sort rows
3×3 Matrix{Int64}:
 -1   6  4
  7   3  5
  9  -2  8

julia> sortslices([7 3 5; -1 6 4; 9 -2 8], dims=1, lt=(x,y)->isless(x[2],y[2]))
3×3 Matrix{Int64}:
  9  -2  8
  7   3  5
 -1   6  4

julia> sortslices([7 3 5; -1 6 4; 9 -2 8], dims=1, rev=true)
3×3 Matrix{Int64}:
  9  -2  8
  7   3  5
 -1   6  4

julia> sortslices([7 3 5; 6 -1 -4; 9 -2 8], dims=2) # Sort columns
3×3 Matrix{Int64}:
  3   5  7
 -1  -4  6
 -2   8  9

julia> sortslices([7 3 5; 6 -1 -4; 9 -2 8], dims=2, alg=InsertionSort, lt=(x,y)->isless(x[2],y[2]))
3×3 Matrix{Int64}:
  5   3  7
 -4  -1  6
  8  -2  9

julia> sortslices([7 3 5; 6 -1 -4; 9 -2 8], dims=2, rev=true)
3×3 Matrix{Int64}:
 7   5   3
 6  -4  -1
 9   8  -2
```

# Higher dimensions

`sortslices` extends naturally to higher dimensions. E.g., if `A` is a a 2x2x2 array, `sortslices(A, dims=3)` will sort slices within the 3rd dimension, passing the 2x2 slices `A[:, :, 1]` and `A[:, :, 2]` to the comparison function. Note that while there is no default order on higher-dimensional slices, you may use the `by` or `lt` keyword argument to specify such an order.

If `dims` is a tuple, the order of the dimensions in `dims` is relevant and specifies the linear order of the slices. E.g., if `A` is three dimensional and `dims` is `(1, 2)`, the orderings of the first two dimensions are re-arranged such that the slices (of the remaining third dimension) are sorted. If `dims` is `(2, 1)` instead, the same slices will be taken, but the result order will be row-major instead.

# Higher dimensional examples

```
julia> A = [4 3; 2 1 ;;; 'A' 'B'; 'C' 'D']
2×2×2 Array{Any, 3}:
[:, :, 1] =
 4  3
 2  1

[:, :, 2] =
 'A'  'B'
 'C'  'D'

julia> sortslices(A, dims=(1,2))
2×2×2 Array{Any, 3}:
[:, :, 1] =
 1  3
 2  4

[:, :, 2] =
 'D'  'B'
 'C'  'A'

julia> sortslices(A, dims=(2,1))
2×2×2 Array{Any, 3}:
[:, :, 1] =
 1  2
 3  4

[:, :, 2] =
 'D'  'C'
 'B'  'A'

julia> sortslices(reshape([5; 4; 3; 2; 1], (1,1,5)), dims=3, by=x->x[1,1])
1×1×5 Array{Int64, 3}:
[:, :, 1] =
 1

[:, :, 2] =
 2

[:, :, 3] =
 3

[:, :, 4] =
 4

[:, :, 5] =
 5
```



splat:
==================================================

```
splat(f)
```

Equivalent to

```julia
    my_splat(f) = args->f(args...)
```

i.e. given a function returns a new function that takes one argument and splats it into the original function. This is useful as an adaptor to pass a multi-argument function in a context that expects a single argument, but passes a tuple as that single argument.

# Examples

```jldoctest
julia> map(splat(+), zip(1:3,4:6))
3-element Vector{Int64}:
 5
 7
 9

julia> my_add = splat(+)
splat(+)

julia> my_add((1,2,3))
6
```



splice!:
==================================================

```
splice!(a::Vector, index::Integer, [replacement]) -> item
```

Remove the item at the given index, and return the removed item. Subsequent items are shifted left to fill the resulting gap. If specified, replacement values from an ordered collection will be spliced in place of the removed item.

See also: [`replace`](@ref), [`delete!`](@ref), [`deleteat!`](@ref), [`pop!`](@ref), [`popat!`](@ref).

# Examples

```jldoctest
julia> A = [6, 5, 4, 3, 2, 1]; splice!(A, 5)
2

julia> A
5-element Vector{Int64}:
 6
 5
 4
 3
 1

julia> splice!(A, 5, -1)
1

julia> A
5-element Vector{Int64}:
  6
  5
  4
  3
 -1

julia> splice!(A, 1, [-1, -2, -3])
6

julia> A
7-element Vector{Int64}:
 -1
 -2
 -3
  5
  4
  3
 -1
```

To insert `replacement` before an index `n` without removing any items, use `splice!(collection, n:n-1, replacement)`.

```
splice!(a::Vector, indices, [replacement]) -> items
```

Remove items at specified indices, and return a collection containing the removed items. Subsequent items are shifted left to fill the resulting gaps. If specified, replacement values from an ordered collection will be spliced in place of the removed items; in this case, `indices` must be a `AbstractUnitRange`.

To insert `replacement` before an index `n` without removing any items, use `splice!(collection, n:n-1, replacement)`.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


!!! compat "Julia 1.5"
    Prior to Julia 1.5, `indices` must always be a `UnitRange`.


!!! compat "Julia 1.8"
    Prior to Julia 1.8, `indices` must be a `UnitRange` if splicing in replacement values.


# Examples

```jldoctest
julia> A = [-1, -2, -3, 5, 4, 3, -1]; splice!(A, 4:3, 2)
Int64[]

julia> A
8-element Vector{Int64}:
 -1
 -2
 -3
  2
  5
  4
  3
 -1
```



split:
==================================================

```
split(str::AbstractString, dlm; limit::Integer=0, keepempty::Bool=true)
split(str::AbstractString; limit::Integer=0, keepempty::Bool=false)
```

Split `str` into an array of substrings on occurrences of the delimiter(s) `dlm`.  `dlm` can be any of the formats allowed by [`findnext`](@ref)'s first argument (i.e. as a string, regular expression or a function), or as a single character or collection of characters.

If `dlm` is omitted, it defaults to [`isspace`](@ref).

The optional keyword arguments are:

  * `limit`: the maximum size of the result. `limit=0` implies no maximum (default)
  * `keepempty`: whether empty fields should be kept in the result. Default is `false` without a `dlm` argument, `true` with a `dlm` argument.

See also [`rsplit`](@ref), [`eachsplit`](@ref).

# Examples

```jldoctest
julia> a = "Ma.rch"
"Ma.rch"

julia> split(a, ".")
2-element Vector{SubString{String}}:
 "Ma"
 "rch"
```



splitdir:
==================================================

```
splitdir(path::AbstractString) -> (AbstractString, AbstractString)
```

Split a path into a tuple of the directory name and file name.

# Examples

```jldoctest
julia> splitdir("/home/myuser")
("/home", "myuser")
```



splitdrive:
==================================================

```
splitdrive(path::AbstractString) -> (AbstractString, AbstractString)
```

On Windows, split a path into the drive letter part and the path part. On Unix systems, the first component is always the empty string.



splitext:
==================================================

```
splitext(path::AbstractString) -> (String, String)
```

If the last component of a path contains one or more dots, split the path into everything before the last dot and everything including and after the dot. Otherwise, return a tuple of the argument unmodified and the empty string. "splitext" is short for "split extension".

# Examples

```jldoctest
julia> splitext("/home/myuser/example.jl")
("/home/myuser/example", ".jl")

julia> splitext("/home/myuser/example.tar.gz")
("/home/myuser/example.tar", ".gz")

julia> splitext("/home/my.user/example")
("/home/my.user/example", "")
```



splitpath:
==================================================

```
splitpath(path::AbstractString) -> Vector{String}
```

Split a file path into all its path components. This is the opposite of `joinpath`. Returns an array of substrings, one for each directory or file in the path, including the root directory if present.

!!! compat "Julia 1.1"
    This function requires at least Julia 1.1.


# Examples

```jldoctest
julia> splitpath("/home/myuser/example.jl")
4-element Vector{String}:
 "/"
 "home"
 "myuser"
 "example.jl"
```



sprint:
==================================================

```
sprint(f::Function, args...; context=nothing, sizehint=0)
```

Call the given function with an I/O stream and the supplied extra arguments. Everything written to this I/O stream is returned as a string. `context` can be an [`IOContext`](@ref) whose properties will be used, a `Pair` specifying a property and its value, or a tuple of `Pair` specifying multiple properties and their values. `sizehint` suggests the capacity of the buffer (in bytes).

The optional keyword argument `context` can be set to a `:key=>value` pair, a tuple of `:key=>value` pairs, or an `IO` or [`IOContext`](@ref) object whose attributes are used for the I/O stream passed to `f`.  The optional `sizehint` is a suggested size (in bytes) to allocate for the buffer used to write the string.

!!! compat "Julia 1.7"
    Passing a tuple to keyword `context` requires Julia 1.7 or later.


# Examples

```jldoctest
julia> sprint(show, 66.66666; context=:compact => true)
"66.6667"

julia> sprint(showerror, BoundsError([1], 100))
"BoundsError: attempt to access 1-element Vector{Int64} at index [100]"
```



sqrt:
==================================================

```
sqrt(x)
```

Return $\sqrt{x}$.

Throws [`DomainError`](@ref) for negative [`Real`](@ref) arguments. Use complex negative arguments instead. Note that `sqrt` has a branch cut along the negative real axis.

The prefix operator `√` is equivalent to `sqrt`.

See also: [`hypot`](@ref).

# Examples

```jldoctest; filter = r"Stacktrace:(\n \[[0-9]+\].*)*"
julia> sqrt(big(81))
9.0

julia> sqrt(big(-81))
ERROR: DomainError with -81.0:
NaN result for non-NaN input.
Stacktrace:
 [1] sqrt(::BigFloat) at ./mpfr.jl:501
[...]

julia> sqrt(big(complex(-81)))
0.0 + 9.0im

julia> sqrt(-81 - 0.0im)  # -0.0im is below the branch cut
0.0 - 9.0im

julia> .√(1:4)
4-element Vector{Float64}:
 1.0
 1.4142135623730951
 1.7320508075688772
 2.0
```

```
sqrt(A::AbstractMatrix)
```

If `A` has no negative real eigenvalues, compute the principal matrix square root of `A`, that is the unique matrix $X$ with eigenvalues having positive real part such that $X^2 = A$. Otherwise, a nonprincipal square root is returned.

If `A` is real-symmetric or Hermitian, its eigendecomposition ([`eigen`](@ref)) is used to compute the square root.   For such matrices, eigenvalues λ that appear to be slightly negative due to roundoff errors are treated as if they were zero. More precisely, matrices with all eigenvalues `≥ -rtol*(max |λ|)` are treated as semidefinite (yielding a Hermitian square root), with negative eigenvalues taken to be zero. `rtol` is a keyword argument to `sqrt` (in the Hermitian/real-symmetric case only) that defaults to machine precision scaled by `size(A,1)`.

Otherwise, the square root is determined by means of the Björck-Hammarling method [^BH83], which computes the complex Schur form ([`schur`](@ref)) and then the complex square root of the triangular factor. If a real square root exists, then an extension of this method [^H87] that computes the real Schur form and then the real square root of the quasi-triangular factor is instead used.

[^BH83]: Åke Björck and Sven Hammarling, "A Schur method for the square root of a matrix", Linear Algebra and its Applications, 52-53, 1983, 127-140. [doi:10.1016/0024-3795(83)80010-X](https://doi.org/10.1016/0024-3795(83)80010-X)

[^H87]: Nicholas J. Higham, "Computing real square roots of a real matrix", Linear Algebra and its Applications, 88-89, 1987, 405-430. [doi:10.1016/0024-3795(87)90118-2](https://doi.org/10.1016/0024-3795(87)90118-2)

# Examples

```jldoctest
julia> A = [4 0; 0 4]
2×2 Matrix{Int64}:
 4  0
 0  4

julia> sqrt(A)
2×2 Matrix{Float64}:
 2.0  0.0
 0.0  2.0
```



stack:
==================================================

```
stack(iter; [dims])
```

Combine a collection of arrays (or other iterable objects) of equal size into one larger array, by arranging them along one or more new dimensions.

By default the axes of the elements are placed first, giving `size(result) = (size(first(iter))..., size(iter)...)`. This has the same order of elements as [`Iterators.flatten`](@ref)`(iter)`.

With keyword `dims::Integer`, instead the `i`th element of `iter` becomes the slice [`selectdim`](@ref)`(result, dims, i)`, so that `size(result, dims) == length(iter)`. In this case `stack` reverses the action of [`eachslice`](@ref) with the same `dims`.

The various [`cat`](@ref) functions also combine arrays. However, these all extend the arrays' existing (possibly trivial) dimensions, rather than placing the arrays along new dimensions. They also accept arrays as separate arguments, rather than a single collection.

!!! compat "Julia 1.9"
    This function requires at least Julia 1.9.


# Examples

```jldoctest
julia> vecs = (1:2, [30, 40], Float32[500, 600]);

julia> mat = stack(vecs)
2×3 Matrix{Float32}:
 1.0  30.0  500.0
 2.0  40.0  600.0

julia> mat == hcat(vecs...) == reduce(hcat, collect(vecs))
true

julia> vec(mat) == vcat(vecs...) == reduce(vcat, collect(vecs))
true

julia> stack(zip(1:4, 10:99))  # accepts any iterators of iterators
2×4 Matrix{Int64}:
  1   2   3   4
 10  11  12  13

julia> vec(ans) == collect(Iterators.flatten(zip(1:4, 10:99)))
true

julia> stack(vecs; dims=1)  # unlike any cat function, 1st axis of vecs[1] is 2nd axis of result
3×2 Matrix{Float32}:
   1.0    2.0
  30.0   40.0
 500.0  600.0

julia> x = rand(3,4);

julia> x == stack(eachcol(x)) == stack(eachrow(x), dims=1)  # inverse of eachslice
true
```

Higher-dimensional examples:

```jldoctest
julia> A = rand(5, 7, 11);

julia> E = eachslice(A, dims=2);  # a vector of matrices

julia> (element = size(first(E)), container = size(E))
(element = (5, 11), container = (7,))

julia> stack(E) |> size
(5, 11, 7)

julia> stack(E) == stack(E; dims=3) == cat(E...; dims=3)
true

julia> A == stack(E; dims=2)
true

julia> M = (fill(10i+j, 2, 3) for i in 1:5, j in 1:7);

julia> (element = size(first(M)), container = size(M))
(element = (2, 3), container = (5, 7))

julia> stack(M) |> size  # keeps all dimensions
(2, 3, 5, 7)

julia> stack(M; dims=1) |> size  # vec(container) along dims=1
(35, 2, 3)

julia> hvcat(5, M...) |> size  # hvcat puts matrices next to each other
(14, 15)
```

```
stack(f, args...; [dims])
```

Apply a function to each element of a collection, and `stack` the result. Or to several collections, [`zip`](@ref)ped together.

The function should return arrays (or tuples, or other iterators) all of the same size. These become slices of the result, each separated along `dims` (if given) or by default along the last dimensions.

See also [`mapslices`](@ref), [`eachcol`](@ref).

# Examples

```jldoctest
julia> stack(c -> (c, c-32), "julia")
2×5 Matrix{Char}:
 'j'  'u'  'l'  'i'  'a'
 'J'  'U'  'L'  'I'  'A'

julia> stack(eachrow([1 2 3; 4 5 6]), (10, 100); dims=1) do row, n
         vcat(row, row .* n, row ./ n)
       end
2×9 Matrix{Float64}:
 1.0  2.0  3.0   10.0   20.0   30.0  0.1   0.2   0.3
 4.0  5.0  6.0  400.0  500.0  600.0  0.04  0.05  0.06
```



stacktrace:
==================================================

```
stacktrace([trace::Vector{Ptr{Cvoid}},] [c_funcs::Bool=false]) -> StackTrace
```

Return a stack trace in the form of a vector of `StackFrame`s. (By default stacktrace doesn't return C functions, but this can be enabled.) When called without specifying a trace, `stacktrace` first calls `backtrace`.



startswith:
==================================================

```
startswith(s::AbstractString, prefix::Union{AbstractString,Base.Chars})
```

Return `true` if `s` starts with `prefix`, which can be a string, a character, or a tuple/vector/set of characters. If `prefix` is a tuple/vector/set of characters, test whether the first character of `s` belongs to that set.

See also [`endswith`](@ref), [`contains`](@ref).

# Examples

```jldoctest
julia> startswith("JuliaLang", "Julia")
true
```

```
startswith(io::IO, prefix::Union{AbstractString,Base.Chars})
```

Check if an `IO` object starts with a prefix, which can be either a string, a character, or a tuple/vector/set of characters.  See also [`peek`](@ref).

```
startswith(prefix)
```

Create a function that checks whether its argument starts with `prefix`, i.e. a function equivalent to `y -> startswith(y, prefix)`.

The returned function is of type `Base.Fix2{typeof(startswith)}`, which can be used to implement specialized methods.

!!! compat "Julia 1.5"
    The single argument `startswith(prefix)` requires at least Julia 1.5.


# Examples

```jldoctest
julia> startswith("Julia")("JuliaLang")
true

julia> startswith("Julia")("Ends with Julia")
false
```

```
startswith(s::AbstractString, prefix::Regex)
```

Return `true` if `s` starts with the regex pattern, `prefix`.

!!! note
    `startswith` does not compile the anchoring into the regular expression, but instead passes the anchoring as `match_option` to PCRE. If compile time is amortized, `occursin(r"^...", s)` is faster than `startswith(s, r"...")`.


See also [`occursin`](@ref) and [`endswith`](@ref).

!!! compat "Julia 1.2"
    This method requires at least Julia 1.2.


# Examples

```jldoctest
julia> startswith("JuliaLang", r"Julia|Romeo")
true
```



stat:
==================================================

```
stat(file)
```

Return a structure whose fields contain information about the file. The fields of the structure are:

| Name    | Type                            | Description                                                        |
|:------- |:------------------------------- |:------------------------------------------------------------------ |
| desc    | `Union{String, Base.OS_HANDLE}` | The path or OS file descriptor                                     |
| size    | `Int64`                         | The size (in bytes) of the file                                    |
| device  | `UInt`                          | ID of the device that contains the file                            |
| inode   | `UInt`                          | The inode number of the file                                       |
| mode    | `UInt`                          | The protection mode of the file                                    |
| nlink   | `Int`                           | The number of hard links to the file                               |
| uid     | `UInt`                          | The user id of the owner of the file                               |
| gid     | `UInt`                          | The group id of the file owner                                     |
| rdev    | `UInt`                          | If this file refers to a device, the ID of the device it refers to |
| blksize | `Int64`                         | The file-system preferred block size for the file                  |
| blocks  | `Int64`                         | The number of 512-byte blocks allocated                            |
| mtime   | `Float64`                       | Unix timestamp of when the file was last modified                  |
| ctime   | `Float64`                       | Unix timestamp of when the file's metadata was changed             |



stderr:
==================================================

No documentation found for public symbol.

# Summary

```
mutable struct Base.TTY
```

# Fields

```
handle    :: Ptr{Nothing}
status    :: Int64
buffer    :: IOBuffer
cond      :: Base.GenericCondition{Base.Threads.SpinLock}
readerror :: Any
sendbuf   :: Union{Nothing, IOBuffer}
lock      :: ReentrantLock
throttle  :: Int64
```

# Supertype Hierarchy

```
Base.TTY <: Base.LibuvStream <: IO <: Any
```



stdin:
==================================================

No documentation found for public symbol.

# Summary

```
mutable struct Base.TTY
```

# Fields

```
handle    :: Ptr{Nothing}
status    :: Int64
buffer    :: IOBuffer
cond      :: Base.GenericCondition{Base.Threads.SpinLock}
readerror :: Any
sendbuf   :: Union{Nothing, IOBuffer}
lock      :: ReentrantLock
throttle  :: Int64
```

# Supertype Hierarchy

```
Base.TTY <: Base.LibuvStream <: IO <: Any
```



stdout:
==================================================

No documentation found for public symbol.

# Summary

```
mutable struct Base.TTY
```

# Fields

```
handle    :: Ptr{Nothing}
status    :: Int64
buffer    :: IOBuffer
cond      :: Base.GenericCondition{Base.Threads.SpinLock}
readerror :: Any
sendbuf   :: Union{Nothing, IOBuffer}
lock      :: ReentrantLock
throttle  :: Int64
```

# Supertype Hierarchy

```
Base.TTY <: Base.LibuvStream <: IO <: Any
```



step:
==================================================

```
step(r)
```

Get the step size of an [`AbstractRange`](@ref) object.

# Examples

```jldoctest
julia> step(1:10)
1

julia> step(1:2:10)
2

julia> step(2.5:0.3:10.9)
0.3

julia> step(range(2.5, stop=10.9, length=85))
0.1
```



stride:
==================================================

```
stride(A, k::Integer)
```

Return the distance in memory (in number of elements) between adjacent elements in dimension `k`.

See also: [`strides`](@ref).

# Examples

```jldoctest
julia> A = fill(1, (3,4,5));

julia> stride(A,2)
3

julia> stride(A,3)
12
```



strides:
==================================================

```
strides(A)
```

Return a tuple of the memory strides in each dimension.

See also: [`stride`](@ref).

# Examples

```jldoctest
julia> A = fill(1, (3,4,5));

julia> strides(A)
(1, 3, 12)
```



string:
==================================================

```
string(n::Integer; base::Integer = 10, pad::Integer = 1)
```

Convert an integer `n` to a string in the given `base`, optionally specifying a number of digits to pad to.

See also [`digits`](@ref), [`bitstring`](@ref), [`count_zeros`](@ref).

# Examples

```jldoctest
julia> string(5, base = 13, pad = 4)
"0005"

julia> string(-13, base = 5, pad = 4)
"-0023"
```

```
string(xs...)
```

Create a string from any values using the [`print`](@ref) function.

`string` should usually not be defined directly. Instead, define a method `print(io::IO, x::MyType)`. If `string(x)` for a certain type needs to be highly efficient, then it may make sense to add a method to `string` and define `print(io::IO, x::MyType) = print(io, string(x))` to ensure the functions are consistent.

See also: [`String`](@ref), [`repr`](@ref), [`sprint`](@ref), [`show`](@ref @show).

# Examples

```jldoctest
julia> string("a", 1, true)
"a1true"
```



strip:
==================================================

```
strip([pred=isspace,] str::AbstractString) -> SubString
strip(str::AbstractString, chars) -> SubString
```

Remove leading and trailing characters from `str`, either those specified by `chars` or those for which the function `pred` returns `true`.

The default behaviour is to remove leading and trailing whitespace and delimiters: see [`isspace`](@ref) for precise details.

The optional `chars` argument specifies which characters to remove: it can be a single character, vector or set of characters.

See also [`lstrip`](@ref) and [`rstrip`](@ref).

!!! compat "Julia 1.2"
    The method which accepts a predicate function requires Julia 1.2 or later.


# Examples

```jldoctest
julia> strip("{3, 5}\n", ['{', '}', '\n'])
"3, 5"
```



subtypes:
==================================================

```
subtypes(T::DataType)
```

Return a list of immediate subtypes of DataType `T`. Note that all currently loaded subtypes are included, including those not visible in the current module.

See also [`supertype`](@ref), [`supertypes`](@ref), [`methodswith`](@ref).

# Examples

```jldoctest
julia> subtypes(Integer)
3-element Vector{Any}:
 Bool
 Signed
 Unsigned
```



success:
==================================================

```
success(command)
```

Run a command object, constructed with backticks (see the [Running External Programs](@ref) section in the manual), and tell whether it was successful (exited with a code of 0). An exception is raised if the process cannot be started.



sum:
==================================================

```
sum(f, itr; [init])
```

Sum the results of calling function `f` on each element of `itr`.

The return type is `Int` for signed integers of less than system word size, and `UInt` for unsigned integers of less than system word size.  For all other arguments, a common return type is found to which all arguments are promoted.

The value returned for empty `itr` can be specified by `init`. It must be the additive identity (i.e. zero) as it is unspecified whether `init` is used for non-empty collections.

!!! compat "Julia 1.6"
    Keyword argument `init` requires Julia 1.6 or later.


# Examples

```jldoctest
julia> sum(abs2, [2; 3; 4])
29
```

Note the important difference between `sum(A)` and `reduce(+, A)` for arrays with small integer eltype:

```jldoctest
julia> sum(Int8[100, 28])
128

julia> reduce(+, Int8[100, 28])
-128
```

In the former case, the integers are widened to system word size and therefore the result is 128. In the latter case, no such widening happens and integer overflow results in -128.

```
sum(itr; [init])
```

Return the sum of all elements in a collection.

The return type is `Int` for signed integers of less than system word size, and `UInt` for unsigned integers of less than system word size.  For all other arguments, a common return type is found to which all arguments are promoted.

The value returned for empty `itr` can be specified by `init`. It must be the additive identity (i.e. zero) as it is unspecified whether `init` is used for non-empty collections.

!!! compat "Julia 1.6"
    Keyword argument `init` requires Julia 1.6 or later.


See also: [`reduce`](@ref), [`mapreduce`](@ref), [`count`](@ref), [`union`](@ref).

# Examples

```jldoctest
julia> sum(1:20)
210

julia> sum(1:20; init = 0.0)
210.0
```

```
sum(A::AbstractArray; dims)
```

Sum elements of an array over the given dimensions.

# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> sum(A, dims=1)
1×2 Matrix{Int64}:
 4  6

julia> sum(A, dims=2)
2×1 Matrix{Int64}:
 3
 7
```

```
sum(f, A::AbstractArray; dims)
```

Sum the results of calling function `f` on each element of an array over the given dimensions.

# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> sum(abs2, A, dims=1)
1×2 Matrix{Int64}:
 10  20

julia> sum(abs2, A, dims=2)
2×1 Matrix{Int64}:
  5
 25
```



sum!:
==================================================

```
sum!(r, A)
```

Sum elements of `A` over the singleton dimensions of `r`, and write results to `r`.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> sum!([1; 1], A)
2-element Vector{Int64}:
 3
 7

julia> sum!([1 1], A)
1×2 Matrix{Int64}:
 4  6
```



summary:
==================================================

```
summary(io::IO, x)
str = summary(x)
```

Print to a stream `io`, or return a string `str`, giving a brief description of a value. By default returns `string(typeof(x))`, e.g. [`Int64`](@ref).

For arrays, returns a string of size and type info, e.g. `10-element Array{Int64,1}`.

# Examples

```jldoctest
julia> summary(1)
"Int64"

julia> summary(zeros(2))
"2-element Vector{Float64}"
```



supertype:
==================================================

```
supertype(T::DataType)
```

Return the supertype of DataType `T`.

# Examples

```jldoctest
julia> supertype(Int32)
Signed
```



supertypes:
==================================================

```
supertypes(T::Type)
```

Return a tuple `(T, ..., Any)` of `T` and all its supertypes, as determined by successive calls to the [`supertype`](@ref) function, listed in order of `<:` and terminated by `Any`.

See also [`subtypes`](@ref).

# Examples

```jldoctest
julia> supertypes(Int)
(Int64, Signed, Integer, Real, Number, Any)
```



swapfield!:
==================================================

```
swapfield!(value, name::Symbol, x, [order::Symbol])
swapfield!(value, i::Int, x, [order::Symbol])
```

Atomically perform the operations to simultaneously get and set a field:

```
y = getfield(value, name)
setfield!(value, name, x)
return y
```

!!! compat "Julia 1.7"
    This function requires Julia 1.7 or later.




swapglobal!:
==================================================

```
swapglobal!(module::Module, name::Symbol, x, [order::Symbol=:monotonic])
```

Atomically perform the operations to simultaneously get and set a global.

!!! compat "Julia 1.11"
    This function requires Julia 1.11 or later.


See also [`swapproperty!`](@ref Base.swapproperty!) and [`setglobal!`](@ref).



swapproperty!:
==================================================

```
swapproperty!(x, f::Symbol, v, order::Symbol=:not_atomic)
```

The syntax `@atomic a.b, _ = c, a.b` returns `(c, swapproperty!(a, :b, c, :sequentially_consistent))`, where there must be one `getproperty` expression common to both sides.

See also [`swapfield!`](@ref Core.swapfield!) and [`setproperty!`](@ref Base.setproperty!).



symdiff:
==================================================

```
symdiff(s, itrs...)
```

Construct the symmetric difference of elements in the passed in sets. When `s` is not an `AbstractSet`, the order is maintained.

See also [`symdiff!`](@ref), [`setdiff`](@ref), [`union`](@ref) and [`intersect`](@ref).

# Examples

```jldoctest
julia> symdiff([1,2,3], [3,4,5], [4,5,6])
3-element Vector{Int64}:
 1
 2
 6

julia> symdiff([1,2,1], [2, 1, 2])
Int64[]
```



symdiff!:
==================================================

```
symdiff!(s::Union{AbstractSet,AbstractVector}, itrs...)
```

Construct the symmetric difference of the passed in sets, and overwrite `s` with the result. When `s` is an array, the order is maintained. Note that in this case the multiplicity of elements matters.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.




symlink:
==================================================

```
symlink(target::AbstractString, link::AbstractString; dir_target = false)
```

Creates a symbolic link to `target` with the name `link`.

On Windows, symlinks must be explicitly declared as referring to a directory or not.  If `target` already exists, by default the type of `link` will be auto- detected, however if `target` does not exist, this function defaults to creating a file symlink unless `dir_target` is set to `true`.  Note that if the user sets `dir_target` but `target` exists and is a file, a directory symlink will still be created, but dereferencing the symlink will fail, just as if the user creates a file symlink (by calling `symlink()` with `dir_target` set to `false` before the directory is created) and tries to dereference it to a directory.

Additionally, there are two methods of making a link on Windows; symbolic links and junction points.  Junction points are slightly more efficient, but do not support relative paths, so if a relative directory symlink is requested (as denoted by `isabspath(target)` returning `false`) a symlink will be used, else a junction point will be used.  Best practice for creating symlinks on Windows is to create them only after the files/directories they reference are already created.

See also: [`hardlink`](@ref).

!!! note
    This function raises an error under operating systems that do not support soft symbolic links, such as Windows XP.


!!! compat "Julia 1.6"
    The `dir_target` keyword argument was added in Julia 1.6.  Prior to this, symlinks to nonexistent paths on windows would always be file symlinks, and relative symlinks to directories were not supported.




systemerror:
==================================================

```
systemerror(sysfunc[, errno::Cint=Libc.errno()])
systemerror(sysfunc, iftrue::Bool)
```

Raises a `SystemError` for `errno` with the descriptive string `sysfunc` if `iftrue` is `true`



take!:
==================================================

```
take!(b::IOBuffer)
```

Obtain the contents of an `IOBuffer` as an array. Afterwards, the `IOBuffer` is reset to its initial state.

# Examples

```jldoctest
julia> io = IOBuffer();

julia> write(io, "JuliaLang is a GitHub organization.", " It has many members.")
56

julia> String(take!(io))
"JuliaLang is a GitHub organization. It has many members."
```

```
take!(c::Channel)
```

Removes and returns a value from a [`Channel`](@ref) in order. Blocks until data is available. For unbuffered channels, blocks until a [`put!`](@ref) is performed by a different task.

# Examples

Buffered channel:

```jldoctest
julia> c = Channel(1);

julia> put!(c, 1);

julia> take!(c)
1
```

Unbuffered channel:

```jldoctest
julia> c = Channel(0);

julia> task = Task(() -> put!(c, 1));

julia> schedule(task);

julia> take!(c)
1
```



tan:
==================================================

```
tan(x)
```

Compute tangent of `x`, where `x` is in radians.

```
tan(A::AbstractMatrix)
```

Compute the matrix tangent of a square matrix `A`.

If `A` is symmetric or Hermitian, its eigendecomposition ([`eigen`](@ref)) is used to compute the tangent. Otherwise, the tangent is determined by calling [`exp`](@ref).

# Examples

```jldoctest
julia> tan(fill(1.0, (2,2)))
2×2 Matrix{Float64}:
 -1.09252  -1.09252
 -1.09252  -1.09252
```



tand:
==================================================

```
tand(x)
```

Compute tangent of `x`, where `x` is in degrees. If `x` is a matrix, `x` needs to be a square matrix.

!!! compat "Julia 1.7"
    Matrix arguments require Julia 1.7 or later.




tanh:
==================================================

```
tanh(x)
```

Compute hyperbolic tangent of `x`.

See also [`tan`](@ref), [`atanh`](@ref).

# Examples

```jldoctest
julia> tanh.(-3:3f0)  # Here 3f0 isa Float32
7-element Vector{Float32}:
 -0.9950548
 -0.9640276
 -0.7615942
  0.0
  0.7615942
  0.9640276
  0.9950548

julia> tan.(im .* (1:3))
3-element Vector{ComplexF64}:
 0.0 + 0.7615941559557649im
 0.0 + 0.9640275800758169im
 0.0 + 0.9950547536867306im
```

```
tanh(A::AbstractMatrix)
```

Compute the matrix hyperbolic tangent of a square matrix `A`.



tanpi:
==================================================

```
tanpi(x)
```

Compute $\tan(\pi x)$ more accurately than `tan(pi*x)`, especially for large `x`.

!!! compat "Julia 1.10"
    This function requires at least Julia 1.10.


See also [`tand`](@ref), [`sinpi`](@ref), [`cospi`](@ref), [`sincospi`](@ref).



task_local_storage:
==================================================

```
task_local_storage(key)
```

Look up the value of a key in the current task's task-local storage.

```
task_local_storage(key, value)
```

Assign a value to a key in the current task's task-local storage.

```
task_local_storage(body, key, value)
```

Call the function `body` with a modified task-local storage, in which `value` is assigned to `key`; the previous value of `key`, or lack thereof, is restored afterwards. Useful for emulating dynamic scoping.



tempdir:
==================================================

```
tempdir()
```

Gets the path of the temporary directory. On Windows, `tempdir()` uses the first environment variable found in the ordered list `TMP`, `TEMP`, `USERPROFILE`. On all other operating systems, `tempdir()` uses the first environment variable found in the ordered list `TMPDIR`, `TMP`, `TEMP`, and `TEMPDIR`. If none of these are found, the path `"/tmp"` is used.



tempname:
==================================================

```
tempname(parent=tempdir(); cleanup=true) -> String
```

Generate a temporary file path. This function only returns a path; no file is created. The path is likely to be unique, but this cannot be guaranteed due to the very remote possibility of two simultaneous calls to `tempname` generating the same file name. The name is guaranteed to differ from all files already existing at the time of the call to `tempname`.

When called with no arguments, the temporary name will be an absolute path to a temporary name in the system temporary directory as given by `tempdir()`. If a `parent` directory argument is given, the temporary path will be in that directory instead.

The `cleanup` option controls whether the process attempts to delete the returned path automatically when the process exits. Note that the `tempname` function does not create any file or directory at the returned location, so there is nothing to cleanup unless you create a file or directory there. If you do and `cleanup` is `true` it will be deleted upon process termination.

!!! compat "Julia 1.4"
    The `parent` and `cleanup` arguments were added in 1.4. Prior to Julia 1.4 the path `tempname` would never be cleaned up at process termination.


!!! warning
    This can lead to security holes if another process obtains the same file name and creates the file before you are able to. Open the file with `JL_O_EXCL` if this is a concern. Using [`mktemp()`](@ref) is also recommended instead.




textwidth:
==================================================

```
textwidth(c)
```

Give the number of columns needed to print a character.

# Examples

```jldoctest
julia> textwidth('α')
1

julia> textwidth('⛵')
2
```

```
textwidth(s::AbstractString)
```

Give the number of columns needed to print a string.

# Examples

```jldoctest
julia> textwidth("March")
5
```



thisind:
==================================================

```
thisind(s::AbstractString, i::Integer) -> Int
```

If `i` is in bounds in `s` return the index of the start of the character whose encoding code unit `i` is part of. In other words, if `i` is the start of a character, return `i`; if `i` is not the start of a character, rewind until the start of a character and return that index. If `i` is equal to 0 or `ncodeunits(s)+1` return `i`. In all other cases throw `BoundsError`.

# Examples

```jldoctest
julia> thisind("α", 0)
0

julia> thisind("α", 1)
1

julia> thisind("α", 2)
1

julia> thisind("α", 3)
3

julia> thisind("α", 4)
ERROR: BoundsError: attempt to access 2-codeunit String at index [4]
[...]

julia> thisind("α", -1)
ERROR: BoundsError: attempt to access 2-codeunit String at index [-1]
[...]
```



throw:
==================================================

```
throw(e)
```

Throw an object as an exception.

See also: [`rethrow`](@ref), [`error`](@ref).



time:
==================================================

```
time(t::TmStruct) -> Float64
```

Converts a `TmStruct` struct to a number of seconds since the epoch.

```
time() -> Float64
```

Get the system time in seconds since the epoch, with fairly high (typically, microsecond) resolution.



time_ns:
==================================================

```
time_ns() -> UInt64
```

Get the time in nanoseconds. The time corresponding to 0 is undefined, and wraps every 5.8 years.



timedwait:
==================================================

```
timedwait(testcb, timeout::Real; pollint::Real=0.1)
```

Wait until `testcb()` returns `true` or `timeout` seconds have passed, whichever is earlier. The test function is polled every `pollint` seconds. The minimum value for `pollint` is 0.001 seconds, that is, 1 millisecond.

Return `:ok` or `:timed_out`.

# Examples

```jldoctest
julia> cb() = (sleep(5); return);

julia> t = @async cb();

julia> timedwait(()->istaskdone(t), 1)
:timed_out

julia> timedwait(()->istaskdone(t), 6.5)
:ok
```



titlecase:
==================================================

```
titlecase(c::AbstractChar)
```

Convert `c` to titlecase. This may differ from uppercase for digraphs, compare the example below.

See also [`uppercase`](@ref), [`lowercase`](@ref).

# Examples

```jldoctest
julia> titlecase('a')
'A': ASCII/Unicode U+0041 (category Lu: Letter, uppercase)

julia> titlecase('ǆ')
'ǅ': Unicode U+01C5 (category Lt: Letter, titlecase)

julia> uppercase('ǆ')
'Ǆ': Unicode U+01C4 (category Lu: Letter, uppercase)
```

```
titlecase(s::AbstractString; [wordsep::Function], strict::Bool=true) -> String
```

Capitalize the first character of each word in `s`; if `strict` is true, every other character is converted to lowercase, otherwise they are left unchanged. By default, all non-letters beginning a new grapheme are considered as word separators; a predicate can be passed as the `wordsep` keyword to determine which characters should be considered as word separators. See also [`uppercasefirst`](@ref) to capitalize only the first character in `s`.

See also [`uppercase`](@ref), [`lowercase`](@ref), [`uppercasefirst`](@ref).

# Examples

```jldoctest
julia> titlecase("the JULIA programming language")
"The Julia Programming Language"

julia> titlecase("ISS - international space station", strict=false)
"ISS - International Space Station"

julia> titlecase("a-a b-b", wordsep = c->c==' ')
"A-a B-b"
```



to_indices:
==================================================

```
to_indices(A, I::Tuple)
```

Convert the tuple `I` to a tuple of indices for use in indexing into array `A`.

The returned tuple must only contain either `Int`s or `AbstractArray`s of scalar indices that are supported by array `A`. It will error upon encountering a novel index type that it does not know how to process.

For simple index types, it defers to the unexported `Base.to_index(A, i)` to process each index `i`. While this internal function is not intended to be called directly, `Base.to_index` may be extended by custom array or index types to provide custom indexing behaviors.

More complicated index types may require more context about the dimension into which they index. To support those cases, `to_indices(A, I)` calls `to_indices(A, axes(A), I)`, which then recursively walks through both the given tuple of indices and the dimensional indices of `A` in tandem. As such, not all index types are guaranteed to propagate to `Base.to_index`.

# Examples

```jldoctest
julia> A = zeros(1,2,3,4);

julia> to_indices(A, (1,1,2,2))
(1, 1, 2, 2)

julia> to_indices(A, (1,1,2,20)) # no bounds checking
(1, 1, 2, 20)

julia> to_indices(A, (CartesianIndex((1,)), 2, CartesianIndex((3,4)))) # exotic index
(1, 2, 3, 4)

julia> to_indices(A, ([1,1], 1:2, 3, 4))
([1, 1], 1:2, 3, 4)

julia> to_indices(A, (1,2)) # no shape checking
(1, 2)
```



touch:
==================================================

```
touch(path::AbstractString)
touch(fd::File)
```

Update the last-modified timestamp on a file to the current time.

If the file does not exist a new file is created.

Return `path`.

# Examples

```julia-repl
julia> write("my_little_file", 2);

julia> mtime("my_little_file")
1.5273815391135583e9

julia> touch("my_little_file");

julia> mtime("my_little_file")
1.527381559163435e9
```

We can see the [`mtime`](@ref) has been modified by `touch`.

```
Base.touch(::Pidfile.LockMonitor)
```

Update the `mtime` on the lock, to indicate it is still fresh.

See also the `refresh` keyword in the [`mkpidlock`](@ref) constructor.



trailing_ones:
==================================================

```
trailing_ones(x::Integer) -> Integer
```

Number of ones trailing the binary representation of `x`.

# Examples

```jldoctest
julia> trailing_ones(3)
2
```



trailing_zeros:
==================================================

```
trailing_zeros(x::Integer) -> Integer
```

Number of zeros trailing the binary representation of `x`.

# Examples

```jldoctest
julia> trailing_zeros(2)
1
```



transcode:
==================================================

```
transcode(T, src)
```

Convert string data between Unicode encodings. `src` is either a `String` or a `Vector{UIntXX}` of UTF-XX code units, where `XX` is 8, 16, or 32. `T` indicates the encoding of the return value: `String` to return a (UTF-8 encoded) `String` or `UIntXX` to return a `Vector{UIntXX}` of UTF-`XX` data. (The alias [`Cwchar_t`](@ref) can also be used as the integer type, for converting `wchar_t*` strings used by external C libraries.)

The `transcode` function succeeds as long as the input data can be reasonably represented in the target encoding; it always succeeds for conversions between UTF-XX encodings, even for invalid Unicode data.

Only conversion to/from UTF-8 is currently supported.

# Examples

```jldoctest
julia> str = "αβγ"
"αβγ"

julia> transcode(UInt16, str)
3-element Vector{UInt16}:
 0x03b1
 0x03b2
 0x03b3

julia> transcode(String, transcode(UInt16, str))
"αβγ"
```



transpose:
==================================================

```
transpose(A)
```

Lazy transpose. Mutating the returned object should appropriately mutate `A`. Often, but not always, yields `Transpose(A)`, where `Transpose` is a lazy transpose wrapper. Note that this operation is recursive.

This operation is intended for linear algebra usage - for general data manipulation see [`permutedims`](@ref Base.permutedims), which is non-recursive.

# Examples

```jldoctest
julia> A = [3 2; 0 0]
2×2 Matrix{Int64}:
 3  2
 0  0

julia> B = transpose(A)
2×2 transpose(::Matrix{Int64}) with eltype Int64:
 3  0
 2  0

julia> B isa Transpose
true

julia> transpose(B) === A # the transpose of a transpose unwraps the parent
true

julia> Transpose(B) # however, the constructor always wraps its argument
2×2 transpose(transpose(::Matrix{Int64})) with eltype Int64:
 3  2
 0  0

julia> B[1,2] = 4; # modifying B will modify A automatically

julia> A
2×2 Matrix{Int64}:
 3  2
 4  0
```

For complex matrices, the `adjoint` operation is equivalent to a conjugate-transpose.

```jldoctest
julia> A = reshape([Complex(x, x) for x in 1:4], 2, 2)
2×2 Matrix{Complex{Int64}}:
 1+1im  3+3im
 2+2im  4+4im

julia> adjoint(A) == conj(transpose(A))
true
```

The `transpose` of an `AbstractVector` is a row-vector:

```jldoctest
julia> v = [1,2,3]
3-element Vector{Int64}:
 1
 2
 3

julia> transpose(v) # returns a row-vector
1×3 transpose(::Vector{Int64}) with eltype Int64:
 1  2  3

julia> transpose(v) * v # compute the dot product
14
```

For a matrix of matrices, the individual blocks are recursively operated on:

```jldoctest
julia> C = [1 3; 2 4]
2×2 Matrix{Int64}:
 1  3
 2  4

julia> D = reshape([C, 2C, 3C, 4C], 2, 2) # construct a block matrix
2×2 Matrix{Matrix{Int64}}:
 [1 3; 2 4]  [3 9; 6 12]
 [2 6; 4 8]  [4 12; 8 16]

julia> transpose(D) # blocks are recursively transposed
2×2 transpose(::Matrix{Matrix{Int64}}) with eltype Transpose{Int64, Matrix{Int64}}:
 [1 2; 3 4]   [2 4; 6 8]
 [3 6; 9 12]  [4 8; 12 16]
```

```
transpose(F::Factorization)
```

Lazy transpose of the factorization `F`. By default, returns a [`TransposeFactorization`](@ref), except for `Factorization`s with real `eltype`, in which case returns an [`AdjointFactorization`](@ref).



trues:
==================================================

```
trues(dims)
```

Create a `BitArray` with all values set to `true`.

# Examples

```jldoctest
julia> trues(2,3)
2×3 BitMatrix:
 1  1  1
 1  1  1
```



trunc:
==================================================

```
trunc([T,] x)
trunc(x; digits::Integer= [, base = 10])
trunc(x; sigdigits::Integer= [, base = 10])
```

`trunc(x)` returns the nearest integral value of the same type as `x` whose absolute value is less than or equal to the absolute value of `x`.

`trunc(T, x)` converts the result to type `T`, throwing an `InexactError` if the truncated value is not representable a `T`.

Keywords `digits`, `sigdigits` and `base` work as for [`round`](@ref).

To support `trunc` for a new type, define `Base.round(x::NewType, ::RoundingMode{:ToZero})`.

See also: [`%`](@ref rem), [`floor`](@ref), [`unsigned`](@ref), [`unsafe_trunc`](@ref).

# Examples

```jldoctest
julia> trunc(2.22)
2.0

julia> trunc(-2.22, digits=1)
-2.2

julia> trunc(Int, -2.22)
-2
```

```
trunc(dt::TimeType, ::Type{Period}) -> TimeType
```

Truncates the value of `dt` according to the provided `Period` type.

# Examples

```jldoctest
julia> trunc(DateTime("1996-01-01T12:30:00"), Day)
1996-01-01T00:00:00
```



truncate:
==================================================

```
truncate(file, n)
```

Resize the file or buffer given by the first argument to exactly `n` bytes, filling previously unallocated space with '\0' if the file or buffer is grown.

# Examples

```jldoctest
julia> io = IOBuffer();

julia> write(io, "JuliaLang is a GitHub organization.")
35

julia> truncate(io, 15)
IOBuffer(data=UInt8[...], readable=true, writable=true, seekable=true, append=false, size=15, maxsize=Inf, ptr=16, mark=-1)

julia> String(take!(io))
"JuliaLang is a "

julia> io = IOBuffer();

julia> write(io, "JuliaLang is a GitHub organization.");

julia> truncate(io, 40);

julia> String(take!(io))
"JuliaLang is a GitHub organization.\0\0\0\0\0"
```



trylock:
==================================================

```
trylock(lock) -> Success (Boolean)
```

Acquire the lock if it is available, and return `true` if successful. If the lock is already locked by a different task/thread, return `false`.

Each successful `trylock` must be matched by an [`unlock`](@ref).

Function `trylock` combined with [`islocked`](@ref) can be used for writing the test-and-test-and-set or exponential backoff algorithms *if it is supported by the `typeof(lock)`* (read its documentation).



tryparse:
==================================================

```
tryparse(type, str; base)
```

Like [`parse`](@ref), but returns either a value of the requested type, or [`nothing`](@ref) if the string does not contain a valid number.

```
tryparse(::Type{SimpleColor}, rgb::String)
```

Attempt to parse `rgb` as a `SimpleColor`. If `rgb` starts with `#` and has a length of 7, it is converted into a `RGBTuple`-backed `SimpleColor`. If `rgb` starts with `a`-`z`, `rgb` is interpreted as a color name and converted to a `Symbol`-backed `SimpleColor`.

Otherwise, `nothing` is returned.

# Examples

```jldoctest; setup = :(import StyledStrings.SimpleColor)
julia> tryparse(SimpleColor, "blue")
SimpleColor(blue)

julia> tryparse(SimpleColor, "#9558b2")
SimpleColor(#9558b2)

julia> tryparse(SimpleColor, "#nocolor")
```



tuple:
==================================================

```
tuple(xs...)
```

Construct a tuple of the given objects.

See also [`Tuple`](@ref), [`ntuple`](@ref), [`NamedTuple`](@ref).

# Examples

```jldoctest
julia> tuple(1, 'b', pi)
(1, 'b', π)

julia> ans === (1, 'b', π)
true

julia> Tuple(Real[1, 2, pi])  # takes a collection
(1, 2, π)
```



typeassert:
==================================================

```
typeassert(x, type)
```

Throw a [`TypeError`](@ref) unless `x isa type`. The syntax `x::type` calls this function.

# Examples

```jldoctest
julia> typeassert(2.5, Int)
ERROR: TypeError: in typeassert, expected Int64, got a value of type Float64
Stacktrace:
[...]
```



typeintersect:
==================================================

```
typeintersect(T::Type, S::Type)
```

Compute a type that contains the intersection of `T` and `S`. Usually this will be the smallest such type or one close to it.

A special case where exact behavior is guaranteed: when `T <: S`, `typeintersect(S, T) == T == typeintersect(T, S)`.



typejoin:
==================================================

```
typejoin(T, S, ...)
```

Return the closest common ancestor of types `T` and `S`, i.e. the narrowest type from which they both inherit. Recurses on additional varargs.

# Examples

```jldoctest
julia> typejoin(Int, Float64)
Real

julia> typejoin(Int, Float64, ComplexF32)
Number
```



typemax:
==================================================

```
typemax(T)
```

The highest value representable by the given (real) numeric `DataType`.

See also: [`floatmax`](@ref), [`typemin`](@ref), [`eps`](@ref).

# Examples

```jldoctest
julia> typemax(Int8)
127

julia> typemax(UInt32)
0xffffffff

julia> typemax(Float64)
Inf

julia> typemax(Float32)
Inf32

julia> floatmax(Float32)  # largest finite Float32 floating point number
3.4028235f38
```



typemin:
==================================================

```
typemin(T)
```

The lowest value representable by the given (real) numeric DataType `T`.

See also: [`floatmin`](@ref), [`typemax`](@ref), [`eps`](@ref).

# Examples

```jldoctest
julia> typemin(Int8)
-128

julia> typemin(UInt32)
0x00000000

julia> typemin(Float16)
-Inf16

julia> typemin(Float32)
-Inf32

julia> nextfloat(-Inf32)  # smallest finite Float32 floating point number
-3.4028235f38
```



typeof:
==================================================

```
typeof(x)
```

Get the concrete type of `x`.

See also [`eltype`](@ref).

# Examples

```jldoctest
julia> a = 1//2;

julia> typeof(a)
Rational{Int64}

julia> M = [1 2; 3.5 4];

julia> typeof(M)
Matrix{Float64} (alias for Array{Float64, 2})
```



undef:
==================================================

```
UndefInitializer
```

Singleton type used in array initialization, indicating the array-constructor-caller would like an uninitialized array. See also [`undef`](@ref), an alias for `UndefInitializer()`.

# Examples

```julia-repl
julia> Array{Float64, 1}(UndefInitializer(), 3)
3-element Array{Float64, 1}:
 2.2752528595e-314
 2.202942107e-314
 2.275252907e-314
```



unescape_string:
==================================================

```
unescape_string(str::AbstractString, keep = ())::AbstractString
unescape_string(io, s::AbstractString, keep = ())::Nothing
```

General unescaping of traditional C and Unicode escape sequences. The first form returns the escaped string, the second prints the result to `io`. The argument `keep` specifies a collection of characters which (along with backlashes) are to be kept as they are.

The following escape sequences are recognised:

  * Escaped backslash (`\\`)
  * Escaped double-quote (`\"`)
  * Standard C escape sequences (`\a`, `\b`, `\t`, `\n`, `\v`, `\f`, `\r`, `\e`)
  * Unicode BMP code points (`\u` with 1-4 trailing hex digits)
  * All Unicode code points (`\U` with 1-8 trailing hex digits; max value = 0010ffff)
  * Hex bytes (`\x` with 1-2 trailing hex digits)
  * Octal bytes (`\` with 1-3 trailing octal digits)

See also [`escape_string`](@ref).

# Examples

```jldoctest
julia> unescape_string("aaa\\nbbb") # C escape sequence
"aaa\nbbb"

julia> unescape_string("\\u03c0") # unicode
"π"

julia> unescape_string("\\101") # octal
"A"

julia> unescape_string("aaa \\g \\n", ['g']) # using `keep` argument
"aaa \\g \n"
```



union:
==================================================

```
union(s, itrs...)
∪(s, itrs...)
```

Construct an object containing all distinct elements from all of the arguments.

The first argument controls what kind of container is returned. If this is an array, it maintains the order in which elements first appear.

Unicode `∪` can be typed by writing `\cup` then pressing tab in the Julia REPL, and in many editors. This is an infix operator, allowing `s ∪ itr`.

See also [`unique`](@ref), [`intersect`](@ref), [`isdisjoint`](@ref), [`vcat`](@ref), [`Iterators.flatten`](@ref).

# Examples

```jldoctest
julia> union([1, 2], [3])
3-element Vector{Int64}:
 1
 2
 3

julia> union([4 2 3 4 4], 1:3, 3.0)
4-element Vector{Float64}:
 4.0
 2.0
 3.0
 1.0

julia> (0, 0.0) ∪ (-0.0, NaN)
3-element Vector{Real}:
   0
  -0.0
 NaN

julia> union(Set([1, 2]), 2:3)
Set{Int64} with 3 elements:
  2
  3
  1
```



union!:
==================================================

```
union!(s::Union{AbstractSet,AbstractVector}, itrs...)
```

Construct the [`union`](@ref) of passed in sets and overwrite `s` with the result. Maintain order with arrays.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


# Examples

```jldoctest
julia> a = Set([3, 4, 5]);

julia> union!(a, 1:2:7);

julia> a
Set{Int64} with 5 elements:
  5
  4
  7
  3
  1
```



unique:
==================================================

```
unique(itr)
```

Return an array containing only the unique elements of collection `itr`, as determined by [`isequal`](@ref) and [`hash`](@ref), in the order that the first of each set of equivalent elements originally appears. The element type of the input is preserved.

See also: [`unique!`](@ref), [`allunique`](@ref), [`allequal`](@ref).

# Examples

```jldoctest
julia> unique([1, 2, 6, 2])
3-element Vector{Int64}:
 1
 2
 6

julia> unique(Real[1, 1.0, 2])
2-element Vector{Real}:
 1
 2
```

```
unique(f, itr)
```

Return an array containing one value from `itr` for each unique value produced by `f` applied to elements of `itr`.

# Examples

```jldoctest
julia> unique(x -> x^2, [1, -1, 3, -3, 4])
3-element Vector{Int64}:
 1
 3
 4
```

This functionality can also be used to extract the *indices* of the first occurrences of unique elements in an array:

```jldoctest
julia> a = [3.1, 4.2, 5.3, 3.1, 3.1, 3.1, 4.2, 1.7];

julia> i = unique(i -> a[i], eachindex(a))
4-element Vector{Int64}:
 1
 2
 3
 8

julia> a[i]
4-element Vector{Float64}:
 3.1
 4.2
 5.3
 1.7

julia> a[i] == unique(a)
true
```

```
unique(A::AbstractArray; dims::Int)
```

Return unique regions of `A` along dimension `dims`.

# Examples

```jldoctest
julia> A = map(isodd, reshape(Vector(1:8), (2,2,2)))
2×2×2 Array{Bool, 3}:
[:, :, 1] =
 1  1
 0  0

[:, :, 2] =
 1  1
 0  0

julia> unique(A)
2-element Vector{Bool}:
 1
 0

julia> unique(A, dims=2)
2×1×2 Array{Bool, 3}:
[:, :, 1] =
 1
 0

[:, :, 2] =
 1
 0

julia> unique(A, dims=3)
2×2×1 Array{Bool, 3}:
[:, :, 1] =
 1  1
 0  0
```



unique!:
==================================================

```
unique!(f, A::AbstractVector)
```

Selects one value from `A` for each unique value produced by `f` applied to elements of `A`, then return the modified A.

!!! compat "Julia 1.1"
    This method is available as of Julia 1.1.


# Examples

```jldoctest
julia> unique!(x -> x^2, [1, -1, 3, -3, 4])
3-element Vector{Int64}:
 1
 3
 4

julia> unique!(n -> n%3, [5, 1, 8, 9, 3, 4, 10, 7, 2, 6])
3-element Vector{Int64}:
 5
 1
 9

julia> unique!(iseven, [2, 3, 5, 7, 9])
2-element Vector{Int64}:
 2
 3
```

```
unique!(A::AbstractVector)
```

Remove duplicate items as determined by [`isequal`](@ref) and [`hash`](@ref), then return the modified `A`. `unique!` will return the elements of `A` in the order that they occur. If you do not care about the order of the returned data, then calling `(sort!(A); unique!(A))` will be much more efficient as long as the elements of `A` can be sorted.

# Examples

```jldoctest
julia> unique!([1, 1, 1])
1-element Vector{Int64}:
 1

julia> A = [7, 3, 2, 3, 7, 5];

julia> unique!(A)
4-element Vector{Int64}:
 7
 3
 2
 5

julia> B = [7, 6, 42, 6, 7, 42];

julia> sort!(B);  # unique! is able to process sorted data much more efficiently.

julia> unique!(B)
3-element Vector{Int64}:
  6
  7
 42
```



unlock:
==================================================

```
unlock(lock)
```

Releases ownership of the `lock`.

If this is a recursive lock which has been acquired before, decrement an internal counter and return immediately.



unmark:
==================================================

```
unmark(s::IO)
```

Remove a mark from stream `s`. Return `true` if the stream was marked, `false` otherwise.

See also [`mark`](@ref), [`reset`](@ref), [`ismarked`](@ref).



unsafe_copyto!:
==================================================

```
unsafe_copyto!(dest::Ptr{T}, src::Ptr{T}, N)
```

Copy `N` elements from a source pointer to a destination, with no checking. The size of an element is determined by the type of the pointers.

The `unsafe` prefix on this function indicates that no validation is performed on the pointers `dest` and `src` to ensure that they are valid. Incorrect usage may corrupt or segfault your program, in the same manner as C.

```
unsafe_copyto!(dest::Array, do, src::Array, so, N)
```

Copy `N` elements from a source array to a destination, starting at the linear index `so` in the source and `do` in the destination (1-indexed).

The `unsafe` prefix on this function indicates that no validation is performed to ensure that N is inbounds on either array. Incorrect usage may corrupt or segfault your program, in the same manner as C.



unsafe_load:
==================================================

```
unsafe_load(p::Ptr{T}, i::Integer=1)
unsafe_load(p::Ptr{T}, order::Symbol)
unsafe_load(p::Ptr{T}, i::Integer, order::Symbol)
```

Load a value of type `T` from the address of the `i`th element (1-indexed) starting at `p`. This is equivalent to the C expression `p[i-1]`. Optionally, an atomic memory ordering can be provided.

The `unsafe` prefix on this function indicates that no validation is performed on the pointer `p` to ensure that it is valid. Like C, the programmer is responsible for ensuring that referenced memory is not freed or garbage collected while invoking this function. Incorrect usage may segfault your program or return garbage answers. Unlike C, dereferencing memory region allocated as different type may be valid provided that the types are compatible.

!!! compat "Julia 1.10"
    The `order` argument is available as of Julia 1.10.


See also: [`atomic`](@ref)



unsafe_modify!:
==================================================

```
unsafe_modify!(p::Ptr{T}, op, x, [order::Symbol]) -> Pair
```

These atomically perform the operations to get and set a memory address after applying the function `op`. If supported by the hardware (for example, atomic increment), this may be optimized to the appropriate hardware instruction, otherwise its execution will be similar to:

```
y = unsafe_load(p)
z = op(y, x)
unsafe_store!(p, z)
return y => z
```

The `unsafe` prefix on this function indicates that no validation is performed on the pointer `p` to ensure that it is valid. Like C, the programmer is responsible for ensuring that referenced memory is not freed or garbage collected while invoking this function. Incorrect usage may segfault your program.

!!! compat "Julia 1.10"
    This function requires at least Julia 1.10.


See also: [`modifyproperty!`](@ref Base.modifyproperty!), [`atomic`](@ref)



unsafe_pointer_to_objref:
==================================================

```
unsafe_pointer_to_objref(p::Ptr)
```

Convert a `Ptr` to an object reference. Assumes the pointer refers to a valid heap-allocated Julia object. If this is not the case, undefined behavior results, hence this function is considered "unsafe" and should be used with care.

See also [`pointer_from_objref`](@ref).



unsafe_read:
==================================================

```
unsafe_read(io::IO, ref, nbytes::UInt)
```

Copy `nbytes` from the `IO` stream object into `ref` (converted to a pointer).

It is recommended that subtypes `T<:IO` override the following method signature to provide more efficient implementations: `unsafe_read(s::T, p::Ptr{UInt8}, n::UInt)`



unsafe_replace!:
==================================================

```
unsafe_replace!(p::Ptr{T}, expected, desired,
               [success_order::Symbol[, fail_order::Symbol=success_order]]) -> (; old, success::Bool)
```

These atomically perform the operations to get and conditionally set a memory address to a given value. If supported by the hardware, this may be optimized to the appropriate hardware instruction, otherwise its execution will be similar to:

```
y = unsafe_load(p, fail_order)
ok = y === expected
if ok
    unsafe_store!(p, desired, success_order)
end
return (; old = y, success = ok)
```

The `unsafe` prefix on this function indicates that no validation is performed on the pointer `p` to ensure that it is valid. Like C, the programmer is responsible for ensuring that referenced memory is not freed or garbage collected while invoking this function. Incorrect usage may segfault your program.

!!! compat "Julia 1.10"
    This function requires at least Julia 1.10.


See also: [`replaceproperty!`](@ref Base.replaceproperty!), [`atomic`](@ref)



unsafe_store!:
==================================================

```
unsafe_store!(p::Ptr{T}, x, i::Integer=1)
unsafe_store!(p::Ptr{T}, x, order::Symbol)
unsafe_store!(p::Ptr{T}, x, i::Integer, order::Symbol)
```

Store a value of type `T` to the address of the `i`th element (1-indexed) starting at `p`. This is equivalent to the C expression `p[i-1] = x`. Optionally, an atomic memory ordering can be provided.

The `unsafe` prefix on this function indicates that no validation is performed on the pointer `p` to ensure that it is valid. Like C, the programmer is responsible for ensuring that referenced memory is not freed or garbage collected while invoking this function. Incorrect usage may segfault your program. Unlike C, storing memory region allocated as different type may be valid provided that that the types are compatible.

!!! compat "Julia 1.10"
    The `order` argument is available as of Julia 1.10.


See also: [`atomic`](@ref)



unsafe_string:
==================================================

```
unsafe_string(p::Ptr{UInt8}, [length::Integer])
```

Copy a string from the address of a C-style (NUL-terminated) string encoded as UTF-8. (The pointer can be safely freed afterwards.) If `length` is specified (the length of the data in bytes), the string does not have to be NUL-terminated.

This function is labeled "unsafe" because it will crash if `p` is not a valid memory address to data of the requested length.



unsafe_swap!:
==================================================

```
unsafe_swap!(p::Ptr{T}, x, [order::Symbol])
```

These atomically perform the operations to simultaneously get and set a memory address. If supported by the hardware, this may be optimized to the appropriate hardware instruction, otherwise its execution will be similar to:

```
y = unsafe_load(p)
unsafe_store!(p, x)
return y
```

The `unsafe` prefix on this function indicates that no validation is performed on the pointer `p` to ensure that it is valid. Like C, the programmer is responsible for ensuring that referenced memory is not freed or garbage collected while invoking this function. Incorrect usage may segfault your program.

!!! compat "Julia 1.10"
    This function requires at least Julia 1.10.


See also: [`swapproperty!`](@ref Base.swapproperty!), [`atomic`](@ref)



unsafe_trunc:
==================================================

```
unsafe_trunc(T, x)
```

Return the nearest integral value of type `T` whose absolute value is less than or equal to the absolute value of `x`. If the value is not representable by `T`, an arbitrary value will be returned. See also [`trunc`](@ref).

# Examples

```jldoctest
julia> unsafe_trunc(Int, -2.2)
-2

julia> unsafe_trunc(Int, NaN)
-9223372036854775808
```



unsafe_wrap:
==================================================

```
unsafe_wrap(Array, pointer::Ptr{T}, dims; own = false)
```

Wrap a Julia `Array` object around the data at the address given by `pointer`, without making a copy.  The pointer element type `T` determines the array element type. `dims` is either an integer (for a 1d array) or a tuple of the array dimensions. `own` optionally specifies whether Julia should take ownership of the memory, calling `free` on the pointer when the array is no longer referenced.

This function is labeled "unsafe" because it will crash if `pointer` is not a valid memory address to data of the requested length. Unlike [`unsafe_load`](@ref) and [`unsafe_store!`](@ref), the programmer is responsible also for ensuring that the underlying data is not accessed through two arrays of different element type, similar to the strict aliasing rule in C.



unsafe_write:
==================================================

```
unsafe_write(io::IO, ref, nbytes::UInt)
```

Copy `nbytes` from `ref` (converted to a pointer) into the `IO` object.

It is recommended that subtypes `T<:IO` override the following method signature to provide more efficient implementations: `unsafe_write(s::T, p::Ptr{UInt8}, n::UInt)`



unsigned:
==================================================

```
unsigned(T::Integer)
```

Convert an integer bitstype to the unsigned type of the same size.

# Examples

```jldoctest
julia> unsigned(Int16)
UInt16
julia> unsigned(UInt64)
UInt64
```

```
unsigned(x)
```

Convert a number to an unsigned integer. If the argument is signed, it is reinterpreted as unsigned without checking for negative values.

See also: [`signed`](@ref), [`sign`](@ref), [`signbit`](@ref).

# Examples

```jldoctest
julia> unsigned(-2)
0xfffffffffffffffe

julia> unsigned(Int8(2))
0x02

julia> typeof(ans)
UInt8

julia> signed(unsigned(-2))
-2
```



uperm:
==================================================

```
uperm(file)
```

Get the permissions of the owner of the file as a bitfield of

| Value | Description        |
|:----- |:------------------ |
| 01    | Execute Permission |
| 02    | Write Permission   |
| 04    | Read Permission    |

For allowed arguments, see [`stat`](@ref).



uppercase:
==================================================

```
uppercase(c::AbstractChar)
```

Convert `c` to uppercase.

See also [`lowercase`](@ref), [`titlecase`](@ref).

# Examples

```jldoctest
julia> uppercase('a')
'A': ASCII/Unicode U+0041 (category Lu: Letter, uppercase)

julia> uppercase('ê')
'Ê': Unicode U+00CA (category Lu: Letter, uppercase)
```

```
uppercase(s::AbstractString)
```

Return `s` with all characters converted to uppercase.

See also [`lowercase`](@ref), [`titlecase`](@ref), [`uppercasefirst`](@ref).

# Examples

```jldoctest
julia> uppercase("Julia")
"JULIA"
```



uppercasefirst:
==================================================

```
uppercasefirst(s::AbstractString) -> String
```

Return `s` with the first character converted to uppercase (technically "title case" for Unicode). See also [`titlecase`](@ref) to capitalize the first character of every word in `s`.

See also [`lowercasefirst`](@ref), [`uppercase`](@ref), [`lowercase`](@ref), [`titlecase`](@ref).

# Examples

```jldoctest
julia> uppercasefirst("python")
"Python"
```



valtype:
==================================================

```
valtype(T::Type{<:AbstractArray})
valtype(A::AbstractArray)
```

Return the value type of an array. This is identical to [`eltype`](@ref) and is provided mainly for compatibility with the dictionary interface.

# Examples

```jldoctest
julia> valtype(["one", "two", "three"])
String
```

!!! compat "Julia 1.2"
    For arrays, this function requires at least Julia 1.2.


```
valtype(type)
```

Get the value type of a dictionary type. Behaves similarly to [`eltype`](@ref).

# Examples

```jldoctest
julia> valtype(Dict(Int32(1) => "foo"))
String
```



values:
==================================================

```
values(iterator)
```

For an iterator or collection that has keys and values, return an iterator over the values. This function simply returns its argument by default, since the elements of a general iterator are normally considered its "values".

# Examples

```jldoctest
julia> d = Dict("a"=>1, "b"=>2);

julia> values(d)
ValueIterator for a Dict{String, Int64} with 2 entries. Values:
  2
  1

julia> values([2])
1-element Vector{Int64}:
 2
```

```
values(a::AbstractDict)
```

Return an iterator over all values in a collection. `collect(values(a))` returns an array of values. When the values are stored internally in a hash table, as is the case for `Dict`, the order in which they are returned may vary. But `keys(a)` and `values(a)` both iterate `a` and return the elements in the same order.

# Examples

```jldoctest
julia> D = Dict('a'=>2, 'b'=>3)
Dict{Char, Int64} with 2 entries:
  'a' => 2
  'b' => 3

julia> collect(values(D))
2-element Vector{Int64}:
 2
 3
```



varinfo:
==================================================

```
varinfo(m::Module=Main, pattern::Regex=r""; all=false, imported=false, recursive=false, sortby::Symbol=:name, minsize::Int=0)
```

Return a markdown table giving information about public global variables in a module, optionally restricted to those matching `pattern`.

The memory consumption estimate is an approximate lower bound on the size of the internal structure of the object.

  * `all` : also list non-public objects defined in the module, deprecated objects, and compiler-generated objects.
  * `imported` : also list objects explicitly imported from other modules.
  * `recursive` : recursively include objects in sub-modules, observing the same settings in each.
  * `sortby` : the column to sort results by. Options are `:name` (default), `:size`, and `:summary`.
  * `minsize` : only includes objects with size at least `minsize` bytes. Defaults to `0`.

The output of `varinfo` is intended for display purposes only.  See also [`names`](@ref) to get an array of symbols defined in a module, which is suitable for more general manipulations.



vcat:
==================================================

```
vcat(A...)
```

Concatenate arrays or numbers vertically. Equivalent to [`cat`](@ref)`(A...; dims=1)`, and to the syntax `[a; b; c]`.

To concatenate a large vector of arrays, `reduce(vcat, A)` calls an efficient method when `A isa AbstractVector{<:AbstractVecOrMat}`, rather than working pairwise.

See also [`hcat`](@ref), [`Iterators.flatten`](@ref), [`stack`](@ref).

# Examples

```jldoctest
julia> v = vcat([1,2], [3,4])
4-element Vector{Int64}:
 1
 2
 3
 4

julia> v == vcat(1, 2, [3,4])  # accepts numbers
true

julia> v == [1; 2; [3,4]]  # syntax for the same operation
true

julia> summary(ComplexF64[1; 2; [3,4]])  # syntax for supplying the element type
"4-element Vector{ComplexF64}"

julia> vcat(range(1, 2, length=3))  # collects lazy ranges
3-element Vector{Float64}:
 1.0
 1.5
 2.0

julia> two = ([10, 20, 30]', Float64[4 5 6; 7 8 9])  # row vector and a matrix
([10 20 30], [4.0 5.0 6.0; 7.0 8.0 9.0])

julia> vcat(two...)
3×3 Matrix{Float64}:
 10.0  20.0  30.0
  4.0   5.0   6.0
  7.0   8.0   9.0

julia> vs = [[1, 2], [3, 4], [5, 6]];

julia> reduce(vcat, vs)  # more efficient than vcat(vs...)
6-element Vector{Int64}:
 1
 2
 3
 4
 5
 6

julia> ans == collect(Iterators.flatten(vs))
true
```



vec:
==================================================

```
vec(a::AbstractArray) -> AbstractVector
```

Reshape the array `a` as a one-dimensional column vector. Return `a` if it is already an `AbstractVector`. The resulting array shares the same underlying data as `a`, so it will only be mutable if `a` is mutable, in which case modifying one will also modify the other.

# Examples

```jldoctest
julia> a = [1 2 3; 4 5 6]
2×3 Matrix{Int64}:
 1  2  3
 4  5  6

julia> vec(a)
6-element Vector{Int64}:
 1
 4
 2
 5
 3
 6

julia> vec(1:3)
1:3
```

See also [`reshape`](@ref), [`dropdims`](@ref).



versioninfo:
==================================================

```
versioninfo(io::IO=stdout; verbose::Bool=false)
```

Print information about the version of Julia in use. The output is controlled with boolean keyword arguments:

  * `verbose`: print all additional information

!!! warning
    The output of this function may contain sensitive information. Before sharing the output, please review the output and remove any data that should not be shared publicly.


See also: [`VERSION`](@ref).



view:
==================================================

```
view(A, inds...)
```

Like [`getindex`](@ref), but returns a lightweight array that lazily references (or is effectively a *view* into) the parent array `A` at the given index or indices `inds` instead of eagerly extracting elements or constructing a copied subset. Calling [`getindex`](@ref) or [`setindex!`](@ref) on the returned value (often a [`SubArray`](@ref)) computes the indices to access or modify the parent array on the fly.  The behavior is undefined if the shape of the parent array is changed after `view` is called because there is no bound check for the parent array; e.g., it may cause a segmentation fault.

Some immutable parent arrays (like ranges) may choose to simply recompute a new array in some circumstances instead of returning a `SubArray` if doing so is efficient and provides compatible semantics.

!!! compat "Julia 1.6"
    In Julia 1.6 or later, `view` can be called on an `AbstractString`, returning a `SubString`.


# Examples

```jldoctest
julia> A = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> b = view(A, :, 1)
2-element view(::Matrix{Int64}, :, 1) with eltype Int64:
 1
 3

julia> fill!(b, 0)
2-element view(::Matrix{Int64}, :, 1) with eltype Int64:
 0
 0

julia> A # Note A has changed even though we modified b
2×2 Matrix{Int64}:
 0  2
 0  4

julia> view(2:5, 2:3) # returns a range as type is immutable
3:4
```



wait:
==================================================

```
wait([x])
```

Block the current task until some event occurs, depending on the type of the argument:

  * [`Channel`](@ref): Wait for a value to be appended to the channel.
  * [`Condition`](@ref): Wait for [`notify`](@ref) on a condition and return the `val` parameter passed to `notify`. Waiting on a condition additionally allows passing `first=true` which results in the waiter being put *first* in line to wake up on `notify` instead of the usual first-in-first-out behavior.
  * `Process`: Wait for a process or process chain to exit. The `exitcode` field of a process can be used to determine success or failure.
  * [`Task`](@ref): Wait for a `Task` to finish. If the task fails with an exception, a `TaskFailedException` (which wraps the failed task) is thrown.
  * [`RawFD`](@ref): Wait for changes on a file descriptor (see the `FileWatching` package).

If no argument is passed, the task blocks for an undefined period. A task can only be restarted by an explicit call to [`schedule`](@ref) or [`yieldto`](@ref).

Often `wait` is called within a `while` loop to ensure a waited-for condition is met before proceeding.

```
wait(c::Channel)
```

Blocks until the `Channel` [`isready`](@ref).

```jldoctest
julia> c = Channel(1);

julia> isready(c)
false

julia> task = Task(() -> wait(c));

julia> schedule(task);

julia> istaskdone(task)  # task is blocked because channel is not ready
false

julia> put!(c, 1);

julia> istaskdone(task)  # task is now unblocked
true
```

Special note for [`Threads.Condition`](@ref):

The caller must be holding the [`lock`](@ref) that owns a `Threads.Condition` before calling this method. The calling task will be blocked until some other task wakes it, usually by calling [`notify`](@ref) on the same `Threads.Condition` object. The lock will be atomically released when blocking (even if it was locked recursively), and will be reacquired before returning.



walkdir:
==================================================

```
walkdir(dir; topdown=true, follow_symlinks=false, onerror=throw)
```

Return an iterator that walks the directory tree of a directory. The iterator returns a tuple containing `(rootpath, dirs, files)`. The directory tree can be traversed top-down or bottom-up. If `walkdir` or `stat` encounters a `IOError` it will rethrow the error by default. A custom error handling function can be provided through `onerror` keyword argument. `onerror` is called with a `IOError` as argument.

See also: [`readdir`](@ref).

# Examples

```julia
for (root, dirs, files) in walkdir(".")
    println("Directories in $root")
    for dir in dirs
        println(joinpath(root, dir)) # path to directories
    end
    println("Files in $root")
    for file in files
        println(joinpath(root, file)) # path to files
    end
end
```

```julia-repl
julia> mkpath("my/test/dir");

julia> itr = walkdir("my");

julia> (root, dirs, files) = first(itr)
("my", ["test"], String[])

julia> (root, dirs, files) = first(itr)
("my/test", ["dir"], String[])

julia> (root, dirs, files) = first(itr)
("my/test/dir", String[], String[])
```



which:
==================================================

```
which(f, types)
```

Returns the method of `f` (a `Method` object) that would be called for arguments of the given `types`.

If `types` is an abstract type, then the method that would be called by `invoke` is returned.

See also: [`parentmodule`](@ref), [`@which`](@ref Main.InteractiveUtils.@which), and [`@edit`](@ref Main.InteractiveUtils.@edit).

```
which(types::Type{<:Tuple})
```

Returns the method that would be called by the given type signature (as a tuple type).

```
which(module, symbol)
```

Return the module in which the binding for the variable referenced by `symbol` in `module` was created.



widemul:
==================================================

```
widemul(x, y)
```

Multiply `x` and `y`, giving the result as a larger type.

See also [`promote`](@ref), [`Base.add_sum`](@ref).

# Examples

```jldoctest
julia> widemul(Float32(3.0), 4.0) isa BigFloat
true

julia> typemax(Int8) * typemax(Int8)
1

julia> widemul(typemax(Int8), typemax(Int8))  # == 127^2
16129
```



widen:
==================================================

```
widen(x)
```

If `x` is a type, return a "larger" type, defined so that arithmetic operations `+` and `-` are guaranteed not to overflow nor lose precision for any combination of values that type `x` can hold.

For fixed-size integer types less than 128 bits, `widen` will return a type with twice the number of bits.

If `x` is a value, it is converted to `widen(typeof(x))`.

# Examples

```jldoctest
julia> widen(Int32)
Int64

julia> widen(1.5f0)
1.5
```



withenv:
==================================================

```
withenv(f, kv::Pair...)
```

Execute `f` in an environment that is temporarily modified (not replaced as in `setenv`) by zero or more `"var"=>val` arguments `kv`. `withenv` is generally used via the `withenv(kv...) do ... end` syntax. A value of `nothing` can be used to temporarily unset an environment variable (if it is set). When `withenv` returns, the original environment has been restored.

!!! warning
    Changing the environment is not thread-safe. For running external commands with a different environment from the parent process, prefer using [`addenv`](@ref) over `withenv`.




write:
==================================================

```
write(io::IO, x)
```

Write the canonical binary representation of a value to the given I/O stream or file. Return the number of bytes written into the stream. See also [`print`](@ref) to write a text representation (with an encoding that may depend upon `io`).

The endianness of the written value depends on the endianness of the host system. Convert to/from a fixed endianness when writing/reading (e.g. using  [`htol`](@ref) and [`ltoh`](@ref)) to get results that are consistent across platforms.

You can write multiple values with the same `write` call. i.e. the following are equivalent:

```
write(io, x, y...)
write(io, x) + write(io, y...)
```

# Examples

Consistent serialization:

```jldoctest
julia> fname = tempname(); # random temporary filename

julia> open(fname,"w") do f
           # Make sure we write 64bit integer in little-endian byte order
           write(f,htol(Int64(42)))
       end
8

julia> open(fname,"r") do f
           # Convert back to host byte order and host integer type
           Int(ltoh(read(f,Int64)))
       end
42
```

Merging write calls:

```jldoctest
julia> io = IOBuffer();

julia> write(io, "JuliaLang is a GitHub organization.", " It has many members.")
56

julia> String(take!(io))
"JuliaLang is a GitHub organization. It has many members."

julia> write(io, "Sometimes those members") + write(io, " write documentation.")
44

julia> String(take!(io))
"Sometimes those members write documentation."
```

User-defined plain-data types without `write` methods can be written when wrapped in a `Ref`:

```jldoctest
julia> struct MyStruct; x::Float64; end

julia> io = IOBuffer()
IOBuffer(data=UInt8[...], readable=true, writable=true, seekable=true, append=false, size=0, maxsize=Inf, ptr=1, mark=-1)

julia> write(io, Ref(MyStruct(42.0)))
8

julia> seekstart(io); read!(io, Ref(MyStruct(NaN)))
Base.RefValue{MyStruct}(MyStruct(42.0))
```

```
write(filename::AbstractString, content)
```

Write the canonical binary representation of `content` to a file, which will be created if it does not exist yet or overwritten if it does exist.

Return the number of bytes written into the file.



xor:
==================================================

```
xor(x, y)
⊻(x, y)
```

Bitwise exclusive or of `x` and `y`. Implements [three-valued logic](https://en.wikipedia.org/wiki/Three-valued_logic), returning [`missing`](@ref) if one of the arguments is `missing`.

The infix operation `a ⊻ b` is a synonym for `xor(a,b)`, and `⊻` can be typed by tab-completing `\xor` or `\veebar` in the Julia REPL.

# Examples

```jldoctest
julia> xor(true, false)
true

julia> xor(true, true)
false

julia> xor(true, missing)
missing

julia> false ⊻ false
false

julia> [true; true; false] .⊻ [true; false; false]
3-element BitVector:
 0
 1
 0
```



zero:
==================================================

```
zero(x)
zero(::Type)
```

Get the additive identity element for the type of `x` (`x` can also specify the type itself).

See also [`iszero`](@ref), [`one`](@ref), [`oneunit`](@ref), [`oftype`](@ref).

# Examples

```jldoctest
julia> zero(1)
0

julia> zero(big"2.0")
0.0

julia> zero(rand(2,2))
2×2 Matrix{Float64}:
 0.0  0.0
 0.0  0.0
```



zeros:
==================================================

```
zeros([T=Float64,] dims::Tuple)
zeros([T=Float64,] dims...)
```

Create an `Array`, with element type `T`, of all zeros with size specified by `dims`. See also [`fill`](@ref), [`ones`](@ref), [`zero`](@ref).

# Examples

```jldoctest
julia> zeros(1)
1-element Vector{Float64}:
 0.0

julia> zeros(Int8, 2, 3)
2×3 Matrix{Int8}:
 0  0  0
 0  0  0
```



zip:
==================================================

```
zip(iters...)
```

Run multiple iterators at the same time, until any of them is exhausted. The value type of the `zip` iterator is a tuple of values of its subiterators.

!!! note
    `zip` orders the calls to its subiterators in such a way that stateful iterators will not advance when another iterator finishes in the current iteration.


!!! note
    `zip()` with no arguments yields an infinite iterator of empty tuples.


See also: [`enumerate`](@ref), [`Base.splat`](@ref).

# Examples

```jldoctest
julia> a = 1:5
1:5

julia> b = ["e","d","b","c","a"]
5-element Vector{String}:
 "e"
 "d"
 "b"
 "c"
 "a"

julia> c = zip(a,b)
zip(1:5, ["e", "d", "b", "c", "a"])

julia> length(c)
5

julia> first(c)
(1, "e")
```
