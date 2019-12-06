# Shell vs Exec

<!--TOC_START-->
## Contents
- [Overview](#overview)
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


## Tasks
