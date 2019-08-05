# TL-FRAUD #

Welcome to the TL-FRAUD repo. This collection contains fraud related tools. There are various credential stuffing tools, configuration files, and custom scripts to attempt fraud against services and organizations.

Files in this collection have been gathered via distributed trawling of the internet, and deduplicated where applicable.

## Disclaimer ##

The files contained in this repo are for research purposes only. They are provided as-is and have no guarantee of functionality.

## What is Credential Stuffing? ##

Credential stuffing is a fraud technique that leverages database dumps to brute force logins on a given service. The more fresh and/or relevant a given database dump is, the higher the chance of success.

Combolists are combinations of usernames and passwords, stored line by line in a text file. They are the most common way of storing credentials for an attack.

## Mitigations ##

There are numerous mitigations that can assist in preventing the success of a credential stuffing attack. These include WAFs, CAPCHAs, Rate Limiting, and a defense in depth approach to protecting your application.

## Navigating the Repo ##

The repo is divided into several folders, containing specific categories of activity.

Zip files may have the same or similar names, so each filename contains an identifier based on the first 6 characters of the SHA1 hash of the file. The formula is:

    FILENAME.SHA1.EXTENSION

Non Zip files may contain this naming pattern as well.

## Collection Highlights ## 

There is a large number of configuration files for popular credential stuffing tools, SentryMBA, BlackBullet, AIOC, Woxy and Storm.

## Contributing ## 

Contributions to this repo are welcome. Simply fork this repo, open a pull request and consult with the repo maintainers about it. 

### Guidelines ###

- Please submit larger files (> 5 MB) as a zip file in order to make cloning this a reasonable exercise.
- Please try and follow our naming convention for zip files in order to deduplicate and identify hashes. 

Files are subject to rejection if they do not meet our guidelines.

### We will NOT accept the following ###

- Combolists
- Database dumps
- Any credentials for active sites, user, admin or otherwise
