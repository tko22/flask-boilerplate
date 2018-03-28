# Conventions
- **Controllers**, which describe API endpoints will be defined under ``api/views/*``. We will be using [Flask Blueprints](http://flask.pocoo.org/docs/0.12/blueprints/) for easier collaborations in view controllers. Be sure to know how to use them. <br>
... Blueprints simplify the application by splitting it under relevant components. To register a Blueprint, you must import it and register it under ```__init__.py```.
```
from api.views import main
app.register_blueprint(main.mod)
```
- The **Database** Structure will be defined under ``api/models.py``. Look at the Database Schema Section to know how to update your database. We are using [SQLAlchemy](http://docs.sqlalchemy.org/en/latest/) as our ORM, which allows us to create, query, and filter through the database easily. 

For more Flask Conventions, look at [this](https://github.com/hack4impact-uiuc/wiki/wiki/Flask-API-Conventions)

## Utility Functions
I've provided a couple utility functions/classes to help with Database Serialization and Responses. They are all located in `./api/utils.py`. 
- `Mixin` is a class for all tables (represented by classes) in `models.py` to extend. This will add a `to_dict()` serialization function.  
- `create_response(data={}, status=200, message='')` is a helper function to create responses. This follows the API specification described [here](https://github.com/hack4impact-uiuc/wiki/wiki/Our-REST-API-Specification). You must provide a dictionary for data. 
- `serialize_list()` is a helper function to serialize a list of SQLAlchemy objects. Look at `./api/views/main.py` for a use case.

## Git Flow 
Before you start making changes, make sure you have the most recently updated version of `master`:
```
git pull
```

Make a new branch for your changes:
```
git checkout -b <branch_name>
```

If you want to see all of your branches that exist:
```
git branch
```

If you want to switch to a branch that already exists:
```
git checkout <branch_name>
```

Make sure you commit your changes to your own branch! 

Push your code and submit a PR to leave it up for review:
```
git push
```
This might walk you through some remote branch push settings, just follow what it says. It should only happen the first time you push to a new branch

Then go to this repo on Github, refresh the page, and you should see an option to create a pull request from your branch.
## Code Reviews
It is recommended to:
1) Keep PRs small and manageable
2) Put up a PR early on (even before it is ready for review), so you can get early feedback

### Labels:
#### `In Progress` 
Use this while you are working on your changes. Reviewers can take a look to make sure you're on the right track and make some suggestions along the way. Also use this as a way to ask questions about your code (_Is this the right way to do x?, Does this follow conventions properly?, etc._).

#### `Ready For Review`
Use this when you feel like your code is ready to be thoroughly reviewed before shipping. Assign your PR to your technical lead and teammates who know more about the areas you worked on (Github might have suggestions based on previous contributions).

#### `In Review`
Reviewers, set this to indicate the PR is currently being reviewed.

#### `SHIP IT`
Reviewers, set this to indicate the PR is ready to be merged, but let the pull requester do the merging.

PRs can't be merged without at least one reviewer approving your changes. If waiting on your reviewer becomes a blocker, bug them about it!
