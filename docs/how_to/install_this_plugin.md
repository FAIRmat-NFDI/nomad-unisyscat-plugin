# Deploying a NOMAD Oasis with the UniSysCat Plugin

## Prerequisites
- A GitHub account, can be created for free on [github.com](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home)
- Docker installed on your computer, installation instructions can be found on
[docs.docker.com/desktop/](https://docs.docker.com/desktop/)
- The following instructions are for Windows operating system. If you are using Linux please refer to the detailed instructions [here](https://github.com/FAIRmat-NFDI/AreaA-Examples/tree/main/tutorial13/part4) or read the [NOMAD plugin documentation](https://nomad-lab.eu/prod/v1/staging/docs/howto/oasis/plugins_install.html) for all details on how to deploy the plugin on your NOMAD instance.

## Outline
1. Create a Docker image
2. Add the plugin
3. Update permissions
4. Run the OASIS

## 1. Create a Docker image
We will now create a custom docker image for your OASIS.
There is a GitHub template repository with predefined workflows that can be used for this at [github.com/FAIRmat-NFDI/nomad-distribution-template](https://github.com/FAIRmat-NFDI/nomad-distribution-template).

To use the template you should choose the "Create an new repository" option after pressing
the green "Use this template" button in the upper right corner.
Please note that you have to be logged into to GitHub to see this option.

![gif for creating an Oasis depolyment on Github](../images/Deploying%20Oasis%20with%20plugin.gif)

## 2. Add the plugin
We will now add the plugin we developed as a demonstration for UniSysCat.
To do this we need to add the following line to the `plugins.txt` file:
```
git+https://github.com/FAIRmat-NFDI/nomad-unisyscat-plugin.git@main
```

We can do this directly from the GitHub web UI.
Once this is saved, a workflow will run to create the image.

![gif for adding the plugin to NOMAD Oasis deployment](../images/Deploying%20Oasis%20with%20plugin%202.gif)

## 3. Run the OASIS
1. Make sure you have [docker](https://docs.docker.com/engine/install/) installed.
Docker nowadays comes with `docker compose` built in. Prior, you needed to
install the stand-alone [docker-compose](https://docs.docker.com/compose/install/).
2. Download the `nomad-oasis.zip` archive from your distribution repository to your computer

3. Unzip the `nomad-oasis.zip` file.

![gif for downloading and unzipping the Oasis file](../images/Deploying%20Oasis%20with%20plugin%203.gif)

4. Open Docker desktop.

5. Open the windows command prompt, and set the directory to the location where you have unzipped the nomad-oasis file. Below is an example for navigating to the directory where we saved the file. Make sure to change this to the directory you specified.
```sh
cd C:\Users\Fair-04\Documents\UniSysCat demo\nomad-oasis\nomad-oasis
```

6. Pull the images specified in the `docker-compose.yaml` (retrieved from the `nomad-oasis.zip`).
Note that the image needs to be public or you need to provide a PAT.
```sh
docker compose pull
```
7. And run it with docker compose in detached (--detach or -d) mode
```sh
docker compose up -d
```
8. Optionally you can now test that NOMAD is running with
```
curl localhost/nomad-oasis/alive
```
![gif for pulling and decomposing the Oasis with Docker](../images/Deploying%20Oasis%20with%20plugin%204.gif)

9. Finally, open [NOMAD Oasis](http://localhost/nomad-oasis) in your browser to start using your new NOMAD Oasis.
```
http://localhost/nomad-oasis
```


![gif for accessing NOMAD Oasis locally](../images/Deploying%20Oasis%20with%20plugin%205.gif)

