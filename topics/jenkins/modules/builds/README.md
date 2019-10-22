# Builds
<!--TOC_START-->
### Contents
- [Overview](#overview)
- [Build Status](#build-status)
- [Build Steps](#build-steps)
- [Console Output](#console-output)
- [Post-build Actions](#postbuild-actions)
	- [Artifacts](#artifacts)
		- [Accessing Artifacts](#accessing-artifacts)

<!--TOC_END-->
## Overview
A build is a result of an execution of a project (job) in Jenkins.
Builds for projects can be seen on the `Build History` section of the project dashboard:

![Build History](https://lh3.googleusercontent.com/06Et4v1n-eC5_Dq67LiI-pct1crrXtrKypg6AyVgY_gkfoU3jWxxykNHOJNen6BTMwSZlu1GnhPUrrJYCBDQapCzrQScK4hcslMQ1GIH5c19Mz0d3At_BgIUdcysyxaOQos7AoUPyWGUqtxLi-BIZdaqdKMbXdkUqNDCW7y8I8cEwSfIMf_3_O0sMQUiCAq8J0vPxlPM9FNqtbl8h0BTeLBDHed5WrXiOOHq8lllflcD85rbI0xP5XA1dbHet_-QCIA3wE6p2f6XECtZfYUC7JcCEvBXleXQrT4Ijal_Efxfqw4n3v71OTd53Au6JGS8gkVKIghSBjAdH6mafTyRv7_b9i5CD6izk3Q6E3wzHgyGS8shRQPt1__YjsE9jnFoTTktwxui9h2_7jGn5RxBf1Oz-mnXJKkXAi3Y_GF5oErfp3-GBTtORZ1NZ6MfgB6c8dlCNUOg_rUKalQN3fk18XB2mqW_nHzujSxIv6GRmFuLJYJ8yCfQPJhDsxpOhjIt26tqqKqD5tW4ooiEGsk-xxyS1VDK-wi0-bFRubjlDP_5IPbEU-9sJEswE_XnOKMNk03xQT1TLl7iirpJrPr12KaoZqsgBqO3itSVLbu9eJRziYIHl5_Pfab9gDO2oApzHCbBjgWZ9OXO6LjJEio6BwL3KKyPWIrUn5Iw2R6kJorIgCOMMaPUpwAjCKxujK8XTwJxcELlNm7si6PHlowJ8juJjcTZIn4W_kRhmuP1YOppD_iO=w422-h189-no)

Builds are named by the order that they were executed, so the first build ever executed will be called `#1` and the second `#2` etc.

## Build Status
The status of the build can have a few different values:
- `SUCCESS`: The build succeeded.  
    If all the buld steps complete successfully then this will be the build status.
- `FAILURE`: The build failed.
    If any of the steps exit with a non-zero status (if they throw an error), then the build status will go to failed.
- `ABORTED`: The build aborted before it finished.
    This exit status is more uncommon that the former statuses, this status must be set either by yourself or plugins that are being used in the project.

## Build Steps
Build steps are basically where you configure what your job is going to do, depending on your situation this could accomplish many different tasks:
- **Java**  
    If you have a Java project that you are wanting to automate builds for then you may be running commands or using plugins for running Maven, Gradle or Ant.
- **Docker**  
    Docker images can be built for your project.
- **NodeJS**  
    Installing dependencies for your node application before packaging it up for deployment at a later date.
- **Any Other Platforms**  
    With the combination of shell scripting and plugins that are available for Jenkins, the sky truly the limit with what you can automate in a Jenkins build.

We can add build steps by selecting the `Add build step` drop-down button and then selecting the type of build step that we would like to use:
![Jenkins Build Step](https://lh3.googleusercontent.com/ZRxHQq1C74_u6-gG6oQuLoVU8L8ufBx8dhQFjS_zZcdDXDc83vimAQfSVTdw3wsUiMaWcQeYzju0Y4NfhuVgZE8dOZLizz4EWzm5wWfluFteD3tr2dLJLttVi_tVaEGVMSP9JXC_Q7hXdam3p7iShcudrCi8t7pInBeWes88K8C4Ekk9ZwJQedhW3H8ar9qLM3SdwJAEc9DLm9Z1Mwi9ypGD82tjz5H13WGtJhWpUX0zJTvauTzI_2zUUOhUWFr9qqS21h7ASQRopc2RQxGuUgNd-LCGo9gVUqBblEYFj0_yYB9OTNqu1ap1OTEiU06drBUJ6Ls_iw_tih6fTyWzc-RTfZJ5jWcFSLcnmKGx4r5GsXXIIQTfhuu02SOGVZn4ozN75q9-60MV_QZ5e3PDmxsRff28t3NrmIDnLJMGC833rPwuYsshkzNjdaJBb-cwOfsifwZmLfPddhJ7dMsR-NcH_DdNZN4d0dldKFHnAvj-Vgq2H-UMdK8KVzz2UwkHbp6x-dqehbejJv5_toiEgV_tPL-6fIJGJFFkKunvSRQ3TFDpHKTf6E0W4pFg-f6nFAYayeiIV3CGA-tCOkmOR2Y4DtjDFghCAaec22yzxCEq-wj12f_gea0ju7NVwjTjFD8b7B2t15Ai9b2veVAMjIUlzMDM_goMIZHplR4StbZgCEBNb7tX8rymow_36wPO5y3tTxYMiASGgm09DQ2GSBFUoDMaMZAoDsOdQMaJQ6alsdSF=w1165-h721-no)

The types of build steps that are available will depend on the Jenkins Plugins that you have installed.
For the example shown above we can see that some plugins must be installed for Gradle, Maven and GitHub.

Most of the time you can get what you need out of a build step from shell scripting.
It's prefereable to seperate your shell scripts into different build steps to keep you project more maintainable.

For example you could have seperate build steps for compiling, testing and deployment.

## Console Output
The console output is likely one of the main parts of a build that you will be checking for information and debugging purposes.
This section includes the output for any shell scripts and plugins that have been executed in the build step for a project

The console output can be navigated to quickly by selecting the blue or red bulb (<img height="15" src="https://lh3.googleusercontent.com/B5jJbglc5X61XbXAWK_puHwoxjVsVpcTTEToSTGRHN1W_qavtCcVSCYjwZ1k9KcAJb_28ZULWCxN6YhxgkS7B3pSC6XjxHlU2qAAaD2N6z40xjj91UrsNzC_K3qQfwuv6ZsjTA37BdXSE_FIvfjiYBtebgKuxa44MvUbqvN7A8fgbrEICgQhvWkcwb4gsMDq7EY52krPyxjbkkeZODDeJTtc27kon-ZXEfLke1ov57n5TbqedC0wa87xlFoVLw2avme3I2YNlCxfw5b5fJ-YJ_YN1QDOwpUFOMVh8tOxM6YBqtD-dVIMzGNvI3irTpFUrBXPSzCnd9WP4uNUR5v2B-5BIM1w6JdIPaObPmm89pXrqLy0UYsGctfUqd4Y6SN372rEv8ZiIVt8mYqZmg6d3D-MU3xMf32nSmR2UFkaG6IYwGT2w-y-zuLJU179iiHRsXF9NQzNL5cUfkjgWc1VL3s81wfZGBO81WwzAcXx1Tgiw4hLaGw9xUV2at0NZksfOJHdzOGqcIV5sEzFlL3sYU6xftnINZxUDR4vaPaF1xuegUZWHQxFg3bp5Sag7VQ-b2OqoO2j1I46f-ikzqkX4GzYvORjLgceAJ4mLuXURt9A5QdzrvdC7LBo43bwctj3UckEllx89iwcNTURkOE6a6DDcVXu7LRWt-tikGoKgE1lB0SyHlcF2teB9qhIawT7bguRn1fUckUAiDnF-eYa_Js1oCzNf2bRaeVIBrWlXCSvtZd2=w22-h20-no">) on the build history.

Here is a very simple console output example:

![Console Output](https://lh3.googleusercontent.com/EFczWADmtwqLjlr0XEd4iTNjDM4asKOhaeyhB_cQSFqGmK8vwxuFyY9AOXZVU-O_lHDHfaL1f8b7TCcIRze8-A9Svgb_F4ozuMLJG7qtuOr-jCTe_i2e6MZfEYuUEMPVOCLe269Lxuz0duZLjlV6nHHBBHKaQ7HBBGihUKe-kQ1dQuG2_mb7c1lGaSaVQNwFkwUDYggTYFMp09ypVltK8cUEtw02JsN4aWfbbnK9ze3xHI75LsIq1w3ot8AYB9xjW7gL30audvGa0VCtAQr1-5wk-3bR1QGdX1bBcJS2Jtd-Zur9FI6ZEtna-4cDRAvi-cyssk5tmFVN_GbiejMb-dSAn1r3O5t7Ay7jmEqdkypUqQtbcQhTO2y_5MHUhqaBKaecFgZ9OT3zVk37ArOklrJY_mwJp4f1w2bvfbOw_mKzufNWWt-2x0CgChEfvteOSukiRmyYCJaoYa3AVfhQRHlSZ7WJV2bUQABWtngz-A1r8W40dyZ4UM6AFQqW7uUWfj36iOWkvE4SEd-smcL4L0HUr0kglBdL4PT0YQSTVVADkRI2TQeuR-OhfiwStaKFezGbMIRVNmy1_O5O0dS-HRyo89zTCLzAeM4xS1MZM187f11aaeilzlAKYWmc5bnz1Dd-kZ0WkGv_skyI5cobOSH7v936MlEsa7lhJMsXWm59KXygAkyPhKsSKmUUormqI4CSVmZp8OPs4rqIVsPbYbhZ6Knb4hquwNWMmOfT_mIB58-h=w543-h198-no)

## Post-build Actions
Post-build actions are plugins that can be run after you execute all the build steps.
You can add a post-build action by selecting the `Add post-build action` drop-down button and then selecting a post-build action from the list.
Theses actions can be set to run or not run depending on the success of the build steps.

Even if the build failed, you can still run post-build actions as an immediate response to the build failing.
You may want to send an email notification for instance on a build failure.

If the build succeeds, you might want to store the built application files as an artifact for access later on.

### Artifacts
Build artifacts are immutable files that are created as result of the build.
You have complete control over which files you would like to store as an artifact, this can be confured in the `Post-build Actions` section of the project configuration.

The example here will archive any files and store them as artifacts for the project:

![Archive Artifacts](https://lh3.googleusercontent.com/baKKp5oEBI9JVNkw4ykyjB5nFTeAFXJFok5_TtOkD8I0ksIdzoFqYdpbquOmTXQIMiHiS9PKic31rc8yOAvL5Sjr0Ocm6w4j-PewjYjwkRdEvw3mo9gKoKu560h_bZSIb7QUu4UY_nwMihnX9FHJ-rKORN8Sfay3iLMpEJlu3XnaYwxz2grbsY5eYcEClLmGH9lq1mJoBdjpPxYkkmbQu8B7-XQH01nvS3-j0XO76DqlpWxRYFI61K79SEdNLq2oRVXQ8T1d2X0f9nXriso0O5Rjo7H6YtJ8G5hQPBR5dSpwedGkfbfodz2dCt9PHpFRfAeodmYxBYTfVc07OKgqW5_kqqX5-fGIlqBu4-oU2suzqtY3ECw7L2tgB4XClGE2aS6sXT2mALP4KCUy7MqVbcRmlPXbMTJgAxe5n7gMiAM8z2Hsaif60D8HcFfC6TQmRTAUBc6H9vru0zW5avtaVv5ypnp50rWpdx6EjkoMLEhPleH0H15a_jvfAMFNWoEnJ8JImC9jxknviKYavsGwRwqN90GT6josfKEDsaU0DiAlWVuTPVKx1mFWUaog8m_kHyW8huguk4by60YCRRaFGYLu3mLuMTvcnuQqtkd29OqALpq5TNXNeHRbl9gEmak0Z6PepmAloKNsdOIGYtusXXn0tgZTcmdBidIbP_au4KQBBMfcQsVzfxa8BARKSx9dMOq9aMUwMQ2YjiAIY2hWBGaK6pcv1aF02sKEU-wZA2dL2Att=w1161-h276-no)

#### Accessing Artifacts
Once the job has executed, the artifacts are then available on the job dashboard:

![Build Artifacts](https://lh3.googleusercontent.com/Petsj_ebr2qS3OZXyPfCwg79KEn7kfX8MtINz8Wg2asgJUfgNADgcR0HSmBdVRi3Qo_NIm9CQQBn8hzDtK2cpywJqyP6Gu6EoMjne6vkBBAT3O34bKYuPC64l44jQqIiHEJ73T3oi6CeVsUnvkABw_2O0m9q2wS13zVulXCnEVg2tKYPXZPQyFbtgxBriH-Ls94v-hvCBQl4_oWCIZbiqDbBh8Qnhek3W5X3F81baUMXX2mF2IRxUKagOcN2DC_on10bWjKmwCkiBcqk5eSwz-igaF1Gu8n_O1buVFy-xKnf2gMdKskjjl3PrkrqPyD1kq4W_1LOCpuY08Wa7BXT2CE6qgMfRsiBvyiwvr0_QmhyH8JxKAQjyJkfdTYlziBbte9ayPe9hqvu-H8BylON0YKDC3qvcgC6P5npgqZLbK9iXeittZMfE4lF4WWIJUggMxXViELa_ehI9-D0cDPYV7cM5h4Pq67AGO4R8mD4J5baGE7OoXs6DVBvfjPLAh8YGvV2TAhb7aRgU1DFGjzBv1uwQm9zQ7BM0N-51aRjSW6lthX2glngNXSWYbmbPW71itdBehgETOGZiH9agydzkASB4xi0tCAmaMwTTTNbI8BW8yh-zGPvZDumX8nZHL4Pch6UXdFeKhI8oUq-S5WiF1LQ0k8xy3oc_PLRlVsCyohckB_RzYd5XjdGJNRIlOzXov_cDHJqhybLJFJedgpkg7G4_Dxw3EKOn4qHfr9aKNmNRhmp=w443-h355-no)

## Demo
We'll have a look at creating some builds here, focusing on build step configuration, statuses and storing artifacts.

### Create a Job
First we will need a new Jenkins job to work on, create one called anything that you like.

### Add a Build Step
Lets add a build step we know will succeed, select the `Add build step` button and add an `Execute shell` build step.
Add the following script into the `Command` field:
```bash
#! /usr/bin/env bash
echo "Hello from the Jenkins job named: ${JOB_NAME}"
```
Save the job and then build it, you should then have one successful build in your history for that job.
