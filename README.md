# PiCloud

## What is it?
PiCloud is a project for CMPSC 190B: Internet of Things (Fall 2018) at UCSB that deals with cloud-monitoring of a Raspberry Pi's thermal health.

## How did you come up with the name?
iCloud is the cloud service for Apple devices (i.e. iPhone), and since we're dealing with a cloud-oriented project for the Raspberry Pi, we decided to call it PiCloud!

## What are the objectives of this lab?
1. Periodically read the temperature of both the CPU and GPU.
2. Send the temperature data with a timestamp using an MQTT client/broker.
3. Set up a message broker in AWS, and have the Raspberry Pi talk to the broker to set the temperature values.
4. Use AWS Lambda to check that the temperature is within a good range.

## Is there any documentation available for this project?
Yes, we will publish our project report upon completion of this project.

Project created by Dr. Markus Mock, who is the instructor for this course.
