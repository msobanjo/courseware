# Shell vs Exec

## Overview

Instructions, such as *RUN*, *CMD* and *ENTRYPOINT* allow you to either use the **shell** or **exec** forms for running commands when building a *Docker image*. 

The preferred method is to use the *exec* way, so that an unnecessary *sub shell* isn’t made, this is explained below.

Going forward, use *exec* form which looks like this:

```dockerfile
CMD ["/usr/bin/java", "-jar", "/app.jar"]
```

Rather than the *shell* form which looks like this:

```dockerfile
CMD java -jar app.jar
```

## Reasoning

When using the **shell** form, *Docker* will run this as a *shell command* when the container starts up, like this:

`/bin/sh -c "java -jar app.jar"`

The first process of the container when it starts running will be a shell **/bin/sh**, which will then start the *java process*. 

The *shell* in this is unnecessary, when you run the `docker ps` command, you will be able to see under the *COMMAND* column how the initial process has been started.



## Tasks