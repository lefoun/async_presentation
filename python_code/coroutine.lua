function greet()
    print("Hello!")
    coroutine.yield() -- Yields here
    print("Bonjour!")
    coroutine.yield() -- Yields here
    print("Hola!")
    coroutine.yield() -- Yields here
end
  
greeting_coro = coroutine.create(greet)
  
print(coroutine.status(greeting_coro))  -- Prints suspended

coroutine.resume(greeting_coro) -- Prints "Hello!"
coroutine.resume(greeting_coro) -- Prints "Bonjour!"
coroutine.resume(greeting_coro) -- Prints "Hola!"

print(coroutine.status(greeting_coro))  -- Prints dead





-- Example 2

for i=1,10 do
    coroutine.resume(counting_coro)
end

function count()
    for i=1,10 do
        print("coro", i)
        coroutine.yield() -- Yields here
    end
end
