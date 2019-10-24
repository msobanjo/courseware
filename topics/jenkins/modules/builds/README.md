# Builds

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Build Status](#build-status)
- [Build Steps](#build-steps)
- [Console Output](#console-output)
- [Post-build Actions](#postbuild-actions)
	- [Artifacts](#artifacts)
		- [Accessing Artifacts](#accessing-artifacts)
- [Demo](#demo)
	- [Create a Job](#create-a-job)
	- [Add a Build Step](#add-a-build-step)
	- [Run the Job](#run-the-job)
	- [Make the Build Fail](#make-the-build-fail)
	- [Fix the Build and Create Artifacts](#fix-the-build-and-create-artifacts)
	- [Finish Up](#finish-up)

<!--TOC_END-->
## Overview
A build is a result of an execution of a project (job) in Jenkins.
Builds for projects can be seen on the `Build History` section of the project dashboard:

![Build History](https://lh3.googleusercontent.com/06Et4v1n-eC5_Dq67LiI-pct1crrXtrKypg6AyVgY_gkfoU3jWxxykNHOJNen6BTMwSZlu1GnhPUrrJYCBDQapCzrQScK4hcslMQ1GIH5c19Mz0d3At_BgIUdcysyxaOQos7AoUPyWGUqtxLi-BIZdaqdKMbXdkUqNDCW7y8I8cEwSfIMf_3_O0sMQUiCAq8J0vPxlPM9FNqtbl8h0BTeLBDHed5WrXiOOHq8lllflcD85rbI0xP5XA1dbHet_-QCIA3wE6p2f6XECtZfYUC7JcCEvBXleXQrT4Ijal_Efxfqw4n3v71OTd53Au6JGS8gkVKIghSBjAdH6mafTyRv7_b9i5CD6izk3Q6E3wzHgyGS8shRQPt1__YjsE9jnFoTTktwxui9h2_7jGn5RxBf1Oz-mnXJKkXAi3Y_GF5oErfp3-GBTtORZ1NZ6MfgB6c8dlCNUOg_rUKalQN3fk18XB2mqW_nHzujSxIv6GRmFuLJYJ8yCfQPJhDsxpOhjIt26tqqKqD5tW4ooiEGsk-xxyS1VDK-wi0-bFRubjlDP_5IPbEU-9sJEswE_XnOKMNk03xQT1TLl7iirpJrPr12KaoZqsgBqO3itSVLbu9eJRziYIHl5_Pfab9gDO2oApzHCbBjgWZ9OXO6LjJEio6BwL3KKyPWIrUn5Iw2R6kJorIgCOMMaPUpwAjCKxujK8XTwJxcELlNm7si6PHlowJ8juJjcTZIn4W_kRhmuP1YOppD_iO=w422-h189-no)

Builds are named by the order that they were executed, so the first build ever executed will be called `#1` and the second `#2`, etc.

## Build Status
The status of the build can have a few different values:
- `SUCCESS`: The build succeeded.  
    If all the buld steps complete successfully, this will be the build status.
- `FAILURE`: The build failed.
    If any of the steps exit with a non-zero status (if they throw an error), then the build status will go to failed.
- `ABORTED`: The build aborted before it finished.
    This exit status is more uncommon; it must be set either by yourself or plugins that are being used in the project.

## Build Steps
Build steps are effectively where you configure what your job is going to do. Depending on your situation, this could accomplish many different tasks:
- **Java**  
    If you have a Java project that you are wanting to automate builds for, you may be running commands or using plugins for running Maven, Gradle or Ant.
- **Docker**  
    Docker images can be built for your project.
- **NodeJS**  
    Installing dependencies for your node application before packaging it up for deployment at a later date.
- **Any Other Platforms**  
    With the combination of shell scripting and plugins that are available for Jenkins, the sky truly is the limit with what you can automate in a Jenkins' build.

We can add build steps by selecting the `Add build step` drop-down button and then selecting the type of build step that we would like to use:
![Jenkins Build Step](https://lh3.googleusercontent.com/ZRxHQq1C74_u6-gG6oQuLoVU8L8ufBx8dhQFjS_zZcdDXDc83vimAQfSVTdw3wsUiMaWcQeYzju0Y4NfhuVgZE8dOZLizz4EWzm5wWfluFteD3tr2dLJLttVi_tVaEGVMSP9JXC_Q7hXdam3p7iShcudrCi8t7pInBeWes88K8C4Ekk9ZwJQedhW3H8ar9qLM3SdwJAEc9DLm9Z1Mwi9ypGD82tjz5H13WGtJhWpUX0zJTvauTzI_2zUUOhUWFr9qqS21h7ASQRopc2RQxGuUgNd-LCGo9gVUqBblEYFj0_yYB9OTNqu1ap1OTEiU06drBUJ6Ls_iw_tih6fTyWzc-RTfZJ5jWcFSLcnmKGx4r5GsXXIIQTfhuu02SOGVZn4ozN75q9-60MV_QZ5e3PDmxsRff28t3NrmIDnLJMGC833rPwuYsshkzNjdaJBb-cwOfsifwZmLfPddhJ7dMsR-NcH_DdNZN4d0dldKFHnAvj-Vgq2H-UMdK8KVzz2UwkHbp6x-dqehbejJv5_toiEgV_tPL-6fIJGJFFkKunvSRQ3TFDpHKTf6E0W4pFg-f6nFAYayeiIV3CGA-tCOkmOR2Y4DtjDFghCAaec22yzxCEq-wj12f_gea0ju7NVwjTjFD8b7B2t15Ai9b2veVAMjIUlzMDM_goMIZHplR4StbZgCEBNb7tX8rymow_36wPO5y3tTxYMiASGgm09DQ2GSBFUoDMaMZAoDsOdQMaJQ6alsdSF=w1165-h721-no)

The type of build steps that are available will depend on the Jenkins' Plugins that you have installed.
For the example shown above, we can see that some plugins must be installed for Gradle, Maven and GitHub.

Most of the time you can get what you need out of a build step from shell scripting.
It's prefereable to seperate your shell scripts into different build steps, to keep you project more maintainable.

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
Theses actions can be set to run, or not run, depending on the success of the build steps.

Even if the build failed, you can still run post-build actions as an immediate response to the build failing.
For instance, you may want to send an email notification on a build failure.

If the build succeeds, you might want to store the built application files as an artifact for access later on.

### Artifacts
Build artifacts are immutable files that are created as result of the build.
You have complete control over which files you would like to store as an artifact, and this can be confured in the `Post-build Actions` section of the project configuration.

The example here will archive any files and store them as artifacts for the project:

![Archive Artifacts](https://lh3.googleusercontent.com/baKKp5oEBI9JVNkw4ykyjB5nFTeAFXJFok5_TtOkD8I0ksIdzoFqYdpbquOmTXQIMiHiS9PKic31rc8yOAvL5Sjr0Ocm6w4j-PewjYjwkRdEvw3mo9gKoKu560h_bZSIb7QUu4UY_nwMihnX9FHJ-rKORN8Sfay3iLMpEJlu3XnaYwxz2grbsY5eYcEClLmGH9lq1mJoBdjpPxYkkmbQu8B7-XQH01nvS3-j0XO76DqlpWxRYFI61K79SEdNLq2oRVXQ8T1d2X0f9nXriso0O5Rjo7H6YtJ8G5hQPBR5dSpwedGkfbfodz2dCt9PHpFRfAeodmYxBYTfVc07OKgqW5_kqqX5-fGIlqBu4-oU2suzqtY3ECw7L2tgB4XClGE2aS6sXT2mALP4KCUy7MqVbcRmlPXbMTJgAxe5n7gMiAM8z2Hsaif60D8HcFfC6TQmRTAUBc6H9vru0zW5avtaVv5ypnp50rWpdx6EjkoMLEhPleH0H15a_jvfAMFNWoEnJ8JImC9jxknviKYavsGwRwqN90GT6josfKEDsaU0DiAlWVuTPVKx1mFWUaog8m_kHyW8huguk4by60YCRRaFGYLu3mLuMTvcnuQqtkd29OqALpq5TNXNeHRbl9gEmak0Z6PepmAloKNsdOIGYtusXXn0tgZTcmdBidIbP_au4KQBBMfcQsVzfxa8BARKSx9dMOq9aMUwMQ2YjiAIY2hWBGaK6pcv1aF02sKEU-wZA2dL2Att=w1161-h276-no)

#### Accessing Artifacts
Once the job has executed, the artifacts are then available on the job dashboard:

![Build Artifacts](https://lh3.googleusercontent.com/Petsj_ebr2qS3OZXyPfCwg79KEn7kfX8MtINz8Wg2asgJUfgNADgcR0HSmBdVRi3Qo_NIm9CQQBn8hzDtK2cpywJqyP6Gu6EoMjne6vkBBAT3O34bKYuPC64l44jQqIiHEJ73T3oi6CeVsUnvkABw_2O0m9q2wS13zVulXCnEVg2tKYPXZPQyFbtgxBriH-Ls94v-hvCBQl4_oWCIZbiqDbBh8Qnhek3W5X3F81baUMXX2mF2IRxUKagOcN2DC_on10bWjKmwCkiBcqk5eSwz-igaF1Gu8n_O1buVFy-xKnf2gMdKskjjl3PrkrqPyD1kq4W_1LOCpuY08Wa7BXT2CE6qgMfRsiBvyiwvr0_QmhyH8JxKAQjyJkfdTYlziBbte9ayPe9hqvu-H8BylON0YKDC3qvcgC6P5npgqZLbK9iXeittZMfE4lF4WWIJUggMxXViELa_ehI9-D0cDPYV7cM5h4Pq67AGO4R8mD4J5baGE7OoXs6DVBvfjPLAh8YGvV2TAhb7aRgU1DFGjzBv1uwQm9zQ7BM0N-51aRjSW6lthX2glngNXSWYbmbPW71itdBehgETOGZiH9agydzkASB4xi0tCAmaMwTTTNbI8BW8yh-zGPvZDumX8nZHL4Pch6UXdFeKhI8oUq-S5WiF1LQ0k8xy3oc_PLRlVsCyohckB_RzYd5XjdGJNRIlOzXov_cDHJqhybLJFJedgpkg7G4_Dxw3EKOn4qHfr9aKNmNRhmp=w443-h355-no)

## Demo
We'll have a look at creating some builds here, focusing on build step configuration, statuses and storing artifacts.

### Create a Job
First, we will need a new Jenkins job to work on, so create one called anything that you like.

### Add a Build Step
Let's add a build step that we know will succeed. Select the `Add build step` button and add an `Execute shell` build step.
Add the following script into the `Command` field:
```bash
#! /usr/bin/env bash
echo "Hello from the Jenkins job named: ${JOB_NAME}"
```

### Run the Job
Save the job and then build it; you should then have one successful build in your history for that job.
Once you navigate to the console output, you should see an output like this:

![Jenkins Build Output](https://lh3.googleusercontent.com/on72Ii9CCkQQTuiFmNWmvH61TpBvYY9DfNVnfQXTv7iYMd_MpdSDtB2PGlkUhyt95dW8Z3WxcaVu9VjGHpEB_x5YamliFBhLNJaUtJXY8YY4RoiZxOyOzRSMpwUSW9sm1s-pY7SoP0DreTJ7oNbXw3USXP9zL0tXLr-WEdNdjs66c_RrZ_TJDEWHiccdCoenU9ciMquW44xQUpMjnfOg96CHEcsu2kBezWlTNlFU_mgNt7J2kysgLqU1eE1ehzwfDxgDBOwKEji6dXatbjasXK8ZtPpYOPydrfV0QdBV4vZSLvBWTeHf7Y4x4deUOQ1oCILJrRqLQ7l0SYX9WNl838HlYMDs9-UN950CDCXLWN1x9yxTdPlOfQtcr-5Bzj_H8IMPGqI-Tp0p3Kp-MEXFV5tlZkrst32bCb1s1pBnbmH4RqG78AvtWmJmNJ-iovJTJG2ExDoNRpR-MK0odJu2iEqWRI3YUrBxdfkdM364kKrkEfbfW7wPYZP3lJeowDLmrdszAjNrdXUacseTmQh4V5NvKufZC6ejDKO8zw5DV6AOtNoE7Xd8nGF53OMUEb9C-0fzhVZ2cfRWTcbrHMTSlV7JJlR6EHtXguoiH0BnDcMq-NzY0V0Hux47TCmANOf3-zpUohQfasMsA7SooPaISghRh30M_awTPdgOvN8nPtyQZSCUwbgC4OO3pLqgR0J6-mNaA-S7t9pm1WY8Wue3b_0FWLh426cwfXzs_7AK4kjmR2Dc=w613-h311-no)

### Make the Build Fail
Now that the last build succeeded, let's see what a failed build looks like!
All we have to do is make it so that the script we added to the command box "fails".
Jenkins will treat any script or application exiting with a non-zero status as a failure.

So to create a failed build, let's add `exit 1` to the script box, which will make the script exit with a code of `1`:

```bash
#! /usr/bin/env bash
echo "Hello from the Jenkins job named: ${JOB_NAME}"
exit 1
```
![Jenkins Failed Build Output](https://lh3.googleusercontent.com/5rPAcgdY778iHOfaNey8PqLVOesYfu3ZqDMZfuNgAnsbJFrQqbYHEqBpFIsv2HtDLJ7qT3mqAbldXj3mlx33B5tKaaw4dJz7NWbS8NqIp8LeWRmAl7TMX3wQDjEBDkKCLkrbIlM9lv71fMFccRXNzfvK5Oo3U6Gb7uoxbUZlSiHE-pIFPdsdn8vCQOuBsa4NSzJBxa1254SlMCgyaa79p0zdmdfHT44q8uanIavA4Hc3aX-tw1IP66AfiVDlhBUfSbmHRYtRIZ-oR3j9FJkauzoZ_qR81J8eKW8ifNCQifA4MEQHIdRVTykaW6hJBbjMguXOwWyUL17nG3sKjZYPGKfRLQKdsaw1Q6AohSTRmcyBAt8biSd7sC_aDmEePf66-QH2KAZLjkgOovFTzqwwgj6gF7dsYGhNC1TSKZ_S07X-xU9DCD1Jkgume5hR-zFm2HtFXFQY48PgvLEVdaZPuswxcGtchQUCxSF7zyO4wHYfNzDgpd4aBs0zOeqmlYIqGTy6WeEgimy8xLAXJme-hMO2pJ_QpKepbqMlA3hft2cfIqQNJ90skfMx0TMi31hC02sX4LYZgt7MvyvhIFYU3eBz5VtEM5B1qUKSPcHvZqSW99EZT3UxMXjDsTeZFDMUp2dUhZVAEc5VAmox7aG4YazJIDnp9g835xhddqHoi_19OohuUMdR81o8Mbzj4SzusKG4j7AWuFjrgP4aeul-QGhJ_yLaGYrCAKI3Sfx3ipG9zeMM=w617-h356-no)

### Fix the Build and Create Artifacts 
We can, of course, remove the `exit 1` from the build step to unbreak it.
After that, let's change the script to create several files, and then put them in a zip archive called `archive.zip`:

```bash
#! /usr/bin/env bash
echo "Hello from the Jenkins job named: ${JOB_NAME}"
touch 1.txt 2.txt 3.txt 4.txt 5.txt
zip archive.zip *.txt
```

Next, a `Post-build Action` must be configured to archive the zip files. Please refer to the [Artifacts](#artifacts) section for configuring this.

### Finish Up
Now try to run the job. You should see artifacts on the project dashboard. If they don't show up, try refreshing the page.
