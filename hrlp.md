📚 Julia Help Documentation 📚
══════════════════════════════
🕒 Generated on: 2024-11-29T03:43:46.483



⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: !
⚡ ══════════════════════════════════════════════════ ⚡

```
!(x)
```

Boolean not. Implements [three-valued logic](https://en.wikipedia.org/wiki/Three-valued_logic), returning [`missing`](@ref) if `x` is `missing`.

See also [`~`](@ref) for bitwise not.

# Examples

```jldoctest
julia> !true
false

julia> !false
true

julia> !missing
missing

julia> .![true false true]
1×3 BitMatrix:
 0  1  0
```

```
!f::Function
```

Predicate function negation: when the argument of `!` is a function, it returns a composed function which computes the boolean negation of `f`.

See also [`∘`](@ref).

# Examples

```jldoctest
julia> str = "∀ ε > 0, ∃ δ > 0: |x-y| < δ ⇒ |f(x)-f(y)| < ε"
"∀ ε > 0, ∃ δ > 0: |x-y| < δ ⇒ |f(x)-f(y)| < ε"

julia> filter(isletter, str)
"εδxyδfxfyε"

julia> filter(!isletter, str)
"∀  > 0, ∃  > 0: |-| <  ⇒ |()-()| < "
```

!!! compat "Julia 1.9"
    Starting with Julia 1.9, `!f` returns a [`ComposedFunction`](@ref) instead of an anonymous function.


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: accumulate!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: all!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: any!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: append!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: asyncmap!
⚡ ══════════════════════════════════════════════════ ⚡

```
asyncmap!(f, results, c...; ntasks=0, batch_size=nothing)
```

Like [`asyncmap`](@ref), but stores output in `results` rather than returning a collection.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: broadcast!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: circcopy!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: circshift!
⚡ ══════════════════════════════════════════════════ ⚡

```
circshift!(dest, src, shifts)
```

Circularly shift, i.e. rotate, the data in `src`, storing the result in `dest`. `shifts` specifies the amount to shift in each dimension.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


See also [`circshift`](@ref).

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: clamp!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: conj!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: copy!
⚡ ══════════════════════════════════════════════════ ⚡

```
copy!(dst, src) -> dst
```

In-place [`copy`](@ref) of `src` into `dst`, discarding any pre-existing elements in `dst`. If `dst` and `src` are of the same type, `dst == src` should hold after the call. If `dst` and `src` are multidimensional arrays, they must have equal [`axes`](@ref).

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


See also [`copyto!`](@ref).

!!! compat "Julia 1.1"
    This method requires at least Julia 1.1. In Julia 1.0 this method is available from the `Future` standard library as `Future.copy!`.


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: copyto!
⚡ ══════════════════════════════════════════════════ ⚡

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


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: count!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: cumprod!
⚡ ══════════════════════════════════════════════════ ⚡

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


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: cumsum!
⚡ ══════════════════════════════════════════════════ ⚡

```
cumsum!(B, A; dims::Integer)
```

Cumulative sum of `A` along the dimension `dims`, storing the result in `B`. See also [`cumsum`](@ref).

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: delete!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: deleteat!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: digits!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: empty!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: extrema!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: fill!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: filter!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: findmax!
⚡ ══════════════════════════════════════════════════ ⚡

```
findmax!(rval, rind, A) -> (maxval, index)
```

Find the maximum of `A` and the corresponding linear index along singleton dimensions of `rval` and `rind`, and store the results in `rval` and `rind`. `NaN` is treated as greater than all other values except `missing`.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: findmin!
⚡ ══════════════════════════════════════════════════ ⚡

```
findmin!(rval, rind, A) -> (minval, index)
```

Find the minimum of `A` and the corresponding linear index along singleton dimensions of `rval` and `rind`, and store the results in `rval` and `rind`. `NaN` is treated as less than all other values except `missing`.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: get!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: hex2bytes!
⚡ ══════════════════════════════════════════════════ ⚡

```
hex2bytes!(dest::AbstractVector{UInt8}, itr)
```

Convert an iterable `itr` of bytes representing a hexadecimal string to its binary representation, similar to [`hex2bytes`](@ref) except that the output is written in-place to `dest`. The length of `dest` must be half the length of `itr`.

!!! compat "Julia 1.7"
    Calling hex2bytes! with iterators producing UInt8 requires version 1.7. In earlier versions, you can collect the iterable before calling instead.


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: in!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: insert!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: intersect!
⚡ ══════════════════════════════════════════════════ ⚡

```
intersect!(s::Union{AbstractSet,AbstractVector}, itrs...)
```

Intersect all passed in sets and overwrite `s` with the result. Maintain order with arrays.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: invpermute!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isa
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isabspath
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isabstracttype
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isapprox
🔍 ══════════════════════════════════════════════════ 🔍

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


└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isascii
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isassigned
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isbits
🔍 ══════════════════════════════════════════════════ 🔍

```
isbits(x)
```

Return `true` if `x` is an instance of an [`isbitstype`](@ref) type.

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isbitstype
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isblockdev
🔍 ══════════════════════════════════════════════════ 🔍

```
isblockdev(path) -> Bool
```

Return `true` if `path` is a block device, `false` otherwise.

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: ischardev
🔍 ══════════════════════════════════════════════════ 🔍

```
ischardev(path) -> Bool
```

Return `true` if `path` is a character device, `false` otherwise.

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: iscntrl
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isconcretetype
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isconst
🔍 ══════════════════════════════════════════════════ 🔍

```
isconst(m::Module, s::Symbol) -> Bool
```

Determine whether a global is declared `const` in a given module `m`.

```
isconst(t::DataType, s::Union{Int,Symbol}) -> Bool
```

Determine whether a field `s` is declared `const` in a given type `t`.

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isdefined
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isdigit
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isdir
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isdirpath
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isdisjoint
🔍 ══════════════════════════════════════════════════ 🔍

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


└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isdispatchtuple
🔍 ══════════════════════════════════════════════════ 🔍

```
isdispatchtuple(T)
```

Determine whether type `T` is a tuple "leaf type", meaning it could appear as a type signature in dispatch and has no subtypes (or supertypes) which could appear in a call. If `T` is not a type, then return `false`.

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isempty
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isequal
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: iseven
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isexecutable
🔍 ══════════════════════════════════════════════════ 🔍

```
isexecutable(path::String)
```

Return `true` if the given `path` has executable permissions.

!!! note
    This permission may change before the user executes `path`, so it is recommended to execute the file and handle the error if that fails, rather than calling `isexecutable` first.


!!! note
    Prior to Julia 1.6, this did not correctly interrogate filesystem ACLs on Windows, therefore it would return `true` for any file.  From Julia 1.6 on, it correctly determines whether the file is marked as executable or not.


See also [`ispath`](@ref), [`isreadable`](@ref), [`iswritable`](@ref).

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isfifo
🔍 ══════════════════════════════════════════════════ 🔍

```
isfifo(path) -> Bool
```

Return `true` if `path` is a FIFO, `false` otherwise.

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isfile
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isfinite
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isimmutable
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isinf
🔍 ══════════════════════════════════════════════════ 🔍

```
isinf(f) -> Bool
```

Test whether a number is infinite.

See also: [`Inf`](@ref), [`iszero`](@ref), [`isfinite`](@ref), [`isnan`](@ref).

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isinteger
🔍 ══════════════════════════════════════════════════ 🔍

```
isinteger(x) -> Bool
```

Test whether `x` is numerically equal to some integer.

# Examples

```jldoctest
julia> isinteger(4.0)
true
```

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isinteractive
🔍 ══════════════════════════════════════════════════ 🔍

```
isinteractive() -> Bool
```

Determine whether Julia is running an interactive session.

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isless
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isletter
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: islink
🔍 ══════════════════════════════════════════════════ 🔍

```
islink(path) -> Bool
```

Return `true` if `path` is a symbolic link, `false` otherwise.

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: islocked
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: islowercase
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: ismarked
🔍 ══════════════════════════════════════════════════ 🔍

```
ismarked(s::IO)
```

Return `true` if stream `s` is marked.

See also [`mark`](@ref), [`unmark`](@ref), [`reset`](@ref).

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: ismissing
🔍 ══════════════════════════════════════════════════ 🔍

```
ismissing(x)
```

Indicate whether `x` is [`missing`](@ref).

See also: [`skipmissing`](@ref), [`isnothing`](@ref), [`isnan`](@ref).

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: ismount
🔍 ══════════════════════════════════════════════════ 🔍

```
ismount(path) -> Bool
```

Return `true` if `path` is a mount point, `false` otherwise.

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: ismutable
🔍 ══════════════════════════════════════════════════ 🔍

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


└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: ismutabletype
🔍 ══════════════════════════════════════════════════ 🔍

```
ismutabletype(T) -> Bool
```

Determine whether type `T` was declared as a mutable type (i.e. using `mutable struct` keyword). If `T` is not a type, then return `false`.

!!! compat "Julia 1.7"
    This function requires at least Julia 1.7.


└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isnan
🔍 ══════════════════════════════════════════════════ 🔍

```
isnan(f) -> Bool
```

Test whether a number value is a NaN, an indeterminate value which is neither an infinity nor a finite number ("not a number").

See also: [`iszero`](@ref), [`isone`](@ref), [`isinf`](@ref), [`ismissing`](@ref).

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isnothing
🔍 ══════════════════════════════════════════════════ 🔍

```
isnothing(x)
```

Return `true` if `x === nothing`, and return `false` if not.

!!! compat "Julia 1.1"
    This function requires at least Julia 1.1.


See also [`something`](@ref), [`Base.notnothing`](@ref), [`ismissing`](@ref).

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isnumeric
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isodd
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isone
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isopen
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: ispath
🔍 ══════════════════════════════════════════════════ 🔍

```
ispath(path) -> Bool
```

Return `true` if a valid filesystem entity exists at `path`, otherwise returns `false`. This is the generalization of [`isfile`](@ref), [`isdir`](@ref) etc.

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isperm
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: ispow2
🔍 ══════════════════════════════════════════════════ 🔍

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


└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isprimitivetype
🔍 ══════════════════════════════════════════════════ 🔍

```
isprimitivetype(T) -> Bool
```

Determine whether type `T` was declared as a primitive type (i.e. using the `primitive type` syntax). If `T` is not a type, then return `false`.

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isprint
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: ispunct
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isqrt
🔍 ══════════════════════════════════════════════════ 🔍

```
isqrt(n::Integer)
```

Integer square root: the largest integer `m` such that `m*m <= n`.

```jldoctest
julia> isqrt(5)
2
```

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isreadable
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isreadonly
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isready
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isreal
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: issetequal
🔍 ══════════════════════════════════════════════════ 🔍

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


└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: issetgid
🔍 ══════════════════════════════════════════════════ 🔍

```
issetgid(path) -> Bool
```

Return `true` if `path` has the setgid flag set, `false` otherwise.

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: issetuid
🔍 ══════════════════════════════════════════════════ 🔍

```
issetuid(path) -> Bool
```

Return `true` if `path` has the setuid flag set, `false` otherwise.

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: issocket
🔍 ══════════════════════════════════════════════════ 🔍

```
issocket(path) -> Bool
```

Return `true` if `path` is a socket, `false` otherwise.

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: issorted
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isspace
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: issticky
🔍 ══════════════════════════════════════════════════ 🔍

```
issticky(path) -> Bool
```

Return `true` if `path` has the sticky bit set, `false` otherwise.

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isstructtype
🔍 ══════════════════════════════════════════════════ 🔍

```
isstructtype(T) -> Bool
```

Determine whether type `T` was declared as a struct type (i.e. using the `struct` or `mutable struct` keyword). If `T` is not a type, then return `false`.

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: issubnormal
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: issubset
🔍 ══════════════════════════════════════════════════ 🔍

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


└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: istaskdone
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: istaskfailed
🔍 ══════════════════════════════════════════════════ 🔍

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


└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: istaskstarted
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: istextmime
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isunordered
🔍 ══════════════════════════════════════════════════ 🔍

```
isunordered(x)
```

Return `true` if `x` is a value that is not orderable according to [`<`](@ref), such as `NaN` or `missing`.

The values that evaluate to `true` with this predicate may be orderable with respect to other orderings such as [`isless`](@ref).

!!! compat "Julia 1.7"
    This function requires Julia 1.7 or later.


└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isuppercase
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isvalid
🔍 ══════════════════════════════════════════════════ 🔍

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


└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: iswritable
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: isxdigit
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


🔍 ══════════════════════════════════════════════════ 🔍
   📎 Function: iszero
🔍 ══════════════════════════════════════════════════ 🔍

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: keepat!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: kron!
⚡ ══════════════════════════════════════════════════ ⚡

```
kron!(C, A, B)
```

Computes the Kronecker product of `A` and `B` and stores the result in `C`, overwriting the existing content of `C`. This is the in-place version of [`kron`](@ref).

!!! compat "Julia 1.6"
    This function requires Julia 1.6 or later.


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: map!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: maximum!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: merge!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: mergewith!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: minimum!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: modifyfield!
⚡ ══════════════════════════════════════════════════ ⚡

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


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: modifyglobal!
⚡ ══════════════════════════════════════════════════ ⚡

```
modifyglobal!(module::Module, name::Symbol, op, x, [order::Symbol=:monotonic]) -> Pair
```

Atomically perform the operations to get and set a global after applying the function `op`.

!!! compat "Julia 1.11"
    This function requires Julia 1.11 or later.


See also [`modifyproperty!`](@ref Base.modifyproperty!) and [`setglobal!`](@ref).

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: modifyproperty!
⚡ ══════════════════════════════════════════════════ ⚡

```
modifyproperty!(x, f::Symbol, op, v, order::Symbol=:not_atomic)
```

The syntax `@atomic op(x.f, v)` (and its equivalent `@atomic x.f op v`) returns `modifyproperty!(x, :f, op, v, :sequentially_consistent)`, where the first argument must be a `getproperty` expression and is modified atomically.

Invocation of `op(getproperty(x, f), v)` must return a value that can be stored in the field `f` of the object `x` by default.  In particular, unlike the default behavior of [`setproperty!`](@ref Base.setproperty!), the `convert` function is not called automatically.

See also [`modifyfield!`](@ref Core.modifyfield!) and [`setproperty!`](@ref Base.setproperty!).

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: partialsort!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: partialsortperm!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: permute!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: permutedims!
⚡ ══════════════════════════════════════════════════ ⚡

```
permutedims!(dest, src, perm)
```

Permute the dimensions of array `src` and store the result in the array `dest`. `perm` is a vector specifying a permutation of length `ndims(src)`. The preallocated array `dest` should have `size(dest) == size(src)[perm]` and is completely overwritten. No in-place permutation is supported and unexpected results will happen if `src` and `dest` have overlapping memory regions.

See also [`permutedims`](@ref).

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: pop!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: popat!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: popfirst!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: prepend!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: prod!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: push!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: pushfirst!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: put!
⚡ ══════════════════════════════════════════════════ ⚡

```
put!(c::Channel, v)
```

Append an item `v` to the channel `c`. Blocks if the channel is full.

For unbuffered channels, blocks until a [`take!`](@ref) is performed by a different task.

!!! compat "Julia 1.1"
    `v` now gets converted to the channel's type with [`convert`](@ref) as `put!` is called.


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: read!
⚡ ══════════════════════════════════════════════════ ⚡

```
read!(stream::IO, array::AbstractArray)
read!(filename::AbstractString, array::AbstractArray)
```

Read binary data from an I/O stream or file, filling in `array`.

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: readbytes!
⚡ ══════════════════════════════════════════════════ ⚡

```
readbytes!(stream::IO, b::AbstractVector{UInt8}, nb=length(b))
```

Read at most `nb` bytes from `stream` into `b`, returning the number of bytes read. The size of `b` will be increased if needed (i.e. if `nb` is greater than `length(b)` and enough bytes could be read), but it will never be decreased.

```
readbytes!(stream::IOStream, b::AbstractVector{UInt8}, nb=length(b); all::Bool=true)
```

Read at most `nb` bytes from `stream` into `b`, returning the number of bytes read. The size of `b` will be increased if needed (i.e. if `nb` is greater than `length(b)` and enough bytes could be read), but it will never be decreased.

If `all` is `true` (the default), this function will block repeatedly trying to read all requested bytes, until an error or end-of-file occurs. If `all` is `false`, at most one `read` call is performed, and the amount of data returned is device-dependent. Note that not all stream types support the `all` option.

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: replace!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: replacefield!
⚡ ══════════════════════════════════════════════════ ⚡

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


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: replaceglobal!
⚡ ══════════════════════════════════════════════════ ⚡

```
replaceglobal!(module::Module, name::Symbol, expected, desired,
              [success_order::Symbol, [fail_order::Symbol=success_order]) -> (; old, success::Bool)
```

Atomically perform the operations to get and conditionally set a global to a given value.

!!! compat "Julia 1.11"
    This function requires Julia 1.11 or later.


See also [`replaceproperty!`](@ref Base.replaceproperty!) and [`setglobal!`](@ref).

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: replaceproperty!
⚡ ══════════════════════════════════════════════════ ⚡

```
replaceproperty!(x, f::Symbol, expected, desired, success_order::Symbol=:not_atomic, fail_order::Symbol=success_order)
```

Perform a compare-and-swap operation on `x.f` from `expected` to `desired`, per egal. The syntax `@atomicreplace x.f expected => desired` can be used instead of the function call form.

See also [`replacefield!`](@ref Core.replacefield!) [`setproperty!`](@ref Base.setproperty!), [`setpropertyonce!`](@ref Base.setpropertyonce!).

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: resize!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: reverse!
⚡ ══════════════════════════════════════════════════ ⚡

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


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: setdiff!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: setfield!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: setfieldonce!
⚡ ══════════════════════════════════════════════════ ⚡

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


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: setglobal!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: setglobalonce!
⚡ ══════════════════════════════════════════════════ ⚡

```
setglobalonce!(module::Module, name::Symbol, value,
              [success_order::Symbol, [fail_order::Symbol=success_order]) -> success::Bool
```

Atomically perform the operations to set a global to a given value, only if it was previously not set.

!!! compat "Julia 1.11"
    This function requires Julia 1.11 or later.


See also [`setpropertyonce!`](@ref Base.setpropertyonce!) and [`setglobal!`](@ref).

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: setindex!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: setproperty!
⚡ ══════════════════════════════════════════════════ ⚡

```
setproperty!(value, name::Symbol, x)
setproperty!(value, name::Symbol, x, order::Symbol)
```

The syntax `a.b = c` calls `setproperty!(a, :b, c)`. The syntax `@atomic order a.b = c` calls `setproperty!(a, :b, c, :order)` and the syntax `@atomic a.b = c` calls `setproperty!(a, :b, c, :sequentially_consistent)`.

!!! compat "Julia 1.8"
    `setproperty!` on modules requires at least Julia 1.8.


See also [`setfield!`](@ref Core.setfield!), [`propertynames`](@ref Base.propertynames) and [`getproperty`](@ref Base.getproperty).

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: setpropertyonce!
⚡ ══════════════════════════════════════════════════ ⚡

```
setpropertyonce!(x, f::Symbol, value, success_order::Symbol=:not_atomic, fail_order::Symbol=success_order)
```

Perform a compare-and-swap operation on `x.f` to set it to `value` if previously unset. The syntax `@atomiconce x.f = value` can be used instead of the function call form.

See also [`setfieldonce!`](@ref Core.replacefield!), [`setproperty!`](@ref Base.setproperty!), [`replaceproperty!`](@ref Base.replaceproperty!).

!!! compat "Julia 1.11"
    This function requires Julia 1.11 or later.


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: sizehint!
⚡ ══════════════════════════════════════════════════ ⚡

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


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: sort!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: sortperm!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: splice!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: sum!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: swapfield!
⚡ ══════════════════════════════════════════════════ ⚡

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


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: swapglobal!
⚡ ══════════════════════════════════════════════════ ⚡

```
swapglobal!(module::Module, name::Symbol, x, [order::Symbol=:monotonic])
```

Atomically perform the operations to simultaneously get and set a global.

!!! compat "Julia 1.11"
    This function requires Julia 1.11 or later.


See also [`swapproperty!`](@ref Base.swapproperty!) and [`setglobal!`](@ref).

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: swapproperty!
⚡ ══════════════════════════════════════════════════ ⚡

```
swapproperty!(x, f::Symbol, v, order::Symbol=:not_atomic)
```

The syntax `@atomic a.b, _ = c, a.b` returns `(c, swapproperty!(a, :b, c, :sequentially_consistent))`, where there must be one `getproperty` expression common to both sides.

See also [`swapfield!`](@ref Core.swapfield!) and [`setproperty!`](@ref Base.setproperty!).

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: symdiff!
⚡ ══════════════════════════════════════════════════ ⚡

```
symdiff!(s::Union{AbstractSet,AbstractVector}, itrs...)
```

Construct the symmetric difference of the passed in sets, and overwrite `s` with the result. When `s` is an array, the order is maintained. Note that in this case the multiplicity of elements matters.

!!! warning
    Behavior can be unexpected when any mutated argument shares memory with any other argument.


└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: take!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: union!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: unique!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: unsafe_copyto!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: unsafe_modify!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: unsafe_replace!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: unsafe_store!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘


⚡ ══════════════════════════════════════════════════ ⚡
   📎 Function: unsafe_swap!
⚡ ══════════════════════════════════════════════════ ⚡

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

└──────────────────────────────────────────────────┘
