package main

import (
	"fmt"
	"time"
)

func foo(num int) {
	for i := 0; i < 5; i++ {
		fmt.Printf("Go routine number %d!\n", num)
		time.Sleep(1000 * time.Millisecond)
	}
}

func main() {
	fmt.Println("Hello world!")
	for i := 0; i < 5; i++ {
		go foo(i)
	}
	for {
	}
}
