[![General Assembly Logo](https://camo.githubusercontent.com/1a91b05b8f4d44b5bbfb83abac2b0996d8e26c92/687474703a2f2f692e696d6775722e636f6d2f6b6538555354712e706e67)](https://generalassemb.ly/education/web-development-immersive)

# Do you even run?: Run Tracking Application

## Planning Story

## Technologies Used
    1. React
    2. html
    3. JavaScript
    4. jsx
    5. Bootstrap/React-Bootstrap
    6. Python
    7. Django
    8. MDN
    9. axios
    10. Passport JS
    11. MomentJS
    12. Bcrypt
    13. CSS/Sass
    14. Material Design Bootstrap React
    15. SQL/PostgresQL

## User Stories
    1.  As a user, I would like to sign up on a secure account.
    2.  As a user, I would like to sign in to a secure account.
    3.  As a user, I would like to change my password.
    4.  As a user, I would like to create a new run.
    5.  As a user, I would like to edit a run.
    6.  As a user, I would like to delete a run.
    7.  As a user, I would like to view all of my runs.
    8.  As a user, I would like to view my running statistics, including total runs, total distance, and pace (average, fastest).
    9.  As a user, I would like to see a graph or chart of my progress over time.

## Entity Relationship Diagram
![ERD](https://i.imgur.com/226G4dZ.jpg)

## Routes and Paths
| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| POST   | `/sign-up/`             | `users#signup`    |
| POST   | `/sign-in/`             | `users#signin`    |
| PATCH  | `/change-password/`    | `users#changepw`  |
| DELETE | `/sign-out/`           | `users#signout`   |
| GET    | `/runs/`                | `users#index`       |
| GET    | `/runs/:id/`          |`users#show`         |
| PATCH  | `/runs/:id/`             | `users#update`    |
| POST  | `/runs/`               | `users#create`    |
| DELETE | `/runs/:id`           | `users#delete`   |

All data returned from API actions is formatted as JSON.

## Unsolved Problems/Future Versions
Unsolved:  API calls to Unsplash and data conversion moved to back-end.
Version 2: Search and filter Runs, increased statistical analysis
Version 3: View other peoples runs/profiles, Shoe tracker
Version 4: Interact with other users, Calendar view

## Links
[Deployed Frontend](https://robrichardsdpt.github.io/running-app/) <br>
[Deployed Backend](https://running-back-end.herokuapp.com/) <br>
[Frontend Github Repository](https://github.com/robrichardsdpt/running-app)<br>
[Backend Github Repository](https://github.com/robrichardsdpt/running-back-end)

## Installation
  1.  Fork and clone this repository.
  2.  Create and checkout to a new branch, training, for your work.
  3.  Run pipenv shell to start up your virtual environment.
  4.  Run pipenv install to install dependencies.
  5.  Create a psql database for the project
  6.  Type psql to get into interactive shell
  7.  Run CREATE DATABASE "your-DB-name";
  8.  Exit shell
  9.  Open the repository in Atom with atom .
