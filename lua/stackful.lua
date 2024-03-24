-- Function declarations --

function yielding_function()  -- This is a coroutine
    print("I am going to yield!")
    coroutine.yield()
    print("I am going to yield again!")
    coroutine.yield()
end

function a_normal_function() -- This is not a coroutine
    print("I am a normal function and I am going to call a coroutine")
    yielding_function()  -- But it is calling a coroutine
end

function coroutine_function()
    print("Started executing body of coroutine_function")
    a_normal_function()  -- This function will yield! That's weird!
    a_normal_function()  -- // //
    print("Finished executing body of coroutine_function")
end

-- Start of the program --

coro = coroutine.create(coroutine_function)

coroutine.resume(coro)
coroutine.resume(coro)