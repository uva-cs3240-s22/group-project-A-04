# Team A-04 Repository

Sp22 CS 3240 Repository for Team A-04

### Team Members:

**[Scrum Master]** *Samuel Ahn*, \<sya5jv\>

**[Requirements Manager]** *Matthew Kevin Bonner*, \<mkb2dxw\>

**[Testing Manager]** *Daniel Xue*, \<dlx3ud\>

**[DevOps Manager]** *Alex Yu*, \<ay3xqa\>

**[UX Designer]** *Asher Saunders*, \<aas9x\>

TA: *Darrel Zhang*

---

# *Word of Mouth*
A app where you can post and read recipes without the stories or ads. Made with Python 3 and Django 3.

## Table of Contents

+ [Introduction](#introduction)
+ [Technologies](#technologies)
+ [Launch](#launch)
+ [Features](#features)
+ [Development Status](#development-status)

[//]: # (Setup page to describe how to run the project TBD)

---

### Introduction

A place to post recipes, but without the pages and pages of backstory that all cooking webpages now have to force you to scroll through ads. Recipes would include a set of ingredients and directions, as well as images, possible videos, etc.

Users are ables to add new recipes, ingredients, quantities, directions, and images; "favorite", "like", and review recipes; and "fork" recipes — meaning taking an existing recipes, modifying it, and references the original recipe.

---

### Technologies

+ Python 3
+ Django 3
+ HTML5
+ CSS
+ GitHub
+ GitHub Actions CI
+ Heroku
+ PostgreSQL
+ Google OAuth API
+ Some API (TBD)

---

### Launch

This project will have all project files on GitHub with a stable version (master branch) hosted on Heroku, use Postgres database engine for production, and GitHub Actions for continuous integration.

---

### Features

##### Features Roadmap:
+ Sprint 4
    + Main Feature: Posting Recipes
        + Adding Ingredients
        + Adding Quantities
        + Adding Procedure
        + Extra Recipe Functions
            + Pictures
            + Videos
    + Additional Features:
        + Fluid UX/UI
            + Pretty Recipe Component
            + Pretty website
            + Usable menu interfaces for smoother switching between views
        + Recipe Forking
+ Sprint 5
    + Additional Main Feature: Recipe Forking
        + Link back to original source recipe
        + All recipes are forkable
        + All recipes can have multiple independent forks
        + Manage forked recipes (different components or different pages?)
+ More features for Sprints 4, 5, and further sprints TBD

##### To-do:

+ Add a new recipe
    + Add ingredients
    + Add ingredient quantities
    + Add directions
    + Embed images/videos (This counts as addition API)
+ Viewer Features
    + Favorite
    + Like
    + Review
+ Fork Recipes
    + Reference the original recipe

More requirements TBD

---

### Development Status

##### S1 — Project Preparation

+ [X] Project Organization

##### S1.5

+ [X] GitHub Setup

##### S2 — Hosting on Heroku

+ [X] Requirements Elicitation
+ [X] Working Basic Django App Hosted on Heroku

##### S3 — Login Integration

+ [X] Login Integration Using Google Accounts
+ [X] GitHub Actions CI Operational w/ 1 Test Case

##### S4 — First Major Feature

+ [ ] Recipe Adding Feature
+ [ ] GitHub Actions CI Operational w/ Multiple Test Cases

##### S5 — Next Major Feature

+ [ ] Feature Recipe Forking
+ [ ] More GitHub Actions CI Test Cases Operational

##### S6 — Beta Version

+ [ ] Features ***(TBD)***
+ [ ] Extra Features ***(TBD)***
+ [ ] More GitHub Actions CI Test Cases Operational

##### Final — Project Completion

+ [ ] All Features Functional
+ [ ] All GitHub Actions CI Test Cases Operational
+ [ ] Bug Fixes
