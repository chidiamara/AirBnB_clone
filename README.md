# AirBnB_clone - The Console

## Overview

The AirBnB Clone Project is a web application consisting of multiple components that work together seamlessly to provide a professional and user-friendly experience. It is the first step towards building a full-fledged web application.

This dynamic web application comprises the following components:

- A powerful command-line interpreter to facilitate data manipulation without the need for a graphical user interface. This feature is particularly useful for development and debugging purposes.
- A visually appealing website, which serves as the front-end and showcases the final product to end-users, both in static and dynamic formats.
- A robust database or file system for data storage, where data is represented in the form of objects.
- A well-designed API that enables communication between the front-end and the data, including creating, retrieving, updating, and deleting data. The AirBnB_clone project provides support for two different storage types: files and databases.

## Specific Components and their functions

- **The Console:** This component provides a command-line interface where objects can be created and serialized to files. It is also where the first storage engine, the file storage, is created.

- **HTML:** In this component, we focus on making the web application visually appealing and providing a user interface for users.

- **MySQL:** This component focuses on a different type of storage, i.e., the MySQL database. Here, we explore unique ways to store objects and learn how to better manage databases.

- **Fabric Deployment:** With Fabric deployment, we take all the components developed so far and deploy them to our servers.

- **Flask Application Server:** This component integrates the models stored in the database with HTML and other components.

- **REST API:** In this component, objects are converted into JSON format, enabling their integration with other applications.

- **Web Dynamic:** The final component focuses on integrating the JSON API with HTML, allowing for the sharing of the AirBnB clone project we developed.

![console](/console.png)

> This repository is focused on building the Console - CLI to manage the AirBnB_clone project.

## The Console

The console is similar to shell, except it is a single-use function, a command-line interface from which we can create, modify, and delete objects in our file storage. It is a tool, a sandbox where we can play around with ideas to see what does and doesn't work in storage before we build out the rest of the web application. Command line interpreter manages serialization and deserialization of objects.

In the context of the command-line interpreter, serialization and deserialization are used to save and load objects to and from storage, respectively. For example, when an object is created or modified in the console, it is serialized and saved to a file or database. When the object needs to be retrieved later, it is deserialized from the storage format and reconstructed as an object in memory.
