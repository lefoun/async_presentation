function yielding_function()
    print("I am going to yield!")
    coroutine.yield()
end

function a_normal_function()
    print("I am a normal function and I am going to call a coroutine")
    yielding_function()
end

function coroutine_function()
    print("Started executing body of coroutine_function")
    a_normal_function()  -- This function will yield! That's weird!
    a_normal_function()  -- // //
    print("Finished executing body of coroutine_function")
end

coro = coroutine.create(coroutine_function)

coroutine.resume(coro)
coroutine.resume(coro)