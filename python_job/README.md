# Portal Script Runner job - python from repo

phx_test is a test repo that contains a Portal Script Runner python job

- The Portal Script Runner job runs a python script in a Docker image on the Demsdata project on Google Cloud Platform
- based on DNC Tech Training: Portal Script Runner

## Script Runner steps

1. Create person repo with job files
   create deps.txt with list of python libraries
   create python script to run in Portal docker image
2. Create Script Runner job in Portal

   - select python language job type
   - connect to external repo
   - write Portal Startup commands
     cd <project folder>
     ls -l
     pip install -r deps.txt
     python <file.py> > holder.txt

3. Run Script Runner job
