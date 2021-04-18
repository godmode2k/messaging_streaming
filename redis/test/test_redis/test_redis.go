/* --------------------------------------------------------------
Purpose:    Redis test
Author:     Ho-Jung Kim (godmode2k@hotmail.com)
Filename:   test_redis.go
Date:       Since April 13, 2021


Reference:
 - https://github.com/go-redis/redis


License:

*
* Copyright (C) 2021 Ho-Jung Kim (godmode2k@hotmail.com)
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*      http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*
-----------------------------------------------------------------
Note:
-----------------------------------------------------------------
1. Build:
    $ mkdir test_redis
    $ cd test_redis
    $ go mod init test_redis
    $ go get github.com/go-redis/redis/v8

    $ go build test_redis.go
    or
    $ go run test_redis.go
-------------------------------------------------------------- */
package main



//! Header
// ---------------------------------------------------------------

import (
    "fmt"

    "context"
    "github.com/go-redis/redis/v8"
)



//! Definition
// -----------------------------------------------------------------



// -----------------------------------------------------------------



//! Implementation
// -----------------------------------------------------------------

///*
// Example (https://github.com/go-redis/redis)
var ctx = context.Background()
func ExampleClient() {
    rdb := redis.NewClient(&redis.Options{
        Addr:     "localhost:6379",
        Password: "", // no password set
        DB:       0,  // use default DB
    })

    defer rdb.Close()

    err := rdb.Set(ctx, "key", "value", 0).Err()
    if err != nil {
        panic(err)
    }

    val, err := rdb.Get(ctx, "key").Result()
    if err != nil {
        panic(err)
    }
    fmt.Println("key", val)

    val2, err := rdb.Get(ctx, "key2").Result()
    if err == redis.Nil {
        fmt.Println("key2 does not exist")
    } else if err != nil {
        panic(err)
    } else {
        fmt.Println("key2", val2)
    }
    // Output: key value
    // key2 does not exist
}
func main() {
    ExampleClient()
}
//*/



// -----------------------------------------------------------------



//func main() {
//}


