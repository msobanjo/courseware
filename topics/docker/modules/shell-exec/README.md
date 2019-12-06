# Shell vs Exec

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Reasoning](#reasoning)
- [Environment variables limitation](#environment-variables-limitation)
- [Tasks](#tasks)

<!--TOC_END-->
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

## Environment variables limitation

Environment Variables Will Not Work with [] notation.

Because you are not executing a *shell*, but a process directly, you will not be able to use *environment variables* with double braces (**[]**). 

For example, if you had a *JAR file* that you wanted to run in the *home* folder you could run the example below with the *shell* format, this would not work with brackets though:

```dockerfile
CMD java -jar $HOME/app.jar
```

## Tasks
